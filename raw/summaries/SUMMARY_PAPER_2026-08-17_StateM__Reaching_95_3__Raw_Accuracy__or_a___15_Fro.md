---
title: StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling
url: http://arxiv.org/abs/2608.15089v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_07-16-28Z_StateM_Reaching95_3_RawAccuracy_ora__15FrontierRun.md
generated_at: 2026-08-17 21:39
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces StateM, a runtime that improves long-horizon agent performance by organizing execution around durable states and runbooks without altering model weights. On Terminal-Bench 2.1 it lifts GPT‑5.5 xhigh to 92.1% versus the reference 83.1% and reaches 95.3% raw accuracy with GPT‑5.6 Sol xhigh, while DeepSeek‑V4 Flash jumps from 82.7 to 88.1%. The cost of adaptation is under $15 compared to $574 for the reference.

## Key Takeaways
- StateM raises GPT‑5.5 xhigh to 92.1% versus a reference 83.1%, showing that harness scaling can outperform model upgrades alone.
- The runtime achieves 95.3% raw accuracy on GPT‑5.6 Sol xhigh across 445 trials, exceeding the previous best of 91.9% and succeeding on all 89 tasks at least once.
- DeepSeek‑V4 Flash improves from 82.7 to 88.1% with less than $38 adaptation, while total DeepSeek expenditure drops to $52.22 versus $574.68 for the reference.

## Context
Long‑horizon agents often fail due to mutable state and loss of earlier lessons, a problem that current model improvements cannot fully solve. This work demonstrates that execution systems can be upgraded independently of model weights, offering a scalable alternative to training larger models. The approach aligns with trends toward modular AI pipelines where runtime components are decoupled from core capabilities.

## Implications
Practitioners can deploy StateM to boost existing agents without costly retraining, reducing both time and money in AI projects. The method also provides transparent runbooks that aid debugging and compliance, potentially reshaping how organizations manage large language model services across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15089v1)
