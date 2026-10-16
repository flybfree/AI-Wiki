---
title: Same Context, Different Agents: A Behavioral Study of Semantic Layers, Orchestration and Compaction in Data Agents
published: 2026-10-14T21:29:59Z
authors: Zhivar Sourati, Marianne Menglin Liu, Zheng Wang, Rongguang Wang, Sai Ashish Somayajula, Tao Sheng, Kyu J. Han, Sujith Ravi, Dan Roth
url: http://arxiv.org/abs/2610.20959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Context, Different Agents: A Behavioral Study of Semantic Layers, Orchestration and Compaction in Data Agents

## Abstract
Answering questions over heterogeneous data means combining evidence from files, databases, documents and the web. Data agents automate this, but their success depends on context. Three context-engineering techniques (CETs) help by shaping it: semantic layers describe the data, orchestration splits work among agents, and compaction condenses interaction history. Existing studies validate each CET alone, leaving open how agent behavior shapes its effect. We present a comprehensive analysis of the three CETs, alone and combined, with seven large language models (LLMs) on 1,514 long-horizon tasks from five benchmarks, covering behavior, accuracy and cost. We find that data agents without CETs form three behavior groups: investigators, premature answerers that answer without inspecting data, and early stoppers that give up. Each CET delivers its known benefit, from more investigation to smaller prompts, but only the behavior group it matches turns that benefit into accuracy, such as premature answerers under orchestration. For investigators, the same CETs can hurt: the semantic layer stops them from looking, orchestration makes them overconfident, costing 5 percentage points, and compaction makes them repeat steps. Combining CETs yields smaller gains and losses than their sum. We derive guidance for choosing CETs by agent behavior, task demands and accuracy-cost trade-offs.

## Metadata
- **Published**: 2026-10-14T21:29:59Z
- **Authors**: Zhivar Sourati, Marianne Menglin Liu, Zheng Wang, Rongguang Wang, Sai Ashish Somayajula, Tao Sheng, Kyu J. Han, Sujith Ravi, Dan Roth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20959v1)