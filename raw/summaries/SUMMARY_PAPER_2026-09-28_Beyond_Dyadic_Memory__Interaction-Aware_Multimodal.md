---
title: Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations
url: http://arxiv.org/abs/2609.32522v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_12-04-49Z_BeyondDyadicMemory_Interaction_AwareMultimodalMemo.md
generated_at: 2026-09-28 20:39
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces VoxPolyMem, a novel interaction-aware multimodal memory framework designed to address the challenges of long-term memory in multi-party spoken conversations, a domain previously underexplored compared to dyadic text or image-text interactions. By integrating incremental speaker identification with a hierarchical memory structure and formulating retrieval as sequential decision-making via an agentic approach, VoxPolyMem significantly outperforms existing baselines on comprehensive benchmarks like VoxPolyBench, Mem-Gallery, and H2HMem-Multi.

## Key Takeaways
- VoxPolyMem combines incremental speaker identification with a multi-layered memory hierarchy consisting of interaction memory, fact memory, and participant profiles to effectively preserve conversational content, track participants across sessions, and maintain who speaks to whom in complex multi-party settings.
- The retrieval process is modeled as sequential decision-making where an agentic system rewrites queries and dynamically selects tools and memory layers based on accumulated evidence; this is optimized using Evidence-Gain GRPO, a novel training method employing round-wise credit assignment to encourage the acquisition of complementary evidence.
- The authors introduce VoxPolyBench to evaluate memory evolution and reasoning capabilities, demonstrating that VoxPolyMem achieves an overall score of 85.0 on this benchmark (surpassing the strongest baseline by 23.6 points) and exceeds public baselines by over 8 points on Mem-Gallery and H2HMem-Multi, highlighting superior performance in personalized assistance and interaction reasoning.

## Context
Current long-term memory research for AI agents has predominantly focused on dyadic interactions involving text or image-text modalities, leaving the complexities of multi-party spoken dialogues largely unaddressed despite their prevalence in real-world scenarios such as meetings and social gatherings. This gap limits the ability of agents to maintain persistent, personalized assistance in environments where tracking multiple speakers, understanding interaction dynamics, and reasoning over multimodal audio data are essential for coherent

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32522v1)
