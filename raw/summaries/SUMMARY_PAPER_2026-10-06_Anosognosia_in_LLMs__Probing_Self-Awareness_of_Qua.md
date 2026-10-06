---
title: Anosognosia in LLMs: Probing Self-Awareness of Quantized Computational Substrate
url: http://arxiv.org/abs/2610.06174v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_11-55-01Z_AnosognosiainLLMs_ProbingSelf_AwarenessofQuantized.md
generated_at: 2026-10-06 01:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models can recognize degradation in their own computational substrate caused by quantization, drawing inspiration from anosognosia, a condition in which individuals fail to recognize their own impairments. It finds that models generally cannot self-report their quantization state from generated text, but internal representations contain detectable method-specific fingerprints that can be probed or partially learned.

## Key Takeaways
- Existing models fail to self-report their quantization state even when provided with their own generated text as an external cue, showing that generated outputs carry almost no trace of quantization-induced degradation and cannot reliably support self-monitoring.
- Linear probing reveals that internal representations contain clear, method-specific fingerprints of quantization, indicating that degradation is encoded in hidden states even when it is not visible in the model’s outputs.
- Training can help models identify severely degraded outputs, such as those from 4-bit models, by comparison, but models still fail to detect such degradation from a single output, and a shared LoRA trained across quantization levels does not generalize to unseen quantization methods.

## Context
As large language models are increasingly deployed using quantization, pruning, distillation, and other efficiency techniques, understanding whether they can monitor their own computational degradation becomes important for reliability, safety, and interpretability. By connecting model introspection to the neurological concept of anosognosia, the paper highlights that self-awareness in LLMs may depend more on access to internal representations than on observation of generated outputs.

## Implications
For practitioners, the results suggest that model self-reports should not be trusted as reliable indicators of quantization-induced degradation, and that external diagnostics or internal representation probes are likely more effective. For the broader field, the work underscores fundamental limits in generalizable LLM self-monitoring and cautions against assuming that models can robustly recognize changes to their own computational substrate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06174v1)
