# Summary: 2026-07-30_03-32-19Z_Arm2Air_Cross_EmbodimentSkeletonTransferfor3DRelay.md
Saved: 2026-07-30 20:25
Source: 2026-07-30_03-32-19Z_Arm2Air_Cross_EmbodimentSkeletonTransferfor3DRelay.md
Model: None

---

## Summary  
Arm2Air addresses the challenge of placing UAV relays in cluttered urban environments by transferring obstacle‑avoidance skeletons learned from robot arms to a UAV relay‑formation problem. The authors propose a cross‑embodiment transfer pipeline that converts pretrained arm motions into ordered skeletons, trains a transformer on these skeletons, and then fine‑tunes the model with low‑rank adaptation using only three target maps. This approach yields a data‑efficient initialization for UAV relay placement while preserving structural priors from the source domain. The method reduces planning runtime dramatically compared to conventional planners and improves connectivity metrics under high obstruction.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Arm2Air transfers ordered skeleton priors from robot arms to UAV relay formation, enabling cross‑embodiment learning with minimal target data.  
- [Finding 2] The low‑rank adaptation reduces the number of trainable parameters from 1.38 million (full fine‑tuning) to 0.134 million while achieving a 53.6 % lower root mean square error in relay positions.  
- [Finding 3] On high‑obstruction urban maps, Arm2Air improves bottleneck capacity by 32.6 %, cuts hop‑distance variance by 75.2 %, and lowers maximum hop distance by 13.2 % relative to IMPC‑MD.

## Methodology  
The authors start with a pretrained Neural Motion Planner (MP) that generates obstacle‑avoidance trajectories for robot arms. These trajectories are discretized into ordered skeletons, which serve as input features for a transformer encoder. The encoder is fine‑tuned on the nine held‑out 3D urban maps using standard supervised learning. To adapt to the UAV domain with only three target maps, they apply Low‑Rank Adaptation (LoRA), updating a small set of low‑rank matrices instead of all weights. The resulting skeleton initializes a relay chain that is subsequently optimized for connectivity, bottleneck capacity, delay, and movement cost.

## Results  
Experimental evaluation on nine high‑clutter 3D urban maps shows Arm2Air reduces median end‑to‑end planning runtime by 64.9 % compared to the fastest conventional planner. On a separate set of 30 dense‑urban maps with heavy obstructions, it boosts bottleneck capacity by 32.6 %, decreases capacity variance by 74.7 %, shortens maximum hop distance by 13.2 %, and reduces hop‑distance variance by 75.2 % while cutting relay displacement by 16.9 %. The low‑rank fine‑tuning also yields a 53.6 % reduction in root mean square error versus training from scratch with Scratch or Full Fine‑Tuning.

## Significance  
Arm2Air demonstrates that structured, cross‑embodiment priors can be efficiently transferred to robotics tasks requiring spatial reasoning, offering a scalable strategy for autonomous navigation and relay placement. By leveraging low‑rank adaptation, it dramatically cuts computational cost and data requirements, making real‑time deployment feasible in resource‑constrained UAVs.

## Related Concepts  
- Cross‑embodiment transfer learning  
- Low‑Rank Adaptation (LoRA) for fine‑tuning large models  
- Neural Motion Planner (MP) for obstacle avoidance  
- Transformer encoder as a representation learner  
- 3D urban mapping and relay formation optimization
