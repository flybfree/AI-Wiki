---
title: VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks
url: http://arxiv.org/abs/2610.00972v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_03-02-17Z_VeriHarness_ScalingAgenticVerificationforLong_Hori.md
generated_at: 2026-10-01 21:13
model: qwen3.6-35b-a3b
---

## Summary
VeriHarness introduces a framework to enhance verification capabilities for long-horizon LLM agent tasks using a fixed base model without reference answers or grading rubrics at test time. By leveraging repeated sampling, the system employs an agentic verifier equipped with workspace tools and reusable skills to resolve disagreements and challenge consensus, ultimately selecting and revising artifacts based on environmental evidence. The approach achieves state-of-the-art selection scores across five benchmarks and demonstrates significant performance gains through evidence-backed revision, while also showing that verification skills can self-improve from failure feedback.

## Key Takeaways
- VeriHarness exploits the observation that disagreement often reveals correct alternatives while consensus may hide errors; it uses a disagreement resolver to check competing claims against environmental evidence and a consensus challenger to test shared claims for omitted requirements, guiding artifact selection and revision.
- The method achieves the highest selection scores among evaluated baselines across five long-horizon workspace benchmarks using two frontier models; evidence-backed revision yields average performance gains of 6.2 points with Gemini 3.5 Flash and 6.4 points with Claude Opus 4.8 compared to single rollouts.
- Verification skills demonstrate the ability to self-improve from failure feedback, establishing a scalable mechanism for long-horizon verification; additionally, the authors release a comprehensive dataset of approximately 26,000 rollouts across all benchmarks and models, generated at a cost exceeding $100,000, to support future research.

## Context
As large language model

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00972v1)
