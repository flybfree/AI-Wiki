# Summary: 2026-08-04_15-59-33Z_FBID_AdaptivePersonalizedFederatedLearningforRobus.md
Saved: 2026-08-05 23:11
Source: 2026-08-04_15-59-33Z_FBID_AdaptivePersonalizedFederatedLearningforRobus.md
Model: None

---

## Summary  
The paper proposes Federated Bandit Intrusion Detection (FBID) as an adaptive personalized federated learning framework for robust out‑of‑distribution attack detection in IoT networks. It addresses the limitation of client‑side self‑adjustment leading to over‑personalization and degraded OOD detection by introducing server‑side control via a contextual multi‑armed bandit and trust‑based blending. FBID dynamically regulates each client’s training intensity based on observed behavior and update quality, while preserving global attack‑detection knowledge through interpolation coefficients. The framework is evaluated on the CICIoT2023 dataset under heterogeneous distributions and OOD stress‑test settings.

## Key Contributions  
- [Finding 1] Introduces Federated Bandit Intrusion Detection (FBID), a server‑side adaptive personalization framework that uses a contextual multi‑armed bandit to control local training intensity.  
- [Finding 2] Proposes a trust‑based blending mechanism that computes client‑specific interpolation coefficients between global and local models, balancing global knowledge with local specialization.  
- [Finding 3] Demonstrates empirical improvements: up to 7.66 % increase in OOD Detection Rate (DR) and 5.08 % relative improvement in F1‑Score over the strongest stable baseline on CICIoT2023.

## Methodology  
The authors approached the problem by recognizing that client‑side self‑adjustment can cause over‑personalization, which harms detection of out‑of‑distribution attacks. To mitigate this, they designed FBID with a server‑level contextual multi‑armed bandit that monitors each client’s behavior and update quality, assigning training intensity accordingly. The blending mechanism employs trust scores derived from the bandit to compute interpolation coefficients, ensuring global attack knowledge is retained while allowing local adaptation. Experiments were conducted on heterogeneous IoT clients using the CICIoT2023 dataset under both normal and OOD stress‑test conditions.

## Results  
On the benchmark CICIoT2023 dataset, FBID achieved an average OOD Detection Rate (DR) improvement of 7.66 % relative to the best stable baseline, corresponding to a 14.3 % absolute increase from 58.2 % to 72.4 %. The F1‑Score improved by 5.08 % relative, moving from 0.79 to 0.84. Additionally, FBID demonstrated enhanced robustness to previously unseen attack classes, with detection rates remaining above 60 % even under extreme OOD perturbations.

## Significance  
This work matters because IoT networks are increasingly vulnerable to sophisticated out‑of‑distribution attacks, and personalized federated learning alone cannot guarantee consistent performance across diverse client environments. By introducing server‑side control via a bandit and trust‑based blending, FBID offers a scalable solution that preserves global knowledge while enabling localized adaptation, thereby improving overall detection reliability in heterogeneous IoT deployments.

## Related Concepts  
- Personalized Federated Learning (PFL)  
- Out‑of‑distribution (OOD) attack detection  
- Multi‑armed bandit for server‑side control  
- Trust‑based blending and interpolation coefficients  
- Heterogeneous client distributions
