# Summary: 2026-07-24_11-15-27Z_Trajectory_RegularizedStochasticOptimalControlviaK.md
Saved: 2026-07-26 21:48
Source: 2026-07-24_11-15-27Z_Trajectory_RegularizedStochasticOptimalControlviaK.md
Model: None

---

## Summary  
This paper proposes a trajectory‑regularized stochastic optimal control (TRSOC) framework that incorporates the Kullback–Leibler (KL) divergence between the actual and reference trajectory distributions to improve alignment without sacrificing performance. By applying Girsanov’s theorem, the KL term is shown to be equivalent to a quadratic drift mismatch penalty, which preserves the dynamic programming structure of the original problem. The authors derive the corresponding Hamilton–Jacobi–Bellman (HJB) equation and obtain an explicit optimal policy for the linear‑quadratic case with an augmented control cost. Experiments demonstrate that the regularization parameter governs a trade‑off between achieving high performance and preserving the reference trajectory, even when the reference dynamics are learned offline.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-28_15-38-27Z_A2TTA_Anchored_and_AgileTest_TimeAdaptation_summary.md|Summary: 2026-07-28_15-38-27Z_A2TTA_Anchored_and_AgileTest_TimeAdaptationforEvol.md]] — 4 title terms overlap; 5 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The TRSOC formulation introduces KL divergence as a regularizer for stochastic optimal control, providing a principled way to penalize deviations from a desired trajectory.  
- [Finding 2] Girsanov’s theorem reduces the trajectory KL term to a quadratic drift mismatch penalty, preserving the DP structure and enabling an HJB‑based solution.  
- [Finding 3] The method yields a closed‑form optimal control law in the linear‑quadratic setting and empirically shows that the regularization parameter balances performance against reference preservation.

## Methodology  
The authors start from standard stochastic optimal control, which minimizes expected cost under uncertainty. They augment this problem with a KL divergence term between the probability density of the generated trajectory and a predefined reference distribution. Using Girsanov’s theorem, they transform the KL penalty into a quadratic drift mismatch that can be expressed as an additional term in the running cost. This modification leads to a modified Hamilton–Jacobi–Bellman equation whose solution follows the same DP paradigm as the original SOC problem. The regularization parameter is introduced to control the strength of the trajectory‑preserving effect.

## Results  
Theoretical analysis produces an explicit optimal policy that combines the standard LQ cost with the augmented drift mismatch penalty. Numerical experiments confirm that increasing the regularization parameter improves traceability to the reference trajectory while slightly degrading performance, and vice versa. When the reference dynamics are learned from offline data, TRSOC yields more robust control in noisy or uncertain environments compared to plain SOC.

## Significance  
TRSOC bridges theoretical stochastic optimal control with practical trajectory‑tracking goals, offering a principled regularization that can be tuned for robotics, autonomous navigation, and other applications where staying on a desired path is crucial. By preserving the DP structure, it avoids sacrificing optimality while still providing a clear mechanism to enforce reference behavior.

## Related Concepts  
- Stochastic optimal control (SOC)  
- Kullback–Leibler divergence as a regularizer  
- Girsanov’s theorem for change of measure  
- Hamilton–Jacobi–Bellman equation and DP formulation  
- Linear‑quadratic control with augmented cost  
- Trajectory regularization techniques
