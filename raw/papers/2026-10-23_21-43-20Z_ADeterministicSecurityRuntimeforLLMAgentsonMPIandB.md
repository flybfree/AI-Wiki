---
title: A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank
published: 2026-10-23T21:43:20Z
authors: Alfredo Metere
url: http://arxiv.org/abs/2610.33318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank

## Abstract
Large language model agents launch simulations on high-performance computing (HPC) systems, where one sbatch or mpirun can commit thousands of node-hours and a forged result can cost lives. Of 23 surveyed systems, none supervises the running job, and none holds when the control host is compromised. We fix both. Enclawed, our deterministic security runtime for AI agents, has until now served a single user; this work makes it a distributed runtime for parallel HPC and agent swarms. The Enclaweder, our hardware root of trust, keeps a compromised host from becoming a catastrophe. A launch gate decides every launch by policy alone, refusing what it cannot parse. Once the job runs, a swarm chain grants short leases against signed heartbeats and evicts on evidence, and a supervisor around every rank pauses it when its lease lapses and kills it on tampering. Each node signs with its Enclaweder's key, so the host can forge none of it. Enclawed needs no administrator privileges and plugs into existing clusters unchanged, over Secure Shell alone. Supervision leaves the compute loop of a 16-rank LAMMPS job unchanged, on graphics processors too, and adds about 3 s of start-up. Twelve live attacks on Enclaweder-keyed ranks, colluding coordinators included, ended fail-closed. Sixteen agents on a real model attempted 24 launches that planted instructions ordered; the gate denied all 24 and allowed all 108 legitimate ones. Enclawed's core and the HPC Agent Security Benchmark are open source.

## Metadata
- **Published**: 2026-10-23T21:43:20Z
- **Authors**: Alfredo Metere
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33318v1)