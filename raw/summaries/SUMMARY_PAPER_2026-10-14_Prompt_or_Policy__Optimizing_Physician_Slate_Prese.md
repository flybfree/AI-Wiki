---
title: Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators
url: http://arxiv.org/abs/2610.18309v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_12-52-47Z_PromptorPolicy_OptimizingPhysicianSlatePresentatio.md
generated_at: 2026-10-14 00:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the challenge of helping patients compare physician profiles by formulating a slate presentation optimization task: generating short, case-specific summaries of ranked physicians that aid patient decision-making while remaining grounded in profile information. The authors develop an offline evaluation framework using persona-conditioned LLMs to simulate patient choices, then compare prompt-level optimization (GEPA) against parameter-level optimization (GRPO) and their combination, finding that GRPO substantially outperforms GEPA across multiple quality constraints and that combining both approaches yields the best simulated conversion rates.

## Key Takeaways
- The authors introduce a novel offline evaluation framework that uses persona-conditioned LLMs to simulate patient choices without requiring real patient interactions, generating patient personas from attributes extracted from medical cases and evaluating physician presentations for factual accuracy, relevance, naturalness, and simulated patient choice, while also employing a second unseen LLM judge to guard against simulator-specific overfitting.
- GRPO (Group Relative Policy Optimization), a parameter-level optimization method, substantially outperforms GEPA (a prompt-level optimization method) in satisfying the full set of constraints including factual accuracy and relevance, and its gains in simulated conversion persist even under evaluation by an unseen judge, demonstrating robustness rather than overfitting to the simulator.
- Prompt-level and parameter-level optimization play complementary roles: GEPA alone yields smaller improvements, but using GEPA's optimized prompt to initialize GRPO training accelerates convergence and achieves the highest simulated conversion rates, suggesting a practical pipeline where prompt engineering serves as a warm-start for reinforcement learning fine-tuning across two model sizes.

## Context
This work sits at the intersection of recommendation systems, LLM-based user simulation, and reinforcement learning for text generation, contributing to the growing body of research on using synthetic user simulators to evaluate and optimize AI-generated content without costly human-in-the-loop experiments. By framing physician comparison as a slate presentation optimization problem and rigorously testing whether simulated preferences transfer to unseen evaluators, the paper addresses a critical methodological concern in LLM evaluation pipelines: whether optimization gains reflect genuine quality improvements or merely overfitting to a particular simulator's biases.

## Implications
For healthcare technology practitioners and platform developers, these findings offer a practical recipe for improving physician recommendation interfaces: combine prompt-level optimization as an initialization step with parameter-level RL fine-tuning to produce grounded, case-specific physician summaries that genuinely help patients make informed choices. More broadly, the methodology of using persona-conditioned simulators paired with held-out LLM judges provides a reusable evaluation protocol for any domain where AI-generated content must satisfy multiple quality constraints simultaneously, reducing dependence on expensive human evaluation while maintaining robustness against simulator-specific artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18309v1)
