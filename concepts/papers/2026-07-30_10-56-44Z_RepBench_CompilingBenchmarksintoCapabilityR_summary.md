# Summary: 2026-07-30_10-56-44Z_RepBench_CompilingBenchmarksintoCapabilityRepresen.md
Saved: 2026-07-30 21:48
Source: 2026-07-30_10-56-44Z_RepBench_CompilingBenchmarksintoCapabilityRepresen.md
Model: None

---

## Summary  
RepBench introduces a systematic way to compile benchmark papers into structured capability representations for large language models, enabling comparable and reproducible evaluation across diverse tasks. The framework builds an audited corpus of probe texts from 13,427 benchmark papers and 353 public datasets that together cover 94 distinct capabilities. By aggregating these vectors into capability‑aligned clusters, RepBench reveals patterns that raw per‑text embeddings miss. This work provides a reusable closed‑loop pipeline for capability‑focused representation probing.

## Key Contributions  
- [Finding 1] The authors create a taxonomy of 182 capability clusters organized into 13 families by mining 13,427 benchmark papers.  
- [Finding 2] Benchmark‑pooled capability vectors exhibit an interior clustering optimum with only a small number of clusters, outperforming the natural granularity of raw per‑text vectors.  
- [Finding 3] Cross‑benchmark evaluation shows disagreement between readout methods (difference‑in‑means) and aggregation criteria (logistic regression), highlighting their importance as distinct evaluation dimensions.

## Methodology  
The authors first crawl 13,427 benchmark papers to extract capability descriptions, generating a hierarchical taxonomy of clusters. They then harvest 353 public datasets, auditing probe texts for each capability to ensure reliability. For every model‑probe pair they compute per‑text embeddings, pool them into capability vectors using either hierarchical clustering or logistic regression, and evaluate the resulting vectors across twelve large language models via difference‑in‑means and logistic‑regression cell scores.

## Results  
Raw per‑text vectors lack clear natural clusters across all models. In contrast, capability‑pooled vectors consistently form a few tight clusters on every model, achieving an optimal clustering structure. Logistic regression outperforms difference‑in‑means in the majority of capability‑model cells, indicating that aggregation choice matters. Cross‑benchmark transfer evaluation yields the highest mean scores for ten out of twelve models, demonstrating strong generalization.

## Significance  
RepBench standardizes how researchers compare model capabilities across tasks, reducing dependence on a single benchmark source and clarifying which evaluation metrics are most informative. By providing an audited corpus and reproducible pipeline, it advances reproducibility in representation engineering and enables more meaningful interpretation of LLM performance.

## Related Concepts  
- Representation engineering  
- Capability clustering  
- Benchmark aggregation  
- Probe texts  
- Difference‑in‑means evaluation  
- Logistic regression for cell scoring  
- Closed‑loop workflow
