# Summary: 2026-05-26_12-20-53Z_LearningtoAdaptSFTDataforBetterReasoningGeneraliza.md
Saved: 2026-05-26 20:00
Source: 2026-05-26_12-20-53Z_LearningtoAdaptSFTDataforBetterReasoningGeneraliza.md
Model: None

---


## Summary  
The paper addresses the issue that directly fine‑tuning large language models on external SFT data can degrade reasoning generalization when the source distribution differs from the model’s own. It proposes Data Adaptation for Reasoning Tuning (DART), a framework that uses reinforcement learning to transform the fixed SFT dataset into a model‑adapted representation. DART optimizes demonstration transformations to align with the target model’s training preferences, enabling better exploitation of supervision. Experiments show improved generalization and higher efficiency compared to standard or direct RL fine‑tuning.

## Key Contributions  
- DART introduces a reinforcement‑learning mapper that converts SFT data into an adapted dataset tailored to the target model.  
- The approach improves reasoning generalization by aligning source data distribution with the model’s learning dynamics.  
- DART achieves higher training efficiency and surpasses baseline SFT without additional data.

## Methodology  
The authors formulate the adaptation problem as a reinforcement‑learning task where a mapper network receives original SFT demonstrations and outputs transformed demonstrations. The reward function encourages transformations that increase downstream reasoning performance on held‑out test tasks, encouraging alignment with the target model’s distribution. A fixed SFT dataset is used as input; the mapper learns to apply stochastic or deterministic transformations (e.g., paraphrasing, rewriting) to produce output pairs that are more informative for fine‑tuning.

## Results  
Across multiple LLMs and datasets (including MMLU, ARC), DART‑fine‑tuned models achieve 4–7% absolute gains in reasoning accuracy versus standard SFT. Training converges faster with fewer gradient steps, indicating higher efficiency. The mapper’s output is comparable to or better than human‑crafted data.

## Significance  
By decoupling the adaptation step from manual data curation, DART offers a scalable way to improve model performance without requiring large labeled datasets, addressing distribution mismatch and enhancing generalization—a key challenge in LLM fine‑tuning.

## Related Concepts  
- Supervised Fine‑Tuning (SFT)  
- Reinforcement Learning for Data Augmentation  
- Distribution Alignment  
- Reasoning Benchmarks  
- Prompt Engineering  
- Model‑Specific Adaptation

[[2026-05-26_12-20-53Z_LearningtoAdaptSFTDataforBetterReasoningGeneraliza.md]]