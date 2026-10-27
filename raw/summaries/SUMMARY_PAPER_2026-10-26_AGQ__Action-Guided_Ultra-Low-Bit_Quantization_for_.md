---
title: AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models
url: http://arxiv.org/abs/2610.33074v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-21_06-22-51Z_AGQ_Action_GuidedUltra_Low_BitQuantizationforVisio.md
generated_at: 2026-10-26 20:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Action-Guided Quantization (AGQ), a method for ultra-low-bit quantization of Vision-Language-Action (VLA) models that allocates matrix bitwidths by combining action sensitivity analysis with a measured proxy for weight recovery cost under strict storage budgets. On the LIBERO benchmark, AGQ achieves 92.7% task success at 3-bit quantization, outperforming AWQ and GPTQ baselines, and demonstrates that an asymmetric W1.5* configuration can compress a complete model by 6.10× relative to BF16 while retaining 25.5% task success.

## Key Takeaways
- AGQ combines action sensitivity with a measured proxy for weight recovery cost to allocate matrix bitwidths under storage budgets, meaning quantization decisions are not uniform but guided by how sensitive each weight matrix is to the robot's action outputs, enabling smarter bit allocation than fixed-precision approaches.
- The method employs per-channel calibration to compensate for quantization error while maintaining a uniform bitwidth within each matrix to preserve regular memory layouts, and uses bit-dependent grouped lossless coding to reduce resident weight storage alongside block-wise recovery to limit temporary buffer requirements during inference.
- The asymmetric W1.5* configuration uses 4-bit vision weights and a parameter-weighted average of 1.5 bits for language weights, achieving 6.10× complete-model compression relative to BF16 while retaining 25.5% task success on LIBERO, demonstrating that extreme compression is feasible when vision and language components are quantized differently based on their respective sensitivity profiles.

## Context
Vision-Language-Action models represent a frontier in embodied AI, enabling robots to interpret natural-language instructions and execute complex physical tasks, but their multi-billion-parameter architectures make onboard deployment on memory-constrained robot platforms a significant engineering challenge. Existing quantization techniques such as AWQ and GPTQ were designed for language-only models and do not account for the heterogeneous sensitivity profiles across vision encoders, language transformers, and action heads within VLA architectures. This paper addresses a critical gap by introducing action-aware quantization strategies tailored specifically to the multi-modal structure of VLA models, pushing ultra-low-bit compression into a regime where task performance degradation is actively managed rather than merely tolerated.

## Implications
For robotics practitioners and embedded AI engineers, AGQ provides a practical pathway to deploy capable VLA models on resource-limited onboard hardware without relying on cloud connectivity, potentially accelerating the adoption of language-guided manipulation in warehouse automation, assistive robotics, and field-deployable systems. The asymmetric quantization strategy—treating vision and language weights differently based on their action sensitivity—offers a generalizable design principle for compressing any multi-modal model where components contribute unequally to downstream task success, suggesting that future quantization research should move beyond uniform bitwidth assumptions toward component-aware, task-guided compression policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33074v1)
