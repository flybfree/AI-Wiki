# Summary: 2026-07-21_13-37-17Z_SupraCognitiveModes_ARoutedArchitectureforAgentMem.md
Saved: 2026-07-24 00:54
Source: 2026-07-21_13-37-17Z_SupraCognitiveModes_ARoutedArchitectureforAgentMem.md
Model: None

---

## Summary  
This paper introduces Supra Cognitive Modes (SCM), a novel architecture designed to enhance agent memory performance by routing different types of cognitive workloads—such as direct factual lookup, multi-hop reasoning, and long-form synthesis—through a unified substrate using explicit or automatically selected per-query modes. The system leverages fused lexical and dense retrieval mechanisms alongside graph-based and iterative multi-hop handling to efficiently manage complex memory tasks that require both precision and breadth. By integrating multiple granularity embeddings, extracted triples, fact-version metadata, and optional asynchronous enrichments into a single ingest substrate, SCM enables flexible and efficient memory access tailored to individual query demands.

## Key Contributions  
- [Finding 1] The Supra Cognitive Modes (SCM) architecture introduces a dynamic routing mechanism that assigns per-query cognitive modes to distinct retrieval and synthesis payloads over a shared substrate, improving the efficiency of handling mixed-memory tasks.  
- [Finding 2] SCM achieves significantly higher performance on benchmark datasets compared to baseline systems, with scores exceeding 80% on Long-term Conversational Memory (LoCoMo) factoid categories and 86% on LongMemEval, indicating robust memory synthesis capabilities.  
- [Finding 3] The architecture supports task-conditioned routing and failure analysis through a repository-backed reproduction system that preserves end-to-end timing and token ledgers for diagnostic purposes.

## Methodology  
The authors approached the problem by designing SCM as a routed cognitive mode framework where each query is evaluated by a frozen semantic classifier to determine its optimal handling strategy. This classifier dispatches queries among four primary modes: fused lexical-dense lookup, graph-based multi-hop reasoning, iterative multi-hop synthesis, and stratified long-form synthesis. All these modes operate on a shared ingest substrate that combines multi-granularity embeddings (e.g., sentence-level and token-level), extracted relational triples, fact-version metadata, and optional asynchronous enrichments. The system ensures that retrieval and synthesis payloads are dynamically assembled based on the selected mode, minimizing redundant computation while maximizing recall and coherence.

## Results  
Experimental results were evaluated across three benchmarks: LoCoMo (n = 1,986), MemoryAgentBench (MAB; n = 3,671), and LongMemEval (n = 500). The reference run achieved 84.87% accuracy on LoCoMo factoid categories and 68.61% on adversarial abstention tasks, 61.49% across two repetitions on MAB, and 86.00% on LongMemEval. These scores demonstrate that SCM effectively balances precision in factual retrieval with the ability to synthesize coherent long-term narratives. However, raw baseline outputs, end-to-end timing data for LoCoMo and LongMemEval, and complete token ledgers are unavailable due to repository limitations; stored rows also omit some final runtime decisions.

## Significance  
SCM represents a significant advancement in agent memory systems by decoupling cognitive modes from rigid retrieval-synthesis pipelines. By enabling dynamic routing based on query complexity and task type, it improves both efficiency and accuracy in long-term memory tasks. The architecture’s modularity supports scalability across diverse applications such as conversational agents, knowledge graphs, and AI tutors that require nuanced memory handling.

## Related Concepts  
- Cognitive modes  
- Routing architectures  
- Multi-granularity embeddings  
- Fused retrieval systems  
- Graph-based reasoning  
- Long-form synthesis  
- Fact-version metadata  
- Asynchronous enrichments
