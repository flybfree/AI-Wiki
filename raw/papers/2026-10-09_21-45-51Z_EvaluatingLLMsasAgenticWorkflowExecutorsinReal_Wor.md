---
title: Evaluating LLMs as Agentic Workflow Executors in Real-World Customer Support Skills
published: 2026-10-09T21:45:51Z
authors: Md Tahmid Rahman Laskar, Gundeep Singh, Xue-Yong Fu, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay, Shayna Gardiner, Harsh Saini, Matthias Lee, Elena Khasanova, Quinten McNamara, Shashi Bhushan TN
url: http://arxiv.org/abs/2610.14346v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating LLMs as Agentic Workflow Executors in Real-World Customer Support Skills

## Abstract
Enterprise customer-support agents increasingly rely on Large Language Models (LLMs) to execute bounded, tool-using workflows. We study this problem through the lens of Skill LLMs: specialized executors that operate within a selected skill context and must complete a narrow, stateful workflow under policy and tool constraints. We present a benchmark construction pipeline that mines recurrent workflows from real-world transcripts, converts them into structured skill descriptions, maps them to tool requirements, simulates environment state with Model Context Protocol (MCP)-compatible mocks, and generates multi-turn tool-using dialogues. Using this benchmark, we conduct a large-scale zero-shot evaluation of 17 language models spanning closed model families and deployment-oriented open-weight models from 1.7B to 14B parameters, each judged independently by five strong LLM judges, plus a deterministic rule-based evaluator that checks tool coverage, hallucinated tool use, and unsupported claims. We find a consistent ranking in which GPT-5.4 leads by a wide margin and QWEN3.5-9B is the strongest open-weight model (below 20B), outperforming several closed baselines under every judge. We also find that judge choice is not a negligible methodological detail: pairwise judge agreement on the pass/fail verdict averages Kappa=0.524 across 10 judge pairs. These results suggest that comprehensive zero-shot evaluation of skill execution requires judge reliability as carefully as model capability.

## Metadata
- **Published**: 2026-10-09T21:45:51Z
- **Authors**: Md Tahmid Rahman Laskar, Gundeep Singh, Xue-Yong Fu, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay, Shayna Gardiner, Harsh Saini, Matthias Lee, Elena Khasanova, Quinten McNamara, Shashi Bhushan TN
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14346v1)