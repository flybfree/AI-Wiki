---
title: Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States
url: http://arxiv.org/abs/2610.19342v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_00-36-08Z_WhyDoAgentTeamsFailAcrossBoundaries_AFailureTaxono.md
generated_at: 2026-10-14 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces A²-Failures, a taxonomy of 20 failure modes specific to agent-to-agent (A2A) systems where agents act on behalf of different principals with private states, information, and authority. Through analysis of over 2,500 recorded runs spanning 488 scenarios across eight domain families, the authors identify systematic coordination breakdowns that existing multi-agent failure studies—built on assumptions of a single orchestrator or shared workspace—fail to capture. The taxonomy organizes failures into four categories: discovery and delegation, grounding and record consistency, verification, and conduct and fidelity, revealing that current evaluation practices systematically mask internal coordination failures.

## Key Takeaways
- Agents in A2A systems consistently match tasks to peer names mentioned in prompts rather than actively searching for available peers, meaning discovery and delegation failures arise from passive name-matching rather than genuine capability-aware routing. This holds across different agent harnesses and models, suggesting a structural design gap rather than a model-specific flaw.
- Agents never fact-check each other unprompted, meaning verification failures are pervasive and systemic. In mixed-motive or competitive scenarios where one agent's interests oppose another's, the absence of unprompted cross-agent verification allows errors, misrepresentations, or strategic omissions to propagate unchecked through the interaction chain.
- Scoring only the final output rewards the lead agent while hiding internal coordination, verification, and behavioral breakdowns. The authors argue that comprehensive evaluation must score agents individually against their own objectives in addition to overall task outcome, because aggregate scoring conceals the very failure modes that make A2A systems unreliable in practice.

## Context
As autonomous agents increasingly interact across organizational boundaries—buyer agents negotiating with seller agents, legal agents coordinating with compliance agents—the assumption of a single orchestrator or shared workspace that underpins existing multi-agent research no longer holds. This paper addresses a critical gap in the literature by formalizing what goes wrong when agents operate under private states, asymmetric information, and divergent incentives. The release of run logs and the taxonomy provides a shared empirical foundation for the rapidly growing A2A protocol ecosystem, including efforts like the Agent-to-Agent protocol being developed by major technology companies.

## Implications
For practitioners building multi-agent pipelines, this work demonstrates that current evaluation harnesses are structurally blind to the most common failure modes in cross-boundary agent interactions, meaning deployed systems may appear functional while harboring persistent coordination and verification defects. For the field, the taxonomy and dataset establish a benchmark for diagnosing and mitigating A2A failures, pushing evaluation methodology toward per-agent scoring and prompting the design of active discovery, unprompted verification, and fidelity-checking mechanisms as first-class architectural requirements rather than optional add-ons.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19342v1)
