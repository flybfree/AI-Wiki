# Summary: 2026-07-23_14-37-30Z_Mean_to_ScoreDiscreteDiffusion_Posterior_MeanDenoi.md
Saved: 2026-07-24 02:47
Source: 2026-07-23_14-37-30Z_Mean_to_ScoreDiscreteDiffusion_Posterior_MeanDenoi.md
Model: None

---

## Summary  
The paper addresses a fundamental flaw in existing discrete diffusion models that rely on score‑entropy loss: the generated scores can violate Bayes realizability, producing negative pre‑normalization weights and degrading external generative performance. To remedy this, the authors introduce **Mean‑to‑Score Discrete Diffusion (M2S)**, a posterior‑mean denoiser that projects raw scores onto the bridge polytope, guaranteeing non‑negative probabilities at every step. M2S maps the probability simplex to the bridge polytope for uniform corruption and recovers MD4 for absorbing‑mask corruption, while preserving the original CTMC structure. The method is applied to large‑scale CIFAR‑10 and OpenWebText experiments, achieving superior perplexity and fidelity compared with prior checkpoints.

## Key Contributions  
- [Finding 1] **Bridge polytope projection** eliminates negative pre‑normalization weights by mapping scores onto a feasible set that preserves Bayes realizability.  
- [Finding 2] A **kernel‑dependent linear map** from posterior means to scores works for any coordinate‑wise CTMC satisfying mild support conditions, enabling universal application across diffusion models.  
- [Finding 3] M2S **outperforms existing pure‑uniform SEDD, GIDD, and Neural CTMC checkpoints** on both CIFAR‑10 (BPD = 3.129) and OpenWebText (PPL = 143.3 at 128 steps), delivering higher external generative PPL without altering the sampler.

## Methodology  
The authors first analyze why score‑entropy loss alone cannot enforce positivity away from its optimum, noting that raw scores may lie outside the bridge polytope. They then construct M2S by training a denoiser to predict the clean‑token posterior mean and applying an exact linear transformation derived from the forward kernel’s score mapping. This projection is conditioned on the current noisy state, ensuring that each step’s score vector remains inside the polytope. The method is evaluated for two corruption regimes—uniform token masking and absorbing‑mask—where it recovers MD4 exactly, confirming its theoretical robustness.

## Results  
In a controlled 28.4 M‑parameter CIFAR‑10 benchmark, M2S reduces test BPD from 3.173 to 3.129 and improves FID‑50k from \(\CifarSEDDFID\) to \(\CifarMtwoSFID\). On the larger OpenWebText dataset (≈ 262 B token slots), M2S achieves a generative PPL of 143.3 at 128 steps, surpassing pure‑uniform SEDD (183.6) and Neural CTMC checkpoints across all sampling budgets.

## Significance  
By guaranteeing Bayes realizability through bridge polytope projection, M2S resolves a critical limitation of score‑based diffusion models, leading to more reliable negative pre‑normalization weights and higher external generative performance. The method’s universality across CTMCs makes it a scalable upgrade for existing diffusion pipelines.

## Related Concepts  
- Score Entropy Discrete Diffusion (SEDD)  
- Bridge polytope  
- Posterior‑mean denoiser  
- Continuous‑time Markov chain (CTMC)  
- MD4 (Mean‑Discrete‑4)
