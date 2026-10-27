---
title: A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank
url: http://arxiv.org/abs/2610.33318v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_21-43-20Z_ADeterministicSecurityRuntimeforLLMAgentsonMPIandB.md
generated_at: 2026-10-26 20:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Enclawed, a deterministic security runtime designed to supervise LLM agents that launch parallel simulations on high-performance computing clusters via sbatch or mpirun. The system addresses a critical gap identified across 23 surveyed HPC environments: none provides runtime supervision of running jobs, and none remains trustworthy when the control host is compromised. Enclawed closes both gaps through a hardware-rooted trust chain, a policy-governed launch gate, and per-rank supervision that enforces fail-closed behavior under adversarial conditions.

## Key Takeaways
- Enclawed introduces the "Enclaweder," a hardware root of trust that anchors every node's cryptographic identity, ensuring that even a compromised control host cannot forge job results, heartbeats, or supervision decisions. Each rank signs with its Enclaweder's key, making tampering detectable and eviction evidence-based rather than discretionary.
- The launch gate operates purely on policy, refusing any job specification it cannot parse. In evaluation, 16 agents on a real model attempted 24 planted adversarial launches; the gate denied all 24 while permitting all 108 legitimate launches, demonstrating precise policy enforcement without false positives on valid workloads.
- Runtime supervision uses a "swarm chain" granting short leases validated against signed heartbeats, with a per-rank supervisor that pauses a job when its lease lapses and kills it on tampering. Twelve live attacks against Enclaweder-keyed ranks, including colluding coordinators, all ended fail-closed. The overhead is minimal: supervision leaves the compute loop of a 16-rank LAMMPS job unchanged (including on GPUs) and adds only about 3 seconds of start-up time.

## Context
As LLM agents increasingly orchestrate scientific and engineering workflows on HPC clusters—where a single mpirun invocation can commit thousands of node-hours and a fabricated simulation result can have life-or-death consequences—the absence of runtime supervision and host-trust guarantees represents a systemic security gap. This paper matters because it is the first to propose a deterministic, hardware-rooted supervision layer that integrates with existing MPI and batch-scheduled infrastructure without requiring administrator privileges or cluster reconfiguration, operating over SSH alone.

## Implications
For practitioners deploying agentic AI in scientific computing, Enclawed offers a deployable security boundary that prevents both adversarial prompt injection at launch time and runtime tampering during execution, without altering existing job scripts or scheduler configurations. The open-source release of the core runtime and the HPC Agent Security Benchmark provides a reproducible evaluation framework, enabling the community to measure and compare agent supervision guarantees on real clusters. For industry, the fail-closed design and negligible overhead (approximately 3 seconds) suggest that deterministic supervision can be adopted as a default safety layer in any HPC environment where autonomous agents trigger large-scale computations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33318v1)
