# Summary: 2026-08-02_16-22-27Z_EviSD_Evidence_ConditionedSelf_DistillationforSear.md
Saved: 2026-08-04 00:16
Source: 2026-08-02_16-22-27Z_EviSD_Evidence_ConditionedSelf_DistillationforSear.md
Model: None

---

## Summary  
Outcome‑based reinforcement learning enables search‑augmented language agents to learn from verifiable final answers, but its trajectory‑level credit cannot distinguish the contributions of individual actions in a multi‑turn search process. We propose EviSD, an evidence‑conditioned self‑distillation framework that treats instance‑level supporting evidence as privileged information for search actions and golden answers as complementary privilege for answer actions. The framework converts the detached teacher–student gap into a bounded correction to the outcome‑derived GRPO advantage, applying it only to generated action spans. This localizes privileged guidance while preserving the update direction determined by the outcome reward without an auxiliary distillation objective or any change at inference time. Across seven question‑answering benchmarks and three model scales, EviSD achieves the highest macro‑average Exact Match, outperforming previous methods by 1.3–2.3 points.

## Semantic links
- [[concepts/papers/2026-07-21_10-47-27Z_H__2_SD_HybridHindsightSelf_Distillation_summary.md|Summary: 2026-07-21_10-47-27Z_H__2_SD_HybridHindsightSelf_Distillation.md]] — 4 title terms overlap; 16 summary/topic terms overlap; semantic match 0.19
- [[concepts/papers/2026-07-27_02-59-27Z_EviBack_Search_AgentReinforcementLearningvi_summary.md|Summary: 2026-07-27_02-59-27Z_EviBack_Search_AgentReinforcementLearningviaEviden.md]] — 4 title terms overlap; 13 summary/topic terms overlap; semantic match 0.13
- [[concepts/papers/2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionfo_summary.md|Summary: 2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionforEffici.md]] — 4 title terms overlap; 6 summary/topic terms overlap; semantic match 0.11

## Key Contributions  
- Evidence‑conditioned self‑distillation that uses supporting evidence as privileged information for search actions.  
- A bounded correction of the teacher–student gap to the outcome‑derived GRPO advantage applied exclusively to generated action spans.  
- Demonstrated a 1.3–2.3 point improvement in Exact Match across diverse benchmarks with only 6.7%–15.1% token modification.

## Methodology  
EviSD samples actions from the original context and re‑scores them under an action‑aligned context, thereby converting the detached teacher–student gap into a bounded correction to the outcome reward gradient. The correction is applied locally to the spans that were generated during training, allowing the model to receive privileged guidance without introducing any auxiliary distillation loss or altering inference behavior.

## Results  
On seven QA datasets (e.g., SQuAD, Natural Questions) and three backbones ranging from small to large models, EviSD reaches top Exact Match scores. It consistently beats the strongest competing methods by 1.3–2.3 points while modifying only a modest proportion of response tokens—between 6.7% and 15.1%.

## Significance  
This work advances search‑augmented agents by providing an evidence‑aware self‑distillation mechanism that improves reasoning without changing training dynamics or inference pipelines, enabling more efficient and accurate performance gains.

## Related Concepts  
Outcome‑based reinforcement learning, GRPO, self‑distillation, evidence conditioning, action‑aligned context, bounded correction, token‑level adaptation.
