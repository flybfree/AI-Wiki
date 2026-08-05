# Summary: 2026-07-31_18-05-36Z_Cross_BenchmarkGeneralizationinLong_HorizonAgents.md
Saved: 2026-08-04 00:02
Source: 2026-07-31_18-05-36Z_Cross_BenchmarkGeneralizationinLong_HorizonAgents.md
Model: None

---

## Summary  
The authors investigate whether reinforcement‑learning (RL) policies trained in one set of self‑contained tasks can generalize to other long‑horizon Model Context Protocol (MCP) environments without sharing explicit task knowledge. They demonstrate that the model’s behavior—how it forms goals, maintains a working state, and verifies completion—transfers across diverse office workflows and codebases, suggesting that cross‑benchmark generalization stems from behavioral skill rather than memorized schemas. By training an open‑weight mixture‑of‑experts (MoE) model on 363 MCP tasks across 27 categories using a two‑stage SFT‑then‑RL pipeline, they show measurable improvements on five external benchmarks despite the training set containing no software‑engineering examples. This work provides empirical evidence that long‑horizon agents can acquire transferable “ways of working” that persist beyond their original domain.

## Semantic links
- [[concepts/papers/2026-06-18_17-49-36Z_Execution_StateCapsules_Graph_BoundExecutio_summary.md|Summary: 2026-06-18_17-49-36Z_Execution_StateCapsules_Graph_BoundExecution_State.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.06
- [[concepts/papers/2026-07-21_15-57-36Z_ThePriceofReasoning_Cost_QualityTradeoffsin_summary.md|Summary: 2026-07-21_15-57-36Z_ThePriceofReasoning_Cost_QualityTradeoffsinReinfor.md]] — 3 title terms overlap; 1 backlink; 13 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Long‑horizon agents generalize across benchmarks primarily through behavioral changes rather than task‑specific knowledge.  
- [Finding 2] An open‑weight MoE model (Qwen3.5‑122B‑A10B) trained on MCP tasks improves external evaluations by up to +9.6 pp on Toolathlon, even though the training data contain no software‑engineering tasks.  
- [Finding 3] Four recurring behavioral patterns—careful local‑goal formation, building goal‑relevant working state, keeping parent goals stable through repairs, and verification of completion—appear across office workflows and code.

## Methodology  
The authors employ a two‑stage pipeline: first, supervised fine‑tuning (SFT) using a teacher model to align the MoE on MCP tasks; second, reinforcement learning (RL) with greedy pass@1 evaluation. The base family and SFT teacher were chosen based on Toolathlon performance, but no external benchmark task or grader entered training, nor did any external score influence hyperparameters, checkpoint selection, or stopping criteria. Evaluation was performed via greedy pass@1 across five external benchmarks: Toolathlon, τ²‑Bench, BFCL‑V4, SWE‑Bench Pro, and Terminal‑Bench 2.

## Results  
The trained model outperformed the base model on all five external evaluations: +9.6 pp on Toolathlon, +5.3 pp on τ²‑Bench, +3.5 pp on BFCL‑V4, +5.8 pp on SWE‑Bench Pro, and +2.8 pp on Terminal‑Bench 2. Notably, both software‑engineering benchmarks (SWE‑Bench Pro and Terminal‑Bench 2) improved despite the training collection lacking any such tasks.

## Significance  
These results reveal that post‑training can reshape an agent’s operational habits—such as goal formation and verification—that transfer to unrelated environments. This challenges the assumption that cross‑benchmark generalization is limited to memorized task schemas, suggesting a broader capability for long‑horizon agents to acquire reusable procedural skill.

## Related Concepts  
- Reinforcement learning (RL)  
- Mixture‑of‑experts (MoE) models  
- Model Context Protocol (MCP) tasks  
- Toolathlon benchmark  
- SWE‑Bench Pro and Terminal‑Bench 2  
- Long‑horizon agents  
- Transfer learning  
- Behavioral similarity across domains
