---
title: Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection
url: http://arxiv.org/abs/2611.29977v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_03-41-22Z_Conartist_AdaptiveAgenticRed_TeamingofComputer_Usi.md
generated_at: 2026-11-24 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces Conartist, an adaptive agentic red-teaming framework designed to evaluate and exploit the security mechanisms of Computer-Using Agents (CUAs) against multi-step prompt injection. It identifies two core vulnerabilities in agent harnesses: consistency checking, which can be bypassed by embedding malicious actions that appear logically consistent with legitimate task execution, and risk auditing, which itself introduces additional exploitable actions that violate security boundaries. Conartist uses a two-stage cascaded approach: a goal-pollution strategy that establishes deceptive causal dependencies between legitimate user objectives and malicious operations, followed by adaptive refinement based on security-auditing feedback to either avoid triggering risk auditing or induce additional high-risk operations.

## Key Takeaways
- Consistency checking is bypassable: attackers can embed malicious actions that appear logically consistent with legitimate task execution, evading the mechanism designed to prevent agents from deviating from user objectives.
- Risk auditing is itself exploitable: the auditing process introduces additional exploitable actions that violate security boundaries, meaning defensive mechanisms can be manipulated to facilitate attacks rather than prevent them.
- Conartist achieves strong results across five backbone models: a 32.12% attack success rate on a 576-instance tool use benchmark and 66.67% on the Reddit GUI benchmark, outperforming the SOTA attack by 14.41 and 29.17 respectively.
- Analysis of Openclaw, one of the most popular agents, revealed seven realistic exploitable attack patterns, demonstrating that security mechanisms designed to prevent malicious actions can themselves be manipulated to facilitate attacks.

## Context
Computer-Using Agents are increasingly deployed to perform real-world tasks, and agent harnesses are used to enforce security constraints and defend against prompt injection attacks. This paper matters because it reveals that the very mechanisms intended to secure these agents, namely consistency checking and risk auditing, are themselves vulnerable to sophisticated multi-step attacks, exposing a gap in current red-teaming and evaluation practices.

## Implications
For practitioners and the industry, the findings suggest that security auditing and consistency checks cannot be treated as sufficient guarantees of safety; they must be designed and evaluated as attack surfaces themselves. Developers of agent harnesses should incorporate adaptive red-teaming, such as Conartist, into their evaluation pipelines and consider redesigning auditing logic to avoid introducing exploitable high-risk actions. The seven realistic attack patterns identified in Openclaw provide a concrete checklist for hardening agentic systems against multi-step prompt injection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29977v1)
