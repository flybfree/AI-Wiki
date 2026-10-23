---
title: Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought
url: http://arxiv.org/abs/2610.30755v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_05-23-16Z_IsComplexAgenticMemoryAlwaysNeeded_NaiveRAGIsStron.md
generated_at: 2026-10-22 21:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the prevailing assumption that complex agentic memory systems—featuring mutation, structural organization, and learned retrieval strategies—are necessary for long-term conversation understanding in LLMs. The authors introduce Raw-RAG, a naive RAG baseline that performs dense retrieval and reranking directly over raw conversation history, and demonstrate that it outperforms sophisticated agentic memory systems across multiple benchmarks, ranking first in six of seven benchmark-model settings. The findings suggest that preserving raw information and maximizing evidence coverage may be more effective than the elaborate transformations and organizational structures employed by complex memory architectures.

## Key Takeaways
- Raw-RAG, a straightforward dense retrieval and reranking pipeline over unprocessed conversation history, outperforms the strongest compared agentic memory system by 0.13 to 5.53 points across benchmarks including LoCoMo, LongMemEval, MEME, and MemoryAgentBench, ranking first in six of seven benchmark-model configurations. This suggests that the added complexity of agentic memory operations such as mutation, structural reorganization, and learned retrieval strategies does not consistently translate into performance gains for conversational memory tasks.
- The authors identify a critical mechanism explaining why raw retrieval remains competitive: Raw-RAG achieves higher coverage of necessary evidence, which compensates for its lower utilization efficiency. Crucially, the paper demonstrates that useful evidence is not limited to direct answer values but also includes the relational structures and dependency paths required to derive those answers, meaning that transformations applied to memory stores can inadvertently strip away the connective tissue needed for multi-hop reasoning.
- Even when a system is granted complete access to transformed memory stores, an accuracy gap persists relative to retrieval from raw evidence. This finding underscores that information loss during memory transformation is a fundamental bottleneck, and that the act of restructuring or summarizing conversation history can degrade the very information a downstream reader LLM needs to produce correct answers.

## Context
The field of LLM memory has rapidly evolved toward increasingly sophisticated architectures, with agentic memory systems incorporating learned retrieval policies, hierarchical organization, and iterative mutation of stored information. These designs are motivated by the intuition that raw conversation history is noisy, redundant, and difficult to search effectively. This paper directly interrogates that assumption by establishing a rigorous naive baseline and showing it is not merely competitive but often superior, which calls into question whether the research community has been optimizing for architectural complexity rather than evidence fidelity.

## Implications
For practitioners building conversational AI assistants, customer support bots, or long-context agents, this work suggests that a well-tuned dense retrieval and reranking pipeline over raw history may deliver better performance than more complex memory systems at significantly lower engineering and computational cost. For the research community, the paper establishes naive RAG as an essential baseline that any proposed agentic memory system must surpass, raising the bar for future work and redirecting attention toward preserving raw evidence and maximizing coverage rather than inventing ever more elaborate memory transformations. Industry teams should treat Raw-RAG as a mandatory comparison point before investing in custom memory architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30755v1)
