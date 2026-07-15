title: "Summary: 2026-06-24_17-59-02Z_On_PolicySelf_DistillationwithSampledDemonstration.md"
# Summary: 2026-06-24_17-59-02Z_On_PolicySelf_DistillationwithSampledDemonstration.md
Saved: 2026-06-24 22:02
Source: 2026-06-24_17-59-02Z_On_PolicySelf_DistillationwithSampledDemonstration.md
Model: None

---


## Summary  
The paper investigates on‑policy self‑distillation—a technique where a single model serves both teacher and student, using sampled correct demonstrations to condition feedback on student rollouts. It demonstrates that this method can achieve high pass@1 accuracy but inadvertently reduces rollout diversity, causing the pass@k curves to flatten. The authors attribute this loss of diversity to compounding biases introduced when the teacher scores rollouts conditioned on a randomly selected correct rollout. Their contribution is both theoretical and empirical: they derive an optimal self‑distillation policy that tilts the base distribution via conditional mutual information and show, through experiments, that while average performance matches reinforcement learning (RL), functional and semantic diversity drops sharply.

## Key Contributions  
- [Finding 1] On‑policy self‑distillation with sampled demonstrations leads to a marked decrease in rollout diversity, resulting in flattened pass@k accuracy curves.  
- [Finding 2] The optimal self‑distillation policy concentrates probability mass on already‑dominant rollout modes by applying a pointwise conditional mutual information score between the student’s output and the sampled correct context.  
- [Finding 3] Empirical results confirm that self‑distilled models match or exceed RL on average benchmarks but exhibit substantially lower functional and semantic diversity, especially on out‑of‑distribution tasks.

## Methodology  
The authors adopt an on‑policy self‑distillation framework where a single model acts as both teacher and student. A correct demonstration is sampled from the training set; this rollout serves as context for conditioning the teacher’s scoring function on the student’s generated rollout. The teacher evaluates the student’s output, producing token‑level feedback that updates the student via gradient descent. This process repeats across many episodes, allowing the model to learn from its own diverse rollouts while being constrained by the sampled demonstration.

## Results  
Theoretical analysis shows that the optimal policy maximizes mutual information between the student’s rollout and the context, which biases the distribution toward high‑probability paths. Experiments on a graph path‑finding task and science question‑answering benchmarks reveal that self‑distilled models achieve comparable pass@1 scores to RL but produce flatter pass@k curves, indicating diminishing returns in accuracy with more rollouts. Moreover, diversity metrics such as functional coverage and semantic variety are lower, and the models struggle on tasks requiring alternative strategies outside their learned distribution.

## Significance  
This work highlights a critical trade‑off between efficiency and diversity in model training: while self‑distillation can be computationally cheaper than RL, it may sacrifice the richness of generated solutions. For applications that demand diverse or robust strategies—such as OOD reasoning—the reduced functional coverage could lead to suboptimal performance, underscoring the need for methods that preserve both accuracy and variety.

## Related Concepts  
- On‑policy self‑distillation  
- Rollout diversity  
- Conditional mutual information  
- Probability ratio preservation (as in RL)  
- Out‑of‑distribution generalization
