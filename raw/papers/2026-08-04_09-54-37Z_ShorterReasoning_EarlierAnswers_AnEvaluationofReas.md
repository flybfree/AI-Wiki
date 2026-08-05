---
title: Shorter Reasoning, Earlier Answers? An Evaluation of Reasoning Interfaces
published: 2026-08-04T09:54:37Z
authors: Francesca Carlon, Vincent Ginis, Andres Algaba
url: http://arxiv.org/abs/2608.03401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shorter Reasoning, Earlier Answers? An Evaluation of Reasoning Interfaces

## Abstract
Large language models often reason at length before answering, increasing cost and latency. Prompts and trained settings can shorten this reasoning, but a shorter trace may only show that the model stopped sooner. Here, we evaluate paired runs of the same question at matched reasoning horizons across 198 GPQA Diamond and 500 MMLU-Pro questions. We test a numeric/concision prompt that announces a token limit for Qwen3-14B and the trained effort settings of gpt-oss-20b and -120b. The Qwen prompt shortens reasoning traces by 12-17%, while accuracy changes at matched token limits are small and mixed. A concise/early-answer instruction raises MMLU-Pro accuracy by 3.8 percentage points at 512 tokens, including +2.7 points when both runs are unfinished. Its gain at 2,048 tokens is uncertain. For gpt-oss, candidate-logit answers from completed low- and medium-effort reasoning are 14.5-26.3 points more accurate than matched-horizon high-effort answers. Most of the 512-token advantage comes from lower effort finishing earlier, while differences among unfinished runs are smaller and mixed. Wrong early answers often concentrate probability on the chosen option, so earlier stopping does not uniformly improve probability quality. In these tests, a tight deadline can favor lower effort or a concise instruction, whereas allowing high effort to finish can recover higher final accuracy. Evaluations should report correct completion before a deadline, the answer obtained when a run is stopped, differences among unfinished runs, and probability assigned to the correct answer separately.

## Metadata
- **Published**: 2026-08-04T09:54:37Z
- **Authors**: Francesca Carlon, Vincent Ginis, Andres Algaba
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03401v1)