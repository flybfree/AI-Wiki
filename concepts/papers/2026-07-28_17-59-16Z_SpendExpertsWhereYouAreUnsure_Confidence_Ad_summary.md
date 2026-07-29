# Summary: 2026-07-28_17-59-16Z_SpendExpertsWhereYouAreUnsure_Confidence_AdaptiveR.md
Saved: 2026-07-28 23:03
Source: 2026-07-28_17-59-16Z_SpendExpertsWhereYouAreUnsure_Confidence_AdaptiveR.md
Model: None

---

## Summary  
Mixture‑of‑Experts (MoE) LoRA models route every token to a fixed number of experts, which leads to inefficient spending: easy tokens are over‑served while hard ones receive little attention. The authors propose **CARE** – Confidence‑Adaptive Routing of Experts – that treats the router’s output distribution as an intrinsic per‑token uncertainty signal and activates only those experts whose cumulative mass reaches a calibrated threshold. This “nucleus” activation reduces over‑spending on confident tokens, improves service for uncertain ones, and can be tuned to match any compute budget without extra parameters.

## Key Contributions  
- [Finding 1] The router’s output distribution encodes per‑token confidence; high mass = high confidence, flat mass = ambiguity.  
- [Finding 2] CARE activates experts in a nucleus fashion: experts are added in decreasing router weight until their cumulative mass meets a threshold set by a budget thermostat, with a small extension when admitted experts disagree.  
- [Finding 3] Experiments on eight commonsense benchmarks (LLaMA‑3.1‑8B, Qwen2.5‑7B) plus math, code, and knowledge tasks show CARE outperforms fixed top‑k MoE‑LoRA at matched compute, matches the k=4 baseline while using fewer active experts, and also boosts out‑of‑distribution detection over MSP, entropy, and multi‑pass proxies.

## Methodology  
CARE leverages the router’s output distribution as an epistemic uncertainty measure. During forward pass, each token’s expert activation probability is sorted by descending router weight. The algorithm then adds experts one‑by‑one until their combined mass reaches a target threshold computed by a “budget thermostat” that aligns with the desired average number of active experts. If the admitted experts disagree on the token’s prediction (a disagreement signal), a small extension activates additional experts to resolve ambiguity. This procedure is a single‑forward‑pass rule requiring no extra parameters.

## Results  
Across eight commonsense benchmarks evaluated on LLaMA‑3.1‑8B and Qwen2.5‑7B, CARE improves accuracy over fixed top‑k MoE‑LoRA when compute is held constant. It matches the performance of a fixed k=4 configuration while activating fewer experts overall. Moreover, the confidence and disagreement signals derived from routing enhance out‑of‑distribution detection, outperforming MSP (Multi‑Source Prediction), entropy measures, and multi‑pass proxies on several downstream tasks.

## Significance  
CARE provides an efficient, resource‑aware way to allocate expert capacity, reducing over‑spending on easy tokens and improving service for uncertain ones. By aligning activation with per‑token confidence, it lowers compute cost, enhances model robustness, and enables tighter control over MoE LoRA scaling without sacrificing performance.

## Related Concepts  
- Mixture‑of‑Experts (MoE) LoRA: a parameter‑efficient fine‑tuning technique that routes tokens to expert subnetworks.  
- Router output distribution as uncertainty signal: the variance of expert activation probabilities reflects token confidence.  
- Nucleus sampling / nucleus activation: activating experts in order until a cumulative mass threshold is met.  
- Budget thermostat: a calibration mechanism that sets the activation threshold to match a desired average number of active experts.  
- Epistemic reading of disagreement: treating expert disagreement as additional uncertainty requiring extra activation.  
- MSP (Multi‑Source Prediction): an alternative OOD detection method used for comparison.  
- Entropy measures: information‑theoretic uncertainty metrics applied to routing decisions.  
- Multi‑pass proxies: techniques that re‑evaluate token routes in multiple passes for better allocation.
