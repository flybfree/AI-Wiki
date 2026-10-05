---
title: APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory
url: http://arxiv.org/abs/2610.02472v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_20-51-45Z_APDMem_Agent_ControlledProgressiveDisclosureforQue.md
generated_at: 2026-10-04 21:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
APDMem introduces a hierarchical long-term memory architecture for personalized LLM assistants that applies progressive disclosure to memory retrieval, enabling agents to adaptively drill from high-level thematic summaries down to raw conversation messages only when query complexity demands it. The system achieves strong performance on the LongMemEval benchmark for long-context memory reasoning while accessing only 8% of total conversation history, demonstrating a significant cost-fidelity trade-off that avoids the inefficiency of flat retrieval or fixed-granularity approaches.

## Key Takeaways
- APDMem structures conversation history into four progressively detailed layers—thematic summaries, personalized key facts, turn-level evidence notes, and raw messages—allowing a controller agent to perform progressive disclosure at inference time, reading coarse summaries first and drilling into finer evidence only when necessary. This adaptive mechanism means simple queries terminate early at the summary layer, while complex temporal, multi-hop, or exact-evidence queries trigger deeper inspection of the hierarchy, creating a dynamic cost-fidelity trade-off tailored to each query's difficulty.
- A note synthesizer component converts retrieved evidence into a query-focused structure that consolidates facts, orders events chronologically, and flags contradictions before final answer generation, ensuring that the agent produces coherent and factually consistent responses even when evidence is drawn from sparse, distributed conversation history.
- Experimental evaluation on LongMemEval demonstrates that APDMem achieves strong performance for long-context memory reasoning while accessing only 8% of the total conversations, indicating that the hierarchical progressive disclosure strategy drastically reduces retrieval overhead without sacrificing answer quality, a critical efficiency gain for production systems handling extended user histories.

## Context
Personalized LLM assistants increasingly need to recall sparse, temporally distributed evidence from very long conversation histories, yet existing approaches typically rely on flat memory stores or fixed retrieval granularity that either waste tokens on trivial queries or miss critical details for complex ones. APDMem addresses this gap by borrowing the progressive disclosure pattern from software engineering and applying it to memory retrieval, positioning hierarchical memory as a first-class architectural concern rather than a post-hoc optimization. This work sits at the intersection of long-context reasoning, agent orchestration, and retrieval-augmented generation, contributing a principled framework for adaptive memory access that scales with query complexity.

## Implications
For practitioners building conversational AI products, APDMem offers a blueprint for reducing inference costs and token consumption in long-history assistants without degrading answer quality, which is directly relevant to production deployments where latency and compute budgets are constrained. For the broader research community, the hierarchical progressive disclosure paradigm suggests that memory architectures should be query-adaptive rather than static, potentially influencing future designs for agent memory systems, retrieval pipelines, and multi-turn dialogue evaluation benchmarks. Industry teams can adopt the four-layer structure and controller-agent pattern to build assistants that gracefully handle both simple recall and complex temporal reasoning while maintaining operational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02472v1)
