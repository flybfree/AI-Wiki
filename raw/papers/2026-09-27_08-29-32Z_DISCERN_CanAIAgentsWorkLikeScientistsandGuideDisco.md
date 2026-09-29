---
title: DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?
published: 2026-09-27T08:29:32Z
authors: Nan Huang, Mario Tapia-Pacheco, Kun Zhou, Yiming Huang, Kevin José Barrientos Díaz, Tiffany Amariuta, Jingbo Shang
url: http://arxiv.org/abs/2609.33357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?

## Abstract
Reliable automated research requires agents to vet data, verify analyses, and generate hypotheses grounded in trustworthy evidence, potentially reducing routine scientific workload while allowing scientists to focus on interpretation and discovery. Existing benchmarks often only assess analytical task completion or hypothesis generation separately rather than testing whether reliable evidence supports valid and novel claims. We introduce DISCERN (Data Integrity and Scientific Capability: Evidence, Reasoning, and Novelty), a controlled benchmark on real, publicly available datasets that evaluates three key levels of an automated research workflow. The first two levels test data integrity and analysis verification under confounds and tool traps, while the third tests hypothesis generation and revision under adversarial review, including counterfactual cases in which evidence consistent with real data and documented scientific phenomena conflicts with established expectations, motivating alternative explanations and testable hypotheses. Across 203 tasks, eight life-science tracks, and eight models, DISCERN shows that strong aggregate performance can mask level-specific weaknesses. Agents earn perfect scores in only 60.8% of Level 1, 34.2% of Level 2, and 0.6% of Level 3 evaluations, with penalties attributed to rejection of sound data, failure to carry recognized limitations into conclusions, and wide variation in hypothesis production. Cross-track rankings by token and code use are substantially more stable than rankings by evidence judgment, suggesting greater consistency in computational effort than in evidence-based reasoning. These profiles identify opportunities for supervised scientific assistance, but current agents do not yet demonstrate reliable autonomous analysis or discovery. Code and data: https://huggingface.co/datasets/discern-bench-anon/discern-benchmark

## Metadata
- **Published**: 2026-09-27T08:29:32Z
- **Authors**: Nan Huang, Mario Tapia-Pacheco, Kun Zhou, Yiming Huang, Kevin José Barrientos Díaz, Tiffany Amariuta, Jingbo Shang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33357v1)