---
title: StateComp: Learning When to Compress History in Long Horizon Agents
published: 2026-09-23T03:34:08Z
authors: Mingxuan Wang, Hongyue Chen, Yinglong Guo, Fei Luo, Chao Ning, Bo Wang, Guorun Yao, Yanbiao Ma, Jungong Han
url: http://arxiv.org/abs/2609.27298v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StateComp: Learning When to Compress History in Long Horizon Agents

## Abstract
Long-horizon agents continuously accumulate interaction history during task execution, yet the importance of past interactions changes as the agent state evolves. Existing context management methods largely compress history based on fixed windows, periodic schedules, or current relevance, overlooking a more fundamental question: when has a past interaction become safe to replace? Premature compression may remove information still needed for future actions, while overly conservative retention leads to substantial context overhead. To address this, we propose State Conditioned Compression (StateComp), a framework that determines when historical interactions can be safely compressed according to the current agent state. StateComp constructs KEEP and READY supervision through a two-stage annotation procedure and trains an imbalance-aware router on hidden representations from a frozen language model. A bounded state representation further reduces the cost of evaluating long histories, while adjacent READY interactions are grouped into continuous spans and replaced with compact summaries during execution. Experiments on WorkBuddyBench show that StateComp reduces total agent and summarization tokens by 52.27% while maintaining task performance, and achieves a 12.67-fold speedup in representation extraction.

## Metadata
- **Published**: 2026-09-23T03:34:08Z
- **Authors**: Mingxuan Wang, Hongyue Chen, Yinglong Guo, Fei Luo, Chao Ning, Bo Wang, Guorun Yao, Yanbiao Ma, Jungong Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27298v1)