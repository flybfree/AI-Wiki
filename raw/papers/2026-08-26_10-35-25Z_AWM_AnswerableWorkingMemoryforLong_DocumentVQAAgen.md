---
title: AWM: Answerable Working Memory for Long-Document VQA Agents
published: 2026-08-26T10:35:25Z
authors: Dongzhuoran Zhou, Yuqicheng Zhu, Yule Liu, Zhen Yang, Rui Lu, Yuxiao Dong, Jie Tang, Evgeny Kharlamov
url: http://arxiv.org/abs/2608.25618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AWM: Answerable Working Memory for Long-Document VQA Agents

## Abstract
Long-document visual question answering increasingly relies on VLM agents that retrieve candidate pages, inspect page images, write findings to working memory, and synthesize answers. Working memory should carry answer-supporting evidence across page inspections for later grounded answering, yet existing evaluation mainly checks final-answer correctness and evidence-page access. This creates a memory-quality blind spot: an agent may reach the right page and answer correctly while leaving behind memory too generic or incomplete to support answering once page context is removed. We introduce \emph{memory-only answerability}, a diagnostic that asks whether a reader can answer from the question and terminal working memory alone. Building on this diagnostic, \emph{Answerable Working Memory} (AWM) treats terminal working memory as an answerable evidence artifact, and AWM-GRPO incorporates this signal into the GRPO reward while preserving final-answer priority. Under GRPO, this reward assigns higher advantages to answer-correct trajectories whose terminal working memory remains answerable. On \textsc{MMLongBench-Doc}, even when gold evidence pages are provided, 42.5\% of correct answers still cannot be answered from terminal working memory alone. AWM-GRPO improves final-answer accuracy over the RAG baseline by 8.1 and 11.9 points on \textsc{MMLongBench-Doc} and \textsc{LongDocURL} and reduces the memory-missing-correct rate by 2.7 points over answer-only GRPO.

## Metadata
- **Published**: 2026-08-26T10:35:25Z
- **Authors**: Dongzhuoran Zhou, Yuqicheng Zhu, Yule Liu, Zhen Yang, Rui Lu, Yuxiao Dong, Jie Tang, Evgeny Kharlamov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25618v1)