---
title: RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning
url: http://arxiv.org/abs/2607.28156v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-58-57Z_RRM_Experience_DrivenReflectiveRetrievalMemoryforL.md
generated_at: 2026-07-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Reflective Retrieval Memory (RRM), a framework that augments an entity-centric multimodal memory graph with reflective experience memory to improve long‑horizon reasoning. RRM learns reusable retrieval strategies from past tasks and converts them into query‑level guidance, while factual evidence is still retrieved separately. Experiments on M3‑Bench‑Robot, M3‑Bench‑Web, and Video‑MME‑Long show that RRM outperforms prior state‑of‑the‑art methods.

## Key Takeaways
- Reflective experience memory captures reusable search strategies across tasks, unlike episodic or semantic memories which only store factual evidence.  
- The framework converts retrieved experiences into query‑level guidance, keeping answer generation conditioned solely on newly fetched facts.  
- A lifecycle management mechanism regulates the use of experience memory through frequency, reuse feedback, and temporal decay to avoid redundancy.

## Context
Current multimodal long‑term agents rely heavily on external memory to extend context beyond video length, yet most approaches focus only on what is stored rather than how retrieval should be performed. This gap leads to frequent failure modes where agents cannot diagnose why evidence is missing or how to adapt their search strategies. RRM addresses this by introducing a reflective layer that learns from historical trajectories.

## Implications
RRM demonstrates that integrating procedural knowledge into memory can significantly boost performance on long‑horizon multimodal tasks, offering a template for systems that must reason over extended interactions. Practitioners in robotics and AI research can adopt the lifecycle management concept to maintain efficient, low‑noise experience memories.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28156v1)
