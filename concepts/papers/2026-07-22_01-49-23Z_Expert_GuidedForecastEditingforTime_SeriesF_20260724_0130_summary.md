# Summary: 2026-07-22_01-49-23Z_Expert_GuidedForecastEditingforTime_SeriesFoundati.md
Saved: 2026-07-24 01:30
Source: 2026-07-22_01-49-23Z_Expert_GuidedForecastEditingforTime_SeriesFoundati.md
Model: None

---

## Summary  
Time‑series foundation models generate high‑quality forecasts without task‑specific training, yet their outputs are immutable and cannot directly absorb expert feedback. The authors introduce DEFT, an expert‑guided editing framework that balances the naïve “best‑of‑N” exploitation of the model’s predictive distribution with the costly, unstructured search required by optimization methods. By decomposing forecasts into trend and seasonal components and reusing expert scores across component recombinations, DEFT reduces query waste while preserving the frozen nature of the foundation model. The approach consistently improves the effectiveness of sparse test‑time guidance across multiple benchmarks.

## Key Contributions  
- [Finding 1] Expert feedback can only be incorporated through a fixed set of complete trajectory queries because the foundation model remains frozen during inference.  
- [Finding 2] DEFT balances two extremes—pure exploitation (best‑of‑N) and high‑dimensional optimization—by performing component‑wise refinement in a trend–seasonal space, reusing expert scores across recombinations.  
- [Finding 3] Empirical evaluation shows that DEFT outperforms direct search methods such as best‑of‑N, cross‑entropy, and Bayesian optimization on 78 datasets with three foundation models, four feedback types, and seven query budgets.

## Methodology  
The authors generate candidate future trajectories from a frozen time‑series foundation model. Each trajectory is decomposed into trend and seasonal components, which are then recombined to form new forecasts. The expensive expert evaluator scores only the full reconstructed trajectories; the resulting component scores are reused for subsequent recombinations, allowing structured feedback without additional queries. This iterative refinement yields a set of edited forecasts that retain the model’s prior knowledge while adapting to expert guidance.

## Results  
Across seven query budgets, DEFT improves forecast accuracy and reduces the number of needed expert queries compared with baseline methods. The study spans 78 heterogeneous time‑series datasets evaluated on three foundation models and four types of feedback (e.g., loss, uncertainty). A molecular‑dynamics case study demonstrates that the same principle—balancing prior exploitation with structured exploration—can be applied to physically grounded expert signals, suggesting broad applicability beyond conventional forecasting.

## Significance  
DEFT provides a principled way to allocate limited test‑time queries between exploiting a model’s learned distribution and exploring the parameter space of a frozen system. By reusing component scores, it mitigates query inefficiency, making sparse feedback more effective for any task that relies on expert guidance without retraining.

## Related Concepts  
- Time‑series foundation models  
- Expert‑guided editing  
- Best‑of‑N strategy  
- Optimization methods (cross‑entropy, Bayesian)  
- Trend–seasonal decomposition  
- Component‑wise refinement  
- Sparse test‑time guidance
