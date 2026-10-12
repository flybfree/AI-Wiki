---
title: Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels
url: http://arxiv.org/abs/2610.13105v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_06-58-59Z_CanFailedTrajectoriesRevealWhereAgentsGoWrong_Agen.md
generated_at: 2026-10-11 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the challenge of identifying the decisive step responsible for task failure in LLM agent trajectories when only the overall failure outcome is known but no step-level error labels are available. The authors propose SOAP (Spectral scOring with Attention-guided Propagation), a framework that constructs a spectral reference space from LLM representations to score each step's error contribution and then propagates downstream error evidence back toward its likely upstream sources using attention-derived dependencies. Extensive experiments demonstrate that SOAP consistently outperforms competitive baselines in failure attribution accuracy without requiring step-level training labels or a separate success-only reference set.

## Key Takeaways
- SOAP eliminates the need for costly step-level annotations or verified successful trajectories by constructing a spectral reference space directly from LLM representations, assigning each step a base error score based on its projection behavior within that space. This makes failure attribution feasible even when only the final failure outcome is known and no intermediate ground-truth labels exist.
- The paper identifies and addresses the critical "downstream contamination" problem: later steps in a failed trajectory often exhibit stronger failure signals because they inherit errors from an earlier decisive mistake, causing independent scoring methods to incorrectly attribute blame to downstream consequences rather than the true originating error. SOAP solves this by deriving soft step dependencies from attention patterns and propagating downstream error evidence toward its likely upstream sources.
- SOAP requires neither step-level training labels nor a separate success-only reference set, making it a practical and scalable approach for debugging agentic systems in production environments where annotated failure data is expensive or unavailable.

## Context
As LLM-based agents are increasingly deployed in complex multi-step tasks such as software engineering, web navigation, and tool use, understanding where and why an agent fails becomes essential for iterative improvement. Existing failure attribution methods depend on expensive human annotations of individual steps or on curated sets of successful trajectories for comparison, creating a bottleneck for scaling debugging efforts. This paper contributes to the growing field of agentic evaluation by offering a label-free, representation-based approach that leverages the internal attention structure of LLMs themselves to diagnose failures, representing a shift from external annotation pipelines toward self-contained diagnostic frameworks.

## Implications
For practitioners building and maintaining agentic systems, SOAP offers a practical debugging tool that can operate on raw failure logs without requiring teams to manually annotate thousands of trajectory steps, significantly reducing the cost and time of failure analysis. For the broader AI research community, the attention-guided propagation mechanism suggests that internal model representations contain sufficient structural information to localize causal errors, which could inform future work on agent training, reward shaping, and automated curriculum design. The approach also has implications for safety and reliability engineering, as more accurate failure attribution enables targeted interventions rather than broad system-wide retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13105v1)
