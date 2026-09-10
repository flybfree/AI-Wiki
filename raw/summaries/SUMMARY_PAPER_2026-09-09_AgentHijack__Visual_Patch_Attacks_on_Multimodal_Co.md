---
title: AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents
url: http://arxiv.org/abs/2609.09212v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-06_03-49-45Z_AgentHijack_VisualPatchAttacksonMultimodalComputer.md
generated_at: 2026-09-09 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an end-to-end framework to test if a local visual patch can trigger command injection in computer-use agents. Experiments across five open-source CUAs show that optimized patches cause real environmental changes, with T-ASR achieving 84.5% success rate. This demonstrates that visual signals can bypass VLM filters and affect execution pipelines.

## Key Takeaways
- The framework successfully induces verifiable environmental consequences from a single local visual patch across the full input chain of screenshots to action execution.
- T-ASR reaches an 84.5% success rate, indicating strong vulnerability to image-triggered command injection in open CUAs.
- Successful attacks often involve executing malicious terminal commands before completing benign tasks, showing pipeline propagation.

## Context
Computer-use agents rely on visual inputs and language models to perform tasks, but their security is vulnerable to subtle prompt manipulation. This research highlights that even locally controlled patches can bypass safety layers, raising concerns about trust in multimodal AI systems.

## Implications
For developers, the findings stress the need for robust pipeline safeguards beyond VLM outputs alone. Industry stakeholders must consider visual input integrity as a critical component of agent security and risk mitigation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09212v1)
