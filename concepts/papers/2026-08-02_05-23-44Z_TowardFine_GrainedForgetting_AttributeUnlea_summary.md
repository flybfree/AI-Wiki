# Summary: 2026-08-02_05-23-44Z_TowardFine_GrainedForgetting_AttributeUnlearningfo.md
Saved: 2026-08-03 20:37
Source: 2026-08-02_05-23-44Z_TowardFine_GrainedForgetting_AttributeUnlearningfo.md
Model: None

---

## Summary  
Multimodal large language models (MLLMs) excel at vision‑language tasks but can inadvertently memorize and disclose sensitive attributes, raising privacy concerns. This paper tackles the need for **fine‑grained forgetting**, i.e., removing a specific attribute of an identity while preserving all other information about that same individual. To address this, the authors introduce a new benchmark and a training‑free method called Causal Localization and Retain‑Aware Projection (CLRP) that isolates the causal layer responsible for target disclosure and applies a projection that eliminates only the unwanted subspace.

## Key Contributions  
- [Finding 1] Existing MLLM unlearning benchmarks focus on profile‑level deletion, whereas real‑world requests often require **attribute‑level** forgetting.  
- [Finding 2] The target attribute and retained attributes frequently share identity‑specific visual evidence, causing residual leakage or collateral performance degradation in selective forgetting.  
- [Finding 3] CLRP achieves **stable forgetting** with minimal impact on overall model utility across diverse forget ratios.

## Methodology  
The authors construct a benchmark spanning long‑text, numeric, and short‑text targets, multiple forget ratios, and varied question types to capture realistic use cases. Their approach is twofold: first, they perform activation probing to locate the layer that **causally mediates** target disclosure; second, they employ a **retain‑aware projection** that removes only the subspace corresponding to the unwanted attribute while preserving all same‑identity evidence through a lightweight mapping.

## Results  
Experiments on widely used MLLMs such as Flamingo and LLaVA demonstrate that CLRP reduces recall of the target attribute to below 5 % even at high forget ratios (up to 0.8). The method retains other attributes and overall performance within 1 % of a baseline, confirming its effectiveness without requiring any retraining or architectural changes.

## Significance  
By enabling precise, identity‑specific knowledge removal in training‑free settings, CLRP mitigates privacy leakage risks that could arise from coarse‑grained profile deletion. This advancement is crucial for applications where only certain attributes must be erased while the rest of a user’s information remains intact.

## Related Concepts  
- Attribute‑level unlearning  
- Fine‑grained forgetting  
- Multimodal large language models (MLLMs)  
- Training‑free methods  
- Activation patching  
- Retain‑aware projection
