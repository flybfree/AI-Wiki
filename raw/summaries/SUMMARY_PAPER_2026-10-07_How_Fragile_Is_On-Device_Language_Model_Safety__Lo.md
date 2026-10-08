---
title: How Fragile Is On-Device Language Model Safety? Localizing Safety-Critical Parameters for Sparse Fault Analysis
url: http://arxiv.org/abs/2610.09000v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_18-56-14Z_HowFragileIsOn_DeviceLanguageModelSafety_Localizin.md
generated_at: 2026-10-07 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether safety-critical behavior in small language models deployed on-device is concentrated in a sparse subset of parameters, making them vulnerable to targeted attacks. Using LLaMA-2-7B-Chat as a test case, the authors demonstrate that modifying as few as 0.19% of model weights in the MLP down_proj layer can dramatically degrade safety (achieving 53% Basic ASR and 56% GCG ASR) while barely affecting general utility benchmarks. The findings reveal a highly non-uniform distribution of safety sensitivity across the network, with down_proj and o_proj identified as the primary safety-critical components.

## Key Takeaways
- The authors employ two complementary localization methods—low-rank safety-associated subspace analysis and parameter-level safety-utility importance filtering—to identify where safety behavior is concentrated in the model. Both methods independently confirm that safety sensitivity is highly non-uniform, with the MLP down_proj layer consistently emerging as the dominant safety-sensitive component, while o_proj contributes a smaller but measurable effect.
- A striking finding is that perturbing only 0.19% of the total model weights within down_proj is sufficient to produce a 53% Basic Attack Success Rate and a 56% GCG Attack Success Rate, indicating that a very small fault surface can compromise safety alignment almost entirely. Meanwhile, the model's general capability remains largely intact, with tinyBenchmarks accuracy dropping only from 52.2% to 51.6%.
- These results establish a concrete, quantified fault surface for on-device models, demonstrating that safety alignment is not evenly distributed but rather depends on a narrow set of parameters that are disproportionately vulnerable to targeted manipulation, corruption, or adversarial modification.

## Context
As small language models are increasingly embedded in agentic systems, mobile devices, and edge computing platforms, the assumption that model weights remain intact and untampered becomes a critical safety assumption. This paper addresses a gap in the literature by shifting the safety conversation from prompt-level jailbreaks to the physical and computational integrity of locally stored model parameters. It connects the fields of adversarial machine learning, model compression, and embedded systems security by showing that safety alignment in transformer architectures is architecturally fragile in specific, identifiable locations.

## Implications
For practitioners deploying language models on resource-constrained devices, this work argues that blanket integrity protection of all parameters is unnecessary and inefficient; instead, selective protection of safety-critical layers such as down_proj and o_proj can provide meaningful defense at a fraction of the computational cost. For the broader AI safety community, the findings underscore that safety alignment is a structurally brittle property that can be silently undermined by minimal weight perturbations, motivating the development of targeted fault-detection mechanisms and integrity verification protocols specifically designed for on-device and agentic model deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09000v1)
