---
title: Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs
url: http://arxiv.org/abs/2610.09703v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_09-01-09Z_UnderstandingandMitigatingToken_Pruning_InducedVul.md
generated_at: 2026-10-07 21:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents the first comprehensive safety evaluation of Token-Pruning mechanisms in Vision-Language Models, revealing that most pruning strategies significantly degrade model safety as pruning ratios increase. The authors identify a novel vulnerability mechanism called Pruning-Induced Malicious Amplification, where removing background tokens inadvertently amplifies toxic semantics from retained malicious anchors, and propose a plug-and-play Safety-Aware Pruning (SAP) mechanism that mitigates these vulnerabilities while preserving acceleration benefits.

## Key Takeaways
- Most Token-Pruning strategies (such as those that remove redundant visual tokens for acceleration) significantly degrade VLM safety as pruning ratios increase, creating a dangerous trade-off between efficiency and security. However, Query-based Compression exhibits the opposite behavior, with extreme pruning up to 99.8% unexpectedly improving model safety, highlighting that not all pruning approaches carry equal risk.
- The authors identify a previously unrecognized mechanism termed Pruning-Induced Malicious Amplification: when background tokens are removed, the model's attention collapses onto a few retained malicious anchors within the foreground, inadvertently amplifying their toxic semantics under jailbreak attacks. This mechanism explains why standard pruning creates exploitable safety gaps that were not previously understood.
- The proposed Safety-Aware Pruning (SAP) mechanism operates at inference time as a plug-and-play solution through three steps: identifying malicious anchors, restoring pruned benign tokens, and reallocating excessive attention from malicious anchors to benign tokens. Experiments across three safety and four utility benchmarks demonstrate SAP reduces Attack Success Rate by up to 62% without compromising efficiency or model utility.

## Context
Vision-Language Models are increasingly deployed in production systems where inference speed is critical, driving widespread adoption of Token-Pruning techniques to reduce computational overhead. However, the safety community has largely overlooked how these acceleration mechanisms interact with adversarial attacks, leaving a critical gap between performance optimization and security assurance. This paper bridges that gap by systematically evaluating how different pruning strategies reshape model safety behavior and exposing a previously unrecognized amplification mechanism.

## Implications
For practitioners deploying VLMs in safety-critical applications such as content moderation, autonomous systems, or public-facing chatbots, this work demonstrates that standard token-pruning acceleration can silently introduce exploitable vulnerabilities that jailbreak attacks can leverage. The SAP mechanism offers a practical, inference-time mitigation that does not require retraining, making it immediately deployable in existing pipelines. For the broader AI safety field, the finding that extreme Query-based Compression can actually improve safety suggests that pruning strategy selection is a safety decision, not merely a performance optimization, and should be evaluated under adversarial conditions before deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09703v1)
