---
title: Detecting Contaminated Code-Generation Prompt Batches via Influence Functions
published: 2026-08-14T13:37:53Z
authors: Francesco Quinzan, Noor Munir, Yishun Lu, Stephen Roberts
url: http://arxiv.org/abs/2608.14303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Detecting Contaminated Code-Generation Prompt Batches via Influence Functions

## Abstract
Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabilities, CodeSIFT measures the parameter-space influence of generated code and uses a statistical test to determine whether a candidate prompt set deviates from a benign reference distribution. To evaluate our approach, we introduce two benchmark datasets covering a variety of vulnerabilities. We evaluate CodeSIFT on three open-weight code LLMs ranging from 3B to 7B parameters, achieving AUROC scores of up to 0.98 at moderate-to-high injection rates, while maintaining well-calibrated false positive rates and substantially outperforming static analysis baselines. These results suggest that influence-function-based detection is a promising direction for identifying malicious code-generation prompts without requiring prior knowledge of the underlying attack class.

## Metadata
- **Published**: 2026-08-14T13:37:53Z
- **Authors**: Francesco Quinzan, Noor Munir, Yishun Lu, Stephen Roberts
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14303v1)