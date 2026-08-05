# Summary: 2026-07-22_06-32-34Z_Zero_ObservationUserReactivationwithGap_DrivenDime.md
Saved: 2026-07-24 01:28
Source: 2026-07-22_06-32-34Z_Zero_ObservationUserReactivationwithGap_DrivenDime.md
Model: None

---

## Summary  
The paper tackles the problem of recommending items to users who have not interacted with the platform for an extended period—Zero‑Observation Reactivation. By analyzing three Amazon product datasets under a Chronologically Aligned Gap‑Synthesize Protocol, the authors demonstrate that standard sequential recommendation models suffer a monotonic decline in Hit@10 as the gap lengthens, reaching its lowest point beyond one year. Their contribution is a lightweight output‑layer plugin called DeltaGate that routes each representation dimension between a frozen personalized history and a zero‑initialized global prior, conditioned jointly on the gap duration Δt. The solution preserves the backbone’s frozen embeddings while adding only 2–4 % trainable parameters (≈66 K), yielding a 40× reduction in retraining cost compared with full end‑to‑end training.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Zero‑Observation Reactivation is defined and empirically shown to cause Hit@10 to degrade across increasing gap buckets, reaching its minimum beyond one year.  
- [Finding 2] DeltaGate, a frozen‑backbone plugin that conditionally gates each dimension between personalized history and a zero‑initialized global prior, improves performance without retraining the backbone.  
- [Finding 3] The plugin adds only ~66 K trainable parameters (≈2–4 % overhead) and retains observable routing behavior, outperforming baseline models such as SASRec and BERT4Rec on Amazon video‑game data.

## Methodology  
The authors employ a Chronologically Aligned Gap‑Synthesize Protocol that aligns user histories with gap lengths Δt across three Amazon datasets (Video Games, CDs & Vinyl, Movies & TV). They evaluate recurrent, unidirectional, and bidirectional sequential recommendation backbones. DeltaGate is implemented as an output‑layer plugin: the backbone remains frozen, while a lightweight gating module learns to blend each representation dimension between the personalized history vector and a global prior initialized to zero. A diagnostic experiment holds the personalized representation fixed and varies Δt to isolate the gate’s response to gap input.

## Results  
Hit@10 decreases monotonically with longer gaps; the lowest value occurs beyond one year across all datasets. In the >365‑day Video Games bucket, DeltaGate‑augmented SASRec achieves 0.047 Hit@10 versus 0.031 for SASRec alone, and DeltaGate‑augmented BERT4Rec reaches 0.046 versus 0.025 for BERT4Rec. The plugin introduces only ~66 K trainable parameters (≈2–4 % overhead), which is roughly 40× fewer than full end‑to‑end retraining. End‑to‑end training yields higher absolute accuracy but alters backbone embeddings; the frozen DeltaGate preserves zero drift and maintains dimension‑wise routing.

## Significance  
This work provides a practical, low‑cost solution for cold‑start scenarios where users have no recent interaction signals. By freezing the backbone and adding only a few hundred thousand parameters, DeltaGate improves recommendation quality while minimizing computational expense and avoiding catastrophic forgetting of learned representations. The approach is scalable to other domains and can be integrated into existing sequential recommendation pipelines.

## Related Concepts  
Zero‑Observation Reactivation, Gap‑Synthesize Protocol, Dimensional Gating, Frozen Backbone, Hit@10 metric, Amazon datasets (Video Games, CDs & Vinyl, Movies & TV), SASRec, BERT4Rec.
