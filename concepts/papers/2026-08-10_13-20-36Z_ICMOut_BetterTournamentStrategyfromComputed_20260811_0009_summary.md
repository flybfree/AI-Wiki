# Summary: 2026-08-10_13-20-36Z_ICMOut_BetterTournamentStrategyfromComputedContinu.md
Saved: 2026-08-11 00:09
Source: 2026-08-10_13-20-36Z_ICMOut_BetterTournamentStrategyfromComputedContinu.md
Model: None

---

## Summary  
The paper demonstrates that the standard Independent Chip Model (ICM) is insufficient for constructing optimal tournament strategies because it ignores action order, blind obligations, and seat rotation. To address this gap, the authors introduce Strategic‑Continuation Optimization (SCO), a method that evaluates current‑hand outcomes by pricing their successor states with continuation values derived from a finite tournament model. SCO produces a fixed‑ICM policy whose moves differ only in the valuation of those states. The resulting strategy yields measurable gains over the benchmark ICM approach, showing that ICM can misprice value and thus produce sub‑optimal decisions.

## Key Contributions  
- [Finding 1] SCO outperforms the frozen strategic‑continuation benchmark by a mean absolute value error of $9,036 across all state–seat entries.  
- [Finding 2] The benchmark’s jam frequency is reduced by an average of 14.08 % when using SCO’s policy, indicating that ICM misprices the risk of busting.  
- [Finding 3] SCO’s strategy earns $214.33 more prize equity per hand on average and is favored in 2,433 of 2,838 matched units.

## Methodology  
The authors enumerate every possible current‑hand outcome (stack sizes and seat positions) for a three‑player jam/fold tournament with a $1 M prize pool. Each outcome is mapped to its successor state within the finite game model. Continuation values are computed analytically from that model, allowing SCO to optimize a policy that maximizes expected value given those continuation prices. The resulting current‑hand policy is then “frozen” so only the focal player’s decisions change while opponents and the continuation evaluator remain fixed.

## Results  
The experimental evaluation shows a mean absolute value error of $9,036 between SCO’s policy and the benchmark ICM policy across 2,838 state–seat entries. This translates to an average increase in jam frequency of 14.08 % relative to the fixed‑ICM range. Moreover, SCO’s strategy generates $214.33 more prize equity per hand on average and is selected in 2,433 matched units out of 2,838, confirming its superiority.

## Significance  
The findings reveal that ICM alone cannot serve as a reliable objective for tournament strategy construction because it neglects the dynamic pressure exerted by large stacks. SCO’s approach—pricing continuation values from a finite model and optimizing policies accordingly—provides a more accurate representation of expected value, highlighting the necessity of incorporating action order and seat rotation into strategic analysis.

## Related Concepts  
Independent Chip Model (ICM), Strategic‑Continuation Optimization (SCO), continuation values, finite tournament model, jam/fold tournament, policy freezing, value‑to‑policy chain.
