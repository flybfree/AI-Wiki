# Summary: 2026-08-03_08-32-50Z_Energy_EfficientLLMServingviaDisaggregatedAttentio.md
Saved: 2026-08-03 23:46
Source: 2026-08-03_08-32-50Z_Energy_EfficientLLMServingviaDisaggregatedAttentio.md
Model: None

---

## Summary  
Large language model serving demands high‑performance GPUs that often run at maximum frequencies, inflating energy consumption and violating service‑level objectives (SLOs). The paper discovers that the optimal frequencies for attention and feed‑forward networks differ and are highly sensitive to inference phase, workload, and system configuration. Existing frequency‑scaling solutions treat these components independently, creating a large search space and high communication overhead. To resolve this, AFlex jointly optimizes resource allocation and GPU DVFS across both subnetworks using a global scheduler and local controllers.

## Key Contributions  
- [Finding 1] The energy‑optimal frequencies of Attention (A) and FFN (F) are distinct and vary with the inference phase, workload, and system configuration.  
- [Finding 2] Runtime variability combined with independent A/F frequency control generates a large optimization search space and substantial communication overhead.  
- [Finding 3] AFlex introduces a global scheduler and local operator‑level DVFS controller that jointly allocate resources and frequencies, while an interleaved A/F pipeline with dynamic microbatch depth and adaptive request batching reduces pipeline bubbles.

## Methodology  
AFlex tackles the problem by decoupling high‑level resource planning from low‑level frequency scaling. A global scheduler computes a balanced allocation of GPU resources to the disaggregated attention and FFN modules, while each module runs its own DVFS controller that adjusts voltage and frequency in real time based on local load. The framework employs an interleaved execution pipeline where attention and FFN sub‑tasks are mixed dynamically; microbatch depth is tuned per request batch size, and adaptive request batching merges short requests to fill the pipeline without bubbles. This joint optimization reduces communication latency between modules and minimizes idle GPU cycles.

## Results  
Implemented in SGLang on NVIDIA A800 GPUs, AFlex serves Qwen3‑32B and Mixtral‑8×7B under production Conversation and Coding traces. Compared to state‑of‑the‑art disaggregated serving, AFlex cuts energy per token by up to 49 % and compared to pure frequency‑scaling systems it achieves a further 48 % reduction. Crucially, the framework meets both TTFT (turnaround time) and TPOT (throughput) SLOs without sacrificing performance.

## Significance  
By recognizing that attention and FFN have separate frequency sensitivities, AFlex eliminates redundant optimization efforts and dramatically shrinks the search space for energy‑aware serving. The approach delivers substantial energy savings while guaranteeing latency and throughput constraints, supporting sustainable AI deployment at scale.

## Related Concepts  
- Disaggregated attention/FFN serving  
- Dynamic Voltage and Frequency Scaling (DVFS)  
- Global scheduler vs. local controller  
- Interleaved pipeline execution  
- Microbatch depth tuning  
- Adaptive request batching  
- Token‑energy per token metric  
- TTFT (turnaround time) SLO  
- TPOT (throughput) SLO
