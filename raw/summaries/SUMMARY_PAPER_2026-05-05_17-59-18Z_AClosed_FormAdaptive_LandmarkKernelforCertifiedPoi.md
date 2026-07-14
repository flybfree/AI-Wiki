---

title: "Summary: A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification"
url: http://arxiv.org/abs/2605.04046v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md
generated_at: "2026-06-11 10:29"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-05 17-59-18Z Aclosed Formadaptive Landmarkkernelforcertifiedpoi


## Summary
This paper introduces PALACE, a closed‑form adaptive landmark kernel that improves point‑cloud and graph classification by adapting cover parameters without gradient training. The method provides four rigorous guarantees and achieves state‑of‑the‑art performance on benchmark datasets, matching or surpassing existing diagram‑based approaches.

## Key Takeaways
- A structural lower distortion bound λ(τ;ν) is derived from a Lebesgue‑number criterion, offering a (D/L)^2 budget reduction when diagrams concentrate.  
- Equal weights w_k = K^{-1/2} and farthest‑point sampling positions 2‑approximate the optimal k‑center covering radius, both computed solely from training labels.  
- The kernel‑RKHS classification rate O((k−1)√K/(γ√m_min)) is matched by a Le Cam lower bound, yielding a closed‑form filtration selection rule and strong empirical results on COX2, PTC, and DHFR.

## Context
The work advances the field of diagram‑based machine learning for point clouds and graphs, where kernel methods traditionally rely on fixed grids that degrade with domain inflation. By providing adaptive, data‑driven guarantees, PALACE addresses a longstanding challenge in non‑parametric classification.

## Implications
For practitioners, PALACE offers a reliable, calibrated classifier without the need for extensive cross‑validation or calibration splits, reducing computational overhead and improving robustness across diverse datasets. Its strong theoretical foundations make it suitable for deployment where interpretability and provable performance are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.04046v1)
