---
title: InfraPatch: Cross-Task Targeted Grayscale Patch Attacks on Infrared-Adapted Vision-Language Models
url: http://arxiv.org/abs/2609.02233v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_07-42-27Z_InfraPatch_Cross_TaskTargetedGrayscalePatchAttacks.md
generated_at: 2026-09-02 21:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces InfraPatch, a method that creates digital grayscale patches to manipulate infrared-adapted vision-language models toward specific semantic targets. It demonstrates high success rates across various IR-VLM architectures and tasks, showing that small patches can reliably inject chosen behaviors under a controlled threat model.

## Key Takeaways
- InfraPatch achieves targeted attack success rates from 86% to 100% on ten infrared-adapted models using clean-conditioned criteria. - The framework optimizes patch placement with proxy guidance and task‑adaptive objectives, outperforming random placement by up to 10 percentage points. - Small grayscale patches within a ~5% local area can inject desired semantics across image classification, captioning, and binary VQA tasks.

## Context
Infrared vision-language models aim to extend perception beyond visible light, but their security has been underexplored compared to RGB counterparts. This work fills that gap by providing the first systematic analysis of patch‑based adversarial attacks on IR-VLMs, highlighting vulnerabilities in a growing class of low‑visibility AI systems.

## Implications
For developers deploying infrared multimodal systems, this research underscores the need for robust evaluation under realistic digital threats. Practitioners should consider patch‑level defenses and adaptive placement strategies to protect semantic integrity across diverse IR-VLM architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02233v1)
