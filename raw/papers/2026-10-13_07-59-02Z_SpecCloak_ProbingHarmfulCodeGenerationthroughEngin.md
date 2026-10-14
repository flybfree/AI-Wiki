---
title: SpecCloak: Probing Harmful Code Generation through Engineering Specifications
published: 2026-10-13T07:59:02Z
authors: Wenbin Chen, Jiexin Wang, Guanting Wu, Jiaxi Liang, Yi Cai
url: http://arxiv.org/abs/2610.17907v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecCloak: Probing Harmful Code Generation through Engineering Specifications

## Abstract
The code generation capabilities of large language models (LLMs) can equally be misused to implement harmful functionality, underscoring the need to understand their safety behavior in response to programming requests. While request phrasing is known to influence refusal, it remains unclear whether the form in which coding task requirements are stated affects the refusal process for malicious code generation. We introduce PseudoSpec, a template that organizes functional requirements as engineering specifications, and investigate its effects through controlled comparisons, representation analysis, and activation interventions. Across five open-weight models, removing explicit risk keywords only partially reduces refusal, whereas specification prompting substantially lowers refusal even when these keywords are retained. This reduction accompanies consistent shifts toward code-output-related representations, and interventions along condition-difference directions alter refusal behavior. Output analysis further distinguishes code-related responses from generation degeneration. Building on these findings, we propose SpecCloak, a black-box red-teaming framework combining PseudoSpec with discriminator-guided optimization, achieving an average execution-verified attack success rate of 28.91\% across eight target models on RedCode-Gen. We also introduce SpecReveal, a defense prototype combining natural-language intent reconstruction with dual-view detection without target-model fine-tuning. It achieves a 96.88\% attack detection rate in a separate prompt-detection evaluation, with false positives assessed on benign programming and specification-style inputs. These results connect specification-induced response differences to practical security consequences and identify intent reconstruction as a complementary detection approach.

## Metadata
- **Published**: 2026-10-13T07:59:02Z
- **Authors**: Wenbin Chen, Jiexin Wang, Guanting Wu, Jiaxi Liang, Yi Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17907v1)