---
title: Using Fine-Tuned LLMs to Identify Indicators of Vulnerability in UK Police Incident Logs
url: http://arxiv.org/abs/2607.18446v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_18-58-33Z_UsingFine_TunedLLMstoIdentifyIndicatorsofVulnerabi.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether a fine‑tuned language model can reliably detect four vulnerability indicators — mental ill health, substance misuse, alcohol dependence and homelessness — within thousands of UK police incident narratives. The authors report that while the model yields useful prevalence estimates at scale, its outputs are unreliable without correction and cannot be trusted as valid measurements.

## Key Takeaways
- Mental ill health appears in about one‑in‑five incidents, but other indicators show lower rates, indicating uneven detection capability across vulnerability categories.  
- Single‑pass LLM classifications are unstable and tend to over‑assign indicators compared with human reviewers, highlighting the need for aggregation and statistical adjustment.  
- Achieving defensible estimates requires substantial human input and correction, leaving considerable uncertainty that limits suitability for operational decisions.

## Context
This work contributes to the growing body of research on applying large language models to unstructured administrative data in public services. It demonstrates that LLMs can extract meaningful signals from text, yet also underscores persistent challenges such as bias, inconsistency, and the need for human oversight. The findings are relevant to any domain where AI is used to quantify social risk factors.

## Implications
For police agencies, the study suggests that LLM‑based vulnerability screening should be treated as a supportive tool rather than a definitive measure, requiring robust validation pipelines. Practitioners must allocate resources for model refinement and human review to ensure ethical and accurate outcomes in decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18446v1)
