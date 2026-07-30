---
title: Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models
published: 2026-07-29T13:53:02Z
authors: Ashish Prajapati, Om Mohite
url: http://arxiv.org/abs/2607.26922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models

## Abstract
Multi-agent LLM pipeline systems break down the task among multiple roles for better reasoning, but are benchmarked mainly with large-scale commercial models. In this study, we investigate Parishad, a structured multi-agent system involving five roles, by deploying it on Qwen2.5-7B-Instruct, a local model, on two datasets: GSM8K (500 questions) and HumanEval (164 questions), compared with prompting directly and two-call self-refinement. The multi-agent system drops GSM8K accuracy from 75.0\% to 45.0\% with JSON data format due to the error accumulation problem. With plaintext format, the accuracy is restored to 82.0\%. A two-call self-refinement strategy (V1) can achieve 86.2\% accuracy on GSM8K, with 7.4$\times$ lower token usage. However, the same V1 implementation on HumanEval---where direct accuracy is already 96.3\%---actively destroys performance (66.5\%). A task-aware gated redesign (V2) applied to HumanEval preserves accuracy at 95.1\%. Our results demonstrate that communication format and implementation details determine outcomes more than architectural complexity, and that simpler approaches match or outperform multi-agent pipelines for local 7B model deployment. All code and data are released.

## Metadata
- **Published**: 2026-07-29T13:53:02Z
- **Authors**: Ashish Prajapati, Om Mohite
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26922v1)