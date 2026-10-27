---
title: Linear Probes Transfer from Base to Distilled Language Models despite Rotation
url: http://arxiv.org/abs/2610.35586v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_15-15-34Z_LinearProbesTransferfromBasetoDistilledLanguageMod.md
generated_at: 2026-10-27 00:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether linear probes—simple classifiers trained on a language model's internal activations to detect harmful prompts—can be reused unchanged when the underlying model is replaced by a distilled reasoning model or an instruction-tuned chat model. The author trains probes on four base models (Qwen2.5-Math-7B, Llama-3.1-8B, Qwen2.5-14B, Qwen2.5-32B) using the XSTest prompt set, then applies them directly to DeepSeek-R1 distilled successors and developer instruction-tuned variants. Despite the successor models rotating the decision boundary by 17° to 35°, the transferred probes show negligible AUC degradation (−0.011 to +0.027 on XSTest; −0.015 to +0.053 on an independent OR-Bench evaluation), demonstrating practical reusability across model families.

## Key Takeaways
- Linear probes trained on base models transfer to distilled reasoning successors (DeepSeek-R1) and instruction-tuned chat models with minimal performance loss, even though the internal representation geometry rotates by 17° to 35°. The AUC shift is statistically negligible (within ±0.05), meaning auditors can reuse a single probe across model releases rather than retraining for every new version.
- On XSTest, where safe prompts deliberately contain alarming-sounding words, probes reading internal activations outperform a prompt-text-only classifier by 0.15 to 0.20 AUC, confirming that the model's internal state encodes information beyond surface lexical cues. However, on OR-Bench prompts, this advantage shrinks to 0.03–0.20 AUC, and probes flag 29% to 42% of prompts that merely sound harmful but are benign, revealing that part of what probes detect is the appearance of harm rather than genuine harmfulness.
- The degree to which probes capture semantic meaning versus superficial textual patterns is highly test-set dependent. On adversarial sets like XSTest that stress-test surface cues, probes demonstrate genuine internal understanding; on more naturalistic benchmarks like OR-Bench, their advantage narrows, suggesting caution in generalizing probe reliability across evaluation regimes.

## Context
As language model deployment pipelines increasingly involve distillation (e.g., DeepSeek-R1 distilled from reasoning traces) and instruction tuning as standard post-training steps, safety auditing infrastructure must adapt to each new model release. Linear probes have become a popular lightweight auditing tool because they are cheap to train and run, but their practical value hinges on whether they survive model updates. This paper addresses a gap in the interpretability and safety literature: prior work on probing and representation geometry typically assumes a fixed model, while real-world deployment involves successive model versions with altered internal architectures. By quantifying the rotation of decision boundaries and the resulting transfer performance, the paper provides empirical grounding for whether safety auditing tools can be treated as portable assets across a model family.

## Implications
For practitioners and safety auditors, this work suggests that a single probe can be maintained across multiple model releases within a family, reducing the operational cost of safety monitoring and enabling faster deployment of successor models without re-auditing. However, the finding that probes partially detect the appearance of harm rather than harm itself—especially on naturalistic benchmarks—warns against over-reliance on probe-based classifiers as sole safety gates. Industry teams building model pipelines should treat probe transfer as a useful but incomplete safeguard, combining it with prompt-text classifiers and human review, and should validate probe behavior on diverse evaluation sets rather than a single adversarial benchmark before trusting transfer results in production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35586v1)
