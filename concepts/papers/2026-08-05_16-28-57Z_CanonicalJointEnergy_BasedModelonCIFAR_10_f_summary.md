# Summary: 2026-08-05_16-28-57Z_CanonicalJointEnergy_BasedModelonCIFAR_10_failurem.md
Saved: 2026-08-05 22:32
Source: 2026-08-05_16-28-57Z_CanonicalJointEnergy_BasedModelonCIFAR_10_failurem.md
Model: None

---

## Summary  
The paper investigates canonical joint energy‑based models (JEM) on the CIFAR‑10 benchmark, comparing two stochastic samplers—Predictor‑Corrector (PC) and Stochastic Gradient Langevin Dynamics (SGLD)—to determine whether PC retains its theoretical advantage without an annealed noise schedule. The authors report that both methods achieve near‑identical reconstruction accuracy, FID scores, and out‑of‑distribution (OOD) detection performance across training, cold‑start generation, and refinement‑style OOD protocols.

## Key Contributions  
- The authors empirically demonstrate that Predictor‑Corrector and SGLD produce practically indistinguishable outputs on canonical JEM trained with WideResNet‑28‑10.  
- They identify two failure modes: catastrophic late‑training divergence via the outlier‑buffer mechanism and run‑dependent SVHN OOD discrimination, which affect both samplers similarly.  
- The study shows no systematic method‑level advantage of PC over SGLD in any evaluation protocol; differences are within experimental noise.

## Methodology  
The authors reproduce canonical JEM training on two independent runs using WideResNet‑28‑10 without normalization layers. They evaluate three protocols: (i) replacing SGLD with PC throughout the roughly 130 epochs of training, (ii) cold‑start generation measured by FID, and (iii) refinement‑style multi‑OOD detection via AUROC. Failure modes are examined using the canonical outlier‑buffer mechanism and SVHN OOD dynamics.

## Results  
Reconstruction accuracy reaches 92.88 % test accuracy; buffer‑FID is 44.46 (canonical: 92.9 %, 38.40). AUROC differences are below 0.007 across ten checkpoint‑OOD pairs and FID difference <0.5. A hierarchical bootstrap gives a 95 % confidence interval on the macro‑averaged AUROC that contains zero; seed‑level equivalence test cannot establish formal equivalence.

## Significance  
The paper shows that theoretical guarantees of PC do not translate to practical performance in canonical JEM, highlighting the importance of noise schedule and that both samplers are equally effective for reconstruction and OOD detection under fixed noise. This finding informs practitioners about the robustness of sampler choice when practical indistinguishability is the goal.

## Related Concepts  
Joint Energy‑Based Models (JEM), Predictor‑Corrector sampler, Stochastic Gradient Langevin Dynamics (SGLD), canonical outlier‑buffer mechanism, FID, AUROC, OOD detection, WideResNet‑28‑10.
