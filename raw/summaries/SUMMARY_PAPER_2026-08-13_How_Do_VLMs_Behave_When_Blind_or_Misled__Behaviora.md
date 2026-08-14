---
title: How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures
url: http://arxiv.org/abs/2608.13267v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_14-06-35Z_HowDoVLMsBehaveWhenBlindorMisled_BehavioralEvaluat.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SciFigBench, a diagnostic benchmark that tests vision‑language models on scientific figures while evaluating their reliability when visual evidence is missing or misleading. The results show that high perception and reasoning scores do not guarantee behavioral consistency, with GPT‑5.2 excelling in description but hallucinating unreadable content, whereas Gemini 3.1 Pro demonstrates stronger uncertainty detection and resistance to misleading cues.

## Key Takeaways
- GPT‑5.2 achieves the highest description quality (MQM 91.6) and reasoning accuracy (78.4%) but hallucinates in 96% of uncertain cases, highlighting a gap between performance metrics and real‑world reliability.
- Gemini 3.1 Pro, despite slightly lower scores (MQM 90.2, reasoning 81.0%), admits uncertainty in 71% of such cases and attains the highest resistance score (0.91), indicating better handling of incomplete or misleading visual information.
- The A‑R‑I framework reveals that behavioral reliability under uncertainty is a distinct dimension from raw accuracy, underscoring its importance for scientific workflow deployment.

## Context
Vision‑language models are increasingly used to interpret and reason about scientific diagrams, yet most benchmarks focus solely on perception and reasoning without probing how models behave when evidence is incomplete or deceptive. This study bridges that gap by introducing a comprehensive set of stress tests that mimic real‑world uncertainties in scientific figure analysis.

## Implications
For researchers, the findings suggest that model selection should consider behavioral reliability as much as raw performance metrics. In industry, deploying VLMs for scientific data interpretation requires safeguards against hallucinations and misleading inference to ensure trustworthy outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13267v1)
