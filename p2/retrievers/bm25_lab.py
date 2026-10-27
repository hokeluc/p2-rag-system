"""BM25 with the lab's tokenizer: an ablation of the provided bm25 baseline.

It is a copy of bm25.py with one change: the tokenizer is always "lab", whatever [bm25] in p2.toml
says (the baseline uses "codes" by default). Chunking, k1, b and the scoring are the baseline's.

For one query word w in chunk c:
    idf(w)  = ln(1 + (N - df(w) + 0.5) / (df(w) + 0.5))      N chunks, df(w) chunks containing w
    part    = idf(w) * tf * (k1 + 1) / (tf + k1 * (1 - b + b * len(c) / avg_len))
and a chunk's score is the sum of the parts over the distinct query words.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict

from p2 import textproc
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False

TOKENIZER = "lab"


class BM25Lab(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.tokenizer = TOKENIZER
        self.k1, self.b = cfg.bm25_k1, cfg.bm25_b
        token_lists = [textproc.tokens(c.text, self.tokenizer) for c in self.chunks]
        self.lengths = [len(t) for t in token_lists]
        self.n = len(token_lists)
        self.avg_len = (sum(self.lengths) / self.n) if self.n else 0.0
        self.postings: dict[str, list[tuple[int, int]]] = defaultdict(list)  # word -> [(chunk index, tf)]
        for i, toks in enumerate(token_lists):
            for word, tf in Counter(toks).items():
                self.postings[word].append((i, tf))

    def idf(self, word: str) -> float:
        df = len(self.postings.get(word, ()))
        return math.log(1 + (self.n - df + 0.5) / (df + 0.5))

    def score_chunks(self, text: str) -> list[float]:
        scores = [0.0] * self.n
        if not self.n or self.avg_len == 0:
            return scores
        k1, b = self.k1, self.b
        for word in dict.fromkeys(textproc.tokens(text, self.tokenizer)):  # distinct words, first-seen order
            posting = self.postings.get(word)
            if not posting:
                continue
            idf = self.idf(word)
            for i, tf in posting:
                scores[i] += idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * self.lengths[i] / self.avg_len))
        return scores


def build(corpus, cfg):
    return BM25Lab(corpus, cfg)
