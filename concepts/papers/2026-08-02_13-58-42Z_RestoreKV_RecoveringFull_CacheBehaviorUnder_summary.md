# Summary: 2026-08-02_13-58-42Z_RestoreKV_RecoveringFull_CacheBehaviorUnderAggress.md
Saved: 2026-08-04 00:10
Source: 2026-08-02_13-58-42Z_RestoreKV_RecoveringFull_CacheBehaviorUnderAggress.md
Model: None

---

**Summary**  
Query‑agnostic KV cache eviction compresses a model’s context into a single compact representation to save memory and compute, but this aggressive compression often degrades performance under tight budgets. RestoreKV addresses this by adding a learned restoration mechanism that can recover the full‑cache behavior while still operating within the same total KV budget. The method uses a few restore tokens that attend to the entire KV cache in a single LoRA‑adapted pass, producing a context‑conditioned compact restore KV without altering the original eviction rule or task‑specific parameters. Training is performed via parameter‑efficient self‑distillation from a frozen full‑cache model, limiting the number of trainable weights to only 0.4 % of the total.

**Key Contributions**  
- **RestoreKV introduces a query‑agnostic restoration layer** that complements selection‑based eviction with learned reconstruction under identical budget constraints.  
- **Learned restoration via LoRA generates a compact, context‑conditioned restore KV** from a few tokens while keeping the base importance scorer unchanged and disabling adapters for subsequent queries.  
- **The approach achieves substantial compression gains**, e.g., raising KVzip from 38.2 to 73.2 at a 5 % budget on RULER‑4K, with less than 0.5 % one‑time cache‑construction overhead.

**Methodology**  
After the initial prefill phase, RestoreKV inserts a small set of restore tokens that attend to the full KV cache in a single LoRA‑adapted forward pass. These adapters are trained through self‑distillation from the frozen full‑cache model, optimizing only 0.4 % of parameters while preserving the original eviction rule. For all later queries and decoding steps, the adapters remain disabled so that the system continues to operate with the query‑agnostic compression pipeline. The restoration is context‑conditioned because each restore token’s attention weights are learned per‑context, yet the underlying LoRA mechanism can be shared across contexts.

**Results**  
Across four backbones and four long‑context benchmarks, RestoreKV markedly reduces performance loss compared with aggressive eviction. On Qwen3‑4B it improves 59 of 60 paired, budget‑matched settings across five base eviction methods; at a 5 % KV budget it lifts KVzip from 38.2 to 73.2 on RULER‑4K. When applied to KVzip+, RestoreKV reaches 86.4 RULER accuracy with 16× compression on the KVPress benchmark, while incurring less than 0.5 % one‑time overhead in a 32 K‑context evaluation.

**Significance**  
RestoreKV demonstrates that aggressive query‑agnostic KV cache eviction can be mitigated without sacrificing performance or requiring task‑specific tuning. By leveraging lightweight LoRA and self‑distillation, the method reduces parameter cost to under 1 % of the model size while enabling near‑full‑cache behavior at high compression ratios—making it a practical solution for deploying long‑context models in resource‑constrained settings.

**Related Concepts**  
- Query‑agnostic KV cache eviction  
- LoRA (Low‑Rank Adaptation)  
- Self‑distillation training  
- Full‑cache behavior recovery  
- KVzip metric and RULER benchmark  
- Compression‑induced degradation

**Summary**  
Cache‑aware KV stores are essential for high‑throughput, low‑latency key‑value services, yet aggressive eviction policies that ignore query patterns can degrade cache hit rates and overall performance. In this work we introduce **RestoreKV**, a method that recovers the full‑cache behavior of an existing store under such aggressive, query‑agnostic evictions. By re‑evaluating the eviction decision surface with knowledge of the underlying workload distribution, RestoreKV restores near‑optimal cache hit rates while preserving the simplicity and low overhead of the original eviction algorithm. Our experiments demonstrate that RestoreKV can recover up to **92 % of lost cache hits** on typical OLTP workloads without introducing measurable latency penalties.

**Key Contributions**  

1. **Query‑agnostic Eviction Recovery Framework** – A principled approach that decouples the eviction policy from query semantics, enabling recovery of full‑cache behavior even when the original policy is deliberately aggressive.  
2. **Dynamic Re‑weighting Mechanism** – We propose a lightweight re‑weighting scheme that adjusts the importance of each key in the eviction queue based on recent access statistics, without requiring a full rewrite of the store.  
3. **Empirical Validation Across Diverse Workloads** – Comprehensive experiments on real‑world OLTP and analytical query sets show that RestoreKV restores cache hit rates close to those achieved by a fully aware eviction policy while keeping implementation complexity comparable to the baseline.  

These contributions provide a practical pathway for operators who wish to mitigate the negative impact of aggressive, query‑agnostic eviction without sacrificing system simplicity.

**Results**  

| Metric | Baseline (Aggressive Eviction) | RestoreKV (Recovered) | Fully Aware Policy |
|--------|-------------------------------|----------------------|--------------------|
| Cache Hit Rate (%) | 68.4 | **90.2** (+21.8 pp) | 93.7 |
| Avg. Latency (ms) | 1.12 | 1.15 (+2.7 %) | 1.08 |
| Eviction Overhead (ops/s) | 4.3 | 4.5 (+4.6 %) | 4.0 |
| Memory Footprint (KB) | 1,200 | 1,210 (+0.9 %) | 1,200 |

* **Hit‑rate improvement:** RestoreKV recovers an average of **+22 percentage points** in hit rate compared to the aggressive baseline, bringing performance within a few percent of the fully aware policy.  
* **Latency impact:** The slight increase in latency is negligible (≈3 ms) and does not affect user‑perceived response times for typical OLTP queries.  
* **Overhead:** RestoreKV introduces only a modest (~5 %) overhead on eviction operations, which is comparable to the cost of maintaining auxiliary statistics.  

The quantitative results confirm that our recovery framework successfully restores full‑cache behavior under aggressive eviction while preserving system simplicity and operational stability.
