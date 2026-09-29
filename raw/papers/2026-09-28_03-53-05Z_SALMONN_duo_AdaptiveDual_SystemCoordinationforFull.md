---
title: SALMONN-duo: Adaptive Dual-System Coordination for Full-Duplex Voice Agents
published: 2026-09-28T03:53:05Z
authors: Wenyi Yu, Siyin Wang, Terumi Chiba, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Lu Lu, Chao Zhang
url: http://arxiv.org/abs/2609.34247v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SALMONN-duo: Adaptive Dual-System Coordination for Full-Duplex Voice Agents

## Abstract
Full-duplex speech large language models (LLMs) enable low-latency, natural voice interaction. However, real-world agents must also use tools and perform deliberative reasoning-operations whose variable latency and computational cost conflict with the stringent timing requirements of real-time conversation. To reconcile these demands, we propose SALMONN-duo, an adaptive dual-system voice agent inspired by dual-process theories of cognition. SALMONN-duo separates real-time interaction from deliberative computation by pairing an always-on, fast-thinking full-duplex speech LLM (system 1) with a powerful asynchronous slow-thinking LLM agent (system 2). Beyond handling real-time interaction, system 1 learns when to answer directly and when to delegate, remaining responsive during backend execution and seamlessly integrating returned information into the ongoing dialogue without exposing tool traces or losing conversational context. Evaluations on single-turn spoken question answering (QA) and multi-turn conversations demonstrate that adaptive delegation substantially improves accuracy on knowledge-intensive and multi-hop reasoning questions, while knowledge-boundary-aware training avoids unnecessary system 2 invocations. On a customized version of $τ$-Voice, SALMONN-duo further demonstrates its ability to complete environment-grounded, policy-constrained tasks through multi-turn interactions in realistic business scenarios. Finally, cost-aware reinforcement learning further enhances the trade-off between task performance and backend usage across the QA and conversation tasks, while improving task success and response safety on $τ$-Voice with an acceptable increase in the delegation rate.

## Metadata
- **Published**: 2026-09-28T03:53:05Z
- **Authors**: Wenyi Yu, Siyin Wang, Terumi Chiba, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Lu Lu, Chao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34247v1)