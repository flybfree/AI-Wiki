---
title: ARSM: Auto-Regressive State Machine for Agentic Reasoning Compression
url: http://arxiv.org/abs/2609.32852v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_18-26-49Z_ARSM_Auto_RegressiveStateMachineforAgenticReasonin.md
generated_at: 2026-09-28 21:58
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces ARSM (Auto-Regressive State Machine), a training-free framework designed to address the memory bottleneck in LLM-based agents by enabling in-situ reasoning compression through structured state evolution. By reorganizing interaction histories into compact Hypothesis-Action-Result micro-chains and regulating memory via a dynamic state machine, ARSM reduces token consumption without degrading task performance on long-horizon tasks like Webshop and SWE-Bench Lite.

## Key Takeaways
- Existing memory compression techniques often require task-specific optimization or external auxiliary models, which introduces high computational costs and leads to information dilution due to the loss of structured relationships in compressed representations; ARSM eliminates these drawbacks by operating as a lightweight, training-free framework that preserves structural integrity.
- ARSM employs two core mechanisms unified within an auto-regressive generation space: a trajectory abstraction mechanism that compresses interaction histories into compact Hypothesis-Action-Result (HAR) micro-chains, and a dynamic state machine that manages hierarchical memory through atomic operations controlled by a compression parameter, allowing the model to jointly execute actions and update internal states.
- Experimental evaluations across diverse benchmarks including Webshop, Multi-Objective Multi-Hop QA, and SWE-Bench Lite demonstrate that ARSM successfully maintains task performance while significantly reducing token consumption, proving its effectiveness as a practical solution for scaling autonomous agents in long-horizon scenarios without compromising decision consistency.

## Context
As LLM-based agents increasingly tackle complex, multi-step tasks, the exponential growth of context windows creates severe memory bottlenecks that hinder scalability and increase inference costs. Current compression strategies struggle to balance efficiency with fidelity, often sacrificing the nuanced state tracking required for reliable agentic behavior; this work addresses a critical gap by offering a model-agnostic approach to reasoning compression that integrates seamlessly into standard autoregressive generation processes.

## Implications
The

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32852v1)
