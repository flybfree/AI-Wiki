---
title: EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair
url: http://arxiv.org/abs/2607.20019v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_10-59-46Z_EvoDRC_ASelf_EvolvingAgenticFrameworkforAutomatedD.md
generated_at: 2026-07-23 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
EvoDRC introduces a self‑evolving agentic framework for automatically repairing design rule check violations in integrated circuits. The approach reduces the overall repair effort by 73.5 % compared with existing baselines on seven block‑level designs from DAC26, demonstrating that continuous skill evolution can achieve substantial gains.

## Key Takeaways
- EvoDRC initializes layer‑specific repair skills using knowledge distilled from an unrelated reference design and then continuously evolves these skills based on traceable repair experience collected from the target layout.  
- The framework decomposes the layout into bounded repair regions, assigning a language model repair agent to each region while employing local DRC analysis, connectivity checking, and impact‑preview tools for feedback.  
- Repair operations and their resulting DRV changes are stored in a knowledge database that feeds back into skill evolution, creating a closed learning loop.

## Context
Automating DRC closure remains a bottleneck because manual change orders are time‑consuming and error‑prone. This paper contributes to the growing field of AI‑driven design automation by showing how continual skill refinement can outperform static rule‑based solvers on complex block designs, highlighting the potential for iterative learning in hardware synthesis.

## Implications
For industry practitioners, EvoDRC offers a scalable method to reduce manual intervention and accelerate layout iteration. Practitioners can integrate such self‑evolving repair agents into their design flow to maintain high‑quality, rule‑compliant circuits with minimal effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20019v1)
