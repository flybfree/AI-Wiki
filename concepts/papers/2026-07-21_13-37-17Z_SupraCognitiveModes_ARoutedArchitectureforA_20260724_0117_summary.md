# Summary: 2026-07-21_13-37-17Z_SupraCognitiveModes_ARoutedArchitectureforAgentMem.md
Saved: 2026-07-24 01:17
Source: 2026-07-21_13-37-17Z_SupraCognitiveModes_ARoutedArchitectureforAgentMem.md
Model: None

---

## Summary  
The paper introduces Supra Cognitive Modes (SCM), a routed architecture that separates distinct memory‑processing modes—factual lookup, relation‑chain reasoning, and long‑form synthesis—from a single shared ingest substrate. By using a frozen semantic classifier and runtime gates to dispatch queries among fused lexical/dense lookups, graph traversals, or iterative multi‑hop handling, SCM enables agents to perform “supra‑cognitive” operations that combine short‑term recall with long‑term synthesis. Experiments on three benchmarks demonstrate measurable gains in factual accuracy and abstention performance relative to a baseline configuration.

## Key Contributions  
- [Finding 1] Supra Cognitive Modes maps explicit or automatically selected per‑query modes to retrieval and synthesis payloads over one shared ingest substrate, creating a modular routing interface.  
- [Finding 2] The architecture achieves 84.87 % factual accuracy on LoCoMo factoid categories, 68.61 % adversarial abstention, 61.49 % overall on MemoryAgentBench (averaged over two repetitions), and 86.00 % on LongMemEval, surpassing the reference run’s scores.  
- [Finding 3] The design supports causal routing effects, efficiency gains, and a repository‑backed reproduction that enables task‑ and mode‑conditioned failure analysis.

## Methodology  
The authors approached the problem by treating memory as a substrate composed of multi‑granularity embeddings, extracted triples, fact‑version metadata, and optional asynchronous enrichments. A frozen semantic classifier evaluates each query’s mode, while runtime gates route it to one of several processing pipelines: fused lexical/dense lookup for short facts, graph or iterative multi‑hop handling for relational reasoning, and stratified long‑form synthesis for holistic responses. All components share the same ingest substrate, allowing efficient reuse of pre‑computed representations.

## Results  
Experimental results show that SCM’s routed configuration outperforms a baseline in all three benchmarks: LoCoMo factoid tasks reach 84.87 % accuracy and adversarial abstention reaches 68.61 %; MemoryAgentBench yields an average of 61.49 % across two repetitions; LongMemEval attains 86.00 %. The authors note that raw baseline outputs, exact timing data, and complete token ledgers are not publicly available, but stored rows retain the necessary runtime decisions for analysis.

## Significance  
This work matters because it formalizes a routable architecture for agent memory that can dynamically adapt to different cognitive modes, improving both performance and interpretability. By isolating retrieval, relational reasoning, and synthesis into separate pipelines while sharing underlying data, SCM offers a scalable solution for long‑term conversational agents that must balance factual precision with holistic understanding.

## Related Concepts  
Supra Cognitive Modes, routed architecture, shared ingest substrate, frozen semantic classifier, runtime gates, fused lexical/dense lookup, graph traversal, iterative multi‑hop handling, stratified synthesis, multi‑granularity embeddings, extracted triples, fact‑version metadata, causal routing, long‑term conversational memory.
