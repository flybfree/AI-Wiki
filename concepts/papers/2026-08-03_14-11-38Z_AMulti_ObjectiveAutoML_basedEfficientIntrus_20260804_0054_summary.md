# Summary: 2026-08-03_14-11-38Z_AMulti_ObjectiveAutoML_basedEfficientIntrusionDete.md
Saved: 2026-08-04 00:54
Source: 2026-08-03_14-11-38Z_AMulti_ObjectiveAutoML_basedEfficientIntrusionDete.md
Model: None

---

## Summary  
Electric Vehicle Charging Systems (EVCSs) are increasingly networked and vulnerable to cyber‑attacks, making intrusion detection essential. Conventional ML‑based IDSs suffer from high inference latency and large model sizes because they rely on manual feature engineering and hyperparameter tuning. The proposed Multi‑Objective Automated ML (MOO‑AutoML) framework jointly optimizes three objectives—maximizing weighted F1‑score, minimizing the 99th‑percentile inference latency ratio, and minimizing model size ratio—to produce a lightweight, fast, and accurate detector for EVCS security. By automating feature selection with LightGBM importance scores and employing NSGA‑III to tune thresholds and hyperparameters, the method delivers a compact yet high‑performing model that outperforms existing solutions under practical deployment constraints.

## Key Contributions  
- **Lightweight AutoML pipeline**: A streamlined training strategy combined with LightGBM’s automated feature selection reduces both model size and computational overhead.  
- **Multi‑objective optimization via NSGA‑III**: The algorithm simultaneously balances detection accuracy, latency, and model compactness, avoiding trade‑offs typical of single‑objective approaches.  
- **Empirical superiority on benchmark datasets**: Experiments on CICEVSE2024 and CICIDS2017 demonstrate higher weighted F1‑scores, lower P99 inference latency, and smaller model sizes compared to baseline methods.

## Methodology  
The authors first construct a dataset of EVCS network logs, then employ LightGBM to generate feature importance scores. The top‑k features are selected iteratively based on accumulated importance until a predefined threshold is reached. NSGA‑III is then invoked to optimize the selection threshold and key LightGBM hyperparameters (e.g., max_depth, learning_rate) under the three objectives. The genetic algorithm maintains a population of candidate configurations, computes non‑dominated solutions, and evolves toward Pareto‑optimal trade‑offs. The selected configuration yields a final model that is evaluated on detection performance, latency, and size.

## Results  
On CICEVSE2024, the MOO‑AutoML IDS achieves a weighted F1‑score of 0.89 (vs. 0.76 for baseline), P99 inference latency ratio of 0.35 (vs. 0.62), and model size ratio of 0.42 (vs. 0.58). On CICIDS2017, the weighted F1‑score reaches 0.84, with latency ratio 0.38 and size ratio 0.45, outperforming all compared methods across both datasets.

## Significance  
This work bridges the gap between security efficacy and operational efficiency in EVCS IoT deployments. By automating feature selection and multi‑objective tuning, it enables real‑time intrusion detection without sacrificing model performance or latency—critical for large‑scale, cost‑sensitive networks where every millisecond and byte counts.

## Related Concepts  
- Intrusion Detection System (IDS)  
- Electric Vehicle Charging Systems (EVCS)  
- Internet of Things (IoT) security  
- LightGBM algorithm  
- AutoML / Automated Machine Learning  
- Multi‑objective optimization  
- NSGA‑III (Non‑dominated Sorting Genetic Algorithm III)
