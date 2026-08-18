---
title: Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance
published: 2026-08-17T03:31:59Z
authors: Bowen Li, Guojun Wang
url: http://arxiv.org/abs/2608.16055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance

## Abstract
Existing agent benchmarks ask whether the agent finished the task. We ask whether it finished it within policy. We introduce Fiducia-bench, a benchmark for the governability of financial agents---whether they escalate when obligated, abstain when required, and leave an auditable trail---and use it to study a question no prior benchmark addresses: does decomposing an agent into components degrade its governance? It does, and the mechanism is specific. Policy-relevant facts discovered by one component are attenuated at the handoff boundary before reaching the component that must act on them. In a 626-episode experiment across 100 KYC/AML task variants, two models, and three architectures, a 32B open-weights model attenuated 0% of discovered facts under a single-loop baseline, 56% under a fixed pipeline, and 85% under an orchestrator-subagent architecture (all at constraint distance 2). A stronger model (gpt-4.1-mini) attenuated 3-6% under the same conditions, suggesting the governance cost of decomposition is partly a function of model capability. Critically, the same mechanism produces both under-escalation and over-escalation, depending on whether the dropped fact was a risk signal or an exculpating one. The benchmark, all tasks, and the verification harness are open-source

## Metadata
- **Published**: 2026-08-17T03:31:59Z
- **Authors**: Bowen Li, Guojun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16055v1)