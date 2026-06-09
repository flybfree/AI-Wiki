# Summary: 2026-04-28_17-52-38Z_HowFastShouldaModelCommittoSupervision_TrainingRea.md
Saved: 2026-04-29 00:20
Source: 2026-04-28_17-52-38Z_HowFastShouldaModelCommittoSupervision_TrainingRea.md
Model: None

---

## Summary
This paper addresses the critical challenge of "cold-start stalling" in reasoning models, where reinforcement learning from verifiable rewards (RLVR) fails to make progress when the initial success probability is low. The authors introduce a novel training framework based on the Tsallis $q$-logarithm, which defines a continuous loss family $J_Q$ that interpolates between pure exploitation (RLVR) and density estimation (log-marginal-likelihood). By analyzing the gradient amplification factors inherent in this continuum, they demonstrate that intermediate values of $q$ can significantly accelerate escape from poor initial states without incurring the noise memorization associated with pure density estimation. The study further derives two practical algorithms, GARL and PAFT, to estimate these gradients and validates their efficacy across multiple reasoning benchmarks.

## Key Contributions
- **Theoretical Unification of RL and SFT**: The authors establish a formal mathematical link between Reinforcement Learning from Verifiable Rewards (RLVR) and Supervised Fine-Tuning (SFT) by showing they are poles of the same Tsallis loss continuum, differing only by a scalar amplification factor rather than gradient direction.
- **Derivation of GARL and PAFT**: They propose two distinct Monte Carlo estimators for the intractable gradient amplification: Gradient-Amplified RL (GARL), which samples from the prior to amplify gradients, and Posterior-Attenuated Fine-Tuning (PAFT), which importance-resamples from the posterior to enable standard SFT with coherent gradients.
- **Empirical Validation of Cold-Start Mitigation**: The paper provides concrete evidence that GARL at $q=0.75$ successfully escapes cold-start stalling where GRPO fails entirely, while PAFT offers superior stability and performance in warm-start scenarios on complex multi-hop reasoning tasks.

## Methodology
The authors approach the problem by defining a loss family $J_Q$ using the Tsallis $q$-logarithm, which allows for interpolation between the exploitation pole ($q=0$, equivalent to RLVR) and the density-estimation pole ($q=1$, equivalent to log-marginal-likelihood). They analyze the gradient flow dynamics, proving that the exploitation pole requires $\Omega(1/p_0)$ time to escape cold start, whereas the density-estimation pole escapes in $\Theta(\log(1/p_0))$. To implement this theoretically sound but computationally intractable approach, they derive two Monte Carlo estimators. GARL samples trajectories from the prior distribution and amplifies the RL gradient by a factor of $P_{\theta^{-q}}$, while PAFT importance-resamples from the posterior distribution, effectively converting the problem into standard SFT with attenuated weights. Both methods are analyzed for bias and variance, with GARL offering lower variance and PAFT providing semantically coherent gradients.

## Results
Experiments on FinQA, HotPotQA, and MuSiQue datasets demonstrate that GARL at $q=0.75$ substantially mitigates cold-start stalling, achieving success where GRPO fails completely. In warm-start scenarios, GARL at low $q$ dominates on FinQA due to stable training. However, on HotPotQA and MuSiQue, GARL destabilizes during training. In contrast, PAFT at $q=0.75$ provides stable gradients, achieving the best overall performance on HotPotQA with a maj@16 score of 47.9, which represents a significant improvement of +14.4 over GRPO.

## Significance
This work is significant because it provides a theoretical and practical solution to the cold-start problem in reasoning model training, a major bottleneck in post-training alignment. By unifying RL and SFT under a single mathematical framework, it offers researchers a tunable continuum to balance exploration speed and gradient stability, leading to more robust and efficient training of large reasoning models.

## Related Concepts
- Reinforcement Learning from Verifiable Rewards (RLVR)
- Tsallis Entropy and Loss
- Cold-Start Problem in RL
- Gradient Amplification
- Importance Sampling
- Supervised Fine-Tuning (SFT)
- Reasoning Models
