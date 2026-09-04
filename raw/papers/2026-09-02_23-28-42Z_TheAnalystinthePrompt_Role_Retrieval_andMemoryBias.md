---
title: The Analyst in the Prompt: Role, Retrieval, and Memory Biases in LLM Financial Analysis
published: 2026-09-02T23:28:42Z
authors: Ahmed Asaad, Amr Mohamed, Yang Zhang, Omneya Abdelsalam
url: http://arxiv.org/abs/2609.03218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Analyst in the Prompt: Role, Retrieval, and Memory Biases in LLM Financial Analysis

## Abstract
Large Language Models (LLMs) increasingly use user context such as memory, profiles, and role prompts to personalize their responses. This personalization can affect evidence-based judgment: the same evidence may lead to different conclusions under different user contexts. Finance provides a high-stakes setting to study this problem because decisions often depend on interpreting long and complex documents. We test this using 3,575 SEC filings across twelve LLMs. We compare persona-conditioned retrieval, neutral retrieval, and memory-framed context to separate the effect of evidence selection from the effect of interpretation. We find that most user-context spillover comes from how models interpret the same evidence under different roles, rather than from retrieving different evidence. We then test two simple mitigation strategies: expressing the same investor mindset as a user profile instead of an assistant role, and separating evidence-based and personalized outputs. Both reduce spillover, but neither removes it completely, and their effectiveness varies substantially across models.

## Metadata
- **Published**: 2026-09-02T23:28:42Z
- **Authors**: Ahmed Asaad, Amr Mohamed, Yang Zhang, Omneya Abdelsalam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03218v1)