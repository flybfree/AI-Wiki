---
title: Surviving the Router: Optimizing Skill Injections for Retrieval and Execution
url: http://arxiv.org/abs/2610.08098v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_10-28-27Z_SurvivingtheRouter_OptimizingSkillInjectionsforRet.md
generated_at: 2026-10-06 21:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper examines how malicious third-party skills injected into AI agents can survive a skill router that selects skills for execution. It shows that realistic multi-skill retrieval settings substantially reduce the success of existing prompt-injection attacks, then introduces CORSA, a router-aware attack that optimizes injected skills for both retrieval and execution while preserving user utility.

## Key Takeaways
- Existing evaluations often assume the malicious skill has already been selected, but in realistic router-managed environments the injected skill must first compete with many benign skills for retrieval. The paper finds that this retrieval bottleneck reduces the effective attack success rate of existing injections by 87-97%, meaning prior threat estimates can be highly inflated.
- CORSA addresses this limitation by treating skill injection as a router-aware optimization problem. It uses successive optimization stages to first improve the likelihood that the malicious skill is retrieved and then optimize end-to-end execution success across clusters of related tasks, while separately evaluating user utility and injection naturalism.
- The resulting attacks are not tied to a single router or model. The paper reports that CORSA improves retrieval and end-to-end attack success over existing skill injections, preserves user utility, and transfers across different router architectures and LLM backbones, indicating a broad practical threat surface.

## Context
AI agents increasingly rely on modular skill libraries and routers that dynamically select tools or instructions for complex tasks. This architecture creates a new supply-chain attack surface, because malicious content can be embedded in skills that are later retrieved and executed. The paper matters because it moves skill-injection research from idealized execution-only assumptions to realistic retrieval competition, which is central to deployed agent systems.

## Implications
For security practitioners, these findings show that defenses must account for both retrieval and execution, not only whether a malicious skill is present in the catalog. Benchmarks and red-team evaluations should include router-managed multi-skill settings, because attack success can differ dramatically when retrieval is competitive. The transferability of CORSA across routers and LLM backbones also suggests that defenses need to be architecture-agnostic and focused on retrieval filtering, skill provenance, and execution-time safeguards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08098v1)
