# Summary: 2026-07-26_13-01-48Z_ExtendingDesbordantewithProbabilisticFunctionalDep.md
Saved: 2026-07-27 20:19
Source: 2026-07-26_13-01-48Z_ExtendingDesbordantewithProbabilisticFunctionalDep.md
Model: None

---

## Summary  
This paper introduces Probabilistic Functional Dependency (pFD) discovery support within the Desbordante data‑profiling framework, extending its capabilities beyond Approximate Functional Dependencies (AFDs). The authors aim to understand when pFDs provide superior insight over AFDs, implement a novel algorithm for pFD detection, and evaluate its performance against an existing AFD algorithm. By comparing runtimes, memory usage, and output quality, the study demonstrates the practical value of probabilistic models in handling dirty data while preserving Desbordante’s high‑performance C++ core.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A theoretical analysis showing that pFDs can capture more nuanced relationships than AFDs when data contain noise or missing values.  
- [Finding 2] An implementation of a probabilistic functional dependency discovery algorithm integrated into Desbordante, with measured runtimes and memory footprints.  
- [Finding 3] Empirical evidence that the pFD output is not merely a superset of AFD results; instead, it can produce distinct dependencies that AFDs miss.

## Methodology  
The authors first conducted analytical case studies to identify scenarios where pFDs outperform AFDs, then built a C++‑based algorithm that computes conditional probabilities for each candidate pair of attributes. The tool was benchmarked against Desbordante’s standard AFD discovery routine using synthetic and real‑world datasets. Outputs were compared to assess completeness and redundancy.

## Results  
The experimental results reveal that the pFD algorithm runs within 15 % of the AFD baseline while consuming up to 20 % more memory, yet it uncovers additional dependencies in noisy data sets. In three benchmark cases, the pFD output added two new functional relationships absent from AFD detection, confirming its value for richer profiling.

## Significance  
By integrating probabilistic models into Desbordante, the paper expands the tool’s utility for scientific data analysis, enabling more accurate pattern extraction that respects real‑world imperfections. This contributes to both theoretical understanding of fuzzy dependencies and practical performance in high‑throughput profiling pipelines.

## Related Concepts  
- Functional Dependency (FD) – a deterministic relational concept.  
- Approximate Functional Dependency (AFD) – a relaxation allowing approximate matches.  
- Probabilistic Functional Dependency (pFD) – a stochastic extension that models likelihood of dependency given noisy data.  
- Data Profiling – automated extraction of patterns for cleaning, deduplication, and anomaly detection.
