# Summary: 2026-08-07_17-22-29Z_PsychoAgent_AnAffect_SensitiveCognitiveArchitectur.md
Saved: 2026-08-09 23:17
Source: 2026-08-07_17-22-29Z_PsychoAgent_AnAffect_SensitiveCognitiveArchitectur.md
Model: None

---

## Summary  
This paper introduces PsychoAgent, a cognitive architecture that treats factual and affective memories separately while integrating them through a conflict‑aware executive controller for large language model (LLM) agents. By re‑ranking affective traces by salience after an initial semantic relevance filter, the system preserves topical fit but allows emotionally important information to surface in prompts. The authors demonstrate that this architecture outperforms conventional retrieval‑augmented generation baselines on conflict‑critical tasks and is evaluated through human judgments and a three‑day trace experiment. The work shows that affect‑sensitive retrieval can be made an inspectable component of LLM behavior, offering a pathway to model genuine human‑like conflict effects.

## Key Contributions  
- [Finding 1] PsychoAgent separates factual and affective memory streams and uses a conflict‑aware executive controller to merge them.  
- [Finding 2] Affective memories are filtered for semantic relevance first, then re‑ranked by salience to balance topical fit with emotional importance.  
- [Finding 3] The full architecture achieves higher recall of conflict‑critical memories (0.933) than baseline RAG methods (0.500 and 0.667), incurring only a small semantic‑similarity cost.

## Methodology  
The authors designed PsychoAgent as an LLM agent that maintains two memory banks: one for factual data and another for affective traces. An executive controller first checks semantic relevance, then applies a salience re‑ranking to prioritize emotionally salient items. This hybrid retrieval process is embedded within the model’s prompting pipeline. The system was tested across three controlled conflict scenarios where agents must retrieve information that is both relevant and emotionally charged. Human evaluation involved five raters reviewing 27 generated outputs, and a longitudinal trace over three days recorded persistent affect, offline memory recombination, and selective re‑weighting.

## Results  
The full PsychoAgent architecture outperformed semantic‑affective and single‑memory RAG baselines in recall of conflict‑critical memories (0.933 vs. 0.500 and 0.667). Human raters gave the highest mean rating (+0.22 SD) to PsychoAgent outputs after within‑rater standardization, though pairwise differences were not statistically significant. The three‑day trace revealed that affective information remained accessible offline, was recombined with factual data, and could be selectively re‑weighted based on salience, confirming the architecture’s dynamic behavior.

## Significance  
This research demonstrates that integrating affect into LLM memory can improve performance on tasks where emotional relevance matters. By making this mechanism inspectable—through explicit conflict‑aware retrieval—the authors provide a concrete framework for studying and replicating human‑like conflict effects in artificial agents, potentially guiding more empathetic AI interactions.

## Related Concepts  
- Affective memory  
- Cognitive architecture  
- Retrieval‑augmented generation (RAG)  
- Conflict‑aware executive controller  
- Salience re‑ranking  
- Semantic similarity cost
