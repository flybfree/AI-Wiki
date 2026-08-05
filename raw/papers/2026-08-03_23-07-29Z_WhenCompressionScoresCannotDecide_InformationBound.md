---
title: When Compression Scores Cannot Decide: Information Boundaries for Group-Robust LLM Pruning
published: 2026-08-03T23:07:29Z
authors: Andrew Zhang
url: http://arxiv.org/abs/2608.02940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Compression Scores Cannot Decide: Information Boundaries for Group-Robust LLM Pruning

## Abstract
A reproducible compression statistic can still select the wrong candidate. A dense pruning score with 0.906 split-half reliability predicted a 16.1% gain. Its selected endpoint was 6.0% and 7.7% worse than two controls. We model the gap through information interfaces that delimit which distinctions each statistic supports. For equal-weight groups, a conic law gives the exact pooling price for positive linear fixed-candidate damage, including diagonal and full PSD second moments. Three two-world constructions and an exact observation-fiber radius characterize what pooled moments, group-local moments, and reference-path curvature leave unresolved. A group-resolved diagonal recovers broad damage order (Spearman 0.9239) while fine order remains weak. Relative to balanced uniform allocation, a coarse depth allocation cuts worst-group perplexity inflation by 12.6--20.9% across three dense LLMs. Model-specific complete-mask endpoint selection improves over those references by 2.7--8.0%. In OLMoE, router traces predict singleton direction (114/192 versus 81/192 under the strongest relabeling). Finite-menu decisions on one layer yield held-out worst-group KL reductions of 13.7% and 7.2%. Local measurements construct candidates. Selection is licensed by complete candidate endpoints or a validated uniform guarantee, with uncertainty calibrated to every comparison.

## Metadata
- **Published**: 2026-08-03T23:07:29Z
- **Authors**: Andrew Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02940v1)