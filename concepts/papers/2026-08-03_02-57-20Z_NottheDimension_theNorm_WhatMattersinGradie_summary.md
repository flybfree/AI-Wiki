# Summary: 2026-08-03_02-57-20Z_NottheDimension_theNorm_WhatMattersinGradient_Free.md
Saved: 2026-08-03 23:35
Source: 2026-08-03_02-57-20Z_NottheDimension_theNorm_WhatMattersinGradient_Free.md
Model: None

---

## Summary  
The paper investigates why gradient‑free weight perturbation methods for language models still modify every entry of the frozen model’s weight tensor instead of targeting a small, trainable subset. By systematically varying three factors—search dimension, subspace, and norm—while holding candidate scoring and voting constant, the authors isolate which property actually drives performance. Their experiments reveal that neither the number of perturbed dimensions nor the choice of perturbation basis matters; instead, the magnitude of the perturbation (its norm) is the decisive factor, with a narrow safe range that persists across model families and scales.

## Key Contributions  
- [Finding 1] The full‑weight search employed by existing gradient‑free methods is unnecessary; performance can be achieved by perturbing only a few scalars.  
- [Finding 2] Among the three controllable factors, the perturbation norm uniquely determines success, while dimension and subspace have negligible impact when the norm is matched.  
- [Finding 3] The usable range of effective norms collapses to within a factor of five across seven models, indicating a stable “safe region” that transfers regardless of scale or model architecture.

## Methodology  
The authors intervene on one factor at a time inside a fixed pipeline: they generate random weight perturbations, evaluate them with a static scoring and voting scheme, then vary the search dimension (number of perturbed entries), the subspace defined by a basis (e.g., SVD vs. random frame), and the norm (scale). By holding candidate scores and the voting mechanism constant, each factor is isolated to determine its causal effect on final accuracy.

## Results  
Across 49 model‑benchmark cells, perturbing only 12–16 scalars lags full‑weight search by about 1.8 points on average, trailing it in 36 of the cases. Crucially, a random frame with Grassmann overlap at chance level performs identically to the SVD frame once a single scale factor is matched, and at larger scales the SVD directions collapse first. The only consistent performance driver is the perturbation norm; its usable range narrows within a factor of five across seven models, while remaining flat inside that region.

## Significance  
Understanding that the *norm* rather than the *dimension* or *basis* governs gradient‑free adaptation simplifies design: practitioners can fix a modest norm and ignore unnecessary dimension choices. This insight reduces computational cost and memory usage, making parameter‑efficient adaptation more scalable across diverse model families.

## Related Concepts  
- Gradient‑free optimization (e.g., random search, evolutionary strategies)  
- Parameter‑efficient fine‑tuning of large language models  
- SVD basis selection for subspace perturbation  
- Grassmann overlap and random frame sampling  
- Safe region analysis in hyperparameter tuning
