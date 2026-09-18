---
title: How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents
url: http://arxiv.org/abs/2609.20474v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_14-30-14Z_HowDoAgentHarnessesCreateValue_PlanningInformation.md
generated_at: 2026-09-17 21:18
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates how specific components of agent harnesses—specifically planning guidance and verification mechanisms—contribute to the success of stateful Large Language Model (LLM) agents. By analyzing experiments within the $τ^2$-bench, the authors demonstrate that while prewritten plans significantly improve task completion rates, a dedicated verifier is essential for minimizing false positives, particularly in scenarios where the cost of error is high.

## Key Take4
- Prewritten planning guidance provides a significant boost to success rates: The study found that "Fixed" plans improved oracle-verified success by 7.17 percentage points compared to "Sham" text (shuffled policy text), with these improvements being most pronounced in tasks of higher complexity.
- Verifiers are highly effective and cost-efficient: A read-only terminal verifier was able to reject 61% of invalid episodes while only withholding 17% of correct ones, all at a negligible cost of less than one cent per episode.
- The value of components depends on the risk profile: In scenarios with low liability for errors, planning gains are more significant; however, in high-liability environments, the verifier's ability to prevent false positives becomes the dominant factor for safety and reliability.

## Context
As LLM agents transition from simple one-off prompts to complex, stateful workflows like those found in retail or logistics, understanding the mechanics of "agent harnesses" is crucial for building reliable systems. This paper provides a granular look at how these components interact, moving beyond just "bigger models" toward more efficient and verifiable architectural designs.

## Implications
For developers and researchers, this suggests that a standalone verifier can capture nearly all the false-pass benefits of a full planning-plus-verification stack at a fraction of the cost. This allows for the creation of safer, more reliable AI agents by prioritizing verification layers over complex planning when high precision is required but budget constraints exist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.20474v1)
