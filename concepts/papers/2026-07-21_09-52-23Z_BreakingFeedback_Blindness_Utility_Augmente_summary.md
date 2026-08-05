# Summary: 2026-07-21_09-52-23Z_BreakingFeedback_Blindness_Utility_AugmentedTransf.md
Saved: 2026-07-24 00:42
Source: 2026-07-21_09-52-23Z_BreakingFeedback_Blindness_Utility_AugmentedTransf.md
Model: None

---

## Summary  
The paper identifies a structural limitation in existing Transformer models for sequential decision making: they remain *feedback‑blind* because attention retrieval is driven only by observation similarity, even when reward information is supplied as input or used during training. This blindness prevents the model from distinguishing histories that share the same observations but have different action‑reward outcomes, leading to suboptimal choices in non‑stationary environments. To remedy this, the authors introduce the Utility‑Augmented Transformer (UAT), a feedback‑conditioned attention architecture that directly modulates query, key and value projections with a compact utility state.  

## Semantic links
- [[concepts/papers/2026-07-30_05-25-23Z_RecallBeforeYouRank_Similarity_GuidedTop__K_summary.md|Summary: 2026-07-30_05-25-23Z_RecallBeforeYouRank_Similarity_GuidedTop__K_Reusef.md]] — 4 title terms overlap; 13 summary/topic terms overlap; semantic match 0.09
- [[concepts/papers/2026-07-29_13-15-23Z_Hearsay_Vision_LanguageMedicalDiagnosesWith_summary.md|Summary: 2026-07-29_13-15-23Z_Hearsay_Vision_LanguageMedicalDiagnosesWithoutanIm.md]] — 3 title terms overlap; 14 summary/topic terms overlap; semantic match 0.10
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 1 backlink; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The paper formally defines *feedback‑blind retrieval* and proves that any observation‑only attention cannot differentiate histories with different action‑reward outcomes, establishing the problem’s core limitation.  
- [Finding 2] UAT is proposed as a new architecture where a small utility vector is added to the linear projections of queries, keys and values, allowing the action‑reward history to bias context retrieval during the forward pass while preserving a zero‑gate degradation property that recovers the vanilla Transformer when feedback is irrelevant.  
- [Finding 3] Under finite‑horizon Lipschitz assumptions, UAT strictly enlarges the class of observation‑only Transformers and can uniformly approximate any feedback‑dependent decision map.  

## Methodology  
The authors first analyze how standard Transformer attention mechanisms operate in sequential decision making tasks that involve non‑stationary environments and partially observable states. They formalize the limitation as *feedback‑blind retrieval*, demonstrating analytically that attention scores depend solely on observation embeddings, ignoring reward signals. To address this mismatch, they design UAT by injecting a low‑dimensional utility state into the attention computation: each projection (Q, K, V) is replaced with Q + α·U, K + β·U, V + γ·U where α, β, γ are learnable scalars. This simple modification lets the model condition retrieval on both observations and accumulated utility. The architecture retains the zero‑gate property because when U is constant or uninformative, it collapses to the original Transformer.  

## Results  
Across four benchmark tasks—synthetic navigation with hidden goal shifts, non‑stationary sepsis treatment, cross‑market portfolio allocation, and delayed‑feedback recommendation—UAT consistently outperforms observation‑only Transformers, test‑time adaptation baselines, and input‑level feedback approaches. The improvement is especially pronounced in noisy or rapidly changing regimes where stronger adaptation is required. Theoretical analysis shows that UAT can uniformly approximate any decision map that depends on both observations and reward history under the stated Lipschitz constraints.  

## Significance  
This work bridges a longstanding gap between transformer attention mechanisms and real‑world sequential decision making, where rewards provide critical signals for adaptation. By enabling feedback to directly shape context retrieval, UAT improves model robustness and performance, particularly when environments change rapidly or reward signals are weak. The theoretical guarantee that UAT strictly enlarges the observation‑only class provides a solid foundation for future research on adaptive transformer architectures.  

## Related Concepts  
- Feedback‑blindness  
- Observation‑only attention  
- Utility state (compact signal conditioning)  
- Zero‑gate degradation property  
- Lipschitz approximation  
- Non‑stationary environment adaptation  
- Transformer architecture modifications
