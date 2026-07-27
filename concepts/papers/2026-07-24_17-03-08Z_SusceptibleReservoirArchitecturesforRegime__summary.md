# Summary: 2026-07-24_17-03-08Z_SusceptibleReservoirArchitecturesforRegime_Conditi.md
Saved: 2026-07-26 21:55
Source: 2026-07-24_17-03-08Z_SusceptibleReservoirArchitecturesforRegime_Conditi.md
Model: None

---

## Summary  
Volatility forecasting is dominated by persistence and measurement noise, leaving little residual structure for nonlinear models to exploit. The authors introduce Susceptible Architectures (SUSA), a reservoir‑design framework that captures regime‑conditional volatility dynamics across calm, onset, recovery, and persistent‑stress states. Two concrete implementations—complex‑valued open‑chain reservoirs and periodic reservoirs—are combined with regime‑conditioned expert modules to interpret these features. An open‑system Qiskit implementation uses q‑qubit reservoirs while preserving an AR‑Ridge anchor and a bounded residual correction trained under QLIKE.

## Key Contributions  
- [Finding 1] SUSA provides a principled reservoir design that isolates volatility’s residual structure, enabling nonlinear models to learn meaningful patterns beyond GARCH.  
- [Finding 2] The two reservoir implementations (open‑chain and periodic) each exploit distinct frequency components of the signal, improving forecast accuracy for specific assets such as IWM and XLP.  
- [Finding 3] An ensemble stacking of SUSA forecasts with HARQ‑style predictions yields a statistically significant QLIKE gain of 0.0116 and wins in 75 % of test scenarios.

## Methodology  
The authors adopt a reservoir‑design principle where the input series is fed into a complex‑valued open‑chain or periodic reservoir, generating latent states that encode regime information. Regime‑conditioned experts map these latent states to forecast outputs. An AR‑Ridge model serves as an anchor for the residual correction, and QLIKE loss is used to train the bounded correction. In the quantum variant, q‑qubit reservoirs are simulated in Qiskit while maintaining the same architectural constraints.

## Results  
Experiments were conducted on 16 U.S. equity and exchange‑traded‑fund series using a 12‑observation input window and a five‑observation forecast horizon across three disjoint training, validation, and test folds. SUSA models achieved QLIKE improvements that are statistically significant for IWM and XLP relative to GARCH baselines. Stacked ensembles combining SUSA with HARQ predictions outperformed the strongest constituent by 0.0116 in mean QLIKE and won in 75 % of test cases.

## Significance  
By isolating residual volatility structure through reservoir architectures, SUSA offers a novel pathway to improve nonlinear forecasts beyond traditional GARCH models. The regime‑conditional design enables more robust predictions under varying market conditions, while the ensemble approach demonstrates practical gains in real‑world trading scenarios.

## Related Concepts  
- Reservoir computing: using dynamical systems to learn complex functions.  
- QLIKE loss: a regularized loss function that bounds residual correction.  
- HARQ (Hybrid AR‑GARCH): a hybrid model combining AR and GARCH components.  
- Complex‑valued signals: representing oscillatory data in the complex plane.  
- q‑qubit reservoir: quantum‑inspired reservoir architecture using qubits.
