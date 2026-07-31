# Summary: 2026-07-30_14-41-05Z_HARGO_Heterogeneity_AwareReward_GuidedOptimization.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-41-05Z_HARGO_Heterogeneity_AwareReward_GuidedOptimization.md
Model: None

---

## Summary  
The paper addresses the problem that supervised fine‑tuning (SFT) for large language models on heterogeneous high‑performance computing tasks yields inconsistent performance across classification, factual QA, and generation because reward distributions differ dramatically. It proposes HARGO, a Heterogeneity‑Aware Reward‑Guided Optimization framework that learns per‑response importance weights without task labels by fusing confidence‑modulated advantage signals derived from group‑level reward contrast and reference model log‑probabilities. This approach enables fine‑grained optimization for tasks with extreme heterogeneity in answer length and reward scales. The contribution is the design of HARGO, which outperforms nine benchmark methods across all primary metrics.

## Key Contributions  
- [Finding 1] Uniform RL methods like GRPO are suboptimal for heterogeneous HPC tasks due to disparate reward distributions and answer‑length scales.  
- [Finding 2] HARGO introduces per‑response importance weighting via confidence‑modulated advantage, computing both a discrimination signal from group‑level reward contrast and a confidence signal from reference model log‑probabilities.  
- [Finding 3] Ablation studies confirm complementary contributions of the discrimination and confidence signals to overall performance.

## Methodology  
The authors tackled the heterogeneity by first training LLMs on SFT for each HPC task, then applying RL post‑training. Instead of using a single global reward, they compute advantage ratios across response groups, derive a discrimination signal that quantifies how much one group outperforms another relative to baseline, and generate a confidence signal from the log‑probabilities of reference model outputs. These signals are combined to modulate advantages, producing per‑response importance weights that guide optimization. The process is fully unsupervised with respect to task‑type labels.

## Results  
Across four HPC tasks (binary race detection, MLPerf benchmark QA, and semantic generation) and nine RL methods including GRPO, PPO, and DQN variants, HARGO achieved the highest WinRate (54.62 %), Data Race F1 (91.30 %), and PLP Similarity (0.8558). All other methods fell short on at least one metric; for example, GRPO reached 48.7 % win rate but produced verbose answers with high token count. The ablation experiments show that removing either the discrimination or confidence signal drops performance by ~3–5 % in the most sensitive tasks.

## Significance  
HARGO demonstrates a principled way to align LLMs with diverse HPC task objectives without requiring task‑specific reward engineering, which is crucial for real‑world deployment where tasks vary widely. By leveraging both inter‑group reward contrast and model confidence, it yields more faithful and concise outputs, reducing token waste and improving win rates across heterogeneous settings.

## Related Concepts  
- Reinforcement Learning (RL) post‑training of LLMs  
- Heterogeneous task environments  
- Per‑response importance weighting  
- Confidence‑modulated advantage signals  
- Group‑level reward contrast  
- Reference model log‑probability
