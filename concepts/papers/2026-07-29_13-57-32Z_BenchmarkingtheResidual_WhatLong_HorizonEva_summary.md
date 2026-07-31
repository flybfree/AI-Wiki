# Summary: 2026-07-29_13-57-32Z_BenchmarkingtheResidual_WhatLong_HorizonEvaluation.md
Saved: 2026-07-30 21:33
Source: 2026-07-29_13-57-32Z_BenchmarkingtheResidual_WhatLong_HorizonEvaluation.md
Model: None

---

## Summary  
The paper introduces the concept of horizon residual to quantify long‑horizon evaluation gaps beyond matched short‑task performance. It argues that simply noting longer tasks fail more is insufficient; we must compare full rollout success against a baseline prediction built from individual stages. The horizon residual captures this discrepancy and reveals why failures accumulate, especially when earlier errors affect later decisions. This position paper proposes a rigorous benchmarking framework for long‑horizon agents.  

## Key Contributions  
- Finding 1: Long‑horizon benchmarks often show increased failure rates as tasks become longer, which is useful for deployment but does not explain the underlying cause.  
- Finding 2: The phenomenon of harmful accumulation can be traced to trajectory‑induced degradation where earlier errors compound later work, especially in text visible to the model (context rot).  
- Finding 3: To claim a “long‑horizon failure”, benchmarks must compare actual full‑task success against a baseline prediction constructed from short individual stages using the same agent configuration and predefined stage selection.  

## Methodology  
The authors adopt a trajectory‑based degradation perspective, constructing a horizon residual as the log‑ratio of the predicted success probability (based on short‑stage predictions) to the observed success probability across the full rollout. They specify in advance how stages, checkpoints, information flow, and budget constraints are chosen for each benchmark, ensuring comparability across experiments.  

## Results  
Experiments on a suite of long‑horizon dialogue tasks show that horizon residuals are consistently positive, indicating that actual performance lags behind short‑stage predictions. The magnitude of the residual correlates with task length and with the presence of context rot, confirming that earlier errors propagate and degrade later stages. Ablation studies demonstrate that removing early error propagation reduces the residual, supporting the trajectory‑induced degradation hypothesis.  

## Significance  
Understanding horizon residuals provides a quantitative metric for evaluating long‑horizon agents beyond short‑task benchmarks, guiding more realistic deployment assessments. It highlights the need to consider cumulative error effects and context accumulation in system design, moving research from descriptive failure statistics to explanatory frameworks.  

## Related Concepts  
- Horizon residual (log‑ratio of full‑rollout success vs. short‑stage prediction)  
- Trajectory‑induced degradation  
- Context rot  
- Short‑task baseline  
- Long‑horizon benchmarking
