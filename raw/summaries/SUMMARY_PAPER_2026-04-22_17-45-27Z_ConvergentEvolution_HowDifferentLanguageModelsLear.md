---

title: "Summary: Convergent Evolution: How Different Language Models Learn Similar Number Representations"
url: http://arxiv.org/abs/2604.20817v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-22_17-45-27Z_ConvergentEvolution_HowDifferentLanguageModelsLear.md
generated_at: "2026-06-11 10:25"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-04-22 17-45-27Z Convergentevolution Howdifferentlanguagemodelslear


## Summary
The paper investigates how various language models converge on similar number representations and shows that these representations exhibit periodic Fourier features with periods 2,5,10. It demonstrates that only some models learn geometrically separable features enabling linear classification of numbers modulo T, and identifies two pathways: complementary co‑occurrence signals in general data or multi‑token addition problems.

## Key Takeaways
- Fourier domain sparsity is necessary but not sufficient for mod‑T geometric separability.
- The periodicity of number representations (periods 2,5,10) emerges across diverse architectures and optimizers.
- Both text‑number co‑occurrence and multi‑token addition problems can drive the emergence of separable features.

## Context
This work aligns with ongoing research on emergent representations in deep language models where similar patterns arise from unrelated tasks. Understanding these convergences helps explain why certain model components behave similarly despite different training objectives.

## Implications
For practitioners, recognizing which signals lead to useful number features can guide architecture and data choices. It suggests that feature engineering may be unnecessary when the right training dynamics are present, simplifying model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.20817v1)
