"""Listwise reranker: Claude reorders the top 20 of the hybrid retriever.

This is rerank_one() of the 13 lab's pipeline.py. The first stage's top candidates are shown as
numbered passages (the first passage_chars characters of each), one claude -p call per query, and the
reply is forced into {"order": [n numbers]} by a schema whose items run from 1 to n, so no number
can name a missing passage. A reply that is not each number once, or a failed call, keeps the
first-stage order (a warning goes to stderr). Items below the candidates keep their order underneath.

Settings, all optional, in a [rerank] table of p2.toml: candidates (20) and passage_chars (600).
`search` reranks documents; `search_chunks` reranks the first stage's top chunks the same way.
"""

from __future__ import annotations

import sys

from p2 import claude, retrievers
from p2.runfile import order

NEEDS_CLAUDE = True
DEFAULT_CANDIDATES = 20
DEFAULT_PASSAGE_CHARS = 600

PROMPT = """Below are {n} passages, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n: int) -> dict:
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        table = cfg.table("rerank")
        self.candidates = int(table.get("candidates", DEFAULT_CANDIDATES))
        self.passage_chars = int(table.get("passage_chars", DEFAULT_PASSAGE_CHARS))
        self.first = retrievers.build("hybrid", corpus, cfg)
        self.model = cfg.model
        self.chunk_text = {c.id: c.text for c in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)}

    def rerank(self, query: str, ranked: list[tuple[str, float]], text_of) -> list[tuple[str, float]]:
        """ranked is the full first-stage ranking; the top candidates are reordered by Claude."""
        top, rest = ranked[: self.candidates], ranked[self.candidates :]
        if len(top) < 2:
            return ranked
        n = len(top)
        passages = "\n\n".join(f"[{i}] {text_of(item)[: self.passage_chars]}" for i, (item, _) in enumerate(top, 1))
        reply = claude.call(
            PROMPT.format(n=n, query=query, passages=passages), schema(n),
            model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg),
        )
        got = (reply.output or {}).get("order")
        if reply.error or not isinstance(got, list) or sorted(got) != list(range(1, n + 1)):
            print(f"  warning: keeping the first-stage order ({reply.error or f'reply was not each of 1 to {n} once: {got}'})", file=sys.stderr, flush=True)
            return ranked
        # scores must not increase down the list, so rank the reply with descending scores above the rest
        new = [top[i - 1][0] for i in got]
        top_scores = [float(len(ranked) - r) for r in range(n)]
        rest_scores = [float(len(rest) - r) / (len(rest) + 1) for r in range(len(rest))]
        return order(list(zip(new, top_scores)) + [(item, s) for (item, _), s in zip(rest, rest_scores)])

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search(text, len(self.corpus.docs))
        return self.rerank(text, ranked, lambda d: self.corpus.docs[d].text)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        ranked = self.first.search_chunks(text, max(k, self.candidates))
        return self.rerank(text, ranked, lambda c: self.chunk_text[c])[:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
