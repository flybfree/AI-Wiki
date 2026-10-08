---
title: Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents
url: http://arxiv.org/abs/2610.09469v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_05-24-40Z_Secure_CUA_ControllingUntrustedInfluenceinComputer.md
generated_at: 2026-10-07 22:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Secure-CUA, a security framework for computer-use agents (CUAs) that perform tasks across desktops, mobile apps, and web browsers by observing graphical interfaces and issuing clicks or keystrokes. The authors formalize security requirements to protect agents from adversaries who embed malicious instructions or misleading visual cues within untrusted content, and they instantiate these requirements through an "action transaction" mechanism that commits to explicit per-action programs before any untrusted content is accessed. Evaluation on 400 WebArena tasks shows Secure-CUA achieves a 53.55% task success rate, closely matching the 55.12% of an unprotected Vanilla-CUA while dramatically outperforming the 13.17% of CaMeL-CUA.

## Key Takeaways
- The paper identifies a critical attack surface for computer-use agents: untrusted content within GUIs (such as web pages, pop-ups, or embedded text) can be weaponized by adversaries to embed hidden instructions or misleading visual cues that redirect the agent's commands to wrong interface targets or alter its intended actions, effectively hijacking the agent's decision-making pipeline.
- Secure-CUA's core innovation is the "action transaction" concept, where the agent commits to an explicit per-action program before accessing any untrusted content. Each transaction predefines its queries to untrusted regions and the permitted uses of their responses, and the system masks untrusted regions while evaluating the transaction through an isolated query model. This design ensures security by construction under the model's assumptions, rather than relying on post-hoc filtering.
- The evaluation demonstrates that security does not require a severe utility tradeoff: across 6,000 execution traces spanning 400 WebArena tasks, three frontier models, and five random seeds, Secure-CUA retains 53.55% task success compared to 55.12% for an unprotected baseline, a marginal 1.57-point drop, while CaMeL-CUA collapses to 13.17%, showing that naive security constraints can destroy agent utility.

## Context
Computer-use agents represent a rapidly growing class of AI systems that interact with graphical user interfaces to automate tasks across diverse software environments, from web browsing to desktop productivity applications. As these agents gain autonomy and access to sensitive operations such as file management, financial transactions, and communication, the attack surface presented by untrusted content embedded within the very interfaces they must observe becomes a first-order security concern. This paper addresses a gap in the literature by formalizing security at both the decision level and the execution level of GUI commands, rather than treating agent safety as a purely prompt-level or output-filtering problem.

## Implications
For practitioners deploying CUAs in enterprise or consumer settings, Secure-CUA demonstrates that structural security guarantees can be achieved with minimal performance overhead, making it feasible to integrate robust defenses into production agent pipelines without sacrificing task completion rates. The action transaction model also offers a reusable architectural pattern for other autonomous agent systems that must interact with untrusted environments, suggesting that pre-committing to constrained interaction protocols before content access is a broadly applicable defense strategy. Industry stakeholders building agentic automation tools should consider adopting transaction-based isolation to mitigate prompt-injection and visual-manipulation attacks that currently threaten the reliability and trustworthiness of computer-use agents at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09469v1)
