# Summary: 2026-07-31_17-54-46Z_SigncompressionforMuon_SignMuon_MuonSign_andtheLim.md
Saved: 2026-08-03 10:28
Source: 2026-07-31_17-54-46Z_SigncompressionforMuon_SignMuon_MuonSign_andtheLim.md
Model: None

---

## Summary
This paper investigates the theoretical and practical limits of applying sign compression to the Muon optimizer, a matrix-aware optimization technique designed for efficient large-scale training. The authors introduce SignMuon and its variants, which compress updates to one bit per parameter by taking the elementwise sign, aiming to minimize communication costs in distributed settings. While these methods offer extreme compression efficiency, the study reveals fundamental theoretical flaws: specifically, placing the sign operator before or on both sides of the Linear Minimization Oracle (LMO) can cause the optimizer to ascend rather than descend, even on simple linear functions. Furthermore, standard error feedback mechanisms fail to correct this divergence when applied to the Muon output, although they do restore convergence when applied to the gradient itself.

## Key Contributions
- **Theoretical Divergence of Sign Placement**: The authors provide explicit counterexamples proving that signing the gradient before the Linear Minimization Oracle (MuonUSign) or on both sides (MuonSign) leads to ascent rather than descent, demonstrating that no general placement of the sign operator around the oracle guarantees convergence.
- **Failure of Error Feedback on Output**: It is shown that applying error feedback directly to Muon’s compressed output does not rescue the method from divergence; this failure persists across all smoothness constants, step sizes, and momentum parameters, highlighting a critical limitation in standard bias-correction techniques for this specific architecture.
- **Heuristic Superiority in Practice**: Despite theoretical guarantees favoring sign-after-the-LMO variants (which are proven to converge at an $\mathcal{O}(T^{-1/2})$ rate), empirical results on CIFAR-10 and nanoGPT tasks reveal that the theoretically divergent sign-before-LMO heuristics consistently outperform them, suggesting that practical performance metrics may contradict theoretical convergence bounds in large-scale settings.

## Methodology
The authors combine rigorous theoretical analysis with extensive empirical experimentation. Theoretically, they construct small, explicit mathematical instances to test the behavior of different sign placements relative to the LMO, analyzing whether the resulting updates constitute a descent direction. They also analyze the stability of error feedback mechanisms when applied to either the gradient or the optimizer's output. Empirically, they evaluate these methods on centralized and federated CIFAR-10 classification tasks and a nanoGPT speedrun, comparing the performance of theoretically convergent variants against heuristic approaches that violate theoretical assumptions.

## Results
Theoretical analysis confirms that SignMuon can ascend on linear functions and that error feedback fails to stabilize the optimizer when applied to its output. However, experiments show that the variant compressing after the LMO achieves standard convergence rates for smooth nonconvex problems. In practice, however, the ordering reverses: methods using sign-before-the-LMO heuristics achieve superior performance on real-world datasets like CIFAR-10 and nanoGPT, despite their theoretical instability.

## Significance
This work highlights a critical disconnect between theoretical convergence guarantees and practical performance in highly compressed optimization. It warns practitioners that while error feedback is standard for biased compressors, it may not suffice for matrix-aware optimizers like Muon unless applied carefully to the gradient rather than the update. The findings suggest that in large-scale systems, heuristic choices regarding compression placement may outweigh theoretical stability concerns, urging a re-evaluation of convergence criteria in practical deep learning contexts.

## Related Concepts
- SignSGD
- Linear Minimization Oracle (LMO)
- Error Feedback (EF21)
- Matrix-aware Optimizers
- Communication-efficient Distributed Optimization
- Nonconvex Optimization
