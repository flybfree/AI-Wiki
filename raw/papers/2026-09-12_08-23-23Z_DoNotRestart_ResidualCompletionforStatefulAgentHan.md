---
title: Do Not Restart: Residual Completion for Stateful Agent Handoffs
published: 2026-09-12T08:23:23Z
authors: Runzhi Deng, Yiming Zhong, Fang Zhao, Pan Zhou
url: http://arxiv.org/abs/2609.13800v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Not Restart: Residual Completion for Stateful Agent Handoffs

## Abstract
Routing and cascades reduce tool-agent cost by transferring control across models, but stateful handoffs must preserve accepted choices, realized effects, and unfinished obligations. We formulate this as commitment-constrained residual completion and introduce Commitment-Frontier Residual Completion (CFRC). CFRC enforces target-before-proposal, whole-proposal-before-authority, and live-evidence-before-success: it freezes a residual contract from accepted progress, closes the successor continuation into an evidence-linked graph, and admits execution only when the remainder is covered, with live receipts discharging obligations. We establish contract-relative partial correctness, which extends to the original residual request under complete contract construction. Across five environments and two same-provider model pairs, CFRC achieves comparable macro accuracy to strong full-task agents at only 22.0%-34.6% of their inference cost, with additional cross-provider results demonstrating broader transfer.

## Metadata
- **Published**: 2026-09-12T08:23:23Z
- **Authors**: Runzhi Deng, Yiming Zhong, Fang Zhao, Pan Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13800v1)