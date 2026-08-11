# Summary: 2026-08-10_12-53-06Z_BidirectionalContextSelf_DistillationforReinforcem.md
Saved: 2026-08-11 00:08
Source: 2026-08-10_12-53-06Z_BidirectionalContextSelf_DistillationforReinforcem.md
Model: None

---

## Summary  
The paper proposes BCSD (Bidirectional Context Self‑Distillation), a framework that aligns reinforcement learning with external natural‑language skill guidance for LLM agents. It addresses the gap where standard RL rewards ignore how effectively policies translate skill instructions into actions. By using two complementary viewpoints—an augmented high‑level meta‑skill view and a reduced task‑specific view—the method rescales the RL advantage to reflect genuine skill utilization. Experiments on ALFWorld and WebShop show BCSD outperforms prior methods across model scales, demonstrating that context‑aware reward shaping can improve agent performance.

## Key Contributions  
- [Finding 1] BCSD integrates self‑distillation with reinforcement learning, achieving better skill usage than task‑level rewards alone.  
- [Finding 2] The framework employs a bidirectional view of each trajectory, combining meta‑skill guidance and pruned guidance to generate richer token‑level signals.  
- [Finding 3] Ablation studies confirm that both the augmented and reduced context views contribute uniquely to performance gains.

## Methodology  
The authors begin with an LLM agent trained on external natural‑language skills for tasks such as ALFWorld and WebShop. Instead of using a single RL reward, they replace it with a self‑distilled advantage that is modulated by signals from two complementary context views. The augmented view supplies higher‑level meta‑skill guidance, while the reduced view strips away general cues to highlight task‑specific tokens. These token‑level signals are fused and used to rescale the RL loss, allowing the agent to prioritize actions that effectively use the provided skills.

## Results  
On ALFWorld, BCSD raises success rates by 12.3 % compared with a baseline RL method; on WebShop it improves average transaction value by 8.7 %. Across small, medium and large model sizes, BCSD consistently outperforms prior self‑distillation and RL baselines, with gains diminishing only slightly for the largest models.

## Significance  
This work bridges the gap between external skill guidance and reinforcement learning, offering a scalable approach that improves LLM agents without retraining on task‑specific data. It shows that context‑aware reward shaping can unlock latent reasoning capabilities, making skill‑based agents more reliable and efficient.

## Related Concepts  
Self‑distillation, reinforcement learning, external skills, meta‑skill guidance, token‑level signal fusion, RL advantage scaling, bidirectional view, ablation study.
