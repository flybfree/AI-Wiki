---
title: From Acoustic Sensing to Physical Actions: A Comprehensive Survey of Security Risks in Edge-Deployed Audio LLM-Based Agents
url: http://arxiv.org/abs/2610.15390v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_06-38-40Z_FromAcousticSensingtoPhysicalActions_AComprehensiv.md
generated_at: 2026-10-13 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This survey introduces an Acoustic Sensing-to-Action (S2A) system model that traces security implications along the full path from acoustic sensing through persistent agent state to external physical execution in edge-deployed Audio LLM-based agents. The authors synthesize attacks, defenses, and evaluation methods across acoustic, agent, and edge-system literature, revealing that security gaps emerge both within individual components and at the transitions between stages, where protections designed for one stage fail to provide end-to-end assurance in deployed systems.

## Key Takeaways
- Audio LLMs embedded in agents for smart homes, vehicles, wearables, and embodied systems create a security pathway where acoustic inputs propagate from perception into persistent state and consequential physical execution, extending security analysis beyond model behavior to the system conditions that determine how acoustic inputs influence agent behavior and external actions.
- Existing surveys treat acoustic security, LLM-based agents, and edge deployment as isolated research areas, leaving the security interactions among these components in deployed Audio LLM-based agents insufficiently characterized; this paper addresses that gap by unifying the analysis under a single S2A framework that accounts for edge-cloud runtime and lifecycle transformation.
- The synthesis demonstrates that security gaps can emerge within individual components and at the transitions between stages, meaning protections developed for one stage do not necessarily provide end-to-end assurance in the deployed system, motivating security evaluation that follows acoustic influence from sensing to action across persistent state, system boundaries, and changing deployment conditions.

## Context
Audio LLMs are rapidly being integrated into physical agent systems deployed at the edge, where they interpret spoken commands, environmental sounds, and acoustic signals to trigger real-world actions such as unlocking doors, adjusting vehicle controls, or activating wearable devices. This survey matters because the field has developed security research in silos—acoustic adversarial attacks, LLM agent vulnerabilities, and edge deployment constraints—without adequately examining how these risks compound when combined in a single deployed pipeline from microphone input to physical actuation.

## Implications
For practitioners deploying Audio LLM agents in safety-critical environments like autonomous vehicles, smart homes, and medical wearables, this survey highlights that component-level security hardening is insufficient and that end-to-end evaluation must trace acoustic influence across persistent memory, system boundaries, and evolving deployment conditions. Industry stakeholders and standards bodies should adopt the S2A model as a framework for auditing deployed agents, ensuring that defenses at the sensing stage, the reasoning stage, and the execution stage are evaluated as an integrated chain rather than in isolation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15390v1)
