---
title: CoMPASS: Collaborative Molecular Property Prediction via Adaptive Small-Large Model Synergy
url: http://arxiv.org/abs/2608.30674v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_12-14-01Z_CoMPASS_CollaborativeMolecularPropertyPredictionvi.md
generated_at: 2026-08-31 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoMPASS, a framework that combines a graph attention network with large language model reasoning to improve molecular property prediction. By retrieving relevant training molecules and using an agreement-aware gate, the system reduces LLM interference in high-confidence predictions while enhancing accuracy where uncertainty exists. Experiments on six classification and two regression benchmarks show measurable gains.

## Key Takeaways
- CoMPASS uses a retrieval-calibrated approach that grounds LLMs with evidence from locally relevant training molecules rather than relying solely on prompting.
- The agreement-aware gate limits LLM correction to cases where the model is uncertain, preserving high-confidence predictions unchanged.
- Ablations confirm that validation-calibrated retrieval and bounded fusion are essential for performance improvements.

## Context
Current molecular property prediction struggles with balancing statistical reliability and chemical reasoning. Graph neural networks offer reliable outputs but lack interpretability, while LLMs provide rationales but are not quantitative. Integrating these two paradigms remains a key research challenge.

## Implications
This work demonstrates that generative AI can act as an auxiliary corrector rather than a replacement for calibrated models, offering a scalable method to boost prediction accuracy in drug discovery and materials science. Practitioners can adopt the retrieval-calibrated framework to improve model robustness without sacrificing interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30674v1)
