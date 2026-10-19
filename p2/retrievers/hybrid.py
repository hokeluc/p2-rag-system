"""Hybrid retriever: reciprocal rank fusion (k = 60) of bm25 and dense.

This is rrf() of the 13 lab's pipeline.py: each item scores the sum of 1 / (k + rank) over the
rankings it appears in. Both systems are asked for every document (or chunk), not a top 10, so an
item that is 11th in both lists can still reach the fused top 10. search fuses document rankings and
search_chunks fuses chunk rankings, so `p2 answer` works with hybrid.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False
DEFAULT_RRF_K = 60  # used only when p2.toml has no [hybrid] rrf_k
PARTS = ("bm25", "dense")


def rrf(rankings, k: int = DEFAULT_RRF_K) -> list[tuple[str, float]]:
    """Fuse rankings (each a list of (id, score), best first); an id missing from one ranking adds nothing."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1 / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        self.rrf_k = int(cfg.table("hybrid").get("rrf_k", DEFAULT_RRF_K))
        self.parts = [retrievers.build(name, corpus, cfg) for name in PARTS]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(self.parts[0].chunks)

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([p.search(text, self.n_docs) for p in self.parts], self.rrf_k)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        return rrf([p.search_chunks(text, self.n_chunks) for p in self.parts], self.rrf_k)[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
