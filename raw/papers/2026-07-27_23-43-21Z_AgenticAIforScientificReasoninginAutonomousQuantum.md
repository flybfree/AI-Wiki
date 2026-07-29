---
title: Agentic AI for Scientific Reasoning in Autonomous Quantum Sensing Experiments
published: 2026-07-27T23:43:21Z
authors: Takuya Isogawa, Ryotaro Okabe, Nutdech Phadetsuwannukun, Mingda Li, Paola Cappellaro
url: http://arxiv.org/abs/2607.25145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic AI for Scientific Reasoning in Autonomous Quantum Sensing Experiments

## Abstract
We implement an agentic AI workflow built around a large language model (LLM) agent for autonomous experiments with nitrogen-vacancy (NV) centers in diamond. NV centers are a widely used platform for quantum sensing, and the ability to control many measurements from a computer makes NV experiments a natural setting for autonomous workflows. We make two main contributions. First, we demonstrate an autonomous NV experiment workflow that combines persistent project records, quantitative calculation and data analysis tools, and deterministic experiment control. In one autonomous experiment, the agent selected a single NV center, calibrated its resonant frequency, measured \(T_2^\ast\) with Ramsey measurements, and added a Carr--Purcell--Meiboom--Gill (CPMG) measurement to check a weak feature that could be related to nearby \(^{13}\mathrm{C}\). Second, we introduce two offline benchmarks that evaluate the agent's reasoning separately from laboratory execution. We evaluated both benchmarks with GPT-5.4, GPT-5.5, and GPT-5.6 Sol. In the Ramsey checkpoint benchmark, greater reasoning effort generally improved recognition of a residual resonance calibration offset. By contrast, in the pulsed optically detected magnetic resonance (pODMR) data evaluation benchmark, pulse sequence information alone produced more false positive resonance judgments at higher reasoning effort. Requiring an expected signal calculation kept false positive rates low across all three models and reasoning settings. The results suggest a clear division of labor for autonomous experiments. The agent forms scientific hypotheses and uses quantitative tools to evaluate data, while deterministic code controls the hardware and enforces safety constraints.

## Metadata
- **Published**: 2026-07-27T23:43:21Z
- **Authors**: Takuya Isogawa, Ryotaro Okabe, Nutdech Phadetsuwannukun, Mingda Li, Paola Cappellaro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25145v1)