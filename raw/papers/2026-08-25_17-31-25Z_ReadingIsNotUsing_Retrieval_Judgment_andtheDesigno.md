---
title: Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows
published: 2026-08-25T17:31:25Z
authors: Miao Liu, Zhizhe Liu
url: http://arxiv.org/abs/2608.24842v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows

## Abstract
Large language models (LLMs) are increasingly deployed as AI analysts to process financial disclosures and support AI-assisted investment decisions. Yet such systems are usually evaluated by what they can retrieve, not whether retrieved information affects their judgments. We identify a retrieval-integration gap in long-context financial analysis. Holding focal-firm information fixed and varying only unrelated context from 2,000 to 128,000 tokens, we find that a risk disclosure's influence on investment judgments falls to the experimental noise floor even as direct retrieval remains accurate. The pattern replicates across model families and judgment tasks and in experiments removing real disclosures from actual 10-K filings. More capable models postpone but do not eliminate the gap. Causal memory interventions show that compressed summaries and source-text lookup jointly transmit disclosures into judgments. Workflow architecture determines whether this transmission succeeds: chunk-and-summarize pipelines evict relevant information, whereas a targeted, structured restatement adjacent to the decision restores its influence. AI analyst performance is therefore jointly determined by model capability and workflow architecture. Retrieval-based evaluations can certify systems whose investment judgments ignore information they demonstrably retrieved.

## Metadata
- **Published**: 2026-08-25T17:31:25Z
- **Authors**: Miao Liu, Zhizhe Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24842v1)