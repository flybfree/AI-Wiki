# Summary: 2026-07-23_14-37-30Z_Mean_to_ScoreDiscreteDiffusion_Posterior_MeanDenoi.md
Saved: 2026-07-24 03:03
Source: 2026-07-23_14-37-30Z_Mean_to_ScoreDiscreteDiffusion_Posterior_MeanDenoi.md
Model: None

---

## Summary  
Score Entropy Discrete Diffusion (SEDD) aims to generate discrete token sequences by denoising scores that encode posterior information, but its score‑entropy loss does not guarantee that the resulting score vectors are compatible with any valid clean‑token posterior. This leads to violations of the coordinate‑box constraint and can produce negative pre‑normalization weights in finite‑step sampling. The authors introduce **mean‑to‑score** (M2S), a denoiser that predicts a clean‑token posterior mean and maps it onto scores via an exact kernel‑dependent linear transform, thereby enforcing Bayes realizability. Their method resolves the score‑box problem while preserving the population optimum of the score‑entropy loss.

## Key Contributions  
- [Finding 1] SEDD’s score‑entropy loss has the correct population optimum but fails to enforce Bayes realizability away from it, causing roughly one quarter of complete score vectors to violate the coordinate box and more than half to be materially incompatible with any posterior.  
- [Finding 2] M2S predicts a clean‑token posterior mean and converts it to scores using an exact linear map that projects the probability simplex onto the bridge polytope; for uniform corruption this mapping is optimal, while absorbing‑mask corruption yields the MD4 objective exactly.  
- [Finding 3] Empirically, a 170 M‑parameter M2S model trained on ~262 B OpenWebText token slots outperforms pure‑uniform SEDD, GIDD, and Neural CTMC checkpoints at every sampling budget, achieving generative PPL = 143.3 (128 steps) versus 183.6 for the strongest baseline.

## Methodology  
The authors address the incoherence between posterior means and score vectors by constructing a **posterior‑mean denoiser** that is kernel‑dependent. For any coordinate‑wise continuous‑time Markov chain (CTMC) satisfying a mild support condition, they define an exact linear transformation that maps the clean‑token posterior mean to a score vector lying on the bridge polytope. This construction avoids heuristic projections and guarantees that all generated scores are jointly induced by some valid posterior under the forward kernel.

## Results  
In a controlled 28.4 M‑parameter CIFAR‑10 experiment, M2S lowers test BPD from **3.173** to **3.129** and improves FID‑50k from \(\CifarSEDDFID\) to \(\CifarMtwoSFID\). On the larger 170 M‑parameter checkpoint trained on OpenWebText, M2S consistently outperforms all evaluated checkpoints across sampling budgets; at 128 steps it reaches a generative PPL of **143.3**, compared with **183.6** for pure‑uniform SEDD.

## Significance  
By eliminating negative pre‑normalization weights and preserving the score‑entropy loss’s population optimum, M2S provides a theoretically sound denoiser that yields reliable generation without altering the underlying sampler. This resolves a fundamental limitation of existing discrete diffusion methods and opens the door to more robust generative models in token‑level tasks.

## Related Concepts  
Score Entropy Discrete Diffusion (SEDD), posterior‑mean denoisers, bridge polytope, coordinate box constraints, Bayes realizability, continuous‑time Markov chain (CTMC) with mild support condition, conditional score mapping, external generative PPL, MD4 objective.
