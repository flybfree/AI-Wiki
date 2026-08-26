---
title: Automata from Agent Traces: Failure and Next-Step Prediction
url: http://arxiv.org/abs/2608.23670v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_17-58-01Z_AutomatafromAgentTraces_FailureandNext_StepPredict.md
generated_at: 2026-08-25 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a compact finite‑state machine that captures the shared behavioral topology of LLM agents across many execution traces, enabling reliable next‑step and failure prediction. The FSM is built from twelve public datasets, remains small (7–43 states), and can be generated in milliseconds while achieving near‑perfect fit on held‑out data.

## Key Takeaways
- The FSM compresses an entire trace corpus into a single structure that links next‑step and failure events across runs.  
- State‑level context improves next‑step prediction over existing memory mechanisms on every ground‑truth dataset.  
- Per‑state features yield AUROC up to 0.94 for failure detection, allowing early stopping from partial traces.

## Context
LLM agents generate long, unstructured logs that hinder safety monitoring and runtime oversight. Traditional methods treat each trace independently or only after success, missing the underlying pattern that could be reused across failures. This work introduces a model‑agnostic primitive to expose that pattern.

## Implications
The FSM offers practitioners a lightweight tool for auditing and monitoring agent behavior without retraining models. By linking prediction with early detection, it can reduce operational risk in real‑world deployments of generative AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23670v1)
