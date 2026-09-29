---
title: IGSD: Environment-Verified Hindsight Self-Distillation for Search Agents
published: 2026-09-26T14:57:17Z
authors: Angqing Jiang, Gaoming Zhang, Chaoqun Zhang, Jianchun Song, Liyuan Kong, Kena Qi, Wei Lin, Defu Lian
url: http://arxiv.org/abs/2609.32694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IGSD: Environment-Verified Hindsight Self-Distillation for Search Agents

## Abstract
On-policy self-distillation densifies agent training without external teachers: a policy conditioned on privileged hindsight provides step-level guidance for its own unprivileged rollouts. For search agents, however, hindsight can make the teacher prefer a query that does not improve retrieval from the student's state. Existing methods either distill this preference directly or filter it with model-internal scores, but neither strategy verifies the query's executed retrieval consequence. We propose Information-Gain-Gated Self-Distillation (IGSD), which verifies on-policy token proposals with environment feedback before distilling them. Treating each query token as a micro-action, IGSD completes the teacher's token proposal and the student's sampled token into matched queries and executes both from the same failed state with the same retriever. Shared counterfactual controls account for query-conditioned shifts in answer likelihood, so their difference, the executed paired information gain, provides a relative utility contrast for the retrieved documents. IGSD uses this contrast as a positive-only soft weight for candidate-pair distillation, while leaving the GRPO objective unchanged and confining verification to training. Across seven single-hop and multi-hop QA benchmarks, IGSD reaches macro-average exact-match accuracies of 42.8% and 47.0% with 3B and 7B policies, respectively, without inference-time verification. These results support environment-verified hindsight as an effective approach to reliable action-level supervision for search agents.

## Metadata
- **Published**: 2026-09-26T14:57:17Z
- **Authors**: Angqing Jiang, Gaoming Zhang, Chaoqun Zhang, Jianchun Song, Liyuan Kong, Kena Qi, Wei Lin, Defu Lian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32694v1)