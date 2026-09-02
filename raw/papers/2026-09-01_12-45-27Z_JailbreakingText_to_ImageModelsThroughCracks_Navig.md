---
title: Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate
published: 2026-09-01T12:45:27Z
authors: Kaiyan Wen, Shijie Zhang, Lu Yu, Guangdong Bai
url: http://arxiv.org/abs/2609.01168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate

## Abstract
Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers.In this paper, we introduce the \emph{Detection Surface}, a unified geometric framework that characterizes the decision boundaries induced by heterogeneous T2I safety filters and their joint effect on the jailbreak search space. This formulation reveals that successful evasion is governed by a sparse and non-convex region shaped by cross-layer conflicts, where mutations that bypass one filter may increase exposure to another. Motivated by this analysis, we propose \emph{CRACK}, a multi-agent debate framework for adaptive jailbreak search that decomposes jailbreak search into exploration, diagnosis, and arbitration. CRACK coordinates an Attack Agent, a Defense Agent, and a Judge Agent to iteratively generate prompt mutations, obtain layer-specific diagnostic feedback, and optimize mutation strategies through reward-guided refinement. Through repeated rounds of debate, CRACK adapts its search direction to the evolving cross-layer constraints while preserving the original harmful intent. Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63\% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.

## Metadata
- **Published**: 2026-09-01T12:45:27Z
- **Authors**: Kaiyan Wen, Shijie Zhang, Lu Yu, Guangdong Bai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01168v1)