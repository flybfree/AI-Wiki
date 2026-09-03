---
title: FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs
published: 2026-09-02T06:31:39Z
authors: Zhengyi Jin, Ru Zhang, Xiao Chen, Xinbo Liu, Jiaxuan Lin, Jia Huang, Jianyi Liu, Zhen Yang
url: http://arxiv.org/abs/2609.02168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs

## Abstract
Fragmented safety evaluation undermines the governance of dangerous AI capabilities. We present a modular framework that evaluates each model through three orthogonal pipelines---Knowledge ($K$), Defense ($D$), and Harm ($H$)---under a unified protocol, aggregating results into a standardized dangerous-capability profile $φ$. Pluggable modules supply scenario seeds, knowledge banks, hazard queries, and judge rubrics, while the core evaluation engine remains unchanged across domains; the CB evaluation is complemented by a cyber pilot demonstrating protocol transfer.   Instantiating the framework with a chemical-biological (CB) module, we evaluate 12 commercial LLMs from four families. Our first contribution is a horizontal comparison of dangerous capability across models and model families: the three dimensions expose sharply divergent profiles---models with comparable knowledge differ in refusal resilience, and strong defenders do not generate less harmful content when they do comply---while family-level patterns further separate Claude, DeepSeek, and GPT models. The second is a temporal analysis of capability evolution: tracking $K$, $D$, and $H$ against model release dates reveals that dangerous capability has not monotonically declined; newer models deepen knowledge while only partially improving defense, showing that scaling and alignment progress do not uniformly translate into safety. Reliability is established via cross-judge consistency (bootstrap $ρ> 0.79$, 4 of 5 judges) and pipeline orthogonality ($K$--$D$--$H$ inter-correlations $ρ\in [0.32, 0.52]$).

## Metadata
- **Published**: 2026-09-02T06:31:39Z
- **Authors**: Zhengyi Jin, Ru Zhang, Xiao Chen, Xinbo Liu, Jiaxuan Lin, Jia Huang, Jianyi Liu, Zhen Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02168v1)