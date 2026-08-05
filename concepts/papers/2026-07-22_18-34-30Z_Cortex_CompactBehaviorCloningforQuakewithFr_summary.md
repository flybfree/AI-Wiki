# Summary: 2026-07-22_18-34-30Z_Cortex_CompactBehaviorCloningforQuakewithFrozenVis.md
Saved: 2026-07-27 23:21
Source: 2026-07-22_18-34-30Z_Cortex_CompactBehaviorCloningforQuakewithFrozenVis.md
Model: None

---

## Summary  
The authors investigate how far a deliberately simple behavioral‑cloning policy can advance in the visually rich first‑person shooter Quake before introducing reinforcement learning or explicit memory mechanisms. Their contribution is a compact policy, Cortex, that employs only 10.98 million trainable parameters within a six‑layer transformer and leverages a frozen DINOv3 encoder to process visual data. The model is trained on a large but static dataset of Quake recordings, achieving notable performance without any reinforcement learning or memory components. This work demonstrates that limited‑parameter models can still reach meaningful milestones in complex gameplay.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Cortex achieves a compact policy size (≈10 M parameters) while still reaching key environmental points and occasional kills in Quake E1M1, showing that small models can handle rich visual input.  
- [Finding 2] The use of frozen DINOv3 embeddings reduces training time to ~3.3 minutes per epoch on a single RTX 5080, highlighting the efficiency gains from pre‑computed visual features.  
- [Finding 3] Ablations reveal that denser visual tokens improve combat outcomes, whereas longer optimization and naive action history marginally boost offline metrics without consistently enhancing play.

## Methodology  
The authors train Cortex on a frozen subset of the Pixels2Play Quake corpus: 6,849 recordings (~474.7 h) encoded as 17.09 M cached decision frames with corresponding keyboard and mouse actions. A six‑layer transformer processes these frames using the pre‑computed DINOv3 embeddings, which are not updated during training. Training consists of a single epoch that samples 517,048 four‑frame windows; policy‑head optimization on an RTX 5080 takes about three minutes, excluding one‑time feature extraction. Evaluation is performed via two independent batches of 20 stochastic 120‑second episodes, measuring how far the agent progresses and whether it performs actions such as opening doors or killing enemies.

## Results  
Cortex does not complete Quake levels but consistently reaches the opening door, button room, and gate descent; 19 out of 20 episodes in each batch record at least one kill. Compared to released P2P‑150M and NitroGen checkpoints evaluated under identical time constraints, Cortex’s policy remains shallower in five matched‑duration episodes each. Ablation experiments show that richer visual tokens enhance combat performance, while extending optimization or using naive action history yields only marginal offline gains without improving live play.

## Significance  
This study proves that a minimal set of trainable parameters combined with frozen vision encodings can produce usable behavior in complex video games, challenging the assumption that large models are necessary for meaningful gameplay. It also provides a template for efficient policy training on static visual data, which could be extended to other domains where reinforcement learning is impractical.

## Related Concepts  
- Behavioral cloning  
- Frozen vision encoders (e.g., DINOv3)  
- Transformer‑based policies  
- Parameter efficiency in deep RL  
- Covariate shift and corrective data augmentation
