---
title: ExecCritic: Learn to Test, Test to Improve for Coding Agents
url: http://arxiv.org/abs/2609.09133v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_17-53-37Z_ExecCritic_LearntoTest_TesttoImproveforCodingAgent.md
generated_at: 2026-09-08 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ExecCritic, a framework that separates test generation from code repair in coding agents to avoid false confidence when both are generated together. By training distinct roles — Test and Repair — using Qwen-3.5 as the backbone, the system learns behaviorally valid tests and feedback‑guided revisions. On SWE-bench Verified, the approach improves resolved rates by 8 points compared with a no‑test baseline.

## Key Takeaways
- The Test agent must generate repository‑native tests that correctly distinguish correct from incorrect patches, preventing errors from aligning between patch and test.  
- The Repair agent benefits from execution feedback only when the associated test is valid, avoiding reinforcement of false confidence.  
- Role‑specific post‑training boosts the Qwen Test agent’s success rate to 62.2% and composition yields 72.6%, an 11.4‑point gain over the original baseline.

## Context
The paper addresses a longstanding challenge in automated code repair: agents often produce both patches and tests that share errors, leading to misleading performance metrics. By decoupling test creation from repair and training each component separately with reinforcement learning, ExecCritic offers a more reliable evaluation of agent behavior.

## Implications
For developers and AI practitioners, ExecCritic demonstrates how targeted feedback can substantially enhance code‑repair accuracy without requiring stronger models or oracle data at inference time. This framework could be adopted to improve tooling in software engineering pipelines where correctness is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09133v1)
