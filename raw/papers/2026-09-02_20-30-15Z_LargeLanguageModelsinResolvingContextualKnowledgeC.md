---
title: Large Language Models in Resolving Contextual Knowledge Conflicts
published: 2026-09-02T20:30:15Z
authors: Xinye Yang, Zhenyang Liu, Ruisi Li, Yuanyuan Lei
url: http://arxiv.org/abs/2609.03148v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large Language Models in Resolving Contextual Knowledge Conflicts

## Abstract
Most prior works focused on conflicts between an LLM's internal parametric knowledge and externally provided context. In contrast, we investigate how LLMs handle conflicts that arise within contextual knowledge itself. We introduce a taxonomy of six types of contextual conflicts (factual, inferential, temporal, granularity, perspective, and ambiguity) and contribute a comprehensive dataset ContextConflict for this setting. The dataset contains 5,781 samples, covers both reasoning and summarization tasks, and includes both explicit contradictions and implicit conflicts that require multi-step reasoning. Experiments on nine LLMs show that current models still fall short in resolving contextual knowledge conflicts. We further provide mechanistic interpretability insights into how LLMs process such conflicts, revealing their latent awareness of conflicts and the representational geometry underlying conflict processing. In addition, our analysis uncovers a consistent model bias towards earlier evidence, and this positional preference serves as a key obstacle to effective conflict resolution. Motivated by these findings, we further propose a simple training-free, label-free steering method that steers activations to encourage a more comprehensive incorporation of evidences for better conflict resolution. On our dataset, the method consistently improves accuracy on reasoning tasks and generates higher-quality, more balanced summaries for summarization tasks.

## Metadata
- **Published**: 2026-09-02T20:30:15Z
- **Authors**: Xinye Yang, Zhenyang Liu, Ruisi Li, Yuanyuan Lei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03148v1)