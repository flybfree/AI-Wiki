---
title: Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions
url: http://arxiv.org/abs/2609.32428v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_10-02-57Z_AuthorizationClosureGraph_MinimalRepairforLLMAgent.md
generated_at: 2026-09-28 20:33
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces the Authorization-Closure-Graph (ACG) framework to address the challenge of managing user authorization for tool-using LLM agents when instructions evolve over time. ACG represents authorization as an evolving, versioned state that selectively invalidates only the authority impacted by instruction revisions while preserving unaffected portions, thereby computing a minimal repair to identify missing evidence or permissions. Evaluations across three advanced LLMs demonstrate that ACG consistently enhances both action safety and task success rates compared to existing approaches.

## Key Takeaways
- Existing methods lack a principled mechanism to handle partial instruction changes, often resulting in the need for full re-authorization or retaining stale authority; ACG solves this by maintaining a versioned state that tracks dependencies and selectively revokes only the specific authorizations affected by a revision.
- The framework introduces a "minimal repair" computation that precisely identifies only the missing evidence or authority required to proceed with an updated instruction, ensuring agents can adapt dynamically without requesting redundant permissions for unchanged parts of the task.
- Empirical tests across three advanced LLMs in two natural tasks show that ACG consistently improves action safety rates and task success rates, proving its effectiveness in balancing security with usability in evolving agent workflows.

## Context
As LLM agents increasingly perform state-changing actions via tools in real-world applications, ensuring secure and efficient user authorization is critical to prevent unauthorized modifications or security breaches. Current authorization mechanisms

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32428v1)
