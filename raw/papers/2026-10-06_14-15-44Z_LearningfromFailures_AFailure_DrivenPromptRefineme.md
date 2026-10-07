---
title: Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis
published: 2026-10-06T14:15:44Z
authors: Mandana Ghadamian, David Mohaisen
url: http://arxiv.org/abs/2610.08405v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis

## Abstract
Large Language Models have emerged as promising tools for software vulnerability analysis, but their effectiveness depends heavily on prompt design. Existing research primarily compares prompting strategies using aggregate performance metrics, providing limited insight into why models fail or how prompts can be improved systematically. We propose Failure-Driven Prompt Refinement (FDPR), a methodology that analyzes recurring model failures to guide evidence-based prompt refinement. Using the Damn Vulnerable Java Application (DVJA), we identify recurring failure modes, including false positives, false negatives, unsupported reasoning, and CWE misclassification, and translate them into targeted prompt refinements. We then evaluate the resulting prompt on the Juliet Test Suite and perform cross-model validation to assess generalizability. The results show that failure-driven refinement improves the reliability of LLM-based vulnerability analysis while yielding reusable prompt design principles. More broadly, this work demonstrates that recurring model failures provide a principled foundation for prompt engineering, enabling the systematic development of more reliable LLM-based vulnerability analysis systems.

## Metadata
- **Published**: 2026-10-06T14:15:44Z
- **Authors**: Mandana Ghadamian, David Mohaisen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08405v1)