---
title: Automata from Agent Traces: Failure and Next-Step Prediction
published: 2026-08-24T17:58:01Z
authors: Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton Da Costa, Ilham Wicaksono, Adriano Koshiyama
url: http://arxiv.org/abs/2608.23670v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automata from Agent Traces: Failure and Next-Step Prediction

## Abstract
LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

## Metadata
- **Published**: 2026-08-24T17:58:01Z
- **Authors**: Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton Da Costa, Ilham Wicaksono, Adriano Koshiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23670v1)