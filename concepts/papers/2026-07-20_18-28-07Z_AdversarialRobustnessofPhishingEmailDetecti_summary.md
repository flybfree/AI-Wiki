# Summary: 2026-07-20_18-28-07Z_AdversarialRobustnessofPhishingEmailDetection_ACom.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_18-28-07Z_AdversarialRobustnessofPhishingEmailDetection_ACom.md
Model: None

---

## Summary  
The paper aims to evaluate the adversarial robustness of two phishing‑email detection methods—a simple TF‑IDF + logistic regression baseline and a fine‑tuned DistilBERT classifier—by testing them on clean data and emails deliberately altered to evade detection. It contributes a controlled pairwise comparison that shows both models degrade similarly under adversarial conditions despite achieving >98 % accuracy on clean data, and it provides detailed error analysis revealing complementary failure modes.

## Key Contributions  
- **Finding 1:** Clean‑data accuracy does not guarantee robustness; both models drop to roughly 64 % on adversarial tests.  
- **Finding 2:** The two models exhibit nearly identical performance loss (35.40 pp) indicating similar vulnerability despite different architectures.  
- **Finding 3:** Pairwise error analysis shows 54.9 % agreement, with each model making roughly equal exclusive errors, suggesting complementary rather than identical failure patterns.

## Methodology  
The authors assembled a unified corpus of 82,255 emails from six public datasets and fine‑tuned DistilBERT on this data while constructing a TF‑IDF + logistic regression baseline. They evaluated the classifiers under three conditions: normal in‑distribution emails, synthetic phishing examples, and adversarial phishing generated with GAN‑based perturbations. Accuracy was measured across all sets to compare performance.

## Results  
Both models achieved >98 % accuracy on clean data; after adversarial testing TF‑IDF + LR fell to 64.00 % and DistilBERT to 63.64 %, a gap of only 0.36 percentage points (equivalent to one email in the 275‑sample adversarial set). LIME, SHAP, and attention‑rollout analyses indicate that each model relies on different evidence yet shows similar vulnerability.

## Significance  
This work demonstrates that phishing detection systems must be stress‑tested against adversarial inputs; high clean accuracy alone is insufficient. It underscores the need for robustness evaluation as a standard part of security AI development, helping practitioners prioritize defenses that survive real‑world evasion attempts.

## Related Concepts  
Adversarial attacks, classifier robustness, fine‑tuned transformers, TF‑IDF baseline, pairwise error analysis, LIME/SHAP interpretability, phishing detection.
