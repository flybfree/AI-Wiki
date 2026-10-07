---
title: WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration
published: 2026-10-06T07:01:38Z
authors: Qi Cheng, Shengyu Chen, Wei Cheng, Zhengzhang Chen, Xiaowei Jia, Haoyu Wang, Haifeng Chen
url: http://arxiv.org/abs/2610.07860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration

## Abstract
Multi-agent systems are increasingly deployed for complex knowledge work, yet their orchestration layers remain largely memoryless: each new task is decomposed, assigned, and executed from scratch with no benefit from prior successful executions. We present WorkflowOps, a multi-agent workflow orchestration framework that learns agent collaboration priors from historical workflows and expands its agent pool on demand to cover new capability requirements. Our approach introduces three coupled mechanisms. First, a transition probability matrix captures pairwise agent collaboration frequencies from past workflows and applies them as soft guidance during DAG workflow construction through intra-layer ordering optimization, probability-thresholded edge suggestion, and transitive reduction for parallelism maximization. Second, a sufficiency-driven agent creation loop detects capability gaps via semantic matching scores, generates specialized agents through an LLM, and simultaneously injects them into the collaboration matrix, so that newly created agents are immediately usable with predicted collaboration priors. Third, a layered semantic matching strategy uses pre-trained sentence embeddings for fast, deterministic capability matching as a first pass, invoking LLM verification only for low-confidence cases, thereby reducing LLM routing calls by over 80\% compared to pure-LLM approaches. Experiments on mixed code, math, and question-answering suites show that WorkflowOps improves end-to-end pass rates over recent workflow-construction baselines, with the largest gains on structured, decomposable tasks where past agent handoff patterns transfer.

## Metadata
- **Published**: 2026-10-06T07:01:38Z
- **Authors**: Qi Cheng, Shengyu Chen, Wei Cheng, Zhengzhang Chen, Xiaowei Jia, Haoyu Wang, Haifeng Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07860v1)