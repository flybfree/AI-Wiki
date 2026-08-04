# Summary: 2026-08-02_13-03-48Z_AmortizingtheCalibrationTriple_AProjection_Consist.md
Saved: 2026-08-04 00:08
Source: 2026-08-02_13-03-48Z_AmortizingtheCalibrationTriple_AProjection_Consist.md
Model: None

---

## Summary  
The paper proposes a projection‑consistent neural operator that amortizes the calibration of local‑stochastic volatility, replacing costly iterative fixed‑point solves with a single forward pass that respects static‑arbitrage and Dupire constraints. It jointly outputs an implied‑volatility surface, Dupire local volatility, LSV leverage, and the conditional moment required by the projection identity. The approach is derived from option‑price marginals using a division‑free residual in log‑implied‑variance coordinates and a Gyöngy quotient Fokker–Planck equation.

## Key Contributions  
- [Finding 1] A projection‑consistent neural operator that jointly satisfies static‑arbitrage, Dupire, LSV leverage, and the conditional moment constraints.  
- [Finding 2] Derivation of a division‑free Dupre residual in log‑implied‑variance coordinates enabling efficient online calibration.  
- [Finding 3] Empirical evidence showing reduced forward‑start and cliquet errors (0.1–0.2 pp) and latency drop from 98.5 ms to 0.6 ms compared with particle methods.

## Methodology  
The authors construct a residual system for the calibration triple, using DeepONet or Fourier Neural Operator implementations to enforce constraints. Starting from finite quotes they compute a quotient Fokker–Planck equation after Gyöngy projection and train a neural operator that maps option‑price marginals to the required quantities while preserving the projection identity.

## Results  
In synthetic tests, forward‑start error 0.1 pp, cliquet error 0.2 pp; calibration latency 0.6 ms (vs 98.5 ms). Local‑volatility RMSE reduced by 36%; leverage RMSE down 7–16% versus baselines.

## Significance  
By moving the expensive fixed‑point solve offline, online calibration becomes a single operator evaluation, enabling real‑time pricing and improving accuracy; this amortization is crucial for high‑frequency trading where latency and precision are paramount.

## Related Concepts  
local stochastic volatility, Dupire calibration, projection identity, Gyöngy quotient Fokker–Planck equation, DeepONet/FNO neural operators, static arbitrage constraints, residual identification.
