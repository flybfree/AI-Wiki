---
title: Enmo Safety: External, Non-invasive, Model-agnostic Oversight for Off-the-Shelf Language Models
published: 2026-11-06T17:28:13Z
authors: Mohammed Nayeem Khan, Sarun Kumar K. S., Allan Kevin T., Chirag Vaidya, Vrishank Tiwari
url: http://arxiv.org/abs/2611.10099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enmo Safety: External, Non-invasive, Model-agnostic Oversight for Off-the-Shelf Language Models

## Abstract
We study a safety harness that improves itself without touching model weights. Enmo Safety wraps a chat model with a deterministic input assessment, trigger-matched safety guidance, spotlighting of untrusted content, and an output guard. A reflector model turns failures into one bounded update per round, and an update is kept only if it lowers harm without raising refusal of benign prompts on a held-out dev split. Every version is snapshotted and every decision ledgered. We evaluate a bare model, the seed harness and the evolved harness on six open benchmarks (HarmBench, AdvBench, JailbreakBench, XSTest, AgentHarm, deepset prompt-injections). On 150 items and on a 290-item holdout, none of the before/after differences on two models was statistically significant. A fourth iteration ran six policy models on a fresh 300-item split: the harness cut the unsafe rate significantly on two models (12.9% to 7.1%, p = 0.035; 10.2% to 3.6%, p = 0.036), not on the other four, and raised agentic-harm labels on two. Whether the rules fired was unrelated to outcome (Fisher p from 0.30 to 1.0), and the helpfulness clauses made agentic harm worse than no harness on obfuscated attacks. A reworded clause and an input-normalisation step form harness v22, at a measured cost in benign tool-task refusal. Each cell is one run, so these estimates do not establish a general safety improvement. Code, harness versions and ledger: https://github.com/rioryugen/enmo_safety

## Metadata
- **Published**: 2026-11-06T17:28:13Z
- **Authors**: Mohammed Nayeem Khan, Sarun Kumar K. S., Allan Kevin T., Chirag Vaidya, Vrishank Tiwari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.10099v1)