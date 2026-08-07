# Summary: 2026-08-06_07-14-58Z_ConsistencyHasaComputableBlindSpot_ACommutationThe.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_07-14-58Z_ConsistencyHasaComputableBlindSpot_ACommutationThe.md
Model: None

---

## Summary  
This paper introduces a commutation‑based theory that explains the systematic blind spot in label‑free reliability for vision‑language figure reading. It shows that an error is invisible to a perturbation exactly when two edits **commute**, meaning it belongs to the joint centralizer of all possible edits, a set that can be computed rather than guessed. The authors complement this by defining a computable equivariance condition: after an edit the correct answer must change in a predictable way. By pairing these invariance and equivariance sets they create the Equivariance‑Consistency Score (ECS), a training‑free detector that ranks which blind spot is larger. The framework predicts measurable gains on matched data, confirming the blind spot’s existence across three models and a human sample immune to circularity.

## Key Contributions  
- [Finding 1] A computable “blind spot” for label‑free reliability is identified as the joint centralizer of commuting edits, which shrinks when more edits are added.  
- [Finding 2] Matched edit pairs provide a complete characterization of affine reading errors; no swap‑only suite can achieve this completeness, and cyclic relabeling closes most of the gap for label permutations.  
- [Finding 3] The Equivariance‑Consistency Score (ECS) is released as REND‑EQUIV, delivering a training‑free ranking that aligns with hand‑labeled data and predicts gains on real samples.

## Methodology  
The authors treat reliability as the intersection of two algebraic relations: invariance (answers unchanged under perturbations) and equivariance (answers change by a computable amount). They compute the centralizer of all commuting edit pairs, which forms the set of invisible errors. Simultaneously they generate matched edit suites that satisfy an affine reading error condition, establishing a complete equivariance set for those edits. The ECS is derived as the ratio or overlap of these two sets, producing a scalar score without any training data.

## Results  
Experiments on three vision‑language models and a human‑annotated dataset show that the ECS correctly orders the magnitude of blind spots predicted by the commutation theory. A second method—testing invariance families—confirms that the blind spot is intrinsic to the relation, not implementation noise. Cyclic relabeling experiments demonstrate the predicted gain on matched real data, and the framework explains an observed inversion in classifier‑metamorphic testing literature: detectability depends jointly on the edit relation and the fault class.

## Significance  
This work provides a theoretical foundation for label‑free reliability that bridges invariance and equivariance, turning a previously mysterious blind spot into a computable quantity. By offering REND‑EQUIV, it enables systematic comparison of models without labels or training, advancing both theory and practice in vision‑language systems.

## Related Concepts  
commutation, centralizer, invariant set, equivariance, joint property, fault class, classifier metamorphic testing, label‑free reliability, affine reading errors, cyclic relabeling.
