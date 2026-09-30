---
title: Traverse: Learning When to Remember, Reset, and Redirect for Long-Horizon Web Search
published: 2026-09-29T09:13:44Z
authors: Jingyuan Ma, Lynx Aster, He Zhang, Siyao Song, Weijie Yuan, Zhe Zhang, Kai Jia, Zhifang Sui
url: http://arxiv.org/abs/2609.37082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Traverse: Learning When to Remember, Reset, and Redirect for Long-Horizon Web Search

## Abstract
Long-horizon information-seeking agents often accumulate noisy or misleading context, causing early mistakes to persist and making recovery increasingly difficult. We introduce an autonomous search harness in which the agent manages its own search process through three states: Rubric, Answer, and Verify. The agent first defines criteria for a valid answer, searches under these criteria, and then independently verifies the result before deciding whether to terminate or continue searching. It is further equipped with a Seal Memory tool that enables active context management. Training this behavior with reinforcement learning, however, can induce Seal Collapse, resulting in unstable training and preventing the agent from reliably learning when and how to use its memory tools. We solve this with a simple strategy that trains only the final segment after context management. Our 35B model achieves 72.83 on BrowseComp, outperforming comparable open-source systems, and consistently improves over the base model across BrowseComp-ZH, xbench, DeepSearchQA, WideSearch, financial investigation, and product search. Ablations show that autonomous compression outperforms automatic compaction and validate our RL design.

## Metadata
- **Published**: 2026-09-29T09:13:44Z
- **Authors**: Jingyuan Ma, Lynx Aster, He Zhang, Siyao Song, Weijie Yuan, Zhe Zhang, Kai Jia, Zhifang Sui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37082v1)