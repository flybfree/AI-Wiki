---
title: BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics
url: http://arxiv.org/abs/2608.16211v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_07-44-57Z_BaT_TowardsSelf_EvolvingMedicalResearchAgentwithSt.md
generated_at: 2026-08-17 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BaT, a recursive self-improvement system that enables medical research agents to evolve through multiple stages of training. On AutoMedBench-Lite, the 4‑billion and 9‑billion parameter models outperform their Qwen Instruct baselines by more than double, with BaT‑9B achieving an Overall score of 79.6, surpassing Claude Opus at 4.6.

## Key Takeaways
- BaT uses a Stage Bank to create content‑isolated training states outside the policy‑update loop, allowing agents to learn from each stage without interference.
- The BiCuRL method selects the next curriculum using a fixed held‑out evaluation and verifies rollouts with task rubrics before updating the policy via GRPO.
- On AutoMedBench-Lite, BaT‑4B and BaT‑9B more than double the Overall scores of their Qwen Instruct baselines.

## Context
Long‑horizon agents aim to automate end‑to‑end medical workflows that involve multiple stages and sensitive data. Structured benchmarks provide stage‑level rubrics for failure localization, yet current post‑training methods discard these diagnostics, limiting self‑evolution. BaT bridges this gap by preserving diagnostic information within a recursive training loop.

## Implications
For researchers, BaT demonstrates that stage‑aware evaluation can drive substantial performance gains in specialized domains like medical imaging. For industry practitioners, the approach offers a scalable framework to iteratively improve agent capabilities without sacrificing safety or regulatory compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16211v1)
