---
title: Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution
url: http://arxiv.org/abs/2610.09772v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_09-53-28Z_DecouplingLogicfromPersona_StructuralImmunityofEdg.md
generated_at: 2026-10-07 21:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how small language-model agents running on edge devices suffer from "persona-logic interference" when conversational history and persona instructions pollute the context window needed for correct reasoning. The authors propose a Decoupling Architecture (AO-DA) that splits logical inference from persona expression into two separate inference paths on a single INT4 base model using hot-swappable LoRA adapters, demonstrating that the logic path remains structurally invariant to context pollution while the mixed single-pass approach degrades monotonically.

## Key Takeaways
- The decoupled logic path achieves structural immunity to context pollution: its prompt remains fixed at 180 tokens (Llama-3.1-8B) or 167 tokens (Gemma-3-4B) regardless of pollution level, while the mixed single-pass prompt balloons from 242 to 1,203 tokens. Across 40 runs per condition, the decoupled logic outputs are byte-identical across all four pollution levels, confirming that isolating the core turn from persona-heavy history eliminates interference entirely.
- The mixed single-pass approach degrades monotonically in composite logic score, dropping from 0.669 to 0.150 on Llama and from 0.487 to 0.150 on Gemma as pollution increases. The dominant failure mode is the inability to emit the required structured output (Micro-State), affecting 80–95% of Llama runs and 100% of Gemma runs at the two highest pollution levels, revealing that persona instructions actively corrupt format compliance.
- The dedicated-adapter, dedicated-format path outperforms the single pass on the 8B model (failure rate 0–20% versus 80–95%, with paired effect sizes of +0.30 to +0.50 and Cliff's delta of 0.50–0.85 at Holm-adjusted p ≤ 0.03), but both approaches collapse on the 4B model, indicating a minimum model-capacity threshold below which architectural separation alone cannot rescue logical reliability. The separation costs one extra decode on a topic's first turn (28.2 s versus 18.2 s on Llama) yet enables persona hot-swapping in just 1.7 ms without re-executing the logic path.

## Context
Edge-deployed small language models are increasingly used in privacy-sensitive, offline, or latency-constrained settings where a single context window must simultaneously carry persona instructions, long conversational history, and the current reasoning turn. This paper addresses a fundamental tension in the field: the same context window that gives an agent its character also introduces noise that corrupts its logical output, a problem that larger cloud models can absorb through sheer capacity but that small INT4 models cannot. By formalizing this as "persona-logic interference" and proposing a two-path architecture validated across 480 controlled runs, the work bridges the gap between prompt-engineering heuristics and principled architectural design for resource-constrained agents.

## Implications
For practitioners building on-device assistants, chatbots, or embedded reasoning agents, the findings suggest that architectural separation of logic and persona is not merely an optimization but a structural necessity for maintaining output reliability as conversations grow longer and persona instructions become more elaborate. The hot-swappable LoRA adapter mechanism offers a practical path for multi-persona or multi-character deployments without re-running expensive logic inference, which is especially valuable for consumer hardware like laptops and mobile devices. However, the collapse observed on the 4B model warns that model capacity remains a hard floor: no amount of architectural cleverness can substitute for sufficient parameter count when structured output fidelity is required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09772v1)
