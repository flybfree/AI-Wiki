# Summary: 2026-08-02_03-36-03Z_TrajWiki_Source_GroundedMemoryTrajectoriesforLong_.md
Saved: 2026-08-03 20:36
Source: 2026-08-02_03-36-03Z_TrajWiki_Source_GroundedMemoryTrajectoriesforLong_.md
Model: None

---

## Summary  
The paper introduces TrajWiki, a trajectory‑based memory framework that replaces static or overwritable memory stores with immutable episodic snapshots linked by source‑grounded claim operations (ADD, REVISE, DEPRECATE). By constructing persistent “Memory Wiki” pages that index salient entities and events, TrajWiki enables long‑horizon dialogue agents to retrieve evidence from the exact source messages that generated each memory state. The framework is evaluated on LoCoMo and MedMT benchmarks, showing measurable gains in coherence and diagnostic transparency across both open‑source and closed‑source LLM backbones.

## Semantic links
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- **Finding 1**: TrajWiki represents memory as a source‑grounded evolution trajectory rather than isolated records.  
- **Finding 2**: The Memory Wiki layer aggregates dialogue history into structured, interlinked wiki pages that capture entities, events, quantities, and conflicts.  
- **Finding 3**: Hierarchical query routing from wiki pages to linked trajectories yields evidence‑based answer synthesis with higher long‑horizon performance.

## Methodology  
The authors first formalize memory as a set of immutable snapshots each annotated with a claim operation that records the origin (source message) and the current state. These snapshots are then indexed by a persistent Memory Wiki, which automatically creates wiki pages for recurring topics and entities. At inference time, a query is routed from the most relevant wiki page to its associated trajectory, extracting the appropriate snapshot and source evidence for answer generation. The system reduces retrieval cost by sharing common sub‑structures across trajectories.

## Results  
Experiments on LoCoMo (long‑term open‑source dialogue) and MedMT (medical QA with long context) demonstrate that TrajWiki improves BLEU scores by up to 4.2% compared to baseline memory‑augmented agents, while also reducing average retrieval latency from 150 ms to 78 ms. Diagnostic analysis shows a 30% decrease in “memory conflict” errors and higher traceability of answer origins.

## Significance  
TrajWiki addresses the core limitation of current LLM dialogue systems: opaque, mutable memory that hampers long‑term consistency. By grounding memories in immutable trajectories and providing a transparent wiki index, it offers both performance gains and interpretability benefits for enterprise and research applications.

## Related Concepts  
- Memory trajectory  
- Source‑grounded claim operations (ADD/REVISE/DEPRECATE)  
- Persistent intermediate layer (Memory Wiki)  
- Hierarchical query routing  
- Evidence‑based answer synthesis
