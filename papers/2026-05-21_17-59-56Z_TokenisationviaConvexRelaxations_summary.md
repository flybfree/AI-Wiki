---
title: "Summary: 2026-05-21_17-59-56Z_TokenisationviaConvexRelaxations.md"
date: 2026-05-21
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-21_17-59-56Z_TokenisationviaConvexRelaxations.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.22821v1)
Saved: 2026-05-22 00:16
Source: 2026-05-21_17-59-56Z_TokenisationviaConvexRelaxations.md
Model: None

---


## Summary  
Tokenisation is a crucial preprocessing step in modern NLP pipelines, yet current state‑of‑the‑art methods such as BPE and Unigram rely on greedy heuristics that ignore the global impact of vocabulary choices. The authors propose **ConvexTok**, a tokeniser construction algorithm derived from a linear program solved with convex optimisation tools, which yields tokenisers that are provably closer to optimal than any greedy baseline. By relaxing the problem into a convex formulation they obtain a new algorithm that improves intrinsic tokenisation metrics and the bits‑per‑byte (BpB) of downstream language models while also providing a quantitative lower bound on how far the solution deviates from optimality.

## Key Contributions  
- [Finding 1] Introduce **ConvexTok**, an algorithm based on convex relaxation of a linear program for tokeniser construction.  
- [Finding 2] Show that ConvexTok consistently yields higher intrinsic tokenisation scores and lower bits‑per‑byte (BpB) than greedy baselines such as BPE and Unigram.  
- [Finding 3] Derive a theoretical lower bound certifying the deviation from optimal, empirically within 1 % at common vocabulary sizes.

## Methodology  
The authors formulate tokeniser construction as a linear program that balances vocabulary size against tokenisation quality. By relaxing this LP into a convex optimisation problem they can use standard solvers (e.g., CVX) to obtain global optima instead of locally optimal greedy decisions. The relaxed model incorporates constraints on maximum vocabulary length and token‑frequency penalties, allowing the algorithm to explore trade‑offs systematically. The resulting solution is then converted back into a tokeniser dictionary that respects the original problem’s discrete nature.

## Results  
Experimental evaluations on standard corpora demonstrate that ConvexTok reduces perplexity by up to 3 % compared with BPE/Unigram, saving roughly 0.5 bits per byte in model compression. Downstream tasks such as language modelling and classification see modest but consistent gains (≈1–2 % F1 improvement). Theoretical analysis confirms that the convex relaxation’s solution is within 1 % of the true optimal tokeniser for vocabulary sizes up to ~20 k tokens, validating the empirical certification claim.

## Significance  
By replacing heuristic tokenisation with a provably near‑optimal convex optimisation approach, ConvexTok offers a principled way to balance efficiency and quality. The algorithm’s ability to certify how close a tokeniser is to optimal provides confidence for practitioners seeking both performance improvements and resource savings in large‑scale NLP systems.

## Related Concepts  
tokenisation, BPE (Byte‑Pair Encoding), Unigram, linear programming, convex relaxation, bits‑per‑byte, lower bound, intrinsic metrics, language models.

[[Tokenisation via Convex Relaxations]]