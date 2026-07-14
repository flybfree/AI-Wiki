---

title: "Summary: Augmenting Molecular Language Models with Local $n$-gram Memory"
url: http://arxiv.org/abs/2606.12113v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_14-07-18Z_AugmentingMolecularLanguageModelswithLocal_n__gram.md
generated_at: "2026-06-11 10:56"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-10 14-07-18Z Augmentingmolecularlanguagemodelswithlocal N  Gram


## Summary
The paper proposes MolGram, a method that adds an $n$-gram memory module to transformer models for SMILES strings. It improves generation and prediction tasks by injecting local pattern context without changing tokenization.

## Key Takeaways
- MolGram maps frequent local string patterns to learned embeddings using scalable hash lookups, providing an inductive bias that guides the model on chemically meaningful motifs.
- The module dynamically injects these regional embeddings into hidden states, allowing long-range dependencies to benefit from explicit local memory without extra parameters beyond a small lookup table.
- Experiments show MolGram outperforms baselines across unconditional generation, forward reaction prediction, and retrosynthesis with 3× more parameters than the added module.

## Context
In molecular language modeling, standard tokenization breaks chemical motifs into isolated characters, limiting models' ability to capture local structures. This work addresses that gap by embedding locality directly into neural representations.

## Implications
The approach demonstrates that lightweight inductive biases can boost performance in complex tasks like synthesis planning. Practitioners can adopt MolGram to improve model efficiency and accuracy without retraining from scratch.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12113v1)
