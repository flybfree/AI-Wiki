---
title: Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities
url: http://arxiv.org/abs/2607.16175v1
type: paper-summary
date: 2026-07-19
source_paper: 2026-07-17_17-55-19Z_EvaluatingOpen_WeightLLMsforGeneratingStructuredTh.md
generated_at: 2026-07-19 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates open-weight LLMs for generating Structured Threat Information Expression (STIX) from Connected Autonomous Vehicle vulnerability descriptions, achieving high F1 scores across various mapping tasks. Single-model configurations reach F1 0.94 for SDO, 0.63 for SRO, and 0.99 for CWE, while full MITRE ATT&CK mapping remains difficult. Multi-agent setups improve some metrics but still face challenges.

## Key Takeaways
- Single-model configurations achieve F1 scores of 0.94 for SDO, 0.63 for SRO, and 0.99 for CWE mapping.
- Complete MITRE ATT&CK mapping remains challenging across all models.
- In a multi-agent setup Gemma-4-31B and Codestral-22B achieve F1 scores of 0.91 for SDOs and 0.43 for SROs.

## Context
The broader AI research landscape is moving toward automated threat intelligence generation to reduce manual data processing in security operations. This study contributes by applying open-weight LLMs to a specific domain—CAV vulnerabilities—to produce STIX objects, highlighting both strengths and limitations of current models.

## Implications
For automotive security teams, these results suggest that open-weight LLMs can automate the creation of structured threat reports, accelerating incident response. However, the incomplete MITRE ATT&CK mapping indicates a need for further model refinement to cover all attack techniques, ensuring comprehensive defense strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16175v1)
