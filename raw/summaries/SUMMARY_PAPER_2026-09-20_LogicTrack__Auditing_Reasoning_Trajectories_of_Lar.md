---
title: LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers
url: http://arxiv.org/abs/2609.21492v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_08-46-37Z_LogicTrack_AuditingReasoningTrajectoriesofLargeLan.md
generated_at: 2026-09-20 20:06
model: freedomaisvr/gemma-4-12b-it
---

## Summary
LogicTrack is a neuro-symbolic framework designed to address the issue of "logical hallucinations" in Large Language Models (LLMs), where models may reach correct final answers through flawed intermediate reasoning steps. By auto-formalizing these reasoning chains into symbolic representations and verifying them with automated theorem provers, the system ensures that each step of a Chain-of-Thought (CoT) process is logically sound.

## Key Takeaways
- The framework addresses a critical gap in current LLM training where optimization relies primarily on final outcome accuracy rather than the logical validity of intermediate steps; LogicTrack ensures that the reasoning path itself is verifiable and correct.
- It introduces Solver-Based Backtracking Reward (SBR), a novel step-wise scoring mechanism that utilizes automated theorem provers to quantify logical soundness, which then guides the model's backtracking tree search during inference time.
- The researchers developed a method to generate high-quality Supervised Fine-Tuning (SFT) data from these backtracking trajectories, allowing models to internalize the ability to audit and correct their own reasoning as an intrinsic capability rather than just a post-hoc check.

## Context
As LLMs are increasingly deployed in high-stakes domains like medicine, law, and engineering, the "black box" nature of their reasoning becomes a significant safety concern. This paper contributes to the field by moving beyond simple output verification toward a more rigorous, neuro-symbolic approach that validates the internal logic of AI thought processes.

## Implications
For researchers and practitioners, this work provides a roadmap for creating more trustworthy and verifiable AI systems that can be audited for logical consistency. By enabling models to self-correct based on formal logic, it paves the way for LLMs to be used in environments where "getting the right answer for the wrong reason" is not an acceptable risk.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21492v1)
