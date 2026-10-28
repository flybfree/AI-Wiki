---
title: Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces
url: http://arxiv.org/abs/2610.37255v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_13-52-25Z_YourPolicyIsSecretlyaHarness_TheDecisionGeometryof.md
generated_at: 2026-10-27 22:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates what a language model agent's policy actually learns from its harness—the prompts, tools, and control logic used during training and deployment—and what persists when that harness changes. The authors prove theoretically that under KL-regularized control, a trained policy encodes the action preferences of its training harness, and they decompose deployed performance into two separable terms: the harness ceiling (the best return the harness offers) and the policy mismatch (the return lost to the model's own suboptimal decisions). Empirical results in MiniWoB++ and Terminal-Bench Lite confirm that post-training makes a model's preferences brittle and harness-specific, and that ceiling-minus-mismatch is a reliable predictor of whether a new harness will outperform the original after retraining.

## Key Takeaways
- The log odds of an optimal policy under KL-regularized control recover the relative preference the harness assigns to each action, meaning a trained policy is not a general-purpose decision-maker but a carrier of its harness's specific action biases. This implies that post-training does not produce a transferable policy but rather one tightly coupled to the interface geometry it was trained under.
- Deployed return decomposes cleanly into the harness ceiling minus the policy mismatch. Training only reduces the mismatch term, while swapping the harness shifts both terms simultaneously. Consequently, benchmarking a fixed model across different harnesses conflates the quality of the harness with the model's ability to exploit it, making such comparisons fundamentally confounded.
- In MiniWoB++, reversing the order of observation fields leaves every optimal decision mathematically unchanged yet collapses a trained model's success rate from 85.0% to 19.2%, demonstrating extreme brittleness to superficial harness changes. Conversely, harnesses that raise the ceiling but are rejected by fixed-model comparisons actually outperform the original agent after further training under them, and the ceiling-minus-mismatch metric measured beforehand accurately predicts these gains.

## Context
This work sits at the intersection of reinforcement learning theory, LLM agent evaluation, and the rapidly growing practice of designing agent harnesses for coding, tool use, and interactive tasks. As organizations increasingly fine-tune models under specific prompt templates, tool schemas, and control loops, the implicit assumption that a trained policy transfers across interface changes has gone largely unexamined. By formalizing the harness as a geometric object that shapes the policy's decision space, the paper provides a theoretical lens that challenges the standard practice of evaluating harnesses by running a fixed model through them, a practice common in agent benchmarking pipelines.

## Implications
For practitioners building and iterating on agent systems, this research warns that harness design is not a neutral wrapper around a model but a co-training artifact that bakes interface-specific preferences into the policy, making naive transfer across prompt or tool changes unreliable. The ceiling-minus-mismatch decomposition offers a practical diagnostic: teams can estimate a new harness's potential before committing to expensive retraining, and they should avoid fixed-model comparisons that confound harness quality with model exploitation. For the broader field, the findings suggest that robust agent evaluation requires either retraining under each candidate harness or explicitly measuring and separating the two terms, rather than relying on single-model benchmarks that obscure where performance gains or losses actually originate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37255v1)
