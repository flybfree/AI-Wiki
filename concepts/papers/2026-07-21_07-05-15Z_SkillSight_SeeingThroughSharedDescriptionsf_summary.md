# Summary: 2026-07-21_07-05-15Z_SkillSight_SeeingThroughSharedDescriptionsforAccur.md
Saved: 2026-07-24 00:32
Source: 2026-07-21_07-05-15Z_SkillSight_SeeingThroughSharedDescriptionsforAccur.md
Model: None

---

## Summary  
The paper identifies that skill descriptions share common descriptive patterns, which cause dense retrievers to over‑estimate relevance and create an energy gap between queries and skill documents, leading to inaccurate skill selection. SkillSight proposes a training‑free calibration framework that separates this shared background from task‑relevant signals in both semantic and lexical spaces.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 12 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Shared descriptive background systematically inflates dense relevance scores and creates an energy gap between queries and skill documents.  
- [Finding 2] Semantic Background Calibration estimates a background subspace using IDF‑identified generic tokens to reduce similarity caused by generic tokens.  
- [Finding 3] Lexical Evidence Calibration downweights shared background tokens, recovering discriminative token‑level evidence.

## Methodology  
The authors propose SkillSight as a training‑free retrieval framework that operates in two calibration stages: first, Semantic Background Calibration builds a subspace of IDF‑identified generic tokens and projects queries/skills onto its orthogonal complement; second, Lexical Evidence Calibration applies token‑level weighting to suppress the influence of these background tokens while preserving task‑specific signals. The framework is applied to dense retrieval without any fine‑tuning.

## Results  
Experiments on SRA‑Bench and SkillBench‑Supp show consistent improvements across recall metrics. SkillSight improves Recall@10 by up to 20.21 percentage points over the original dense retriever, achieves best performance among three agent models, outperforms LLM Selection by up to 4.97 pp, and is up to 1,248 times faster than Dense+Reranker baseline.

## Significance  
By explicitly calibrating shared background, SkillSight mitigates bias in skill retrieval, enabling accurate and efficient selection without additional training—critical for large language model agents that must choose from vast skill libraries.

## Related Concepts  
dense retrieval, IDF token filtering, semantic subspace projection, lexical evidence weighting, energy gap, task‑relevant signal recovery, training‑free calibration.
