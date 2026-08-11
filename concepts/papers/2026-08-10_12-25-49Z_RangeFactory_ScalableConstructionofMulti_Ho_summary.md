# Summary: 2026-08-10_12-25-49Z_RangeFactory_ScalableConstructionofMulti_HopCyberR.md
Saved: 2026-08-10 23:48
Source: 2026-08-10_12-25-49Z_RangeFactory_ScalableConstructionofMulti_HopCyberR.md
Model: None

---

## Summary  
RangeFactory introduces an automated framework for constructing multi‑hop cyber ranges directly from isolated vulnerability environments, treating the construction process as a dependency‑resolution problem that is validated by end‑to‑end attack execution. By extracting real‑world dependency information and using template‑guided orchestration, the system automatically composes large‑scale attack chains while confirming at runtime which dependencies actually hold. The framework generates RangeBench, a benchmark containing 1,148 validated ranges spanning 287 distinct attack chains, and annotates 5,541 outcome trajectories for further analysis.

## Key Contributions  
- **Automated dependency‑resolution construction**: RangeFactory builds multi‑hop cyber ranges automatically from actual attack logs without manual specification.  
- **Large‑scale benchmark (RangeBench)**: The system produces 1,148 validated range instances and a corpus of 5,541 outcome‑annotated trajectories for analysis.  
- **Sustained‑compromise gap**: Experiments show that 24.5 %–47.0 % of attacks fail to complete the remaining path after an initial foothold is established.

## Methodology  
The authors first parse real attack logs to infer dependency graphs between vulnerabilities and network segments. Known dependencies are resolved using template‑driven orchestration that suggests how tasks should be sequenced. To validate these inferred dependencies, RangeFactory executes full end‑to‑end attacks; any runtime failures trigger feedback loops that refine the construction. The resulting validated ranges are stored in RangeBench with outcome annotations.

## Results  
RangeFactory generated 1,148 multi‑hop cyber ranges covering 287 unique attack chains. A total of 5,541 trajectory outcomes were annotated, allowing precise measurement of success rates. When the entry vulnerability is compromised, roughly a quarter to almost half of the attacks stop short of completing the full chain, indicating a significant sustained‑compromise gap. The evaluation also examined how depth, network scale, and task information affect failure probabilities.

## Significance  
By providing a scalable, data‑driven pipeline for multi‑hop cyber range construction, RangeFactory enables researchers to study LLM agents’ ability to maintain persistent attacks across complex environments. It reveals that establishing an initial foothold does not guarantee successful completion of the attack, highlighting a critical bottleneck in current security testing. The annotated dataset serves as a valuable resource for training and benchmarking advanced attack‑simulation models.

## Related Concepts  
- Cyber ranges  
- Multi‑hop attack chains  
- Dependency resolution  
- End‑to‑end validation  
- Vulnerability orchestration  
- RangeBench benchmark
