---
title: Beyond a Single Judge: Simulating Social Persona Panels for Generative UI Evaluation
published: 2026-07-30T16:13:36Z
authors: Zheng Wu, Yibo Luo, Pu Zhang, Cheng Yang, Zhuosheng Zhang
url: http://arxiv.org/abs/2607.28439v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond a Single Judge: Simulating Social Persona Panels for Generative UI Evaluation

## Abstract
Generative UI (GenUI) lets large language models synthesize a complete, renderable interface directly from a natural-language instruction, but evaluating the quality of what they generate remains an open problem. Human evaluation is costly and rater-variant, while LLM-as-a-judge is scalable but reflects only a single implicit viewpoint, unable to capture how different populations of real users actually perceive the same interface. We propose the Evidence-Grounded, Social-Weighted Persona Panel (ESPP), a three-stage GenUI evaluation method in which a panel of psychologically diverse, evidence-grounded personas independently rates a screenshot, exchanges opinions under a trait-derived, semantically-gated bounded-confidence mechanism, and is aggregated via Delphi-inspired social weighting into a single judgment. ESPP tracks human judgment substantially more closely than a naive single-pass judge, raising Pearson $r$ from $0.716$ to $0.922$, and a prompt-ensemble control recovers only about a third of this gap, isolating genuine persona and evidence grounding as the dominant source of improvement. Beyond this fidelity gain, retaining each panelist's individual rating further reveals that user subgroups agree on overall model rankings yet diverge sharply on specific rating dimensions, a structural disagreement a single homogeneous judge would systematically erase. The codes are available at https://github.com/Wuzheng02/ESPP.

## Metadata
- **Published**: 2026-07-30T16:13:36Z
- **Authors**: Zheng Wu, Yibo Luo, Pu Zhang, Cheng Yang, Zhuosheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28439v1)