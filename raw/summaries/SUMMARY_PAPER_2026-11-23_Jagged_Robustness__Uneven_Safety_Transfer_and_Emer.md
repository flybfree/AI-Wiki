---
title: Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization
url: http://arxiv.org/abs/2611.27424v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_10-24-25Z_JaggedRobustness_UnevenSafetyTransferandEmergingVu.md
generated_at: 2026-11-23 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how quantization—a technique for compressing model parameters to enable efficient inference—unevenly affects different capability domains in large language models, specifically examining Qwen3-4B. The authors identify a phenomenon they term "Jagged Robustness," where model safeguards and bias handling degrade under quantization while other capabilities like truthfulness remain relatively stable. They further demonstrate that adversarial suffix attacks benign for full-precision models can jailbreak quantized models, revealing hidden vulnerabilities introduced by compression.

## Key Takeaways
- Model safeguards and bias handling degrade under quantization, evidenced by increased compliance with unsafe requests in quantized models compared to their full-precision counterparts. This means safety guardrails that function reliably in full models may fail silently after compression, creating a false sense of security for deployed systems.
- Multiple factors drive Jagged Robustness, including task complexity, evaluation methodology, and generation coherence. This indicates that the degradation is not uniform or predictable across all tasks, making it difficult to assess quantization safety through any single benchmark or evaluation approach.
- Universal adversarial suffix attacks that are harmless to full-precision models can successfully jailbreak quantized models, exposing emergent vulnerabilities that do not exist in the uncompressed model. This finding demonstrates that quantization can introduce entirely new attack surfaces rather than merely reducing existing robustness.

## Context
As large language models are increasingly deployed in resource-constrained environments—on-device inference, edge computing, and cost-sensitive production systems—quantization has become a standard deployment practice. However, the AI safety community has largely assumed that quantized models inherit the safety properties of their full-precision predecessors. This paper challenges that assumption by systematically auditing safety-critical domains including safeguards, instruction-following, ethics, and bias, revealing that the transfer of safety behavior across capability domains is fundamentally uneven and unpredictable.

## Implications
For practitioners deploying quantized models in production, this work signals that safety evaluations conducted on full-precision models cannot be assumed to transfer to quantized deployments, requiring dedicated safety audits at each quantization level. For the broader AI safety field, the discovery of emergent vulnerabilities unique to quantized models—such as new jailbreak attack surfaces—demands that quantization be treated as a distinct safety-relevant transformation rather than a purely performance optimization. Industry teams shipping compressed models should incorporate quantization-specific adversarial testing and safety regression benchmarks into their deployment pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27424v1)
