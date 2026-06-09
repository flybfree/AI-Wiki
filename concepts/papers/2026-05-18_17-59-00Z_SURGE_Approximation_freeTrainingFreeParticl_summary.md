# Summary: 2026-05-18_17-59-00Z_SURGE_Approximation_freeTrainingFreeParticleFilter.md
Saved: 2026-05-19 01:03
Source: 2026-05-18_17-59-00Z_SURGE_Approximation_freeTrainingFreeParticleFilter.md
Model: None

---

## Summary
This paper introduces SURGE, a novel inference-time guidance algorithm designed to enhance the sample quality of diffusion-based generative models without requiring gradient computations or extensive computational overhead. The authors address the limitations of existing techniques that rely on repeated score or gradient evaluations, which often introduce bias and significant computational costs. By leveraging a derivative-free approach based on Girsanov change of measure, SURGE performs path-wise importance reweighting and periodic resampling of simulated trajectories. This method allows for unbiased terminal laws while maintaining simplicity and efficiency, offering a robust alternative to traditional gradient-based inference-time guidance methods.

## Key Contributions
- **Derivative-Free Guidance**: SURGE eliminates the need for score, Hessian, or PDE evaluations by using a simple multiplicative weight attached to each simulated trajectory, making it fully gradient-free.
- **Theoretical Equivalence**: The authors establish a rigorous mathematical equivalence between path-wise and particle-wise Sequential Monte Carlo (SMC), proving that Girsanov path weights recover previous particle-level weights via backward conditional expectation.
- **Empirical Superiority**: SURGE demonstrates superior performance on synthetic tests and diffusion-model benchmarks, achieving better generation quality with significantly lower implementation complexity compared to existing baselines.

## Methodology
The authors approach the problem by reformulating inference-time guidance as a path-wise importance reweighting problem using the Girsanov theorem. Instead of computing complex gradient-based particle weights, SURGE attaches a multiplicative weight to each simulated trajectory during the diffusion process. This weight is derived from a Girsanov change of measure, which adjusts the probability distribution of the paths without requiring explicit gradient information. The algorithm periodically resamples the particles to maintain diversity and prevent weight degeneracy. By ensuring that the Girsanov path weight admits a backward conditional expectation, the method guarantees that the resulting distribution matches the desired target law unbiasedly. This approach simplifies the implementation by avoiding the need for solving partial differential equations or computing high-order derivatives.

## Results
Empirical evaluations show that SURGE outperforms existing inference-time guidance baselines on both synthetic tests and standard diffusion-model benchmarks. The algorithm achieves higher generation quality metrics while being significantly simpler to implement. Theoretical results confirm that the path-wise reweighting scheme produces the same unbiased terminal law as previous particle-level weights, validating the correctness of the approach. The method demonstrates robustness across various tasks, highlighting its effectiveness in improving sample quality without the computational burden of gradient-based methods.

## Significance
This work is significant because it provides a practical, efficient, and theoretically sound alternative to gradient-based inference-time guidance. By removing the need for score and Hessian evaluations, SURGE reduces computational overhead and implementation complexity, making advanced guidance techniques more accessible. The theoretical equivalence established between path-wise and particle-wise SMC offers new insights into the mathematical foundations of diffusion model guidance, potentially influencing future research in this area.

## Related Concepts
- Diffusion Models
- Inference-Time Guidance
- Sequential Monte Carlo (SMC)
- Girsanov Theorem
- Importance Sampling
- Particle Filtering
- Path-wise Reweighting
- Gradient-Free Optimization

[[2026-05-18_17-59-00Z_SURGE_Approximation_freeTrainingFreeParticleFilter.md]]