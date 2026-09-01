---
title: Wrong Prediction, Right Answer: Recovering Evidence from Collapsed LLM Sequence Scores
url: http://arxiv.org/abs/2608.31068v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_16-43-55Z_WrongPrediction_RightAnswer_RecoveringEvidencefrom.md
generated_at: 2026-08-31 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large language models sometimes give zero scores on reasoning benchmarks despite retaining correct internal representations. It shows that hidden‑state probes can decode answers when sequence scoring collapses, indicating the model’s logic persists beyond output bias. The authors recover performance by fitting a minimal additive correction to unlabeled data.

## Key Takeaways
- Hidden‑state probes successfully decode correct answers when native sequence scores drop, showing internal reasoning survives output collapse.
- Fitting two parameters on only 25 unlabeled examples recovers up to 34 accuracy points for Qwen3.5 and transfers to smaller models like OLMo‑2‑1B and Llama‑3.1‑8B.
- The recovered decisions outperform count‑preserving permutation baselines and are not explained by simple lexical overlap.

## Context
Current benchmarks often conflate output failure with true reasoning inability, leading to overstated model limitations. This study highlights that structural biases can mask latent logic, suggesting a need for more nuanced evaluation beyond surface scores.

## Implications
Practitioners should treat zero‑shot reasoning drops as expression problems rather than capability gaps, allowing targeted fixes without retraining large models. The findings encourage designing lightweight diagnostics that preserve model utility while improving benchmark alignment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.31068v1)
