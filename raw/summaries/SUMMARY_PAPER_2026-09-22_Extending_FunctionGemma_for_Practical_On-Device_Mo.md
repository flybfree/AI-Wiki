---
title: Extending FunctionGemma for Practical On-Device Mobile Function Calling
url: http://arxiv.org/abs/2609.25373v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-21_20-12-22Z_ExtendingFunctionGemmaforPracticalOn_DeviceMobileF.md
generated_at: 2026-09-22 20:20
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper presents a method for adapting the FunctionGemma 270M model to perform practical, real-world Android device actions by introducing a new synthetic dataset called MOBILEACTIONSEXTENDED. The research demonstrates that fine-tuning small language models on specific mobile categories—such as messaging, camera usage, and application management—significantly improves end-to-end accuracy for local system interactions.

## Key Takeaways
- The researchers developed the MOBILEACTIONSEXTENDED dataset, which consists of approximately 9,500 schema-validated conversations covering fifteen distinct device-control categories including phone calls, brightness control, flashlight operation, and application management.
- Evaluation results showed a dramatic improvement in performance: the base model's accuracy rose from 29.3% to 76.5%, while Google’s existing Mobile-Actions variant improved from 17.2% to 76.5% on the new dataset.
- The study successfully produced a "combined model" that achieves an 82.3% accuracy rate on standard tasks; while this is slightly lower than a specialized model (90.3%), it allows for double the category coverage, offering a more versatile solution for diverse user needs.

## Context
This research addresses a critical gap in current AI development where most function-calling models are optimized for web APIs rather than specific mobile hardware interactions. As the industry shifts toward "on-device AI," there is an urgent need for small language models (SLMs) that can operate with low latency and high privacy by executing commands locally on a smartphone's hardware.

## Implications
For developers and researchers, this work proves that synthetic data generation and targeted fine-tuning of compact models can produce highly effective mobile assistants without the need for massive cloud computing resources. It provides a practical roadmap for creating private, responsive AI agents that can handle complex multi-step device operations directly on consumer hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.25373v1)
