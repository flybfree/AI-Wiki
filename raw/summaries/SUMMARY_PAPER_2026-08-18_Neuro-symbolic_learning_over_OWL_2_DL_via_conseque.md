---
title: Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits
url: http://arxiv.org/abs/2608.17741v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_13-04-51Z_Neuro_symboliclearningoverOWL2DLviaconsequence_bas.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Baobab, a neuro‑symbolic learning system that translates an OWL 2 DL ontology grounded in the SROIQ description logic into a Sentential Decision Diagram (SDD) using consequence‑based compilation. The SDD serves as a differentiable circuit whose evidence‑conditioned model counts train a convolutional network to recognize MNIST digits under partial ABox supervision, demonstrating that learned mixtures can outperform single‑model ensembles in reasoning shortcut scenarios.

## Key Takeaways
- Baobab compiles the full SROIQ ontology into an SDD that separates propositional core evidence from active domain features such as nominals and role axioms.  
- The SDD’s weighted model count provides supervision for a CNN, yet when multiple ontologically consistent completions exist, independent perception collapses onto one, revealing a reasoning shortcut.  
- A mixture indexed by query justifications can represent the calibrated posterior, achieving Bayes‑optimal performance where single‑WMC and learned mixtures fail.

## Context
Neuro‑symbolic approaches aim to fuse symbolic knowledge representation with neural pattern recognition, but prior systems either ignore classical entailment or limit themselves to Horn fragments. Baobab addresses this gap by handling the full SROIQ logic while maintaining a differentiable representation that can be trained on real data.

## Implications
The work shows that reasoning shortcuts in non‑Horn description logics can be mitigated with calibrated mixtures, offering a practical path for robust AI systems that rely on symbolic knowledge. Practitioners may leverage Baobab’s compiler to integrate complex ontologies into neural models without sacrificing interpretability or performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17741v1)
