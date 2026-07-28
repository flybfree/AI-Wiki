# Summary: 2026-07-26_07-45-01Z_DelegationIntelligenceinDeepSearch_AControllableFr.md
Saved: 2026-07-27 23:53
Source: 2026-07-26_07-45-01Z_DelegationIntelligenceinDeepSearch_AControllableFr.md
Model: None

---

## Summary  
Deep search is a critical capability for modern agents, yet current evaluation methods treat the entire process as a single end‑to‑end accuracy metric, which obscures how well a model knows when to initiate searches and how to synthesize evidence. The authors introduce **Delegation Intelligence**, a meta‑capability that separates deep‑search competence into two complementary dimensions: Search Decision‑Making (recognizing information insufficiency and deciding whether, when, and how to search) and Information Synthesis & Verification (aggregating, judging, and synthesising noisy or adversarial evidence). To make this capability measurable, they create a controllable synthesis pipeline based on document‑grounded reverse engineering that can generate diverse evaluation scenarios. Their work culminates in **DelegSearchBench**, a benchmark equipped with a protocol that isolates each dimension by varying document composition and tool access.

## Key Contributions  
- [Finding 1] Formalization of Delegation Intelligence into two distinct dimensions (search decision‑making vs. evidence synthesis/verification).  
- [Finding 2] Development of a controllable synthesis pipeline using document‑grounded reverse engineering to produce varied evaluation datasets.  
- [Finding 3] Construction of DelegSearchBench with a disentangled evaluation protocol that isolates each capability dimension.

## Methodology  
The authors approached the problem by first formalizing the meta‑capability and decomposing it into its two sub‑dimensions, which provides a clear theoretical basis for measurement. They then designed a pipeline where researchers can supply documents and specify tool access, allowing the system to generate synthetic deep‑search tasks that vary in composition (e.g., mixture of factual vs. ambiguous statements) and tool availability (e.g., limited or full set). This controllable design enables each dimension to be evaluated independently: by fixing document composition while changing tool access, they isolate search decision‑making; by varying the source reliability of evidence while keeping tools constant, they probe synthesis/verification. The benchmark aggregates these controlled tasks into a single evaluation suite.

## Results  
Across representative models (e.g., GPT‑4, Claude 3), final‑answer accuracy alone cannot reliably indicate Delegation Intelligence. Experiments show that search decision‑making varies widely: some models consistently decide to skip searches when information is sufficient, while others over‑search or under‑search based on document ambiguity. Conversely, evidence synthesis/verification differs markedly; models with strong retrieval skills still produce low‑quality syntheses if source reliability is poor. Quantitative metrics (e.g., decision latency, verification confidence scores) reveal that the two dimensions are largely independent, confirming the disentanglement. The benchmark demonstrates reproducibility: replicating a task with different document sets yields consistent performance across dimensions.

## Significance  
This work matters because it moves beyond black‑box end‑to‑end accuracy to provide a transparent, modular evaluation framework for deep search. Researchers can now diagnose whether a model’s weakness lies in recognizing information gaps or in handling noisy evidence, informing better design of agents that delegate tasks appropriately. The controllable pipeline and benchmark lower the barrier to research reproducibility and enable systematic comparison across models.

## Related Concepts  
- Deep Search  
- End‑to‑end Accuracy  
- Retrieval Quality  
- Long‑Context Comprehension  
- Evidence Verification  
- Tool‑Use Decisions  
- Meta‑Capability  
- Decomposition of Capabilities  
- Controllable Evaluation  
- Benchmarking
