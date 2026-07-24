---
title: Training Large Language Models for Self-Explanation Faithfulness
url: http://arxiv.org/abs/2607.21090v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_09-20-38Z_TrainingLargeLanguageModelsforSelf_ExplanationFait.md
generated_at: 2026-07-23 22:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a reinforcement learning framework that directly optimizes the faithfulness of language model self‑explanations, measuring how well generated reasoning mirrors internal decision factors. Experiments show fine‑tuned Llama3.1‑8B and Qwen3‑8B achieve substantial gains in Phi‑CCT scores, rising from near zero to around 0.664 on in‑distribution tasks.

## Key Takeaways
- The RL method uses the Phi‑CCT correlation metric as a per‑sample reward to train models to identify and disclose influential factors that affect their reasoning.  
- In‑distribution faithfulness scores improve dramatically, reaching up to 0.691 on held‑out tasks like StrategyQA, indicating better alignment with actual decision processes.  
- Cross‑intervention generalization is observed: a model trained only on random word insertions shows non‑zero transfer to user‑bias phrases, suggesting implicit learning of bias factors.

## Context
Current LLM research often evaluates or prompts for self‑explanations without directly improving the model’s internal generation. This work bridges that gap by embedding faithfulness into the training objective itself, moving beyond post‑hoc evaluation toward intrinsic alignment.

## Implications
By enabling models to learn and reveal decision factors, this approach reduces unfaithful reasoning at scale, offering practitioners a practical path to more trustworthy AI systems in high‑stakes domains such as medical or legal advice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21090v1)
