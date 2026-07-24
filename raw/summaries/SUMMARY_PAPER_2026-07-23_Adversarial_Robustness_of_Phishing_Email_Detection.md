---
title: Adversarial Robustness of Phishing Email Detection: A Comparative Study of TF-IDF + Logistic Regression and Fine-Tuned DistilBERT
url: http://arxiv.org/abs/2607.18429v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_18-28-07Z_AdversarialRobustnessofPhishingEmailDetection_ACom.md
generated_at: 2026-07-23 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts a controlled pairwise comparison between a TF‑IDF plus logistic regression baseline and a fine‑tuned DistilBERT model for phishing email detection. Both classifiers achieve over 98 % accuracy on clean, in‑distribution test data but suffer comparable degradation when evaluated against deliberately adversarial emails, falling to roughly 64 % accuracy—a drop of about 35 percentage points.

## Key Takeaways
- Clean‑data performance does not predict adversarial robustness; both models experience a similar 35‑point accuracy loss under adversarial testing conditions.  
- Pairwise error analysis reveals that the two approaches share comparable numbers of exclusive errors (24 and 25 respectively), suggesting complementary rather than identical failure modes.  
- The adversarial test set is small (275 samples), yet the models’ gap is only 0.36 percentage points, indicating that their vulnerabilities are closely aligned.

## Context
Machine‑learning classifiers for cybersecurity often rely on clean, in‑distribution evaluation sets, which can mask weaknesses against real‑world attacks. This study underscores a growing need to assess model behavior under adversarial perturbations, especially as generative methods create more sophisticated phishing content.

## Implications
Practitioners should incorporate adversarial testing into their evaluation pipelines rather than treating clean accuracy as the sole metric of success. Model selection and training strategies must consider robustness to evasion attempts to ensure reliable protection against evolving threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18429v1)
