# Summary: 2026-07-28_18-51-11Z_DynamicParameterizationIsNotDynamicInference.md
Saved: 2026-07-29 22:12
Source: 2026-07-28_18-51-11Z_DynamicParameterizationIsNotDynamicInference.md
Model: None

---

## Summary  
The paper challenges the common assumption that input‑dependent controller coefficients indicate “dynamic inference” or computational savings in large language models. It introduces a formal audit framework—Frozen‑Controller Auditing (FCA)—to separate three distinct phenomena: coefficient variation, functional dependence of a frozen model on those coefficients, and actual conditional execution. By caching the full coefficient tensor along an unperturbed trajectory and replaying the frozen model with cross‑input reassignment and token shuffling, the authors demonstrate that performance changes arise from content‑conditioned assignment rather than from recomputing controllers on perturbed hidden states. The study shows that static layerwise profiles retain almost all of the original correct‑to‑global‑mean performance gap, indicating functional reliance but no computational reduction.

## Key Contributions  
- [Finding 1] Frozen‑controller auditing reveals that coefficient variation does not imply dynamic inference; the model still executes every transformer block.  
- [Finding 2] Static layerwise profiles preserve ~98–99 % of the correct‑to‑global‑mean performance gap, showing strong functional dependence on coefficients without computational savings.  
- [Finding 3] Cross‑input reassignment and token shuffling increase negative log‑likelihood by 1.9067 and 2.9637 respectively, indicating that model behavior is highly sensitive to content‑conditioned coefficient assignment.

## Methodology  
The authors implement Frozen‑Controller Auditing (FCA). First, they capture the complete coefficient tensor for a fixed input trajectory before disabling the controller. Then, during inference, the frozen model is replayed with two interventions: cross‑input reassignment of coefficients and token shuffling. Static layerwise profiles are estimated from an independent calibration set to serve as benchmarks. Crucially, no new controller computation occurs on perturbed hidden states; performance differences are measured solely by replaying the cached model under these assignments.

## Results  
Across seven independently trained 76 M FeatureGate Transformers and three 504 M models, static layerwise profiles retain 98.70 % and 99.43 % of the original correct‑to‑global‑mean performance gap, respectively. Layer identity explains 87–96 % of coefficient variance. FCA execution is measured to be 30.8 % slower than a dense baseline that recomputes controllers on each block. On the public MUDDPythia‑1.4B checkpoint, cross‑input reassignment raises NLL by 1.9067 and token shuffling by 2.9637, confirming strong content‑conditioned dependency. Both model families execute every transformer block.

## Significance  
These findings debunk the conflation of dynamic parameterization with dynamic inference. Functional dynamics—evident in coefficient variation and layerwise profile preservation—do not translate into computational savings; the model still runs all blocks at full cost. The paper urges researchers to report three separate metrics: (1) whether coefficients vary, (2) how functionally the frozen model depends on those coefficients, and (3) actual inference time. This clarifies misinterpretations of “dynamic” models in large‑scale language systems.

## Related Concepts  
- Dynamic inference  
- Frozen controller auditing  
- Static layerwise profiles  
- Cross‑input reassignment  
- Token shuffling  
- Negative log‑likelihood penalty  
- FeatureGate Transformers
