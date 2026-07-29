---
title: ScoreShield: Differentially Private Release of Similarity Scores
url: http://arxiv.org/abs/2607.25041v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_20-02-28Z_ScoreShield_DifferentiallyPrivateReleaseofSimilari.md
generated_at: 2026-07-28 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ScoreShield, a differentially private mechanism for releasing cosine similarity scores and Gram matrices. It adds calibrated Gaussian noise based on global sensitivity and then projects the noisy vectors onto the feasible set of valid cosine objects. The approach achieves (ε,δ)-DP while improving utility compared to naïve Gaussian perturbation.

## Key Takeaways
- ScoreShield uses a perturb‑then‑project method that respects differential privacy by calibrating Gaussian noise to the global sensitivity of the score release regime.  
- The exact Frobenius metric projection provides utility guarantees and converges to feasibility for large Gram releases, reducing risk from Θ(n³) to O(n²).  
- Local bounds improve at low‑rank Grams, offering sharper privacy‑utility trade‑offs.

## Context
AI systems increasingly rely on similarity scores for tasks such as retrieval and recommendation. Traditional release of these scores can expose individual records, enabling membership inference attacks. Differential privacy offers a formal way to limit this risk but often at the cost of high distortion that degrades performance.

## Implications
ScoreShield enables practitioners to deploy similarity APIs safely without sacrificing much ranking accuracy. This balances privacy requirements with practical utility, supporting broader adoption in biometrics and RAG applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25041v1)
