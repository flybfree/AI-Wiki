# Summary: 2026-07-25_05-10-01Z_MixQuant_AdaptiveMixed_PrecisionQuantizationforLar.md
Saved: 2026-07-27 23:35
Source: 2026-07-25_05-10-01Z_MixQuant_AdaptiveMixed_PrecisionQuantizationforLar.md
Model: None

---

## Summary  
The paper addresses a limitation of existing mixed‑precision quantization methods, which allocate bitwidths under a single fixed memory budget that cannot adapt to deployment constraints. It shows that a layer’s sensitivity is not independent but strongly influenced by the bitwidths of its upstream layers, causing traditional adaptive scores to be suboptimal. MixQuant proposes an adaptive framework that can serve any budget with a single calibration pass while respecting these dependencies. The approach yields higher accuracy and lower perplexity than prior baselines across several LLMs under both AWQ and GPTQ quantization schemes.

## Key Contributions  
- [Finding 1] A layer’s sensitivity depends strongly on the bitwidths of its upstream layers, shifting the preferred bit allocation when those bits change.  
- [Finding 2] Current adaptive methods ignore this dependency, solving the budget allocation problem for a single fixed memory budget only.  
- [Finding 3] MixQuant provides budget‑agnostic scores by marginalizing each layer’s distortion over random quantized upstream configurations and then greedily allocates bits to avoid the lowest bitwidths.

## Methodology  
MixQuant wraps any base post‑training quantizer, treating it as a black box. It first computes marginalized distortion values for each layer across many random quantizations of its upstream layers, producing budget‑agnostic sensitivity scores. The framework then calibrates the allocator’s parameters on the plans it generates, penalizing allocations that would leave any layer at the minimum bitwidth. Finally, a single greedy pass selects the optimal bit allocation for any given memory budget, enabling deployment with one calibration.

## Results  
Across Llama‑3.2‑3B, Llama‑2‑7B, and Mistral‑7B under both AWQ and GPTQ quantization, MixQuant improves average accuracy by up to 8 points compared with adaptive and mixed‑precision baselines. At the tightest budget it reduces perplexity from 12.43 to 10.70, matching an integer linear programming (ILP) solver while incurring negligible deployment cost.

## Significance  
This work matters because it decouples quantization quality from a rigid memory budget, allowing models to adapt automatically to the limited resources of real‑world deployments. By respecting layer dependencies and avoiding low‑bitwidth penalties, MixQuant delivers state‑of‑the‑art performance with minimal calibration effort, paving the way for more efficient LLM inference.

## Related Concepts  
mixed‑precision quantization, adaptive quantization, bitwidth allocation, sensitivity scoring, marginalization over random configurations, greedy allocation, ILP solver.
