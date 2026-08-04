# Summary: 2026-08-02_13-03-48Z_AmortizingtheCalibrationTriple_AProjection_Consist.md
Saved: 2026-08-04 00:10
Source: 2026-08-02_13-03-48Z_AmortizingtheCalibrationTriple_AProjection_Consist.md
Model: None

---

## Summary  
The paper tackles the calibration of local‑stochastic volatility (LSV) by amortizing an expensive McKean–Vlasov fixed point into a single projection‑consistent neural operator. By reformulating the calibration problem in log‑implied‑variance coordinates and applying Gyöngy’s quotient Fokker–Planck equation, the authors derive a division‑free residual that can be learned jointly with an SV backbone to satisfy static‑arbitrage, Dupire surface, local‑volatility leverage, and the projection identity. The proposed operator is implemented as both DeepONet and Fourier Neural Operator (FNO) variants, which enforce quote fit, arbitrage constraints, and all calibration requirements in one forward pass. Empirically, this approach reduces calibration latency from 98 ms to under a millisecond while improving error metrics by up to 36 % relative to particle‑based baselines.

## Key Contributions  
- [Finding 1] A division‑free Dupire residual expressed in log‑implied‑variance coordinates and its quotient Fokker–Planck form after Gyöngy projection, enabling a single‑step calibration operator.  
- [Finding 2] Joint learning of an implied‑volatility surface, Dupire local volatility, LSV leverage, and the conditional moment required by the projection identity using DeepONet/FNO implementations that enforce all constraints simultaneously.  
- [Finding 3] Conditional identification proof and empirical consistency demonstration under LSV existence and inverse residual stability, showing latency reduction from 98.5 ms to 0.6 ms with error improvements of 0.1–0.2 pp in forward‑start and cliquet simulations.

## Methodology  
The authors start from a finite set of option quotes and an existing stochastic‑volatility (SV) model that provides marginals. They construct a residual system where the target is to match the observed price surface, enforce static‑arbitrage constraints, reproduce Dupire’s local volatility, compute LSV leverage, and satisfy the projection identity linking implied variance and its conditional moment. The residual is written as a quotient Fokker–Planck equation after Gyöngy projection, which avoids division operations. Using DeepONet or FNO architectures, the network learns an operator that maps input quotes to outputs satisfying all constraints in one forward pass. A witness‑augmented formulation provides a proof of conditional identification and ensures inverse residual stability under LSV existence.

## Results  
Synthetic tests compare the neural‑operator calibration with a particle‑based reference. Forward‑start errors differ by 0.1 pp, cliquet errors by 0.2 pp, while calibration latency drops from 98.5 ms to 0.6 ms. The local‑volatility root‑mean‑square error (RMSE) is reduced by 36 % and leverage RMSE improves by 7–16 % relative to baselines. These gains stem from the amortized nature of the calibration: the heavy solve occurs offline, leaving online inference to a single operator evaluation.

## Significance  
By decoupling the costly fixed‑point solve from real‑time calibration, the method enables sub‑millisecond latency and higher accuracy in LSV pricing, which is critical for high‑frequency trading and risk management. The projection‑consistent neural operator also provides a unified framework that can be extended to other market models requiring similar calibration constraints.

## Related Concepts  
local stochastic volatility (LSV), McKean–Vlasov fixed point, static arbitrage constraints, projection identity, Gyöngy quotient Fokker–Planck equation, DeepONet, Fourier Neural Operator, Dupire local volatility, conditional identification, inverse residual stability.
