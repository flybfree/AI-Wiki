# Summary: 2026-07-20_18-28-07Z_AdversarialRobustnessofPhishingEmailDetection_ACom.md
Saved: 2026-07-24 00:34
Source: 2026-07-20_18-28-07Z_AdversarialRobustnessofPhishingEmailDetection_ACom.md
Model: None

---

## Summary  
The paper aims to evaluate the adversarial robustness of two phishing email detection models: a traditional TF‑IDF + Logistic Regression baseline and a fine‑tuned DistilBERT transformer. It conducts a controlled pairwise comparison on three conditions—normal in‑distribution, synthetic phishing, and adversarial phishing—to reveal how each model degrades under malicious manipulation. The study demonstrates that clean‑data performance does not guarantee resilience, highlighting the need for rigorous adversarial testing.

## Key Contributions  
- [Finding 1] Both models achieve >98 % accuracy on clean test data but drop to ~64 % accuracy when faced with adversarially altered emails, indicating a severe degradation.  
- [Finding 2] The performance gap between the two approaches narrows to only 0.36 percentage points under adversarial conditions, suggesting complementary rather than identical failure modes.  
- [Finding 3] Pairwise error analysis shows the models agree on 54.9 % of adversarial samples while each makes roughly equal numbers of exclusive errors (24 and 25), indicating partial complementarity.

## Methodology  
The authors assembled a unified dataset of 82,255 emails from six public sources, fine‑tuned DistilBERT on this corpus, and used TF‑IDF + Logistic Regression as the baseline. They generated adversarial examples by applying common evasion techniques (e.g., synonym replacement) to both clean and phishing messages, then evaluated each model under three test conditions: normal in‑distribution emails, synthetically altered phishing emails, and fully adversarial emails.

## Results  
On clean data, TF‑IDF + LR achieved 98.12 % accuracy while DistilBERT reached 98.45%. Under synthetic phishing, both models maintained >97 % accuracy. In the adversarial test set (275 samples), TF‑IDF + LR fell to 64.00 % and DistilBERT to 63.64%, a drop of ~35 percentage points each. Pairwise agreement was 54.9 %, with exclusive errors roughly balanced at 24–25 per model.

## Significance  
These findings underscore that high clean‑data accuracy is misleading for security applications and that adversarial testing must be standard practice. The nearly equal degradation of both models reveals a systemic vulnerability in current phishing detection pipelines, prompting researchers to prioritize robustness over raw performance metrics.

## Related Concepts  
- Adversarial attacks on NLP classifiers  
- TF‑IDF + Logistic Regression baseline  
- Fine‑tuned DistilBERT transformer  
- Pairwise error analysis  
- LIME and SHAP interpretability tools  
- Attention rollout for model probing
