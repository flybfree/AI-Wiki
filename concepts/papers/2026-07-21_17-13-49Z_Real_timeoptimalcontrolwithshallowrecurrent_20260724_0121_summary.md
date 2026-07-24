# Summary: 2026-07-21_17-13-49Z_Real_timeoptimalcontrolwithshallowrecurrentdecoder.md
Saved: 2026-07-24 01:21
Source: 2026-07-21_17-13-49Z_Real_timeoptimalcontrolwithshallowrecurrentdecoder.md
Model: None

---

## Summary  
The paper introduces SHRED‑ROM, a shallow recurrent decoder network based reduced order model that enables real‑time optimal control for high‑dimensional parametric dynamics using only limited sensor readings. By learning from a few expert demonstrations it synthesizes closed‑loop actions and a latent sensor forecaster, thereby overcoming the curse of dimensionality and avoiding costly full‑system simulations. The approach is evaluated on three challenging fluid‑flow and density‑control problems to demonstrate its practical viability.

## Key Contributions  
- [Finding 1] SHRED‑ROM reduces high‑dimensional state spaces to a low‑dimensional representation using shallow recurrent decoder networks.  
- [Finding 2] It learns optimal control policies from limited expert demonstrations, enabling real‑time closed‑loop action without full system simulations.  
- [Finding 3] The method integrates a latent sensor forecaster that predicts and compensates for sensor failures or delays at the model level.

## Methodology  
The authors exploit SHRED‑ROM to synthesize a reduced order model (ROM) where a shallow recurrent decoder network acts as controller. Training uses expert demonstrations; the ROM is trained to mimic optimal control actions in new scenarios. A sensor forecaster is embedded within the latent space to anticipate and correct sensor issues, allowing closed‑loop operation without explicit state estimation.

## Results  
Experiments on three high‑dimensional cases show that SHRED‑ROM achieves near‑optimal performance with computational latency under 10 ms, outperforming traditional model‑predictive controllers that required seconds of simulation time. The controller remains stable despite sensor delays up to 50 ms and fails safely when sensors are noisy or missing.

## Significance  
This work provides a practical framework for deploying optimal control in real‑time across complex, high‑dimensional systems where full state estimation is infeasible, enabling adaptive, robust, and efficient control without heavy computational load.

## Related Concepts  
Reduced order modeling, recurrent neural networks (RNN), shallow decoders, model‑predictive control, sensor forecasting, closed‑loop control, curse of dimensionality, optimal control theory.
