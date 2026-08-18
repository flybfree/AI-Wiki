---
title: Picking the Right Image to Classify: Reliable-Input Selection in Teledermatology
url: http://arxiv.org/abs/2608.16198v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_07-28-26Z_PickingtheRightImagetoClassify_Reliable_InputSelec.md
generated_at: 2026-08-17 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces reliable‑input selection, a task of choosing the image that a dermatology model is most likely to classify correctly when faced with distribution shifts in teledermatology. The authors demonstrate that an oracle selecting such images can raise weighted F1 by about 20 percentage points across multiple datasets and backbones. Their study shows that training‑data‑free selectors, which rely only on inference outputs like embeddings or confidence, fail to close the gap with this oracle.

## Key Takeaways
- The oracle gap is substantial: reliable‑input selection can improve performance by roughly 20 percentage points on average across six dermatology datasets and nine frozen backbones.  
- All four benchmarked training‑data‑free selectors—embedding norm, neighborhood consensus, prediction stability under perturbations, and model confidence—recover only a small portion of the oracle’s gain.  
- Even when a small labeled reference set is available, the best fusion selector (confidence plus Mahalanobis distance) still leaves most of the gap unfilled.

## Context
Teledermatology relies on models trained on static datasets that may not reflect real‑world clinical photographs, leading to performance drops. Input selection offers a way to mitigate this without retraining or accessing additional data, which is valuable for deployment in resource‑constrained settings.

## Implications
Practitioners can use confidence scores as a simple proxy for reliable input, though they will see limited improvement. The paper underscores that current methods cannot fully close the oracle gap, suggesting future work on more sophisticated selection strategies or hybrid approaches may be needed to maximize teledermatology accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16198v1)
