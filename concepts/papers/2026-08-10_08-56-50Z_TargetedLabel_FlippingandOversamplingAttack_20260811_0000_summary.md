# Summary: 2026-08-10_08-56-50Z_TargetedLabel_FlippingandOversamplingAttacksonFede.md
Saved: 2026-08-11 00:00
Source: 2026-08-10_08-56-50Z_TargetedLabel_FlippingandOversamplingAttacksonFede.md
Model: None

---

## Summary  
The paper investigates how malicious clients can compromise federated conditional GANs by either flipping labels or up‑weighting poisoned samples during local training, thereby biasing the global generator toward a source class instead of the intended target. By combining theoretical analysis with experiments on FEMNIST, MNIST and CIFAR10, it shows that semantic damage grows linearly with poisoning strength while deviation from the true distribution grows only quadratically, making the attack effective yet hard to detect without label‑aware metrics.  

## Key Contributions  
- [Finding 1] Theoretical analysis shows label‑flipping attacks cause a distributional shift measured by Kullback‑Leibler divergence between clean and poisoned class conditional GANs, with semantic damage scaling linearly with effective poisoning strength.  
- [Finding 2] Empirical experiments on FEMNIST, MNIST, CIFAR10 demonstrate that the attack’s effectiveness grows quadratically in deviation from the true target distribution, making it difficult to detect via label‑agnostic metrics.  
- [Finding 3] The oversampling variant amplifies poisoned samples during local training, leading to a stronger global generator bias and increased Kullback‑Leibler divergence.  

## Methodology  
The authors adopt a federated GAN framework where each client trains locally on its own data. Malicious clients either flip labels or upweight specific classes, causing poisoning. The global generator is updated via federated averaging of local generators. To quantify impact, they compute Kullback‑Leibler divergence between the clean and poisoned class conditional distributions, providing a quantitative measure of distributional shift.  

## Results  
Theoretical analysis predicts a linear increase in KL divergence with poisoning strength while a quadratic increase in deviation from the target distribution. Empirically, on FEMNIST, MNIST and CIFAR10, the attack consistently produces higher generator bias and measurable KL divergence; however, label‑agnostic metrics show only modest changes, confirming that the attack is effective yet hard to detect without label‑aware evaluation.  

## Significance  
This work highlights a critical vulnerability in federated GAN training where adversarial manipulation can degrade model performance without obvious label inconsistencies. By quantifying distortion using KL divergence, it provides a benchmark for detecting poisoning attacks and guides defensive strategies that rely on distribution‑based monitoring rather than simple label checks.  

## Related Concepts  
- Federated learning  
- Conditional Generative Adversarial Networks (GANs)  
- Label flipping / poisoning attacks  
- Kullback‑Leibler divergence as a metric of distributional shift  
- Oversampling in adversarial training
