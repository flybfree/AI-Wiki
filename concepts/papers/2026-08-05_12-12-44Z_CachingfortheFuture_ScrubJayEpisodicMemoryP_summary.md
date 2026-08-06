# Summary: 2026-08-05_12-12-44Z_CachingfortheFuture_ScrubJayEpisodicMemoryPrincipl.md
Saved: 2026-08-05 20:34
Source: 2026-08-05_12-12-44Z_CachingfortheFuture_ScrubJayEpisodicMemoryPrincipl.md
Model: None

---

## Summary  
The paper introduces **ScrubJay‑MEM**, an agent memory system that emulates the perishable, type‑specific episodic memory of western scrub jays to combat outdated contamination in long‑running LLM agents. It operationalizes a per‑memory coefficient πᵢ and utility horizon τᵢ, allowing each stored fact to decay according to its content type while remaining retrievable for a limited time. The authors evaluate this approach on two benchmarks: the Temporal Generalization Test (TGT) with GenGap metrics and MemoryAgentBench EventQA‑64k, where ScrubJay‑MEM achieves sizable improvements over prior models. A decay ablation experiment demonstrates that type‑conditioned decay is essential for these gains.

## Key Contributions  
- [Finding 1] Type‑conditioned temporal decay can be modeled as a per‑memory coefficient πᵢ in an external LLM memory store, enabling automatic classification of memory longevity.  
- [Finding 2] ScrubJay‑MEM yields a positive GenGap (+0.108) on TGT and improves F1 by +2.66 (vs Mem0) and +3.09 (vs Qwen3‑Embedding‑4B) on EventQA‑64k, outperforming baseline retrieval systems.  
- [Finding 3] Removing the decay mechanism collapses the GenGap by a factor of ~5.7, proving that perishable‑fact modeling is necessary for the observed benefits.

## Methodology  
The authors represent each memory as a jointly‑bound **What–Where–When** tuple together with an estimated perishability πᵢ and utility horizon τᵢ. Retrieval is performed via query‑adaptive scoring that selects memories whose decay has not yet expired, while updates are applied retroactively in O(1) LLM calls. The system is benchmarked against existing memory agents (Mem0, Qwen3‑Embedding‑4B) using the TGT and EventQA‑64k datasets.

## Results  
On the Temporal Generalization Test, ScrubJay‑MEM is the only retrieval‑based system with a substantially positive GenGap (+0.108). On MemoryAgentBench EventQA‑64k, its F1 score exceeds Mem0 by 2.66 points and Qwen3‑Embedding‑4B by 3.09 points. The decay ablation study shows that without type‑conditioned decay the GenGap drops dramatically (≈5.7×), confirming the necessity of perishable‑fact modeling.

## Significance  
ScrubJay‑MEM provides a principled, biologically inspired architecture for agent memory that reduces outdated contamination and enables efficient O(1) updates. By aligning LLM memory with the temporal dynamics of episodic animal cognition, it offers a scalable solution for long‑running agents handling perishable facts without sacrificing performance.

## Related Concepts  
- Episodic memory (bird cognition)  
- Temporal decay / perishability coefficient πᵢ  
- Utility horizon τᵢ  
- What–Where–When tuple encoding  
- Query‑adaptive retrieval scoring  
- GenGap metric for temporal reasoning  
- Temporal Generalization Test (TGT) benchmark  
- External LLM memory store  
- Retrieval‑based system performance comparison
