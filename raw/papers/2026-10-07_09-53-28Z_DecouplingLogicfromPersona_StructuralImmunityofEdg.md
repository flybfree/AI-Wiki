---
title: Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution
published: 2026-10-07T09:53:28Z
authors: Masaaki Nakatsu, Reno Wang
url: http://arxiv.org/abs/2610.09772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution

## Abstract
Small language-model agents on edge devices must hold a persona and reason correctly at once, inside one context window that fills with conversational history and persona instructions. We study what happens to the logical part of such an agent when that history is long, misleading and persona-heavy (persona-logic interference), and present a Decoupling Architecture (AO-DA) that separates logical inference ("What") from persona expression ("How") into two inference paths on one INT4 base model with hot-swappable LoRA adapters. The logic path receives only the core turn and emits a verifiable structured state (Micro-State); the persona path renders it in character with the full history. In same-base-model ablations on an Apple M2 laptop (Llama-3.1-8B-Instruct and Gemma-3-4B-it, 4-bit; 480 runs over 4 pollution levels x 3 arms x 2 tasks x 2 personas x 5 seeds) we find: (i) the decoupled logic path is structurally invariant to pollution: its prompt stays at 180 (Llama) or 167 (Gemma) tokens while the mixed single-pass prompt grows from 242 to 1,203, and its outputs are byte-identical across levels (40/40); (ii) the mixed single pass degrades monotonically (composite logic score 0.669 to 0.150 on Llama, 0.487 to 0.150 on Gemma), mostly by failing to emit the required structured output (80-95% of runs on Llama, 100% on Gemma at the two highest levels); (iii) with the same pollution fed into the decoupled logic path, the dedicated-adapter, dedicated-format path is still more robust than the single pass on the 8B model (failure 0-20% vs 80-95%; paired $Δ$ +0.30 to +0.50, Cliff's $δ$ 0.50-0.85, Holm-adjusted $p \le 0.03$) but not on the 4B model, where both collapse. Separation costs one extra decode on a topic's first turn (28.2 s vs 18.2 s on Llama) and buys persona hot-swapping in 1.7 ms without re-running the logic path. Code, rubric, fixtures, adapters and logs are released.

## Metadata
- **Published**: 2026-10-07T09:53:28Z
- **Authors**: Masaaki Nakatsu, Reno Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09772v1)