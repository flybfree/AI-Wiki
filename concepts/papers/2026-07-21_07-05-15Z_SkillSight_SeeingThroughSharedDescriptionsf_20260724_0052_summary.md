# Summary: 2026-07-21_07-05-15Z_SkillSight_SeeingThroughSharedDescriptionsforAccur.md
Saved: 2026-07-24 00:52
Source: 2026-07-21_07-05-15Z_SkillSight_SeeingThroughSharedDescriptionsforAccur.md
Model: None

---

## Summary  
SkillSight addresses a critical bottleneck in large‑language model agents: retrieving the correct skill from an expanding library when descriptions are highly similar and share common phrasing. The authors demonstrate that shared descriptive background inflates dense relevance scores, creates an energy gap between queries and documents, and masks task‑relevant cues, leading to poor retrieval performance. Their contribution is a training‑free calibration framework that explicitly reduces this background noise while preserving discriminative signals.

## Key Contributions  
- [Finding 1] Shared descriptive patterns across skill descriptions systematically inflate dense relevance scores by inducing an energy gap between queries and skill documents.  
- [Finding 2] This background obscures task‑relevant signals, causing retrieval systems to focus on generic tokens rather than discriminative evidence.  
- [Finding 3] A training‑free calibration approach—Semantic Background Calibration (IDF‑based subspace) and Lexical Evidence Calibration (downweighting shared tokens)—restores accurate skill retrieval without additional learning.

## Methodology  
SkillSight proposes a two‑stage, training‑free calibration pipeline. First, **Semantic Background Calibration** extracts a background subspace using IDF‑ranked generic tokens that appear in many skills, thereby reducing similarity driven by common phrasing. Second, **Lexical Evidence Calibration** downweights these shared background tokens at the token level, allowing task‑specific evidence to dominate the embedding space. The calibrated embeddings are then used for dense retrieval without any fine‑tuning or reranking.

## Results  
Experiments on SRA‑Bench and SkillBench‑Supp show consistent gains: Recall@10 improves by up to 20.21 percentage points over the original dense retriever, and SkillSight achieves the best overall performance across three agent models, outperforming LLM Selection by up to 4.97 ppt. Moreover, SkillSight is up to 1,248 times faster than the Dense + Reranker baseline, highlighting both accuracy and efficiency gains.

## Significance  
By identifying shared descriptive background as a primary source of bias in skill retrieval, SkillSight offers a practical solution that improves agent capability selection without retraining models. This reduces latency and computational cost while maintaining high precision, making large‑scale LLM agents more reliable and scalable.

## Related Concepts  
dense retrieval, IDF (inverse document frequency), background subspace, calibration, shared descriptive patterns, task‑relevant signals, training‑free adaptation, token‑level weighting.
