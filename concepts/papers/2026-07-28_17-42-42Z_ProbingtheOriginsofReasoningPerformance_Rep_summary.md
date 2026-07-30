# Summary: 2026-07-28_17-42-42Z_ProbingtheOriginsofReasoningPerformance_Representa.md
Saved: 2026-07-29 20:17
Source: 2026-07-28_17-42-42Z_ProbingtheOriginsofReasoningPerformance_Representa.md
Model: None

---

## Summary  
The paper investigates why reinforcement‑learning (RL) models outperform supervised fine‑tuned (SFT) models on mathematical reasoning tasks, focusing on internal representational quality. It provides two converging lines of evidence: linear probes show RL models have more structured answer‑prediction representations, and mean ablation reveals hierarchical layer importance in RL versus uniform SFT representation. The authors also examine token‑count variability across problem instances to infer adaptive compute allocation.

## Key Contributions  
- [Finding 1] Linear probes indicate that RL models achieve higher accuracy in predicting answer correctness than SFT models, suggesting their hidden representations are more linearly separable and structured.  
- [Finding 2] Mean ablation studies reveal that RL models develop a hierarchical architecture where deeper layers become progressively more critical, whereas SFT models distribute importance uniformly across layers.  
- [Finding 3] Token‑count variability analysis shows higher variability in some RL‑tuned models compared to SFT counterparts, indicating adaptive compute allocation and revealing the spread of plausible on‑policy reasoning.

## Methodology  
The authors employ two complementary probing techniques: (1) linear classification probes trained on layer‑wise hidden states to predict answer correctness, measuring accuracy differences between RL and SFT models; and (2) mean ablation studies that quantify per‑layer contribution by removing each layer’s output and averaging across problems. Additionally, they perform token‑count variability analysis by sampling multiple solutions for the same problem and recording the distribution of token lengths.

## Results  
Probes consistently show RL models have higher probe accuracy than SFT models (e.g., 84 % vs 71 %). Ablation results confirm a hierarchical importance drop‑off in RL, with top layers contributing ~30 % more to performance than lower layers, while SFT shows flat contributions. Token‑count variability is higher for RL models on some problems (standard deviation >5 tokens) compared to SFT (SD <2 tokens), indicating adaptive compute.

## Significance  
These findings clarify the mechanistic advantage of RL training over supervised fine‑tuning: it induces more structured, hierarchical representations and enables variable compute allocation, which can affect solution stability. Understanding this representational shift is crucial for designing efficient reasoning systems and avoiding under‑determined policies.

## Related Concepts  
- Reinforcement learning (RL) vs. supervised fine‑tuning (SFT)  
- Linear probing of hidden states  
- Hierarchical architecture analysis  
- Token‑count variability as a proxy for compute allocation  
- On‑policy reasoning stability
