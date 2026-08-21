---
title: Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents
published: 2026-08-20T02:11:03Z
authors: Baichuan Li, Junyi Yao, Zihao Zheng
url: http://arxiv.org/abs/2608.19564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents

## Abstract
Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior. We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user. MCB contains 140 primary scenarios, split into 70 development and 70 held-out items, plus a separate 70-item contrast set. It evaluates both action labels and structured tool-call selection. Two non-authors independently label the 70 held-out primary and 70 contrast items (97.1% agreement, Cohen's kappa = 0.962); a blind third resolves four disagreements, replacing eight author labels by non-author majority. Across Claude and Qwen, models verify changing facts more reliably than they ask users to resolve ambiguity. Bare Qwen asks on 0/12 clarification items while verifying 12/18 freshness items. Few-shot prompting raises accuracy from 0.557 to 0.771 (paired delta = +0.214, Holm-adjusted exact McNemar p_H = 0.002), yet clarification recall remains 0.333. The policy prompt reduces erroneous persistence from 0.243 to 0.100 (p_H = 0.038), although its accuracy gain is not significant. Label-tool agreement is 57% for each Claude model and 23% for Qwen; Qwen accuracy falls from 0.557 to 0.343 (p_H = 0.047). Memory evaluation must test both stated decisions and tool-call choices.

## Metadata
- **Published**: 2026-08-20T02:11:03Z
- **Authors**: Baichuan Li, Junyi Yao, Zihao Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19564v1)