---
title: From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners
published: 2026-09-11T08:31:23Z
authors: Frank Nie, Shuyao Wang, Ethan B. Liu
url: http://arxiv.org/abs/2609.12578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners

## Abstract
A compact controller can coordinate stronger experts by selecting whom to consult, formulating requests, and integrating their responses. We study whether learning from both the controller's decisions and the experts' reasoning and code improves its generation after expert removal. We introduce \textsc{Rivet} for \emph{collaboration internalization}: expert-augmented reinforcement learning applies a shared outcome signal to controller decisions and returned expert spans, and verified trajectory internalization consolidates complete successful interactions through format-aware supervised training. The deployed controller generates reasoning, code, and interaction structure with local Python execution and no external LLM. Across seven competition-mathematics benchmarks, RIVET-1.7B and RIVET-4B achieve average accuracies of $28.25\%$ and $44.16\%$; Stage~II improves RIVET-4B's accuracy after expert removal by $6.49$ points, and GPQA-Diamond results provide evidence of generalization to scientific reasoning. Ablations show gains from ordinary trajectory supervision and additional format weighting, supporting the effectiveness of training on the content and structure of verified collaborations.

## Metadata
- **Published**: 2026-09-11T08:31:23Z
- **Authors**: Frank Nie, Shuyao Wang, Ethan B. Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12578v1)