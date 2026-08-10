# Summary: 2026-08-07_17-22-29Z_PsychoAgent_AnAffect_SensitiveCognitiveArchitectur.md
Saved: 2026-08-09 23:12
Source: 2026-08-07_17-22-29Z_PsychoAgent_AnAffect_SensitiveCognitiveArchitectur.md
Model: None

---

## Summary  
PsychoAgent proposes a cognitive architecture that treats factual and affective memory as distinct yet interoperable subsystems within large language model agents, guided by an executive controller that resolves conflicts between them. The system demonstrates that emotional significance can bias retrieval even when topics are semantically similar, thereby mimicking human‑like conflict effects. Experiments across three controlled scenarios show the full architecture outperforms baseline RAG methods in retrieving conflict‑critical memories while incurring only a modest loss of topical relevance. Human raters also rated outputs higher on average, confirming that affect‑sensitive retrieval improves perceived quality without sacrificing factual accuracy.

## Key Contributions  
- [Finding 1] PsychoAgent separates affective and factual memory streams, allowing the executive controller to prioritize emotionally salient traces over purely semantic ones.  
- [Finding 2] The conflict‑aware re‑ranking mechanism preserves topical fit while elevating affectively important memories, yielding a higher recall of critical information (0.933 vs. 0.500 and 0.667).  
- [Finding 3] Human evaluation confirms that the architecture produces outputs with superior overall quality (+0.22 SD) and more consistent affect‑driven responses across raters.

## Methodology  
The authors designed PsychoAgent as a modular cognitive system: (1) a factual memory store retrieves information based on semantic similarity; (2) an affective memory store holds emotionally weighted traces; (3) the executive controller evaluates both stores, applying a salience filter that re‑ranks results according to conflict resolution criteria. In each experiment, the full architecture is compared against two baselines: one that only uses factual retrieval and another that combines semantic relevance with a simple affect weighting.

## Results  
Across three controlled conflict scenarios, the full PsychoAgent retrieved 0.933 of conflict‑critical memories, whereas the semantic‑affective baseline achieved 0.500 and the single‑memory RAG baseline 0.667. A three‑day trace analysis revealed persistent affect in offline memory recombination and selective reweighting by the executive controller. Five blinded raters evaluated 27 outputs; after within‑rater standardization, the full architecture had the highest mean rating (+0.22 SD). Pairwise differences were not statistically significant.

## Significance  
By integrating affective significance into retrieval, PsychoAgent provides a principled framework for modeling human‑like conflict effects in LLM agents, offering an inspectable mechanism that can be evaluated both quantitatively and qualitatively. This work advances the field of affect‑aware AI by demonstrating measurable benefits over standard RAG approaches while maintaining factual integrity.

## Related Concepts  
- Affective memory / emotional salience  
- Conflict resolution in cognitive architectures  
- Retrieval‑augmented generation (RAG) baselines  
- Executive controller mechanisms  
- Human‑like cognition modeling
