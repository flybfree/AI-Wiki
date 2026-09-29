---
title: Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations
published: 2026-09-26T12:04:49Z
authors: Wenxu Jia, Xize Cheng, Zihan Zhang, Dongjie Fu, Linjun Li, Wenshi Chen, Yangyang Wu, Tao Jin
url: http://arxiv.org/abs/2609.32522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations

## Abstract
Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving long-term memory for multi-party spoken conversations underexplored. This setting requires preserving conversational content, identifying participants across sessions, and retaining who speaks to whom. To this end, we propose VoxPolyMem, an interaction-aware multimodal memory framework combining incremental speaker identification with a memory hierarchy comprising interaction memory, fact memory, and participant profiles. We formulate retrieval as sequential decision-making, where an agent rewrites queries and selects retrieval tools and memory layers based on accumulated evidence to address information gaps. We further introduce Evidence-Gain GRPO (EG-GRPO), which uses round-wise credit assignment to encourage complementary evidence acquisition. We also construct VoxPolyBench to evaluate memory evolution, personalized answering, memory retrieval and reasoning, and interaction reasoning and attribution in multi-party spoken conversations. VoxPolyMem achieves an overall score of 85.0 on VoxPolyBench, surpassing the strongest evaluated baseline by 23.6 points. On Mem-Gallery and H2HMem-Multi, it scores 89.6 and 74.4, respectively, exceeding the strongest evaluated public memory baselines by over 8 points each. These results highlight its potential for persistent, personalized assistance in multi-party multimodal interactions. Code and datasets are available at https://voxpolymem.github.io/VoxPolyBench/demo/

## Metadata
- **Published**: 2026-09-26T12:04:49Z
- **Authors**: Wenxu Jia, Xize Cheng, Zihan Zhang, Dongjie Fu, Linjun Li, Wenshi Chen, Yangyang Wu, Tao Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32522v1)