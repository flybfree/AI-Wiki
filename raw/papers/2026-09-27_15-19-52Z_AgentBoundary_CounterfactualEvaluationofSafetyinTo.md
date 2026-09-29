---
title: AgentBoundary: Counterfactual Evaluation of Safety in Tool-Using LLM Agents
published: 2026-09-27T15:19:52Z
authors: Tianzhuo Yang, Zirui Mi, Yantao Huang, Guoxi Zhang, Jiawei Chen, Yaodong Yang, Jingwei Yi
url: http://arxiv.org/abs/2609.33658v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentBoundary: Counterfactual Evaluation of Safety in Tool-Using LLM Agents

## Abstract
Safety alignment for large language models (LLMs) in conversational settings is largely framed around whether to answer or refuse a request. In agentic settings, however, the same models must decide whether to act as permission-critical evidence emerges during execution. This creates a distinct challenge: apparent risk, action permissibility, and task competence are easily confounded, making agentic over-refusal difficult to distinguish from ordinary task failure. To address this, we introduce AgentBound, the first four-way counterfactual generation-and-evaluation framework for tool-using agent safety. AgentBound transforms the same executable workflow by independently varying apparent risk and action permissibility, enabling controlled comparisons of risky-looking but authorized tasks and routine-looking but unauthorized tasks. These comparisons jointly diagnose over-refusal and unsafe compliance while controlling for task competence. We instantiate AgentBound as a human-validated 4,000-task evaluation suite with trajectory-based and post-state-based judgments. Across 17 model and harness configurations, high safety frequently coexists with poor authorized-task completion: GPT-5.5 blocks 99.5\% of routine-looking unauthorized actions yet completes only 28.7\% of risky-looking authorized tasks. We further train a lightweight runtime calibration module that improves authorized-task completion by 18.2\% on average across 10 evaluated configurations, while improving unsafe-action blocking by 5.4\% on average. These show that effective agentic alignment requires action decisions to track permission-relevant execution evidence, rather than refusal strength alone.

## Metadata
- **Published**: 2026-09-27T15:19:52Z
- **Authors**: Tianzhuo Yang, Zirui Mi, Yantao Huang, Guoxi Zhang, Jiawei Chen, Yaodong Yang, Jingwei Yi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33658v1)