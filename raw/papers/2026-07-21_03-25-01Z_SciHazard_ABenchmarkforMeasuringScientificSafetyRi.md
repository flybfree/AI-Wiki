---
title: SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring
published: 2026-07-21T03:25:01Z
authors: Chunxiao Li, Yuan Xiong, Lijun Li, Tianyi Du, Wenlong Zhang, Lei Bai, Jing Shao
url: http://arxiv.org/abs/2607.18665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring

## Abstract
Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance. Existing benchmarks often rely on templated queries disconnected from real-world hazards, and employ LLM-as-a-Judge paradigms without domain grounding. To address this, we introduce SciHazard, a real-world-grounded benchmark for scientific risks and a dataset agnostic evaluation framework for measuring harmfulness. SciHazard contains 2400 hazardous questions and 600 oversafety questions across 12 disciplines, with both queries grounded in regulated entities and documented failure scenarios. To compute \textsc{DeHarm-Score} , we develop a decomposed evaluating procedure that combines query hazard severity, refusal behavior, and response-level risk. For non-refused responses, it further decomposes response-level harm into \textsc{Executability}, quantified via dynamic checklists with importance weighting, and \textsc{Net-new risk}, assessed through retrieval-augmented claim extraction and synthesis-barrier verification. An expert-validation study shows that \textsc{DeHarm-Score} improves agreement with expert annotations by 90.17\% over the strongest baseline. We benchmark 31 frontier LLMs and deep research agents in an extensive scientific safety evaluation. Notably, deep research agents yield 32.3\% higher mean \textsc{DeHarm-Score} than standard LLMs, exposing autonomous agents as a critical blind spot in current safety defenses. Code and dataset are available at https://anonymous.4open.science/r/DeharmScore-7B55.

## Metadata
- **Published**: 2026-07-21T03:25:01Z
- **Authors**: Chunxiao Li, Yuan Xiong, Lijun Li, Tianyi Du, Wenlong Zhang, Lei Bai, Jing Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18665v1)