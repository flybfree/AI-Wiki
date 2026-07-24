# Summary: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
Model: None

---

## Summary  
The paper addresses deterministic KV‑cache eviction in large language models, showing that this design cannot produce consistent serving‑time estimators because evicted values can be altered to hide the true attention error. It proposes a randomized tail‑sampling scheme with a logit offset and a variance estimator that yields per‑step error certificates at 0.97 empirical coverage without any accuracy loss. Randomization restores identifiability of cache‑induced errors, turning a theoretical impossibility into a practical tool.

## Key Contributions  
- [Finding 1] Deterministic KV‑cache eviction cannot produce consistent serving‑time estimators because evicted values can be altered to hide the true attention error.  
- [Finding 2] A randomized tail sampling with a logit offset yields Hájek‑corrected softmax, providing per‑step error certificates with 0.97 empirical coverage at no accuracy cost.  
- [Finding 3] Error certificates enable attribution of failures between cache‑induced and inherent errors, improving AUC and guiding recomputation.

## Methodology  
The authors analyze the deterministic eviction scheme by constructing adversarial scenarios where deleted tokens are replaced to preserve output while increasing true attention error. They then design a randomized sampling process: each token is included independently with known inclusion probability; a logit offset is applied inside the softmax to achieve Hájek correction; and a variance estimator over retained samples yields a per‑step certificate. The method avoids recomputation of full attention, instead using marginal statistics.

## Results  
Theoretical analysis shows that the randomized design eliminates the inconsistency between eviction and error estimation, achieving 0.97 coverage for the error certificates. Empirically on seven pre‑registered claims across real workloads, three were lost (question‑aware eviction at 25–50% budgets is nearly free). The certificate gated budget escalation adds no benefit; output log‑probability predicts failure better than the certificate, but the certificate provides superior attribution with AUC 0.73–0.75 versus confidence gating’s 0.47–0.54.

## Significance  
This research demonstrates that randomized design can restore identifiability in cache management, turning a theoretical impossibility into a practical tool. By providing unbiased error certificates, it enables better fault analysis and resource allocation without sacrificing model performance, which is crucial for scalable LLM deployment.

## Related Concepts  
- KV‑cache eviction strategies  
- Hájek correction for softmax  
- Randomized tail sampling  
- Error certificates in statistics  
- Attribution of failure modes
