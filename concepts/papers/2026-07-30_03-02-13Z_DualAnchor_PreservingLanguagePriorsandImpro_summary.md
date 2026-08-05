# Summary: 2026-07-30_03-02-13Z_DualAnchor_PreservingLanguagePriorsandImprovingLex.md
Saved: 2026-07-30 21:37
Source: 2026-07-30_03-02-13Z_DualAnchor_PreservingLanguagePriorsandImprovingLex.md
Model: None

---

## Summary  
The paper addresses language‑prior degradation and lexical fidelity gaps in gloss‑free sign language translation using LLM‑based methods. DualAnchor introduces two complementary anchors to preserve linguistic fluency while maintaining visual alignment. It achieves strong performance on benchmark datasets by jointly regularizing the decoder with token‑level prior anchoring and optimal transport alignment. The framework demonstrates that each anchor tackles a distinct problem, leading to overall improvement.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- DualAnchor integrates Token‑Level Prior Anchoring (TPA) and Optimal Transport Alignment (OTA) into a single training pipeline.  
- TPA preserves the LLM’s language prior by regularizing next‑token generation toward its frozen autoregressive distribution.  
- OTA enforces visual‑textual token correspondence with entropy‑regularized optimal transport, improving lexical fidelity.

## Methodology  
The authors propose DualAnchor as a gloss‑free SLT framework that couples TPA and OTA. At each decoding step, the multimodal decoder is constrained by TPA to follow the next‑token distribution of a frozen LLM sharing the same prefix, while simultaneously solving an entropy‑regularized partial optimal transport problem between visual tokens and textual tokens using cosine cost and Sinkhorn optimization.

## Results  
Experimental evaluation on PHOENIX‑2014T and CSL‑Daily shows DualAnchor outperforms prior LLM‑based SLT baselines by 7.3 % BLEU and a 5.1 % reduction in lexical error rate, with TPA alone boosting fluency scores and OTA alone reducing fine‑grained errors.

## Significance  
By explicitly preserving the language model’s internal priors while aligning visual content to textual semantics, DualAnchor mitigates degradation that plagues current LLM‑driven SLT systems. This work provides a principled way to jointly optimize fluency and lexical fidelity, paving the way for more natural sign‑language translation.

## Related Concepts  
- Large Language Models (LLMs)  
- Sign language translation (SLT)  
- Gloss‑free translation  
- Token‑Level Prior Anchoring (TPA)  
- Optimal Transport Alignment (OTA)  
- Entropy regularization  
- Cosine cost  
- Sinkhorn optimization
