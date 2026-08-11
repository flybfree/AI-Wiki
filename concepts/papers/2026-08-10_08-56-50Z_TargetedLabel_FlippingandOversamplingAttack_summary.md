# Summary: 2026-08-10_08-56-50Z_TargetedLabel_FlippingandOversamplingAttacksonFede.md
Saved: 2026-08-10 23:43
Source: 2026-08-10_08-56-50Z_TargetedLabel_FlippingandOversamplingAttacksonFede.md
Model: None

---

## Summary  
The paper investigates adversarial attacks on federated conditional GAN (FCG) systems, focusing on label‑flipping and oversampling attacks that manipulate local training to corrupt the global generator. It proposes theoretical analysis and empirical evaluation showing how these attacks can shift class distributions and cause semantic damage. The authors quantify impact via Kullback‑Leibler divergence and demonstrate linear vs quadratic growth of effects. This work advances understanding of robustness in federated GANs.  

## Key Contributions  
- [Finding 1] Label‑flipping attacks can systematically redirect generated samples from a target label to a source class, causing distributional shift.  
- [Finding 2] Oversampling attacks amplify poisoning by upweighting poisoned samples, increasing influence on the global model.  
- [Finding 3] The semantic damage grows linearly with poisoning strength while detection remains quadratic, making attacks effective yet subtle.  

## Methodology  
The authors conduct theoretical analysis deriving Kullback‑Leibler divergence between clean and poisoned conditional distributions. They implement both label‑flipping and oversampling variants in federated GAN frameworks using FEMNIST, MNIST, CIFAR10 benchmarks. Experiments compare attack strength against detection metrics such as label‑agnostic reconstruction error and distribution similarity scores.  

## Results  
Theoretical analysis shows linear semantic damage versus quadratic deviation from the true target distribution. Empirical results confirm these trends across three datasets, with average Kullback‑Leibler divergence increase of 2.3 bits per poisoning level. Attacks succeed even when label‑agnostic metrics are used, highlighting a hidden vulnerability in current defenses.  

## Significance  
Understanding these attacks is crucial for securing federated learning pipelines where GANs generate sensitive data. The linear‑quadratic gap highlights a vulnerability that many existing safeguards may miss, prompting the need for robust training protocols and detection mechanisms to protect both privacy and model integrity.  

## Related Concepts  
- Federated Learning  
- Conditional Generative Adversarial Networks (FCG)  
- Label Flipping Attacks  
- Oversampling Attacks  
- Kullback‑Leibler Divergence  
- Distributional Shift  
- Semantic Damage  
- Attack Detection Metrics
