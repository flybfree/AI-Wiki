# Summary: 2026-07-24_13-53-58Z_LearningBidirectionalCausalInteractionswithHeteros.md
Saved: 2026-07-26 21:51
Source: 2026-07-24_13-53-58Z_LearningBidirectionalCausalInteractionswithHeteros.md
Model: None

---

## Summary  
The paper tackles the challenge of estimating contemporaneous bidirectional interactions from observational data where each outcome is endogenous to the other. It introduces SEM‑DNN, a heteroscedastic neural simultaneous‑equation estimator that learns reciprocal structural effects without external instruments. The method relies on conditional covariance diagonalization and a diagonal Gaussian quasi‑likelihood that incorporates the system Jacobian. Its contribution is a theoretically grounded identification framework that yields causal‑interpreted coefficients under specific assumptions.

## Key Contributions  
- Finding 1: SEM‑DNN uniquely identifies interaction coefficients by exploiting the fact that true structural shocks have zero conditional means, are conditionally uncorrelated given predetermined covariates, and exhibit nonproportional variances, which cause only the correct coefficients to diagonalize the residual covariance.  
- Finding 2: The neural criterion inherits positive‑definite local curvature of the profiled population criterion under neural‑profile compatibility conditions, guaranteeing identification despite nonunique network parameterizations.  
- Finding 3: Monte‑Carlo experiments with high‑dimensional nuisance functions and non‑Gaussian shocks show that SEM‑DNN recovers structural effects more reliably than parametric regressions, kernel‑based estimators, or separate‑equation neural alternatives, though at a higher computational cost.

## Methodology  
The authors formulate the simultaneous equations as a joint Gaussian model with feature‑dependent variances. They construct a diagonal Gaussian quasi‑likelihood whose likelihood is proportional to the exponential of the negative trace of the conditional residual covariance multiplied by the system Jacobian. Neural networks are used to approximate both the nonlinear mean functions and the variance functions, while the Jacobian is computed analytically. Identification follows from the structural shock assumptions that ensure diagonalization of the covariance matrix.

## Results  
Theoretical analysis establishes unique identification and positive‑definite local curvature for the profiled population criterion, which the implemented neural criterion inherits under compatibility conditions. Empirically, SEM‑DNN outperforms competing methods in terms of mean squared error recovery when information is abundant, confirming its robustness to nonlinearity and non‑Gaussian shocks. The method also demonstrates sensitivity to variance calibration and optimization, highlighting practical considerations.

## Significance  
By providing a neural framework that does not require instrumental variables or strong parametric assumptions, SEM‑DNN enables rigorous study of bidirectional causal interactions in high‑dimensional real‑world data such as ready‑to‑eat cereal scanner records. It improves identification strength, allows assessment of residual diagonalization and variance calibration, and offers a pathway to interpret structural feedbacks without relying on external instruments.

## Related Concepts  
- Simultaneous equations  
- Heteroscedasticity  
- Conditional covariance diagonalization  
- Gaussian quasi‑likelihood  
- Neural profile compatibility  
- Profiled population criterion  
- Structural shocks  
- Causal interpretation  
- Residual diagonalization  
- Variance calibration  
- Optimization sensitivity
