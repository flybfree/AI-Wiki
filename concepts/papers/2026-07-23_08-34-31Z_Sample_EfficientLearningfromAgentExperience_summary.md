# Summary: 2026-07-23_08-34-31Z_Sample_EfficientLearningfromAgentExperience.md
Saved: 2026-07-24 02:34
Source: 2026-07-23_08-34-31Z_Sample_EfficientLearningfromAgentExperience.md
Model: None

---

## Summary  
The paper addresses the challenge of learning from agent experience in a sample‑efficient manner, where costly environment interactions are limited. It observes that while in‑context learning can capture contextual information from past trials, its benefits vanish when the context is removed. The authors propose Experience Distillation as a method to internalize this context into model weights without further interaction. By internalizing the agent's history into model parameters, Experience Distillation avoids the need for external supervision or additional data collection.

## Key Contributions  
- Finding 1: Experience Distillation retains at least 64.8 % of the gains from in‑context learning across both domains.  
- Finding 2: Direct supervised fine‑tuning on the collected experience recovers only 3.8 % performance, highlighting the inefficiency of naïve training.  
- Finding 3: The method matches RL baselines with at least 9.6× fewer environment samples, demonstrating superior sample efficiency.

## Methodology  
The methodology leverages context distillation, which extracts latent representations from the agent’s interaction history and updates model parameters to reflect that knowledge, thereby eliminating the need for additional environment sampling.

## Results  
Our experiments on a diverse benchmark of 749 software‑engineering tasks and six text‑adventure games demonstrate that Experience Distillation retains at least 64.8 % of the performance gains achieved by pure in‑context learning, whereas direct supervised fine‑tuning on the same experience recovers only 3.8 %. Moreover, when compared to standard reinforcement‑learning baselines, our approach achieves comparable results with roughly nine point six times fewer environment samples.

## Significance  
This work matters because it shows that agents can maintain high learning performance while drastically reducing the number of costly trials, which is essential for practical deployment where sample efficiency directly impacts cost and scalability. In real‑world settings where each trial can be expensive or time‑consuming, such a reduction translates into measurable economic and operational benefits.

## Related Concepts  
in‑context learning, context distillation, experience distillation, reinforcement learning baselines, supervised fine‑tuning, curriculum learning
