# Summary: 2026-07-31_17-54-46Z_SigncompressionforMuon_SignMuon_MuonSign_andtheLim.md
Saved: 2026-08-03 10:26
Source: 2026-07-31_17-54-46Z_SigncompressionforMuon_SignMuon_MuonSign_andtheLim.md
Model: None

---

## Summary
This paper investigates the theoretical limits and practical efficacy of sign compression techniques when applied to the Muon optimizer, specifically introducing variants like SignMuon and MuonSign. The authors demonstrate that while compressing updates to a single bit per parameter offers extreme communication efficiency, it introduces fundamental divergence issues due to bias in the gradient estimation. Through rigorous theoretical analysis, they prove that placing the sign function before or on both sides of the Linear Minimization Oracle (LMO) can lead to ascent rather than descent, even on simple linear functions. However, their experimental results reveal a striking contradiction where heuristics that are theoretically divergent often outperform provably convergent methods in real-world deep learning tasks.

## Key Contributions
- **Theoretical Divergence of Sign Placement**: The authors construct explicit counterexamples proving that applying the sign function before the LMO (MuonUSign) or on both sides (MuonSign) can cause the optimizer to ascend, thereby failing to minimize the objective function in general cases.
- **Inefficacy of Standard Error Feedback**: They demonstrate that applying error feedback to Muon’s output does not rescue the method from divergence, as it fails across all smoothness constants and step sizes; however, applying error feedback to the gradient itself restores convergence rates.
- **Heuristic Superiority in Practice**: Despite theoretical guarantees favoring sign-after-LMO variants, empirical results on CIFAR-10 and nanoGPT show that sign-before-LMO heuristics consistently achieve better performance, highlighting a gap between theory and practice at scale.

## Methodology
The authors combine theoretical analysis with extensive empirical experimentation. Theoretically, they analyze the behavior of Muon under extreme compression by constructing small, explicit linear instances to test convergence properties of different sign placements. They evaluate the impact of error feedback mechanisms on both the gradient and the optimizer's output. Empirically, they implement these variants across centralized and federated learning settings on CIFAR-10 and conduct speedrun experiments on nanoGPT models to compare training efficiency and final model quality under one-bit communication constraints.

## Results
Theoretically, the paper proves that SignMuon can ascend on linear functions and that error feedback applied to Muon's output is insufficient for convergence. Conversely, applying error feedback to the gradient allows variants like EF21-MuonUSign to achieve the standard $\mathcal{O}(T^{-1/2})$ rate for squared gradient norms. Experimentally, the ordering reverses: sign-after-the-LMO methods, which are theoretically safer, trail behind the divergent sign-before-LMO heuristics in terms of practical performance on CIFAR-10 and nanoGPT tasks.

## Significance
This work is significant because it challenges the assumption that theoretical convergence guarantees always translate to practical superiority in deep learning optimization. It highlights the critical importance of understanding how compression biases interact with specific optimizer structures like Muon. Furthermore, it provides a cautionary tale for researchers relying solely on theory, suggesting that heuristic placements may offer unexpected benefits in large-scale distributed training scenarios where communication costs are prohibitive.

## Related Concepts
- Muon Optimizer
- Sign Compression
- Error Feedback
- Linear Minimization Oracle (LMO)
- Federated Learning
- Communication-Efficient Optimization
- Nonconvex Optimization
