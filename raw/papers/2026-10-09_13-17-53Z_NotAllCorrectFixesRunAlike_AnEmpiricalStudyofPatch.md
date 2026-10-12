---
title: Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution
published: 2026-10-09T13:17:53Z
authors: Han Peng, Xing Hu, Feifei Niu, Huan Li, Xin Xia
url: http://arxiv.org/abs/2610.13563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution

## Abstract
Repository-level issue-resolution benchmarks such as SWE-bench evaluate submitted patches primarily based on whether they pass the correctness tests, leaving the runtime performance of different test-passing patches largely unexplored. Evaluating patch performance is essential but challenging since designing performance workloads for each benchmark instance is costly. However, these benchmarks already provide a natural candidate: the built-in \emph{FAIL\_TO\_PASS} (F2P) tests, which exercise the behavior affected by the issue fix. We therefore investigate whether the provided F2P tests can be repurposed to evaluate patch performance. Overall, we choose four frontier models, Claude Opus~5, GPT~5.6, DeepSeek V4 Pro, and Qwen~3.8 Max, paired with SWE-agent to resolve the pre-filtered measurable corpus from verified splits of SWE-bench and SWE-bench-Live, yielding 262 cases with at least two different correct solutions, including the developer ground-truth patch. We then measure each solution's runtime performance in instruction count and wall-clock time on the native F2P test, and use Welch ANOVA instead of the RSD proposed in prior work as a more robust statistical discrimination criterion. We find that this methodology exhibits notable discrimination capability in runtime performance and identifies performance differences among patches in almost half of the instances. Our empirical study shows that the runtime performance of generated patches is independent of the issue resolution rate of LLMs, with nearly reversed model rankings. The case study also shows that the performance analysis reveals architectural regression in some patches that the correctness evaluation overlooked. These findings suggest that resolution rate does not adequately characterize LLMs' capability for repository-level issue resolution, motivating future evaluations to consider patch performance alongside it.

## Metadata
- **Published**: 2026-10-09T13:17:53Z
- **Authors**: Han Peng, Xing Hu, Feifei Niu, Huan Li, Xin Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13563v1)