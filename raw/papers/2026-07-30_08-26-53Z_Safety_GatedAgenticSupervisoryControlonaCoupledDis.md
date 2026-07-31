---
title: Safety-Gated Agentic Supervisory Control on a Coupled Distillation Benchmark: Regime Map, Auditable Gate, and Co-Design Findings
published: 2026-07-30T08:26:53Z
authors: Christian Rosenthal
url: http://arxiv.org/abs/2607.27849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety-Gated Agentic Supervisory Control on a Coupled Distillation Benchmark: Regime Map, Auditable Gate, and Co-Design Findings

## Abstract
An open-weight LLM can write composition setpoints every five minutes. What a plant still needs is a hard check: named constraints, logged margins, and an admit/block decision before the regulatory layer moves. This paper puts that check in a rule-based forked-twin counterfactual gate (nine pinned constraints) and leaves the regulatory layer unchanged. On Skogestad's Column A the ladder is PID-only (C0), linear MPC (C1), ungated agent (C2), and gated agent (C3) under one contract: identical level closure (M_D, M_B), scenarios, and seeds; C2/C3 share the linear-MPC backend.   The split is not subtle. Off-nominal target acquisition: the agent beats Pareto-tuned linear MPC in the strong band (C2/C1 IAE ratio 0.361 at the upper CI). Disturbance rejection on the same 16-point grid inverts by 16.03 at the upper CI (10.18 at the point estimate), where an ungated LLM supervisor does not belong. The gate compresses a specification-abandonment attractor into a bounded offset (d approx. -1.4; P95 cell IAE 11.5 to 0.77). A one-line prompt fix removes the attractor at source (6/10 to 0/10; sensitivity only, not a new headline). In a 250-cell statistical pass, 534 of 590 gate interventions are spec-on-bound geometry: the operating specification sits on a safety limit, so a well-behaved OP becomes inoperable while misbehaving ones are only contained; 318 blocks still correct actively harmful proposals.   Headlines are single-column and model-conditional on DeepSeek-V4-Flash. A second-family sweep (NVIDIA Nemotron-3-Super) keeps the disturbance-rejection fails band and plant-side failure geography; magnitudes and protocol operability stay model-conditional, and Super target-acquisition strong cells are survivors only (not confirmation). Transfer means twin, constraint envelope, and setpoint interface, not a second plant class measured here.

## Metadata
- **Published**: 2026-07-30T08:26:53Z
- **Authors**: Christian Rosenthal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27849v1)