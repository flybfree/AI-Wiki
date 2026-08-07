# Summary: 2026-08-06_01-58-00Z_Equation_FreePeriod_AwareForecast_ErrorContraction.md
Saved: 2026-08-06 21:58
Source: 2026-08-06_01-58-00Z_Equation_FreePeriod_AwareForecast_ErrorContraction.md
Model: None

---

## Summary  
The paper proposes a data‑driven method to estimate the dominant negative Lyapunov exponent from short scalar trajectory ensembles without using governing equations or analytical Jacobians. By synchronizing forecast steps with detected orbit periods and extracting contraction rates directly from out‑of‑sample forecast errors, the authors achieve reliable parameter recovery for chaotic maps where positive exponents are trivial.  

## Key Contributions  
- [Finding 1] The method introduces a period‑aware forecast‑error contraction procedure that extracts negative Lyapunov exponent estimates solely from trajectory histories.  
- [Finding 2] It uses k‑nearest‑neighbor predictor training, geometric‑mean absolute forecast error at phase‑consistent horizons, and slope analysis of the log‑error profile to obtain the exponent.  
- [Finding 3] The approach achieves high accuracy (MAE ≈0.01–0.025, R²≈0.89–0.99) on logistic map and two‑dimensional maps without fixed points.  

## Methodology  
The authors train a k‑nearest‑neighbor model on the observed trajectory histories to predict future states. Forecast errors are computed at horizons that align with the detected period, and the geometric mean of absolute errors is taken. The natural logarithm of these errors is plotted versus horizon length; the slope yields the negative Lyapunov exponent. To ensure robustness, only slopes that persist across several transient lengths (consensus) are retained.  

## Results  
On the logistic map the method recovers 92 of 112 negative‑exponent values with a mean absolute error of 0.0253 and R²=0.886. For a two‑dimensional map lacking fixed points, independent scalar pipelines on observables xₙ, yₙ, zₙ obtain MAEs of 0.00879–0.01145 and R²s of 0.983–0.986.  

## Significance  
Because the estimation relies only on observed short sensor responses and does not require known governing equations or analytical Jacobians, it enables repeat‑relaxation experiments where dynamical models are unknown. This opens a practical pathway to monitor stability in real‑time systems with limited data.  

## Related Concepts  
Lyapunov exponent, forecast error, k‑nearest neighbor predictor, phase‑consistent horizons, geometric mean absolute error, negative largest Lyapunov exponent, transient length consensus, data‑driven dynamical system analysis.
