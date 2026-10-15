---
title: CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection
url: http://arxiv.org/abs/2610.20049v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_11-52-03Z_CoRedSkill_StealthySkillCompositionAttacksviaAST_G.md
generated_at: 2026-10-14 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoRedSkill introduces a compositional red-teaming framework that constructs stealthy adversarial attacks by distributing malicious operations across multiple cooperating skills within an agent workflow, using abstract syntax tree (AST) rewriting to inject attack operations into task functions while preserving each skill's original utility. The method achieves a 98.0% attack success rate and 95.3% task completion rate with only a 3.3% audit detection rate, yielding a 90.7% joint success rate that dramatically outperforms four baselines (6.7–42.7%), demonstrating that skill compositions can carry out unauthorized operations that evade individual-package auditing.

## Key Takeaways
- CoRedSkill decomposes existing agent workflows into interdependent skills and embeds attack operations through AST-guided rewriting of task functions, enabling malicious operations to be distributed across multiple skills so that no single skill appears malicious in isolation, making the combined adversarial intent extremely difficult to detect through individual-package auditing.
- The benchmark evaluation covers 150 cases spanning 50 tasks and three distinct attack objectives, measuring attack success, task completion, and audit detection simultaneously; the joint success metric (attack success + task completion + audit evasion in the same case) reaches 90.7%, compared to only 6.7–42.7% for four baseline methods, highlighting a substantial gap in stealthy compositional attack capability.
- Skill instructions guide the agent to autonomously select and invoke the relevant skills, while workflow dependencies and intermediate artifacts connect the injected operations during execution, meaning the attack operates through the agent's own reasoning and tool-use pipeline rather than through overtly suspicious standalone operations.

## Context
As AI agents increasingly rely on modular skill libraries—packages of instructions, executable code, and resources—to extend their capabilities, the security surface expands beyond individual skill auditing to the combinatorial interactions between skills. Existing red-teaming and safety evaluation methods typically assess single tools or prompts in isolation, leaving a critical blind spot for attacks that emerge only when multiple seemingly benign skills are composed together. CoRedSkill addresses this gap by formalizing compositional adversarial threats and providing a concrete AST-based injection mechanism, contributing to the growing body of work on agent safety, tool-use security, and supply-chain auditing for autonomous systems.

## Implications
For practitioners deploying agent frameworks with third-party skill libraries, CoRedSkill demonstrates that current per-package auditing practices are insufficient to catch adversarial behavior hidden in skill composition, suggesting that security reviews must extend to workflow-level dependency analysis and intermediate artifact inspection. For the broader AI safety field, the 90.7% joint success rate signals an urgent need for compositional red-teaming benchmarks and auditing tools that can reason across multi-skill execution traces, and it provides a reproducible evaluation protocol that future safety frameworks can adopt to stress-test agent architectures against stealthy, utility-preserving attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20049v1)
