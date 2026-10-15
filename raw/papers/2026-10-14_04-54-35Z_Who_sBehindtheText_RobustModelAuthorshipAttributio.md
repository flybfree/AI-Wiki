---
title: Who's Behind the Text? Robust Model Authorship Attribution
published: 2026-10-14T04:54:35Z
authors: Minseok Ko, Hyunseok Lee, Woomin Song, Beomjun Kim, Jinwoo Shin, Kunwoong Kim
url: http://arxiv.org/abs/2610.19583v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who's Behind the Text? Robust Model Authorship Attribution

## Abstract
As large language models (LLMs) are increasingly used to generate text, their misuse has become a growing societal problem, with implications for academic misconduct, model distillation, and cyberattacks. For these reasons, Model Authorship Attribution (MAA), which identifies the source model of a given text, is important for promoting the responsible use of LLMs and improving AI safety. In practice, attribution systems must remain reliable beyond the distributions observed during training. They may encounter texts from unseen domains and writing settings, as well as generations from future versions of model families that were not available when the system was trained. However, existing MAA methods often exhibit substantial performance degradation under such distribution shifts. To address this challenge, we propose Authorship Tracing via Likelihood-based Attribution of Sources (ATLAS), which formulates MAA through source-conditioned text modeling rather than direct source prediction. ATLAS learns how text from each source family is generated and attributes a given text by comparing its likelihood under each learned source condition. We aggregate this likelihood evidence at the token level with clipping so that no single token dominates the decision. We further introduce MAABench, a broad MAA benchmark for evaluating practical OOD settings such as domain and version. Our experiments show that ATLAS consistently outperforms existing baselines across MAABench and OpenTuringBench. In particular, when both the generation domain and the model version change on MAABench, ATLAS achieves 74.27% accuracy, 9.00pp higher than the strongest baseline. Beyond MAA, ATLAS can also help identify distillation source models by measuring which source model a target LLM most closely resembles. Our extended experiments show that ATLAS recovers the known teacher of every distilled model we evaluate.

## Metadata
- **Published**: 2026-10-14T04:54:35Z
- **Authors**: Minseok Ko, Hyunseok Lee, Woomin Song, Beomjun Kim, Jinwoo Shin, Kunwoong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19583v1)