# Summary: 2026-07-27_20-02-28Z_ScoreShield_DifferentiallyPrivateReleaseofSimilari.md
Saved: 2026-07-28 22:24
Source: 2026-07-27_20-02-28Z_ScoreShield_DifferentiallyPrivateReleaseofSimilari.md
Model: None

---

## Summary  
The paper tackles the problem of leaking information through similarity‑score releases, which is common in biometrics, RAG, and other retrieval systems that return cosine scores via APIs.  It introduces **ScoreShield**, a differential‑privacy mechanism that first adds calibrated Gaussian noise to the score vector (or Gram matrix) according to its global sensitivity and then projects the noisy result onto the feasible set of valid cosine objects.  The approach guarantees \((\varepsilon,\delta)\)-DP for both individual scores and their pairwise Gram matrices while preserving utility, achieving a risk bound improvement from \(\Theta(n^3)\) to \(\mathcal{O}(n^2)\).  

## Key Contributions  
- [Finding 1] ScoreShield provides \((\varepsilon,\delta)\)-DP guarantees for releasing similarity‑score vectors and Gram matrices.  
- [Finding 2] It employs a perturb‑then‑project mechanism: calibrated Gaussian noise is added to the score vector, then the result is projected onto the cosine feasibility set using an exact Frobenius metric projection.  
- [Finding 3] The exact‑projection bound reduces the squared Frobenius risk of pairwise Gram releases from \(\Theta(n^3)\) for naïve Gaussian baselines to \(\mathcal{O}(n^2)\) with fixed privacy parameters, and offers sharper local bounds at low‑rank Grams.  

## Methodology  
The authors model a similarity score release as a linear map applied to the embeddings of two records.  They compute the global sensitivity of this map, which determines the variance \(\sigma^2\) of Gaussian noise added uniformly across all entries.  After adding this noise, they perform an exact Frobenius‑metric projection onto the set \(\{G \in \mathbb{R}^{n\times n}: G = \cos(\theta_i,\theta_j),\; i,j\}\), which enforces that each entry corresponds to a valid cosine similarity between unit vectors.  For large‑scale Gram releases, they use an averaged alternating‑projection solver; theoretical analysis shows convergence to feasibility and provides utility guarantees for the projection step.  

## Results  
Theoretical analysis demonstrates that the risk bound improves from \(\Theta(n^3)\) to \(\mathcal{O}(n^2)\), meaning the privacy loss grows quadratically rather than cubically with the number of records.  Empirical experiments across RAG, face‑recognition, semantic retrieval, image similarity, and recommender‑system tasks show that ScoreShield retains high recall (within ~5 % of the baseline) while achieving \((\varepsilon,\delta)\)-DP for typical privacy budgets (\(\varepsilon = 1\) or \(0.1\)).  The exact‑projection bound is tight: the Frobenius distance between the noisy, projected Gram and the true cosine matrix is bounded by a constant independent of \(n\).  

## Significance  
ScoreShield enables large‑scale deployment of similarity‑score APIs in privacy‑sensitive domains without sacrificing utility.  By reducing the n‑dependence of privacy risk and preserving ranking quality, it mitigates membership‑inference attacks that could infer individual record membership from score releases.  This work bridges the practical gap between theoretical DP guarantees and real‑world performance, offering a template for other similarity‑based systems.  

## Related Concepts  
- Differential privacy (DP) – formal framework for quantifying information leakage.  
- Gaussian noise – standard additive perturbation used to achieve DP.  
- Frobenius metric projection – exact projection onto the cosine feasibility set.  
- Gram matrices – pairwise similarity representations of embeddings.  
- Cosine similarity – metric used in many retrieval and ranking tasks.  
- Membership inference attacks – attempts to deduce which records contributed a score.  
- Utility vs. privacy trade‑off – balancing accuracy with privacy constraints.
