# Summary: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Saved: 2026-07-24 03:11
Source: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Model: None

---

## Summary  
The paper addresses the problem of estimating errors caused by deterministic key‑value (KV) cache eviction in transformer models, where the top‑k tokens are kept based on importance scores and the rest are discarded. It shows that this deterministic strategy cannot provide a reliable estimator of the true attention‑output error because evicted values can be altered without affecting the retained system state while inflating the observed error arbitrarily. The authors propose a randomized eviction scheme that restores identifiability, allowing the use of an error certificate derived from a Poisson‑sampled tail and a Hájek correction applied to the softmax logits. This certificate serves as a per‑step error bound with 0.97 empirical coverage at no additional computational cost.

## Key Contributions  
- [Finding 1] Deterministic KV‑cache eviction cannot produce a consistent estimator of attention‑output error because evicted values can be changed without altering the retained cache, leading to arbitrarily large observed errors.  
- [Finding 2] Randomized eviction with Poisson sampling and a logit offset yields an error certificate that has 0.97 empirical coverage at no accuracy penalty, providing a reliable per‑step bound.  
- [Finding 3] The certificate enables attribution of cache‑induced failures from inherent model errors, improving AUC to 0.73–0.75 compared with output confidence (0.47–0.54) and guiding better recomputation scheduling.

## Methodology  
The authors first formalize the deterministic eviction process as a loss of information about erased KV entries. They then introduce a randomized design where each token is kept independently with known inclusion probabilities, allowing the use of a Poisson‑sampled tail to approximate the true error distribution. A logit offset implements the Hájek correction inside the softmax, producing unbiased estimates of the retained attention scores. Finally, they compute a variance estimator over the retained set that serves as an error certificate, achieving the desired coverage.

## Results  
Theoretical analysis shows the certificate’s 0.97 empirical coverage with zero accuracy cost. In real workloads, seven pre‑registered claims were lost; three were due to question‑aware eviction at 25–50 % budgets, which incurred negligible overhead. Output log‑probability predicted failures better than the certificate, and budget escalation added no benefit. The certificate’s AUC for distinguishing cache‑induced from inherent failures is 0.73–0.75 versus 0.47–0.54 for confidence gating.

## Significance  
This work bridges a longstanding gap between deterministic performance guarantees and reliable error quantification in large language models, offering a practical tool that improves model debugging without sacrificing inference speed or accuracy.

## Related Concepts  
- KV‑cache eviction strategies (deterministic vs. randomized)  
- Error certificates and coverage bounds  
- Hájek correction for softmax logits  
- Poisson sampling in statistical estimation  
- Attribution of failure modes in neural networks
