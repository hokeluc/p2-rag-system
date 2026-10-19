"""Dense retriever: embed every chunk once, embed the query, and rank chunks by cosine similarity.

This is the embedding arm of the 12 lab's retrieve.py (load_bge, cached_doc_vectors, dense_rankings)
ported to chunks. The model comes from [dense] model in p2.toml and defaults to bge-small-en-v1.5.
Vectors have length 1, so one matrix product of the chunk vectors with the query vector gives every
cosine similarity; ChunkScorer lifts the chunk scores to documents (a document scores its best chunk).
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.model = cfg.table("dense").get("model", embed.BGE)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        if not len(self.chunks):
            return []
        query = self.embedder.encode([text])[0]
        return (self.vectors @ query).tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
