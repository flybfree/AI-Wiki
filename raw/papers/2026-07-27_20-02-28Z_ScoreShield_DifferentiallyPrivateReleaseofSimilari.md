---
title: ScoreShield: Differentially Private Release of Similarity Scores
published: 2026-07-27T20:02:28Z
authors: Behrooz Razeghi, Parsa Rahimi
url: http://arxiv.org/abs/2607.25041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ScoreShield: Differentially Private Release of Similarity Scores

## Abstract
A growing number of applications, such as biometrics and retrieval-augmented generation (RAG), rely on cosine similarity scores computed between vector embeddings of text, images, or audio. These systems return similarity scores through their APIs for ranking and verification. However, such releases can leak information about individual records and enable membership inference attacks. While differential privacy (DP) provides a principled metric for quantifying attack risks, naïve application of DP mechanisms---such as adding i.i.d. Gaussian noise to vector entries---leads to excessive distortion (i.e., low utility) at a given privacy constraint that scales poorly with the number of released scores. We propose \textsc{ScoreShield}, a perturb-then-project mechanism that adds Gaussian noise calibrated to global sensitivity of the chosen score release regime and then projects the result onto the feasibility set of valid cosine objects. \textsc{ScoreShield} satisfies $(\varepsilon,δ)$-DP for releasing similarity score vectors and Gram matrices. We provide utility guarantees for the exact Frobenius metric projection used in the risk analysis, and prove convergence to feasibility for the practical averaged alternating-projection solver used for large-scale Gram releases. For full pairwise cosine Gram release under record-level replacement adjacency, the exact-projection bound improves the $n$-dependence of squared Frobenius risk from $Θ(n^3)$ for the naïve Gaussian baseline to $\mathcal{O}(n^2)$ for fixed privacy parameters, with sharper local bounds at low-rank Grams. We evaluate the mechanism across RAG, face recognition, semantic retrieval, image similarity, and recommender-system tasks.

## Metadata
- **Published**: 2026-07-27T20:02:28Z
- **Authors**: Behrooz Razeghi, Parsa Rahimi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25041v1)