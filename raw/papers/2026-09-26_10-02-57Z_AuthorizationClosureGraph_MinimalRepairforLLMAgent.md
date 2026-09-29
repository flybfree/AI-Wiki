---
title: Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions
published: 2026-09-26T10:02:57Z
authors: Qingzhuo Wang, CaiYi Wang, Jinglu Meng, Ruiyang Qin, Kunyu Peng, Zhihua Wei, Wen Shen
url: http://arxiv.org/abs/2609.32428v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions

## Abstract
Tool-using large language model (LLM) agents increasingly perform state-changing actions that require user authorization. Yet existing approaches do not provide a principled mechanism for selectively updating prior authorization when only part of an instruction changes. To this end, we propose an Authorization-Closure-Graph (ACG)-based framework that represents authorization and its dependencies as an evolving, versioned state. ACG selectively invalidates authority affected by a revision while preserving unaffected portions of the authorization state, and computes a minimal repair that identifies only the missing evidence or authority required for execution. This enables agents to adapt to revised instructions while avoiding stale authority and unnecessary authorization requests. We evaluate ACG across three advanced LLMs in two natural tasks, and ACG consistently improves action safety rate and task success rate. Code is available at https://github.com/weiliang822/ACG.

## Metadata
- **Published**: 2026-09-26T10:02:57Z
- **Authors**: Qingzhuo Wang, CaiYi Wang, Jinglu Meng, Ruiyang Qin, Kunyu Peng, Zhihua Wei, Wen Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32428v1)