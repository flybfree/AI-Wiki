---
title: MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents
published: 2026-07-27T07:37:43Z
authors: Yiwen Ma, Songjun Tu, Qichao Zhang, Dong Li, Linjing Li, Dongbin Zhao
url: http://arxiv.org/abs/2607.24097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents

## Abstract
Memory-augmented LLM agents typically answer queries by retrieving relevant memories and feeding them directly to an answer model. This retrieval-as-evidence paradigm assumes retrieved memories are already suitable for reasoning, leaving the answer model to resolve redundancy, conflicts, and weak relevance while incurring substantial context overhead in long-term memory tasks. We propose MemChain, a trainable post-retrieval memory policy that transforms retrieved candidates into answer-facing active memory, represented as a compact and grounded evidence context. Given a user query and retrieved candidates, MemChain first generates a question-conditioned evidence plan, then constructs an ordered grounded evidence trace that organizes retrieved memories according to their semantic roles and dependencies, and finally executes explicit memory actions to produce a concise evidence context for answer generation. To train the mediator, we introduce a two-stage learning framework. Supervised trace learning first teaches the policy to generate structurally valid plans, traces, actions, and evidence contexts. We then propose Trace-Guided Memory Policy Optimization (TMPO), a reinforcement learning objective that optimizes the memory policy using downstream answer quality while jointly encouraging trace grounding, evidence support, structural validity, and answer stability across multiple rollouts. Experiments on LoCoMo and LongMemEval-S demonstrate that MemChain consistently achieves state-of-the-art performance across both closed-source and open-weight frozen answer models while substantially reducing the memory context passed to the answer model.

## Metadata
- **Published**: 2026-07-27T07:37:43Z
- **Authors**: Yiwen Ma, Songjun Tu, Qichao Zhang, Dong Li, Linjing Li, Dongbin Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24097v1)