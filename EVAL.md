# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Each model that explicitly looks at chunks splits documents
into chunks of 300 words, with each chunk other than the first
using a pre-chunk overlap window of 50 words as to minimize
truncating sentences.

The `dense` retrieval strategy uses the dense retrieval model to encode each document's chunk, which then is combined with the encoded query to form the matrix product/cosine similarity between the chunk and the query vector. Each document is scored off of its best-performing chunk.

The `hybrid` retrieval strategy uses both dense retrieval and the BM25 algorithm to address term and semantic match goals in the same strategy. For each score per algorithm, the strategy uses reciprocal rank fusion to aggregate the results of the two algorithms. My implementation uses ``p2.toml`` to allow the user to specify the constant term for RRF, but the default is ``k = 60.``

The `rerank` retrieval strategy uses the `hybrid` strategy to initially rank the documents in relation to the query, and then uses structured output definitions, a (potentially truncated) document, and an accompanying prompt to pass to an LLM agent to rerank the documents.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.733 | 0.775 | 0.723 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.643 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 0.917 |
| rerank | nDCG@10 | 0.659 | 0.614 | 0.925 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.108 | [-0.133, +0.350] | 0.351 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.268 | [+0.026, +0.508] | 0.349 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.205 | [-0.024, +0.428] | 0.329 | not distinguishable |
| rerank minus dense | Recall@10 | +0.175 | [+0.033, +0.333] | 0.221 | rerank higher |
| rerank minus dense | MRR@10 | +0.212 | [+0.071, +0.383] | 0.231 | rerank higher |
| rerank minus dense | nDCG@10 | +0.243 | [+0.103, +0.402] | 0.219 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.142 | [+0.050, +0.258] | 0.160 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.304 | [+0.140, +0.482] | 0.249 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.280 | [+0.150, +0.417] | 0.194 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

The 95% PI for the difference in strategy by metric tells us if we can confidently say that
a strategy is better for a corpus given the bootstrap distribution. If 0 is included in the distribution, we can't conclude the strategies are distinguishable in a specific direction.

All pairs that did not include rerank were indistiguishable from each other for every metric.
That means that the hybrid and dense strategies are not indistinguishable, as well as the hybrid / BM25 and dense / BM25 strategies.

The rerank strategy performs better than the dense retrieval and hybrid strategies across all three strategies. The rerank strategy performs better than BM25 on the Recall and MRR metrics, but is indistinguishable to BM25 on the nDCG metric, so it could be argued that both algorithms return documents with similar amounts of relevance to the query at hand.

The minimum detectable difference at 20 queries is the threshold in which the difference in means for the pair is a statistically significant result. Below that threshold, the difference in means is not statistically significant, and can be attributed to irreducible noise in data.

The numbers above support the idea of the massive gains in retrieval outcomes when an LLM-assisted rerank step is added to an existing retrieval algorithm strategy. The scores by metric per query class also support the idea of BM25 and Dense retrieval achieving specific purposes - matching on exact terms and words vs. matching on semantic meaning. The hybrid and rerank algorithm show the gains on mixed queries and all queries as a result of their combined and LLM-assisted extra approaches respectively.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I used the rerank system to answer the test questions, as it was the best performing with a small time and token cost compared to the other strategies.

Keeping `prompts/answer.txt` as is returns a 100% verified and 100% declined score.
Commenting out the structured notes (third line) in `prompts/answer.txt` returns the same metrics above.
Commenting out the answer directions (second line) also returns the same metrics above, which means the structured output does a lot of heavy lifting. I can verify separate Claude calls were made because results were not cached and each check took at least a few seconds to run (>3.4 s).

```
"claims": [
        {
          "text": "The operator must contact MSHA within 15 minutes at the toll-free number once it knows or should know an accident involving death occurred.",
          "chunk_id": "cfr30-50.10#0",
          "quote": "The operator shall immediately contact MSHA at once without delay and within 15 minutes at the toll-free number, 1-800-746-1553, once the operator knows or should know that an accident has occurred involving:\n\n(a) A death of an individual at the mine;"
        }
      ],

"claims": [
        {
          "text": "The incombustible content of the combined coal dust, rock dust, and other dust shall be not less than 80 percent where rock dust is required.",
          "chunk_id": "cfr30-75.403#0",
          "quote": "it shall be distributed upon the top, floor, and sides of all underground areas of a coal mine and maintained in such quantities that the incombustible content of the combined coal dust, rock dust, and other dust shall be not less than 80 percent."
        },
        {
          "text": "This 80 percent baseline applies specifically in the absence of methane; the requirement increases only when methane is present.",
          "chunk_id": "cfr30-75.403#0",
          "quote": "Where methane is present in any ventilating current, the percent of incombustible content of such combined dust shall be increased 0.4 percent for each 0.1 percent of methane."
        }
      ],

"claims": [
        {
          "text": "Evacuation drills must be held at least once every six months.",
          "chunk_id": "cfr30-57.4361#0",
          "quote": "At least once every six months, mine evacuation drills shall be held to assess the ability of all persons underground to reach the surface or other designated points of safety within the time limits of the self-rescue devices that would be used during an actual emergency."
        }
      ],
```

Investigating each claim vs. quote for three 'verified' answers:
- The first answer's claim supports the quote from the documents, but is less urgent in tone and leaves out the toll-free number. I would argue the toll-free number should be included in the response given the precariousness of the answer.
- The second answer's first claim supports the quote from the documents. The second claim also supports the quote, but leaves out the quantifiable metrics that defines the increase in the requirement. However, the original question didn't ask for an answer with the presence of methane, so I would define the answer as acceptable.
- The third answer's first claim summarizes the document's quote well and eliminates jargon that can be reasonably assumed (i.e. yes, you need to leave the mine in a normal fashion. Duh.)

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

The corpus is the Big Brother US pages extracted from the Big Brother Wikia, a fan-maintained Big Brother wiki. The corpus contains the season pages for every Big Brother US season, along with every Big Brother US competition, twist, and alliance. Individual houseguest pages were left out to conserve token costs, primarily because alliance and season pages are also included. I was unsure whether to include every single competition, but I figured that might provide more insight into what competitions specific houseguests would have won, so it provides information that wouldn't exist in the corpus otherwise. 

Content on the Big Brother Wiki is licensed under the Creative Commons Attribution-Share Alike License 3.0 (CC-BY-SA), unless otherwise specified.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

I wrote 10 queries myself (`hand` origin) and Claude wrote 20 queries (`claude` origin), but I labeled all the top relevant documents for the overall 30 queries. I used the same classes as the test queries for the shared corpus - identifier, paraphrase, and mixed, because I thought they fit my corpus well; Identifier queries quoted exact page titles or terms, paraphrase worded page content differently, and mixed queries combined the two strategies as expected.

I know the show pretty well, so I wrote queries with a specific term or document in mind, thus I had an idea of which documents would be relevant, and then challenged my assumption by viewing those documents to ensure the document for a specific twist, season, or feature of the game had information I was actually looking for. I turned this into a rule: If the page should be the source of truth for the query and directly addressed what the query is asking, it is a relevant document for that query. (i.e. if someone asks about the Cookout alliance, the Cookout alliance wiki page is a relevant document.)
Some queries quote a twist from a specific season, but pages for both the season and twist exist, so I chose the twist page as the more relevant page because it should theoretically go into depth more than the overall season page. This (and my relevance rule) may be a flawed idea, which may appear in my scoring and results.

I am already familiar with the corpus, so I read all of the pages I was looking for that were related to my queries to find candidates. I did not look at the system's top ten candidates, nor did I read all of the pages in the corpus (The season pages begin to follow the same format after a while with the same general info per-season.)

I used binary labels.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.833 | 0.681 | 0.717 |
| dense | 0.867 | 0.804 | 0.819 |
| hybrid | 0.867 | 0.784 | 0.803 |
| rerank | 0.933 | 0.894 | 0.904 |
| ablation/bm25_lab | 0.800 | 0.670 | 0.701 |

30 judged queries; nDCG uses binary labels; a random ranking of the 526 documents would get recall@10 near 0.019.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=9) | paraphrase (n=10) | mixed (n=11) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.889 | 0.800 | 0.818 |
| bm25 | MRR@10 | 0.889 | 0.561 | 0.619 |
| bm25 | nDCG@10 | 0.889 | 0.619 | 0.665 |
| dense | Recall@10 | 1.000 | 0.700 | 0.909 |
| dense | MRR@10 | 1.000 | 0.562 | 0.864 |
| dense | nDCG@10 | 1.000 | 0.595 | 0.876 |
| hybrid | Recall@10 | 1.000 | 0.800 | 0.818 |
| hybrid | MRR@10 | 0.907 | 0.636 | 0.818 |
| hybrid | nDCG@10 | 0.928 | 0.673 | 0.818 |
| rerank | Recall@10 | 1.000 | 0.900 | 0.909 |
| rerank | MRR@10 | 1.000 | 0.900 | 0.803 |
| rerank | nDCG@10 | 1.000 | 0.900 | 0.830 |
| ablation/bm25_lab | Recall@10 | 0.889 | 0.800 | 0.727 |
| ablation/bm25_lab | MRR@10 | 0.889 | 0.544 | 0.604 |
| ablation/bm25_lab | nDCG@10 | 0.889 | 0.606 | 0.633 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.600 | 0.950 | -0.350 | [-0.700, -0.050] | claude higher |
| bm25 | MRR@10 | 0.500 | 0.771 | -0.271 | [-0.588, +0.047] | not distinguishable |
| bm25 | nDCG@10 | 0.526 | 0.813 | -0.286 | [-0.600, +0.017] | not distinguishable |
| dense | Recall@10 | 0.800 | 0.900 | -0.100 | [-0.400, +0.150] | not distinguishable |
| dense | MRR@10 | 0.662 | 0.875 | -0.212 | [-0.512, +0.075] | not distinguishable |
| dense | nDCG@10 | 0.695 | 0.882 | -0.187 | [-0.468, +0.087] | not distinguishable |
| hybrid | Recall@10 | 0.800 | 0.900 | -0.100 | [-0.400, +0.150] | not distinguishable |
| hybrid | MRR@10 | 0.628 | 0.863 | -0.235 | [-0.561, +0.086] | not distinguishable |
| hybrid | nDCG@10 | 0.666 | 0.872 | -0.206 | [-0.510, +0.080] | not distinguishable |
| rerank | Recall@10 | 0.900 | 0.950 | -0.050 | [-0.300, +0.150] | not distinguishable |
| rerank | MRR@10 | 0.850 | 0.917 | -0.067 | [-0.300, +0.133] | not distinguishable |
| rerank | nDCG@10 | 0.863 | 0.925 | -0.062 | [-0.299, +0.126] | not distinguishable |
| ablation/bm25_lab | Recall@10 | 0.600 | 0.900 | -0.300 | [-0.650, +0.000] | not distinguishable |
| ablation/bm25_lab | MRR@10 | 0.483 | 0.763 | -0.279 | [-0.599, +0.047] | not distinguishable |
| ablation/bm25_lab | nDCG@10 | 0.513 | 0.795 | -0.282 | [-0.597, +0.030] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.050 | -0.200 | +0.250 | [+0.000, +0.550] | not distinguishable |
| MRR@10 | -0.104 | -0.163 | +0.059 | [-0.226, +0.368] | not distinguishable |
| nDCG@10 | -0.069 | -0.168 | +0.100 | [-0.169, +0.399] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.85 (10 queries), claude 0.83 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | +0.033 | [-0.100, +0.167] | 0.212 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.123 | [-0.026, +0.274] | 0.220 | not distinguishable |
| dense minus bm25 | nDCG@10 | +0.102 | [-0.038, +0.243] | 0.205 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.033 | [-0.100, +0.167] | 0.212 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.104 | [-0.019, +0.217] | 0.171 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | +0.086 | [-0.028, +0.187] | 0.155 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.000 | [-0.100, +0.100] | 0.134 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.020 | [-0.125, +0.082] | 0.151 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.016 | [-0.107, +0.070] | 0.128 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.100 | [-0.033, +0.233] | 0.206 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.214 | [+0.074, +0.359] | 0.207 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.187 | [+0.059, +0.325] | 0.192 | rerank higher |
| rerank minus dense | Recall@10 | +0.067 | [-0.067, +0.200] | 0.187 | not distinguishable |
| rerank minus dense | MRR@10 | +0.090 | [-0.028, +0.225] | 0.183 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.085 | [-0.030, +0.214] | 0.176 | not distinguishable |
| rerank minus hybrid | Recall@10 | +0.067 | [+0.000, +0.167] | 0.130 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.110 | [-0.003, +0.237] | 0.175 | not distinguishable |
| rerank minus hybrid | nDCG@10 | +0.101 | [+0.002, +0.215] | 0.152 | rerank higher |
| ablation/bm25_lab minus bm25 | Recall@10 | -0.033 | [-0.100, +0.000] | 0.093 | not distinguishable |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.011 | [-0.028, +0.000] | 0.022 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.016 | [-0.044, +0.000] | 0.035 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.067 | [-0.233, +0.100] | 0.230 | not distinguishable |
| ablation/bm25_lab minus dense | MRR@10 | -0.135 | [-0.287, +0.018] | 0.223 | not distinguishable |
| ablation/bm25_lab minus dense | nDCG@10 | -0.118 | [-0.265, +0.027] | 0.214 | not distinguishable |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.067 | [-0.233, +0.100] | 0.230 | not distinguishable |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.115 | [-0.237, +0.013] | 0.181 | not distinguishable |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.102 | [-0.218, +0.020] | 0.172 | not distinguishable |
| ablation/bm25_lab minus rerank | Recall@10 | -0.133 | [-0.300, +0.000] | 0.222 | not distinguishable |
| ablation/bm25_lab minus rerank | MRR@10 | -0.225 | [-0.374, -0.083] | 0.215 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.203 | [-0.347, -0.070] | 0.204 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

TODO: write what your own-corpus intervals let you claim.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/bm25_lab minus bm25 | Recall@10 | -0.033 | [-0.100, +0.000] | 0.093 | not distinguishable |
| ablation/bm25_lab minus bm25 | MRR@10 | -0.011 | [-0.028, +0.000] | 0.022 | not distinguishable |
| ablation/bm25_lab minus bm25 | nDCG@10 | -0.016 | [-0.044, +0.000] | 0.035 | not distinguishable |
| ablation/bm25_lab minus dense | Recall@10 | -0.067 | [-0.233, +0.100] | 0.230 | not distinguishable |
| ablation/bm25_lab minus dense | MRR@10 | -0.135 | [-0.287, +0.018] | 0.223 | not distinguishable |
| ablation/bm25_lab minus dense | nDCG@10 | -0.118 | [-0.265, +0.027] | 0.214 | not distinguishable |
| ablation/bm25_lab minus hybrid | Recall@10 | -0.067 | [-0.233, +0.100] | 0.230 | not distinguishable |
| ablation/bm25_lab minus hybrid | MRR@10 | -0.115 | [-0.237, +0.013] | 0.181 | not distinguishable |
| ablation/bm25_lab minus hybrid | nDCG@10 | -0.102 | [-0.218, +0.020] | 0.172 | not distinguishable |
| ablation/bm25_lab minus rerank | Recall@10 | -0.133 | [-0.300, +0.000] | 0.222 | not distinguishable |
| ablation/bm25_lab minus rerank | MRR@10 | -0.225 | [-0.374, -0.083] | 0.215 | rerank higher |
| ablation/bm25_lab minus rerank | nDCG@10 | -0.203 | [-0.347, -0.070] | 0.204 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/bm25_lab against bm25 (the name bm25_lab starts with bm25_): it helped 0 queries, hurt 2 and left 28 unchanged.

| Query | Class | Origin | bm25 RR | ablation/bm25_lab RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c18 | mixed | claude | 0.167 | 0.000 | -0.167 | hurt |
| o05 | paraphrase | hand | 0.500 | 0.333 | -0.167 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

TODO: write the ablation: the one change, the hypothesis, the result and the claim.

I predict changing the BM25 tokenizer to the tokenizer used in the lab will lower my MRR@10 metrics across the shared corpus because the lab tokenizer is a lighter version of the current tokenizer used for learning purposes and not optimized for creating optimal tokens.

The BM25 ablation vs the normal BM25 algorithm on the shared corpus is not distinguishable in terms of the interval drawn from the bootstrap distribution in terms of MRR, Recall, and nDCG metrics, but when applied on my own corpus, the ablation gives a worse reciprocal rank metric in some cases when compared to the normal BM25 algorithm. 

These metrics do not support my original hypothesis that MRR@10 is significantly worse as a result of the ablation, but the results do show that for some corpora and query combination the lab ablation results in a lower reciprocal rank. However, across my own corpora, 28 queries were left unchanged. Thus, the ablation doesn't impose a large change in performance across the RAG, coinciding with the conclusion from my hypothesis surrounding the shared corpus.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|c09|big-brother-13-us|golden-key|---|---|
|c20|big-brother-7-us|returning-players|---|---|
|o07|winners-us|big-brother-4-us|---|---|
|o10|the-icons|big-brother-28-us|---|---|


---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 12 | 225,664 | 13,231 | 176.5 | 18,805 | 1,103 | 14.7 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 0 | 440,775 | 7,240 | 140.1 | 14,692 | 241 | 4.7 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 305,186 | 4,533 | 90.2 | 15,259 | 227 | 4.5 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 40 | 581,168 | 17,450 | 257.5 | 14,529 | 436 | 6.4 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.268 | [-0.508, -0.026] | 15,259 | 4.5 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.212 | [-0.383, -0.071] | 15,259 | 4.5 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.304 | [-0.482, -0.140] | 15,259 | 4.5 | rerank higher |
| own: bm25 minus rerank | 30 | -0.214 | [-0.359, -0.074] | 14,692 | 4.7 | rerank higher |
| own: dense minus rerank | 30 | -0.090 | [-0.225, +0.028] | 14,692 | 4.7 | not distinguishable |
| own: hybrid minus rerank | 30 | -0.110 | [-0.237, +0.003] | 14,692 | 4.7 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-bm25_lab.jsonl | bm25_lab | 30 | 0.03 | 1.1 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.04 | 1.2 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.15 | 5.2 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.20 | 6.7 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.03 | 1.7 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.15 | 7.7 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.19 | 9.6 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.08 | 1.9 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.30 | 7.5 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.41 | 10.2 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
