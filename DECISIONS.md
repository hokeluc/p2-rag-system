# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose the Big Brother wiki to use as my corpus because I'm a big fan of the show and I know a decent amount about it's future and past seasons. I wanted to combine my subject matter with something that would be interesting to write queries for, and I also wanted to use something interesting that would fit within the licensing requirements.

I expect that rerank retrieval will perform the best, as the reranker agent has access to actual excerpts of the wiki pages, although it means a higher cost per query. The hybrid stage of the rerank process will capture term-matching and the semantic meaning of wiki pages well, and then the agent will have the final say in the ranking process with an actual pass through the candidates that hybrid retrieval returns.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

I chose to measure the rerank method with two different candidate choices as part of the stretch requirement. Instead of reranking 20 candidates, I chose to rerank 10 candidates and analyze whether the 'bottom 10' candidates from hybrid retrieval made a difference.

| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank | 0.733 | 0.775 | 0.723 |
| rerank_c10 | 0.592 | 0.683 | 0.596 |

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 305,186 | 4,533 | 90.2 | 15,259 | 227 | 4.5 |
| traces/shared-practice-rerank_c10.jsonl | rerank_c10 | 20 | 20 | 0 | 245,172 | 5,855 | 105.1 | 12,259 | 293 | 5.3 |

The first table shows that the 20-candidate reranker performed much better than the 10-candidate reranker, with at least an 8.8% increase across each metric. However, the 10-candidate reranker completed at 85% the time of the 20-candidate reranker and used 25% less tokens. I chose to use the 20-candidate reranker as the baseline for recall and keep the 10-candidate reranker as the stretch: The change in recall, MRR, and nDCG@10 was too much of a loss in performance in exchange for a small gain of time and cost in tokens used. Using the 10-candidate reranker would save me more time and money, but $0.0060 in tokens (approx ~3000 tokens with Sonnet 5.5) is a negligible amount of money (personally) for 20 Claude calls.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

It didn't happen. I disagreed with some of the answers output during the test process for the shared corpus and what was left out, but that's not really something I should overrule, as we were testing the agent. I may not trust some numbers, but I didn't overrule the agent at any point in the process. In the case that the scoring tables weren't a deterministic process set up by the project, I would have asked Claude for a verification file or written a script to calculate the metrics myself and then overruled it's numbers if it hallucinated any metric or used the wrong source comparison (i.e. interval tables).

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

I don't trust this number and finding:

| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.600 | 0.950 | -0.350 | [-0.700, -0.050] | claude higher |

Because my gold set is so small (30 queries), I think the upper bound of the 95% interval being so close to 0 could just be noise on my set's behalf. I didn't do anything to test it, but in order for me to trust it, I would have to extend my gold set to a larger amount of queries to trust the 95% interval given. I think my gold set could still introduce some noise when used for evaluation because thirty queries across three different query types is still not large enough of a dataset.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

The answers for my own corpus's gold set are not completely sound. I mention this in my failure analysis, but some of the relevant documents that were returned actually fit the question I was looking to answer more than the documents I had originally labeled as the source of truth (i.e. winners page not returning.. the winners.) This impacts evaluating the different retrieval metrics on my gold set, so next I'd like to ideally increase the size of my gold set and do a much more in-depth reading of the corpus documents or modify qrels.txt to support the idea of multiple documents influencing the answer. In terms of my existing corpus, I think the corpus would need to be thoroughly santized and cleaned up past ingestion in a production environment. I would also gain confidence in evaluating on my own gold set from getting multiple perspectives of the 'source of relevance' for the hand/claude-written queries.
