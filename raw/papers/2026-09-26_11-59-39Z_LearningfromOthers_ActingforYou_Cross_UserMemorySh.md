---
title: Learning from Others, Acting for You: Cross-User Memory Sharing for LLM Agents
published: 2026-09-26T11:59:39Z
authors: Jinming Hu, Haodong Zhao, Qi Jia, Die Chen, Tianhang Zhao, Sufeng Duan, Gongshen Liu
url: http://arxiv.org/abs/2609.32511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Others, Acting for You: Cross-User Memory Sharing for LLM Agents

## Abstract
Large language model (LLM) agents serving different users often solve related tasks, yet separate user histories can leave reusable experience inaccessible to other agents. Pooling memories expands access but risks transferring preferences that conflict with the receiving user's requirements. We introduce ShareMem, a memory architecture that shares reusable experience while grounding its application in the receiving user's own preferences. Shared experiences indicate how to act and which preferences to consult; the receiving user's memory supplies their concrete values. Two-stage consolidation refines experience locally before integrating accepted edits into a shared pool. During execution, scope-first retrieval jointly selects local and shared experiences under a common entry budget, while a user-bound channel supports initial and agent-initiated preference retrieval. We evaluate ShareMem across web navigation (Mind2Web), online personalized interaction (VitaBench~2.0), and multi-session coding (MemoryCode) with four backbone models. It improves step success, average task success, and dialogue-macro coding scores, respectively, over matched user-local memory across all four models. Ablations favor two-stage consolidation for smaller shared pools, lower induction token usage, and better downstream performance, and support complementarity between experience guidance and active preference retrieval. Further analyses show that sharing helps most when relevant local experience is scarce, while source quality and cross-user preference interference limit useful transfer.

## Metadata
- **Published**: 2026-09-26T11:59:39Z
- **Authors**: Jinming Hu, Haodong Zhao, Qi Jia, Die Chen, Tianhang Zhao, Sufeng Duan, Gongshen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32511v1)