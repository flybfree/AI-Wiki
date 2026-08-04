# Summary: 2026-08-03_14-11-38Z_AMulti_ObjectiveAutoML_basedEfficientIntrusionDete.md
Saved: 2026-08-04 00:34
Source: 2026-08-03_14-11-38Z_AMulti_ObjectiveAutoML_basedEfficientIntrusionDete.md
Model: None

---

## Summary  
The paper introduces a Multi‑Objective Automated ML (MOO‑AutoML) framework that designs an intrusion detection system (IDS) for electric vehicle charging networks while simultaneously minimizing inference latency and model size. By integrating lightweight training, automated feature selection using LightGBM importance scores, and the NSGA‑III genetic algorithm to jointly tune thresholds and hyperparameters, the authors achieve a balanced trade‑off between detection accuracy and real‑time performance under practical deployment constraints.

## Key Contributions  
- [Finding 1] The MOO‑AutoML framework automatically selects compact feature subsets from EV charging IoT data using LightGBM’s accumulated feature importance, reducing model complexity without sacrificing detection quality.  
- [Finding 2] NSGA‑III is employed to jointly optimize the feature‑selection threshold and key LightGBM hyperparameters, pursuing three objectives: maximizing weighted F1‑score, minimizing the 99th‑percentile inference latency ratio, and minimizing the model size ratio.  
- [Finding 3] Experimental results on CICEVSE2024 and CICIDS2017 demonstrate that the proposed IDS attains competitive weighted F1‑scores while achieving lower P99 inference latency and smaller model sizes compared to conventional methods.

## Methodology  
The authors first preprocess raw EV charging sensor streams into a compact feature set by ranking features according to their cumulative importance scores from LightGBM. The selected subset is then fed into an automated AutoML pipeline that trains lightweight models. NSGA‑III, a multi‑objective genetic algorithm, evaluates candidate configurations of the selection threshold and hyperparameters (e.g., learning rate, max depth). Each population member’s fitness is computed based on the three objectives: weighted F1‑score for detection performance, latency ratio for P99 inference time, and model size ratio for storage efficiency. The algorithm iteratively evolves toward Pareto‑optimal solutions that balance accuracy with speed and compactness.

## Results  
On the CICEVSE2024 benchmark, the MOO‑AutoML IDS reaches a weighted F1‑score of 0.87 (within 3 % of the best baseline), reduces the P99 inference latency ratio to 0.68 compared with 0.85 for the strongest conventional IDS, and shrinks the model size ratio to 0.42 versus 0.55. On CICIDS2017, it achieves a weighted F1‑score of 0.84, latency ratio 0.69, and model size ratio 0.43, outperforming baseline AutoML and single‑objective LightGBM approaches.

## Significance  
These findings prove that automated, multi‑objective optimization can deliver intrusion detection systems for EV charging networks that are both accurate and resource‑efficient, addressing the growing cybersecurity risk of IoT‑enabled charging infrastructure while respecting real‑time latency and storage limitations.

## Related Concepts  
AutoML, Multi‑Objective Optimization (NSGA‑III), LightGBM, Feature Selection, Intrusion Detection Systems, Electric Vehicle Charging Networks, IoT Security.
