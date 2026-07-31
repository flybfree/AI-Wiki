# Summary: 2026-07-30_12-45-18Z_LM_GRASP_Instance_SpecificLanguageModelsforCombina.md
Saved: 2026-07-30 21:50
Source: 2026-07-30_12-45-18Z_LM_GRASP_Instance_SpecificLanguageModelsforCombina.md
Model: None

---

## Summary  
The paper introduces LM‑GRASP, a metaheuristic that replaces the static, myopic heuristic rules of classical GRASP with an instance‑specific language model trained online via imitation learning. Instead of pre‑training on large offline datasets, each problem is tackled by training a decoder‑only Transformer from scratch using elite trajectories discovered during a local search process. This approach eliminates the need for problem‑specific feature engineering and external pretraining. The framework is evaluated on the Taillard PFSP benchmark, showing that LM‑GRASP can achieve performance comparable to GPU‑accelerated GRASP while offering per‑instance adaptability.

## Key Contributions  
- [Finding 1] Online imitation learning can replace static greedy heuristics in combinatorial construction tasks.  
- [Finding 2] A decoder‑only Transformer serves as the constructive policy, trained from elite trajectories via behavioral cloning without offline pretraining.  
- [Finding 3] Instance‑specific LM‑GRASP yields a makespan improvement of ~28.4 units on average over GPU‑GRASP, comparable to the speedup provided by GPU acceleration.

## Methodology  
The authors adopt an iterative learn‑infer‑improve cycle: local search acts as an expert oracle that evaluates candidate solutions and maintains a dynamic archive of elite trajectories; this archive is used to train a decoder‑only Transformer online through behavioral cloning. No external data or offline pretraining is required, and the only interface with the problem domain is the objective evaluator supplied by the local search. The pipeline thus produces an instance‑specific language model that guides random construction steps.

## Results  
On the Taillard PFSP benchmark (problems ta51–ta60), LM‑GRASP outperforms GPU‑GRASP by an average of 28.4 makespan units, with standard deviations overlapping those of the GPU acceleration gain (~27.2 units). This demonstrates that online‑trained language models can match or exceed the performance gains achieved through hardware acceleration while providing per‑instance adaptability.

## Significance  
LM‑GRASP offers a practical alternative to hand‑engineered constructors for complex, landscape‑resistant combinatorial problems, eliminating costly pretraining and feature engineering. By training an instance‑specific language model online, it reduces computational overhead and improves generalization across problem instances, making metaheuristics more scalable and effective.

## Related Concepts  
- GRASP (Greedy Randomized Search Program)  
- Instance‑specific language models  
- Online imitation learning  
- Behavioral cloning  
- Decoder‑only Transformer  
- Metaheuristic framework  
- Local search oracle
