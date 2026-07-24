# Summary: 2026-07-22_16-58-45Z_Variance_reducedDomainAdaptationusingPairedSamplin.md
Saved: 2026-07-24 02:08
Source: 2026-07-22_16-58-45Z_Variance_reducedDomainAdaptationusingPairedSamplin.md
Model: None

---

## Summary  
The paper addresses high variance in existing unsupervised domain adaptation (UDA) losses such as correlation alignment and maximum mean discrepancy, which hinder minibatch optimisation. It introduces Paired Sampling for Domain Adaptation (PSDA), a stochastic variance reduction technique that pairs observations within and across domains to form quadruplets sampled together. By minimizing expected gradient variance through linear assignment problems, PSDA offers a finite‑sum structure compatible with classical stochastic variance reduction (SVR) methods. Experiments on three domain shift datasets show improved target accuracy.

## Key Contributions  
- Finding 1: High variance in correlation alignment and MMD losses undermines minibatch optimisation.  
- Finding 2: These losses lack finite‑sum structure, making them incompatible with stochastic variance reduction (SVR).  
- Finding 3: PSDA provides a finite‑sum structured loss that pairs intra‑ and inter‑domain observations into quadruplets.

## Methodology  
The authors propose Paired Sampling for Domain Adaptation (PSDA), which constructs quadruplets by pairing two observations from the source domain with two from the target domain. The pairings are optimized to minimise expected gradient variance, reducing to solving linear assignment problems that match source‑target pairs and intra‑domain pairs. During training, each quadruplet is processed as a single minibatch, ensuring finite‑sum loss accumulation and enabling SVR techniques.

## Results  
Simulations show reduced variance compared with baseline UDA methods. On three benchmark datasets (e.g., CUB200, CUB100, and a synthetic domain shift), PSDA achieves higher target accuracy than correlation alignment and MMD approaches, with lower gradient variance measured via Monte‑Carlo estimates.

## Significance  
By introducing a finite‑sum structured loss that explicitly pairs observations across domains, PSDA alleviates high variance in existing UDA frameworks, enabling more stable and effective minibatch optimisation. This contributes to practical deployment of unsupervised domain adaptation where computational efficiency is crucial.

## Related Concepts  
- Unsupervised Domain Adaptation (UDA)  
- Correlation alignment loss  
- Maximum Mean Discrepancy (MMD) loss  
- Stochastic Variance Reduction (SVR)  
- Finite‑sum structure in losses
