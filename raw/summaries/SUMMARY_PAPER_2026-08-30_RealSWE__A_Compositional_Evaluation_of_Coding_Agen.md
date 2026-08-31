---
title: RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests
url: http://arxiv.org/abs/2608.27831v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_01-57-58Z_RealSWE_ACompositionalEvaluationofCodingAgentsunde.md
generated_at: 2026-08-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares how coding agents perform on real user requests with their performance on the SWE‑bench benchmark, which uses longer, structured GitHub issues. The study shows that most real prompts are short and casual, while benchmarks are formal and detailed, leading to lower resolution rates for agents when faced with realistic inputs.

## Key Takeaways
- 88 % of real user requests consist only of a problem statement or limited extra context, yet they make up just 7 % of benchmark problems.  
- Real prompts are 87 % casually written, whereas benchmarks are 94 % formal, highlighting a stark style gap.  
- Including explicit Desired Behavior and Motivation markedly improves LLM performance, while adding Environment Information or Reproduction Steps yields only token overhead.

## Context
The rapid rise of large language models in software engineering has prompted research into how well they handle everyday user queries rather than curated benchmark tasks. Understanding the mismatch between real‑world prompts and benchmark data is crucial for reliable agent deployment.

## Implications
Practitioners should design prompt templates that explicitly state desired outcomes and motivation to boost model accuracy without unnecessary token bloat. This guidance can lead to more robust, user‑friendly coding assistants in industry settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27831v1)
