# Summary: 2026-08-10_17-39-16Z_BDH_CQ_In_ContextLearningwithRecurrentLatentReason.md
Saved: 2026-08-11 00:18
Source: 2026-08-10_17-39-16Z_BDH_CQ_In_ContextLearningwithRecurrentLatentReason.md
Model: None

---

## Summary  
BDH‑CQ introduces a reasoning model that merges in‑context learning with recurrent latent reasoning, allowing the system to continuously update its memory as new input tokens arrive and then solve a query iteratively within a high‑dimensional latent space without ever verbalizing intermediate steps. The approach achieves a 29.5 % pass@2 on the ARC‑AGI‑1 benchmark at an inference cost of $0.0007 per task, thereby breaking the previously reported cost‑accuracy Pareto frontier and establishing a new state‑of‑the‑art operating point for efficient benchmark performance.

## Key Contributions  
- [Finding 1] BDH‑CQ integrates in‑context learning with recurrent latent reasoning to continuously update memory during inference.  
- [Finding 2] The model solves queries iteratively in a high‑dimensional latent space without explicit verbalization, improving cost‑efficiency.  
- [Finding 3] Experimental results show 29.5 % pass@2 on ARC‑AGI‑1 at $0.0007 per task, surpassing prior models on both accuracy and computational expense.

## Methodology  
The authors propose a recurrent memory that is updated with each input token, feeding into a high‑dimensional latent space where the model performs iterative reasoning steps. The process is driven by in‑context demonstrations; no intermediate outputs are generated, allowing the system to maintain state across tokens while solving the final query.

## Results  
On the public ARC‑AGI‑1 evaluation set, BDH‑CQ with a 150 M‑parameter configuration reaches 29.5 % pass@2 at a computed inference cost of $0.0007 per task. This operating point lies on the newly defined cost‑accuracy Pareto frontier, outperforming previous models in both accuracy and computational efficiency.

## Significance  
The paper establishes a state‑of‑the‑art benchmark for cost‑efficient reasoning, demonstrating that recurrent latent computation can achieve high performance at minimal computational expense. It also provides insights into which concepts remain difficult to learn from demonstrations, guiding future model design toward more robust in‑context capabilities.

## Related Concepts  
- In‑context learning: prompting models with examples to guide behavior.  
- Recurrent memory: maintaining state across tokens during processing.  
- Latent space iteration: solving problems through successive computations within a hidden representation.  
- Cost‑efficiency frontier: the trade‑off between model accuracy and computational cost.
