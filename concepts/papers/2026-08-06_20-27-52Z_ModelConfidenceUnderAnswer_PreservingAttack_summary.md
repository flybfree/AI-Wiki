# Summary: 2026-08-06_20-27-52Z_ModelConfidenceUnderAnswer_PreservingAttacks_AnInf.md
Saved: 2026-08-09 22:25
Source: 2026-08-06_20-27-52Z_ModelConfidenceUnderAnswer_PreservingAttacks_AnInf.md
Model: None

---

## Summary  
The paper investigates how model confidence behaves when adversarial attacks are limited to answer‑preserving perturbations that keep the generated text byte‑identical, probing the tension between an attacker’s ability to manipulate informativeness and a defender’s ability to preserve robustness. It demonstrates that even under strict constraints, confidence readouts can be systematically lowered or raised across multiple vision‑language models, benchmarks, and defense strategies, revealing a “frontier” where informativeness is more manipulable than raw accuracy. The study shows that uniform amplitude certificates do not guarantee adversarial discrimination, and that hidden‑state interventions can achieve comparable confidence shifts without altering the image. Finally, it argues that confidence serves as an integrity‑sensitive metric rather than an intrinsically robust oversight signal.

## Key Contributions  
- **Finding 1:** Answer‑preserving attacks can uniformly reduce or increase model confidence across all tested configurations, contradicting the assumption that a constant amplitude certificate suffices for discrimination.  
- **Finding 2:** The maximum feasible perturbation budget is lower than previously thought; a uniform amplitude certificate below a measurable threshold still yields adversarial discrimination above the answer‑string accuracy floor of 0.617.  
- **Finding 3:** Confidence manipulation can be achieved at the representation level (e.g., hidden‑state interventions) as well as through image perturbations, indicating that confidence is not solely an output‑level artifact.

## Methodology  
The authors adopt a white‑box, image‑only attack framework where each adversarial example must preserve the exact byte sequence of the model’s answer. They evaluate four vision‑language models on three visual question answering datasets, examine five deployed confidence channels, and apply two defense estimators (direct and surrogate). For every estimator‑cell combination they generate feasible perturbations and measure resulting confidence changes. Additionally, they conduct hidden‑state interventions and replicate activation spaces to isolate representation effects.

## Results  
Across 84 estimator‑by‑cell pairs, direct or surrogate attacks produce itemwise feasible perturbations that consistently lower confidence below the answer‑string accuracy floor of 0.617. Uniform amplitude certificates fail to prevent discrimination in all cases. Hidden‑state interventions achieve comparable confidence shifts without image changes. In a confidence‑gated simulation, a token‑probability attack transferred to a hidden‑state gate caused up to 84.8 % of previously rejected wrong answers to be accepted; reweighting by benchmark prevalence still yields accuracy below the no‑gate baseline in eight of twelve cells and all twelve under direct gating.

## Significance  
The findings reveal that confidence is an integrity‑sensitive metric vulnerable to answer‑preserving attacks, undermining its use as a reliable oversight signal. By exposing both image‑level and representation‑level manipulation pathways, the work highlights the need for defenses that protect not only model outputs but also internal representations when evaluating confidence.

## Related Concepts  
- Answer‑preserving adversarial attacks  
- Uniform amplitude certificates  
- Model confidence as an integrity metric  
- Hidden‑state interventions  
- Representation‑level manipulation  
- Answer‑string accuracy floor (0.617)
