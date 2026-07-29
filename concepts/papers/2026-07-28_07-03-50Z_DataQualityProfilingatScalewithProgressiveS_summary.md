# Summary: 2026-07-28_07-03-50Z_DataQualityProfilingatScalewithProgressiveSampling.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_07-03-50Z_DataQualityProfilingatScalewithProgressiveSampling.md
Model: None

---

## Summary  
The paper addresses the challenge of computing high‑quality data‑quality profiles at scale while keeping computational cost low enough for near‑real‑time monitoring. It introduces a benchmark that compares nine progressive‑sampling strategies—both blind and proxy‑guided—across diverse real‑world datasets ranging from 500 K to over 7 M rows. The study shows that naïve assumptions about estimator sharpness are misleading: blind uniform sampling consistently outperforms many sophisticated methods, while proxy‑driven approaches suffer dramatically in both accuracy and runtime. By revealing the root cause of these failures—a mismatch between IQR‑based proxies and categorical quality defects—the work offers a practical recommendation for production‑grade data‑centric AI pipelines.

## Key Contributions  
- [Finding 1] Blind representative samplers (e.g., random uniform, geometric, Yamane) achieve near‑linear O(N⁰·⁹⁶⁴) runtime and maintain mean relative error below 0.5 % across all benchmark datasets, outperforming proxy‑guided methods by an order of magnitude.  
- [Finding 2] Proxy‑guided samplers such as Metropolis‑Hastings or DAG‑based approaches exhibit super‑linear O(N¹·²⁷²) scaling and mean relative errors 19–35 % higher than random uniform, with statistical significance confirmed by Wilcoxon tests (p = 0.002).  
- [Finding 3] The discrepancy stems from an IQR proxy mismatch: numeric outliers dominate the quality‑score proxy while categorical defects remain invisible, causing over‑pursuit of outliers and poor representativeness.

## Methodology  
The authors benchmark nine progressive‑sampling strategies on a curated set of real datasets (NYC 311, NYPD arrests, UCI Adult, IoT streams up to 2.3 M rows, Ultra‑Marathon Running up to 7.4 M rows, synthetic data scaled to 5×10⁶ rows). For each dataset they compute missing‑value rates, duplicate fractions, outlier densities and functional‑dependency violations using a fixed 5 % sampling budget. The evaluation measures mean relative error (MRE) and runtime scaling with dataset size.

## Results  
Random uniform sampling yields an MRE of 0.49 % on NYC 311 data, matching cluster sampling at 0.110 vs. 0.111. DAG‑guided MCMC reaches 19.5 % error—≈40× worse. Across all real datasets DAG is 11–49× worse (Wilcoxon W=0, p=0.002). Runtime: random uniform scales near‑linearly; DAG runs 28–47× slower on ultra‑large data with 6× higher error.

## Significance  
Scalable data‑quality profiling is a prerequisite for reliable AI pipelines; this benchmark proves that representativeness—not domain knowledge—drives sampler quality, enabling cost‑effective production use. The findings guide practitioners to adopt simple, schema‑free random or cluster samplers instead of complex proxy‑guided techniques.

## Related Concepts  
- Progressive sampling (representative subsampling)  
- Mean relative error (MRE) as a profiling metric  
- Proxy‑guided Markov Chain Monte Carlo (MCMC) and DAG sampling  
- IQR‑based quality proxies  
- Complexity scaling O(N^α) in data‑centric AI  

The paper’s contribution is both empirical—demonstrated via extensive benchmarking—and theoretical, clarifying why proxy‑driven methods degrade at scale and recommending a robust, low‑cost alternative for real‑world AI pipelines.
