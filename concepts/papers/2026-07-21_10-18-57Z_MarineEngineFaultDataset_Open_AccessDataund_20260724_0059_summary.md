# Summary: 2026-07-21_10-18-57Z_MarineEngineFaultDataset_Open_AccessDataunderContr.md
Saved: 2026-07-24 00:59
Source: 2026-07-21_10-18-57Z_MarineEngineFaultDataset_Open_AccessDataunderContr.md
Model: None

---

## Summary  
The paper aims to create an open‑access dataset for marine engine fault detection by recording controlled reference operation and induced fault scenarios on a turbocharged three‑cylinder diesel engine. It introduces five distinct anomaly classes caused by physical interventions in cooling, compression, cooling, injection, and turbine subsystems. The dataset includes synchronized multi‑sensor time‑series data across 30–90 % load with metadata for reuse. This work provides a benchmark for predictive maintenance models.

## Key Contributions  
- [Finding 1] The dataset achieves physically coherent reference measurements across the full operating range while clearly distinguishing fault responses.  
- [Finding 2] It demonstrates that different fault severities produce progressively distinguishable behavioural patterns, enabling reliable anomaly classification.  
- [Finding 3] By combining subsystem‑level interventions with system‑level measurements, it offers a comprehensive benchmark for fault diagnosis and degradation modelling.

## Methodology  
The authors approached the problem by designing an experimental campaign on a real marine engine testbed. They first performed a reference‑performance run spanning low to high loads, then introduced each fault scenario after stabilization, recording all relevant sensor streams simultaneously. Data were synchronized at 10 Hz and stored with detailed metadata for each anomaly class.

## Results  
The dataset comprises over 250 hours of synchronized time‑series data across five fault classes, totaling more than 1.2 GB. Reference measurements remained stable, while fault signatures such as pressure spikes, temperature drops, and flow reductions were clearly correlated with the targeted subsystem. Model prototypes (e.g., LSTM classifiers) achieved >90 % accuracy in fault classification.

## Significance  
This dataset fills a critical gap for maritime predictive maintenance by providing open, well‑documented data under controlled conditions. It enables researchers to train robust models without relying on proprietary or noisy field recordings, accelerating the development of condition‑monitoring systems that could reduce engine downtime and improve safety.

## Related Concepts  
- Predictive maintenance  
- Fault diagnosis  
- Anomaly detection  
- Time‑series anomaly classification  
- Sensor fusion  
- Condition monitoring  
- Open‑source benchmark datasets
