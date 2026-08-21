---
title: Repo0: Design-Driven Zero-to-All Code Generation
url: http://arxiv.org/abs/2608.19854v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_10-03-14Z_Repo0_Design_DrivenZero_to_AllCodeGeneration.md
generated_at: 2026-08-20 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Repo0, a framework for zero-to-all code generation that builds an entire software project from natural‑language requirements while preserving a modular repository structure. It uses a Dual-Directed-Acyclic-Graph to represent requirement and component DAGs and their alignment. Experiments on six repositories show Repo0 outperforms the baseline RPG in Functionality Coverage and Pass Rate.

## Key Takeaways  
- The Dual-DAG architectural state enables continuous structural evolution guided by modularity metrics, allowing the system to adapt component boundaries during generation.  
- Structural convergence is achieved before code generation, ensuring that test‑driven development follows a stable architecture.  
- Repo0 improves Functionality Coverage by up to 20.08 percentage points and Pass Rate by up to 29.74 percentage points compared with the strongest baseline.

## Context  
Zero-to-all code generation seeks to create full software projects from textual specifications without pre‑existing repository scaffolding, a challenge for large language model agents that typically assume fixed layouts. This work addresses the need for dynamic architectural planning and structural stability in such environments.

## Implications  
The findings suggest that explicit architectural state can significantly boost performance of AI‑driven code generation pipelines. Practitioners may adopt Dual-DAG models to improve modularity during development, benefiting both research and industry projects requiring rapid prototyping from requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19854v1)
