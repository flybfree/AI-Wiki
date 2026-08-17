---
title: Detecting Contaminated Code-Generation Prompt Batches via Influence Functions
url: http://arxiv.org/abs/2608.14303v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_13-37-53Z_DetectingContaminatedCode_GenerationPromptBatchesv.md
generated_at: 2026-08-16 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CodeSIFT, a threat‑model‑agnostic method that detects malicious prompt batches in code‑generation LLMs by measuring the influence of generated code on model behavior. Using influence functions and statistical tests, it identifies anomalous prompts without needing prior knowledge of specific vulnerabilities. Experiments on three open‑weight models show AUROC up to 0.98 at moderate injection rates while keeping false positives low.

## Key Takeaways
- CodeSIFT leverages influence functions to quantify how prompt batches shift the model’s output space, enabling detection of anomalous behavior across diverse prompts.
- The approach achieves high AUROC scores (up to 0.98) on benchmark datasets that cover various code‑generation vulnerabilities, demonstrating strong performance at moderate injection rates.
- False positive rates remain well‑calibrated and the method outperforms static analysis baselines, highlighting its effectiveness in real‑world deployment.

## Context
The rapid adoption of large language models for code generation has raised security concerns as attackers can craft prompts that produce insecure implementations. Traditional defenses rely on fixed rule sets or known vulnerability signatures, which become ineffective against novel attacks. CodeSIFT addresses this gap by providing a data‑driven, model‑agnostic detection framework grounded in statistical influence analysis.

## Implications
For developers and security teams, CodeSIFT offers a proactive way to monitor prompt batches for anomalous behavior without extensive manual inspection. Its high sensitivity can help catch emerging threats early, reducing the risk of insecure code being deployed. As LLMs become central to software creation pipelines, such detection tools are essential for maintaining robust AI‑assisted development practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14303v1)
