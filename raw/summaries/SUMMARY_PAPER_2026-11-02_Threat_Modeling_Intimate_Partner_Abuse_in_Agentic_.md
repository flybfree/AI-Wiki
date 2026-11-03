---
title: Threat Modeling Intimate Partner Abuse in Agentic Systems
url: http://arxiv.org/abs/2611.00489v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-31_00-28-26Z_ThreatModelingIntimatePartnerAbuseinAgenticSystems.md
generated_at: 2026-11-02 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper applies a technology-facilitated abuse threat model, originally developed for studying intimate partner violence and surveillance, to agentic AI systems that can autonomously perform actions such as sending emails or making reservations. The authors categorize potential abuse scenarios into two distinct threat classes based on system ownership—abuser-as-owner and victim-survivor-as-owner—revealing how agentic systems both amplify existing forms of technology-facilitated abuse and introduce entirely new attack surfaces. The work ultimately proposes research and development directions for mitigating these risks before agentic systems become widely deployed in domestic and personal contexts.

## Key Takeaways
- Abuser-as-owner attacks demonstrate that agentic systems dramatically lower the barrier and increase the scalability of existing technology-facilitated abuse. An abuser who owns or controls an agentic system can leverage its autonomous capabilities—such as automated messaging, scheduling, or data access—to surveil, control, or harass a partner at a scale and frequency that would be impractical with traditional tools, effectively weaponizing automation as a tool of coercive control.
- Victim-survivor-as-owner attacks reveal a novel and previously underexamined attack surface: when the survivor owns the agentic system, abusers can exploit the system's deep connections to external tools, user data, and digital resources to exert influence indirectly. This means that even a system intended to empower the survivor can become a vector through which an abuser gains access to sensitive information, behavioral patterns, or decision-making processes.
- The paper argues that these threats require deliberate investigation and mitigation rather than being treated as edge cases. The authors outline concrete research and development directions, signaling that current agentic system design and safety frameworks do not yet account for the dynamics of intimate partner abuse, surveillance asymmetry, or coercive control embedded in personal technology use.

## Context
Agentic AI systems are rapidly moving from research prototypes into consumer and enterprise products that autonomously interact with calendars, email accounts, smart home devices, and personal data stores. While much of the existing AI safety and security literature focuses on adversarial attacks, prompt injection, or data leakage in enterprise settings, this paper addresses a gap: the interpersonal and domestic power dynamics that shape how technology is used within households. By grounding its analysis in established scholarship on technology-facilitated abuse and intimate partner violence, the work bridges social science and AI safety, a connection that is increasingly urgent as agentic systems gain deeper access to users' private lives.

## Implications
For AI practitioners and product developers, this research signals that agentic system design must incorporate threat models drawn from interpersonal abuse dynamics, not solely from cybersecurity or adversarial ML perspectives. Industry teams building personal assistants, scheduling agents, or smart-home controllers should consider how ownership asymmetries within a household can turn a helpful tool into an instrument of surveillance or control. For researchers, the paper opens a concrete agenda for developing mitigation strategies—such as access controls, behavioral monitoring, and consent-aware architectures—that specifically address the vulnerabilities of victim-survivors interacting with agentic systems, potentially informing policy and safety standards before these technologies reach mass adoption.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00489v1)
