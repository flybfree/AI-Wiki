---
title: Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models
url: http://arxiv.org/abs/2610.10478v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_17-37-19Z_BeforeTheyCanSolve_PredictingPost_TrainingCoding_A.md
generated_at: 2026-10-08 05:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a method for predicting which base model checkpoints are worth investing in expensive agentic post-training for coding tasks, without requiring the base model to drive a full multi-step agent harness from scratch. By replaying successful post-trained agent trajectories and identifying the "decisive step" where a patch flips a repository from failing to passing, the authors construct three lightweight evaluation screens—Decisive-Action BPB, Patch MCQ, and prefix-conditioned pass@K—that closely rank model cohorts in agreement with post-trained SWE-bench Verified pass@1 scores across ten public model pairs.

## Key Takeaways
- End-to-end pass@K evaluation is a poor fit for agentic coding because many base checkpoints cannot reliably produce well-formed tool invocations needed to complete a task, and single-shot or short-horizon tasks sidestep the core capability of maintaining coherent state across many tool-using steps as a repository evolves. This motivates the need for a different evaluation paradigm.
- The authors treat successful post-trained agent trajectories as a "lookahead signal" of base-model potential. By replaying each trajectory and rerunning tests after every code-changing step, they identify the decisive step—the first step whose cumulative patch flips the repository from failing to passing—thereby certifying that the recorded action solves the task given prior context.
- Three screens are built at the decisive step without requiring a base checkpoint to drive the harness from a cold start: (i) Decisive-Action BPB measures probability mass on the certified action, (ii) Patch MCQ tests the checkpoint's choice between the certified action and alternatives rejected by the same verifier, and (iii) prefix-conditioned pass@K evaluates support for functionally-correct generations, crediting any continuation the tests accept. All three rank the cohort in close agreement with post-trained SWE-bench Verified pass@1.

## Context
As large language models increasingly serve as autonomous coding agents, the cost of post-training for agentic capabilities has grown substantially, making it critical to identify promising base checkpoints before committing to expensive fine-tuning rounds. Existing benchmarks like SWE-bench Verified evaluate post-trained agents end-to-end but offer little guidance for selecting base models, since the multi-step tool-calling structure of agentic tasks exposes failure modes that single-shot evaluations miss. This paper bridges that gap by proposing a principled, trajectory-based evaluation framework that decouples base-model quality assessment from full agentic execution.

## Implications
For practitioners and model developers, these screens offer a practical, low-cost way to screen candidate base checkpoints for agentic coding potential using only a benchmark's existing successful trajectories and verifier, dramatically reducing the compute needed before committing to post-training. The approach also generalizes: as new agentic coding benchmarks emerge, their successful traces and verifiers can be repurposed as base-model evaluation tools, potentially accelerating model selection cycles across the industry. For the broader AI research community, the "coverage principle for agentic traces" and the decisive-step certification framework provide a reusable methodology for evaluating multi-step agent capabilities without full rollout.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10478v1)
