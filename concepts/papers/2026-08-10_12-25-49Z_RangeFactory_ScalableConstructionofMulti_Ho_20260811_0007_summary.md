# Summary: 2026-08-10_12-25-49Z_RangeFactory_ScalableConstructionofMulti_HopCyberR.md
Saved: 2026-08-11 00:07
Source: 2026-08-10_12-25-49Z_RangeFactory_ScalableConstructionofMulti_HopCyberR.md
Model: None

---

## Summary  
RangeFactory is an automated framework that builds scalable multi‑hop cyber ranges from isolated vulnerability environments without manual specification. It treats range construction as a dependency‑resolution problem, extracting dependency information from real agent attacks and validating them through end‑to‑end execution. This approach enables the creation of large, validated attack chains for LLM research. The authors evaluate the system on RangeBench, which contains 1,148 validated instances across 287 distinct attack chains.

## Key Contributions  
- [Finding 1] RangeFactory automatically orchestrates multi‑hop cyber ranges by extracting dependency information from actual agent attacks.  
- [Finding 2] It resolves dependencies using template‑guided orchestration and validates runtime dependencies via end‑to‑end attack execution.  
- [Finding 3] The framework generates a corpus of 5,541 outcome‑annotated multi‑hop attack trajectories for training.

## Methodology  
The authors formulate range construction as a dependency resolution task. They collect vulnerability environments and simulate attacks to infer which vulnerabilities must be compromised sequentially. Using known templates that map dependencies, they generate candidate ranges; any unresolved runtime dependencies are resolved by executing the full chain and re‑generating until validation succeeds. This iterative process scales from isolated tasks to complex multi‑host scenarios.

## Results  
RangeFactory constructs RangeBench with 1,148 validated range instances spanning 287 distinct attack chains. Among runs that compromise the entry vulnerability, 24.5–47.0% fail to complete the remaining path, revealing a substantial sustained‑compromise gap. The framework also produces 5,541 outcome‑annotated trajectories for analysis.

## Significance  
By automating multi‑hop cyber range construction, RangeFactory removes a bottleneck in LLM attack research that depends on manually curated scenarios. It supplies scalable, validated data to study attack depth and network scale, enabling more realistic training of agents.

## Related Concepts  
Multi‑hop cyber ranges, dependency resolution, vulnerability orchestration, end‑to‑end validation, synthetic attack corpora, LLM agent evaluation.
