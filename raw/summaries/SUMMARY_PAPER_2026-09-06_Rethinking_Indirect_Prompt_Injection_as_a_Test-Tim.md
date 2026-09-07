---
title: Rethinking Indirect Prompt Injection as a Test-Time Search Problem
url: http://arxiv.org/abs/2609.04495v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_21-28-37Z_RethinkingIndirectPromptInjectionasaTest_TimeSearc.md
generated_at: 2026-09-06 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes indirect prompt injection as a test-time search problem and introduces an agentic attacker that explores the task-specific attack surface. It shows that more compute enables finding attacks but explicit strategy management is needed to avoid redundancy. The findings argue that security evaluations must consider both attacker procedure and budget, not treat success as independent of compute.

## Key Takeaways
- Increasing test-time compute improves vulnerability discovery because attackers can explore larger portions of the environment's attack surface.
- Explicit strategy management is crucial to prevent redundant search paths and sustain gains when budgets grow.
- Attacker behavior must be characterized as an adaptive search, highlighting a previously underexplored security risk for tool-using agents.

## Context
Indirect prompt injection exploits how environments and user tasks shape the set of possible attacks on language models. Traditional security tests assume static attack surfaces, but real-world systems are dynamic and task-dependent, making such assumptions inadequate. This research bridges that gap by modeling search over these variable surfaces.

## Implications
For practitioners, evaluating tool-using agents requires simulating attacker search behavior rather than just measuring prompt success rates. Industry must allocate compute budgets to capture realistic vulnerabilities and design defenses that account for adaptive search strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04495v1)
