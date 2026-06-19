---

title: "Summary: Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach"
url: http://arxiv.org/abs/2605.13830v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_17-52-19Z_QuantifyingSensitivityforTreeEnsembles_Asymbolican.md
generated_at: "2026-06-11 10:40"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces XCount, a method for quantifying sensitivity of tree ensembles by discretizing the input space and enumerating vulnerable regions using an algebraic decision diagram. It claims to compute a quantitative notion with certified error and confidence bounds efficiently. Experiments show speedup over model counters on benchmarks with varying tree size and depth.

## Key Takeaways
- The algorithm encodes the sensitivity problem as an ADD enabling compositional solution.
- It provides a certified error bound guaranteeing correctness of computed sensitive region count.
- XCount achieves significant speedup compared to existing model counter approaches on benchmarks with varying tree size and depth.

## Context
Decision tree ensembles are widely used in safety‑critical AI, yet their sensitivity—how small feature changes cause misclassification—remains hard to measure. Accurate quantification is essential for robustness analysis.

## Implications
This work offers a scalable tool that can be integrated into verification pipelines, enabling faster detection of sensitive features and supporting trustworthy model deployment across industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13830v1)
