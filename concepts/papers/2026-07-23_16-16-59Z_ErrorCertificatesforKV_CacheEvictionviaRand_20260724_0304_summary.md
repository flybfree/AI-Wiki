# Summary: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Saved: 2026-07-24 03:04
Source: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Model: None

---

## Summary  
The paper investigates the reliability of deterministic key‑value (KV) cache eviction in large language models and demonstrates that it cannot provide a consistent estimator of the true attention‑output error because evicted values can be altered without affecting the retained cache. By introducing a randomized design that incorporates a logit offset for Hájek correction, the authors construct an error certificate per step with 0.97 empirical coverage at no loss in model accuracy. Experiments on seven pre‑registered claims show that this approach yields near‑free question‑aware eviction at modest budgets and improves attribution over output confidence gating. The work thus bridges theory and practice by turning a sampling variance estimator into a provable error certificate.

## Key Contributions  
- [Finding 1] Deterministic KV‑cache eviction cannot guarantee that the serving system’s retained values remain unchanged while the true attention‑output error grows arbitrarily, breaking consistency of any estimator.  
- [Finding 2] A randomized eviction scheme with a single logit offset inside the softmax yields a Hájek‑corrected per‑step error certificate achieving 0.97 empirical coverage without affecting model accuracy.  
- [Finding 3] The certificate enables clear attribution between cache‑induced and inherent failures, improving scheduling decisions (AUC ≈ 0.74) compared with confidence gating (AUC ≈ 0.51).

## Methodology  
The authors adopt a Poisson‑sampled tail model where each token’s inclusion probability is known. They insert a logit offset into the softmax to apply Hájek correction, which adjusts the logits for the sampled tail. A variance estimator that surveys only the retained tokens provides an unbiased per‑step estimate of the error variance. This combination creates an error certificate: a bound on how much the true output can differ from what is served, derived directly from the sampling design.

## Results  
Theoretical analysis predicts 0.97 coverage for the certificate across many steps. In practice, seven pre‑registered claims were evaluated; three were lost, but question‑aware eviction at 25–50 % budgets incurred negligible cost. Output log‑probability predicted failures more accurately than the certificate alone, and gating budget escalation based on certificates added no benefit. The attribution metric showed AUC ≈ 0.74 for cache‑induced errors versus 0.48–0.54 for confidence‑based methods.

## Significance  
Provable error certificates transform a stochastic variance estimate into a reliable, per‑step guarantee that can be used to allocate resources efficiently and to distinguish between model bugs and data‑driven failures. This work offers a principled framework for improving the reliability of KV‑cache management in real‑time inference pipelines.

## Related Concepts  
- KV‑cache eviction (deterministic vs randomized)  
- Hájek correction in softmax  
- Logit offset for tail sampling  
- Error certificates and per‑step coverage  
- Attribution metrics (AUC)  
- Survey‑sampling variance estimator  
- Output log‑probability prediction
