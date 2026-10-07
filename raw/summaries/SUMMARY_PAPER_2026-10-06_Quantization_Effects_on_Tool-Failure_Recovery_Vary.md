---
title: Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs
url: http://arxiv.org/abs/2610.07781v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_05-17-10Z_QuantizationEffectsonTool_FailureRecoveryVaryAcros.md
generated_at: 2026-10-06 21:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper examines whether post-training quantization changes language-model agents’ ability to recover from temporary tool failures, using deterministic tool-use tasks and multiple prompts. It finds that comparisons between 8-bit and 4-bit variants of Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct are not stable, because the apparent winner can reverse depending on prompt, task screening, evaluation target, and executor leniency. The main conclusion is that robustness claims about quantized agents require matched task sets, full-pipeline reporting, explicit scoring policies, and uncertainty quantification.

## Key Takeaways
- The direction of the 8-bit versus 4-bit recovery comparison changes across prompts and evaluation targets. On tasks that both variants complete without faults under the same prompt, the difference ranges from 0 to +20.2 percentage points for Llama and from -50.0 to +35.0 points for Qwen. Full-pipeline point estimates favor 8-bit Llama under all five prompts, whereas the Qwen comparison changes direction across prompts.
- The evaluation target can reverse the result. For Llama under one prompt, scoring each variant only on its own clean-passing tasks favors 4-bit by 17.5 points, while scoring the same tasks for both variants gives no difference. Scoring the full pipeline instead favors 8-bit by 28.3 points, showing that task selection and comparison design strongly shape the conclusion.
- Executor leniency is a third decisive choice. Rescoring the same logs with strict output parsing, which 8-bit Llama violates far more often than 4-bit Llama under that prompt, turns the +28.3-point advantage into a -15.0-point disadvantage while leaving Qwen essentially unchanged. This demonstrates that one prompt, one screened task set, and one scoring policy do not establish a stable conclusion about quantized-agent robustness.

## Context
Post-training quantization is widely used to reduce deployment costs for language-model agents, but tool-use agents face dynamic failures where small model changes may affect recovery behavior. This paper matters because agent evaluation often focuses on final success or isolated task performance, while quantization effects can be hidden by evaluation design choices. It highlights that agent robustness is not only a property of the model, but also a property of the measurement protocol used to assess it.

## Implications
For practitioners, choosing quantization levels for agent deployments should not rely on a single benchmark, prompt, or scoring rule. Teams should compare variants on matched tasks, report full-pipeline success for deployment decisions, state the scoring and parsing policy, and quantify uncertainty across tasks rather than injected fault sites. This can prevent misleading conclusions about whether 4-bit models are reliable enough for production tool-use workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07781v1)
