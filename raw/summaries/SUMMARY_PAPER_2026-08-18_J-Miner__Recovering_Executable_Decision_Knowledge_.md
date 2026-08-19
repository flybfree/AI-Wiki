---
title: J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers
url: http://arxiv.org/abs/2608.17063v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_19-09-38Z_J_Miner_RecoveringExecutableDecisionKnowledgefromL.md
generated_at: 2026-08-18 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces J‑Miner, a method for extracting and encoding the internal decision knowledge of fine‑tuned language‑model classifiers into an explicit executable representation. By mining text‑level named concepts across layers and using classifier predictions to learn rules, J‑Miner distills local readouts into compact decision structures that reproduce up to 98.3 % of original decisions while improving behavioral fidelity.

## Key Takeaways
- J‑Miner aggregates vocabulary‑aligned internal signals from multiple layers and token positions to identify named concepts that reflect the semantic evidence behind classifier choices, turning distributed information into a coherent set of decision variables.
- The learned executable rules reproduce up to 98.3 % of source‑classifier decisions and outperform equally compact rule sets derived solely from input words by 6.0–29.5 percentage points in behavioral fidelity.
- A lightweight student can reconstruct the representation using only about one twenty‑fourth of the parameters of the original classifier, achieving 99.8 % of its mean task accuracy on reconstruction tasks.

## Context
Fine‑tuned language models excel at complex text judgments but hide their decision pathways within internal activations that are not directly accessible to users or downstream systems. Extracting this hidden knowledge is crucial for interpretability, transfer learning, and efficient model distillation, as it enables the creation of compact, reusable decision representations without retraining.

## Implications
For practitioners, J‑Miner offers a pathway to make black‑box classifiers more transparent by providing explicit rules that can be inspected and reused across tasks. This capability supports regulatory compliance, model auditing, and the development of smaller, specialized models that inherit performance from larger ones while preserving decision integrity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17063v1)
