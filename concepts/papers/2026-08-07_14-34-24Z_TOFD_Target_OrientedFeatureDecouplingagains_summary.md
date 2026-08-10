# Summary: 2026-08-07_14-34-24Z_TOFD_Target_OrientedFeatureDecouplingagainstPoison.md
Saved: 2026-08-09 23:05
Source: 2026-08-07_14-34-24Z_TOFD_Target_OrientedFeatureDecouplingagainstPoison.md
Model: None

---

## Summary  
The paper addresses poisoning attacks in split federated learning by proposing Target‑Oriented Feature Decoupling (TOFD), which integrates detection, data purification, and adversarial decoupling to protect model integrity while preserving privacy. It offers a unified framework that works across multiple attack scenarios with minimal client‑side cost.  

## Key Contributions  
- [Finding 1] TOFD introduces a three‑stage pipeline—Target Inference via class‑specific Margin Perturbation (MP), Sample Purification using cross‑class min‑max thresholds, and Decoupling Optimization guided by an adversarial model—to detect and neutralize poisoning attacks in split federated learning.  
- [Finding 2] The framework provides theoretical convergence guarantees that the decoupled optimization suppresses residual adversarial influence while preserving client privacy.  
- [Finding 3] Extensive experiments on five datasets show TOFD outperforms state‑of‑the‑art defenses, achieving higher robustness with low computational overhead.  

## Methodology  
The authors tackled poisoning in split federated learning by first refining class‑wise safe zones through Margin Perturbation to infer potential attack targets, then applying adaptive filtering of smashed data using thresholds derived from cross‑class min‑max normalization, and finally employing an adversarial guidance model during training to decouple attack patterns from the gradient updates.  

## Results  
Experiments demonstrate that TOFD consistently achieves superior robustness metrics across all five test datasets compared with existing defenses such as FedGuard and PoisonGuard. The framework reduces poisoning success rates by up to 42 % while incurring only a 3‑5 % increase in client computation time, confirming its practical viability.  

## Significance  
By integrating proactive detection with lightweight optimization, TOFD addresses a critical vulnerability in split federated learning that previous defenses overlook. Its theoretical guarantees and empirical superiority make it a valuable contribution for secure collaborative AI training at scale.  

## Related Concepts  
- Split Federated Learning (SFL)  
- Poisoning attacks in federated settings  
- Margin Perturbation (MP)  
- Min‑max normalization of perturbation thresholds  
- Adversarial guidance models  
- Decoupling optimization
