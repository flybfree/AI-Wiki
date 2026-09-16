---
title: Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act
published: 2026-09-14T19:31:04Z
authors: Yiwei Yang, Haoxiang Zhang, Bingbing Wen, Yao Lu, Yuchen Wu, Lei Zhang, Julian McAuley, Pan Lu, Bill Howe
url: http://arxiv.org/abs/2609.16268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act

## Abstract
Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic environments combining factual question answering and mathematical reasoning tasks, and inject cues that are strongly correlated with specific tools during training but causally irrelevant to tool necessity. Across counterfactual evaluations where cues are present but the associated tools are not required, agents exhibit substantial shortcut behavior, with spurious tool invocation rates increasing by up to 39 percent. However, shortcut formation is not universal: across the conditions we test, it arises only when the agent has already learned to use the target tool reliably, suggesting that task competence, rather than dataset imbalance alone, is a key factor in shortcut learning. A swapped-cue analysis further shows that semantic alignment between cues and tools substantially amplifies this effect. To mitigate these failures, we introduce a dense, decision-level reward in which an LLM judge evaluates the necessity of each tool call. This tool-necessity reward effectively suppresses cue-driven tool use while preserving task performance, providing a practical approach to improving the robustness of LLM agent tool-use policies.

## Metadata
- **Published**: 2026-09-14T19:31:04Z
- **Authors**: Yiwei Yang, Haoxiang Zhang, Bingbing Wen, Yao Lu, Yuchen Wu, Lei Zhang, Julian McAuley, Pan Lu, Bill Howe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16268v1)