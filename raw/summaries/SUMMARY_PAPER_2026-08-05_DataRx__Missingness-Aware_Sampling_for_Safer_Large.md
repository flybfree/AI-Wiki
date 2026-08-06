---
title: DataRx: Missingness-Aware Sampling for Safer Large Language Model Task-Specific Fine-Tuning
url: http://arxiv.org/abs/2608.04322v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_01-05-13Z_DataRx_Missingness_AwareSamplingforSaferLargeLangu.md
generated_at: 2026-08-05 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DataRx, a missingness‑aware sampling method that selects safety examples to fill gaps in the model’s hidden representations rather than relying on token mixing. It demonstrates that with just 1% of BeaverTails data, DataRx cuts the average attack success rate of Llama3‑8B‑Instruct across seven tasks from 59.23 % (random) to 13.70 %. The approach combines safety sampling with synthesis for stronger defenses.

## Key Takeaways
- DataRx treats safety signals as continuous hidden representations, quantifying the gap between model output and reference response.
- It selects only a tiny fraction of safety data yet achieves dramatic improvement in task‑specific fine‑tuning safety.
- Combining DataRx with existing synthesis methods further boosts defense without large extra data.

## Context
In AI safety research, preserving guardrails during LLM fine‑tuning is critical as task‑specific adaptation can erode protections. Current approaches often rely on token‑level mixing or random sampling, which may not address the underlying representation gaps that cause failures.

## Implications
DataRx shows that small, well‑chosen safety samples can significantly enhance model robustness, offering a practical tool for developers seeking efficient safety improvements. This research encourages data‑centric strategies over purely architectural fixes in deploying safe LLMs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04322v1)
