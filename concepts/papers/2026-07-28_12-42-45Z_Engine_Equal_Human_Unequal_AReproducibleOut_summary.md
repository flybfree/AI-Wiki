# Summary: 2026-07-28_12-42-45Z_Engine_Equal_Human_Unequal_AReproducibleOutcomeSke.md
Saved: 2026-07-28 22:48
Source: 2026-07-28_12-42-45Z_Engine_Equal_Human_Unequal_AReproducibleOutcomeSke.md
Model: None

---

## Summary  
The paper investigates why engine‑equal chess positions that humans actually play are not outcome‑balanced, showing systematic skill biases that persist across different player groups and time periods. It demonstrates that the direction of these biases is stable and reproducible, challenging the assumption that equal engine evaluations guarantee fair human results.

## Key Contributions  
- [Finding 1] The study identifies a consistent outcome skew between actual game results and rating predictions for positions judged essentially equal by Stockfish 18.  
- [Finding 2] The bias reproduces across three independent partitions (primary account set, time control, rating band) and persists eight months later, indicating robustness beyond specific conditions.  
- [Finding 3] A linear relationship between two measurements of the same position’s skew is weak on average but strong for popular positions, suggesting that position popularity amplifies the effect.

## Methodology  
The authors collected 1,661 human‑reached positions from Lichess (October 2025) where Stockfish 18 evaluation was within ±10 centipawns of zero and depth‑stable. They measured each position’s outcome skew as the difference between actual scores and predicted scores based on player ratings. Skew was computed in three disjoint groups: primary account set, time control (blitz/rapid), and rating bands. The same positions were re‑measured eight months later to test temporal stability. The replication slope was estimated by regressing one measurement on the other after controlling for opening family and rating effects.

## Results  
The median absolute skew is about 0.018, corresponding to roughly two percentage‑point advantage for White. The skews are stable across partitions; the replication slope is 0.69 (95 % CI [0.65, 0.74]) and rises to 0.94 on the most popular positions. The effect persists under tighter evaluation bands, deeper search depths, and different popularity cut‑offs. Both blitz and rapid controls show similar patterns.

## Significance  
This work shows that equal engine evaluations are not sufficient for predicting human outcomes; inherent position‑based biases exist and can be exploited by stronger players. It highlights the need for more nuanced models of game fairness beyond simple engine scores, informing future research on causal mechanisms in chess.

## Related Concepts  
- Outcome skew, rating prediction error, replication slope, statistical calibration, engine evaluation stability, positional advantage, observational study design.
