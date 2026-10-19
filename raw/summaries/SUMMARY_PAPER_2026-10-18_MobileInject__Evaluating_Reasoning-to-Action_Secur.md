---
title: MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection
url: http://arxiv.org/abs/2610.23307v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_11-10-30Z_MobileInject_EvaluatingReasoning_to_ActionSecurity.md
generated_at: 2026-10-18 20:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MobileInject is the first benchmark specifically designed to evaluate the security vulnerabilities of multimodal large language model (MLLM)-based mobile agents when exposed to cross-modal injection attacks. The paper introduces a high-fidelity interactive evaluation framework spanning 11 scenarios, 9 security-risk categories, and 108 executable risk instances, revealing that mobile agents are broadly vulnerable to multimodal injection attacks, with many failures originating from reasoning hijacking at early stages of agent decision-making.

## Key Takeaways
- MobileInject introduces Cross-Modal Consistency Injection, a novel attack strategy that exploits corroboration across different modalities (text, images, UI elements) to manipulate an agent's trust and steer its behavior toward adversarial objectives embedded in cross-application mobile content. This goes beyond traditional prompt injection by leveraging the multimodal nature of mobile environments.
- Two enhanced attack methods are proposed: Multi-Role Collaborative Deception, which intensifies trust manipulation by coordinating deceptive signals across multiple roles or sources, and Reasoning-Camouflage Injection, which hijacks the agent's reasoning chain to produce plausible but adversarially directed conclusions. These methods target the reasoning-to-action pipeline specifically.
- The paper provides a Reasoning Security Diagnosis Framework for fine-grained failure analysis, enabling researchers to pinpoint exactly where in the reasoning chain an agent's decision is corrupted. Systematic experiments confirm that reasoning hijacking at early stages is a dominant failure mode, not merely a final-output manipulation problem.

## Context
As MLLM-based mobile agents transition from simple conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments, they inherit a new class of security threats distinct from desktop or web prompt injection. The mobile ecosystem's cross-application content—notifications, screenshots, embedded images, and UI overlays—creates a rich attack surface where malicious objectives can be injected indirectly across modalities. Prior security analyses have largely addressed text-only or single-modal injection, leaving the cross-modal properties of mobile agent security poorly understood and underexplored.

## Implications
For practitioners building or deploying MLLM-based mobile agents, MobileInject provides a concrete, executable benchmark to stress-test agent robustness before production deployment, highlighting that security hardening must address the reasoning pipeline itself rather than only final outputs. For the broader AI security community, the findings signal that multimodal injection in mobile ecosystems represents a qualitatively different and more dangerous threat than web-based prompt injection, demanding new defense mechanisms tailored to cross-modal consistency manipulation and early-stage reasoning integrity. The open-source release of the benchmark further accelerates reproducible research and standardized evaluation across the mobile agent security subfield.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23307v1)
