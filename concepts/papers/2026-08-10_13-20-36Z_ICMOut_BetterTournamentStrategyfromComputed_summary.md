# Summary: 2026-08-10_13-20-36Z_ICMOut_BetterTournamentStrategyfromComputedContinu.md
Saved: 2026-08-10 23:50
Source: 2026-08-10_13-20-36Z_ICMOut_BetterTournamentStrategyfromComputedContinu.md
Model: None

---

## Summary  
The paper tackles the limitation of traditional Independent Chip Model (ICM)‑based tournament strategies by introducing Strategic‑Continuation Optimization (SCO), a method that evaluates the full continuation value of each possible current‑hand outcome rather than relying solely on stack‑size prices. By accounting for action order, blind obligations and elimination pressure, SCO produces policies that differ from the fixed‑ICM benchmark and demonstrate measurable gains in prize equity and decision frequency.

## Key Contributions  
- **SCO framework**: Enumerates all current‑hand outcomes, maps them to successor states, computes continuation values from a finite tournament model, and optimizes a frozen current‑hand policy.  
- **Analytic ICM vs. fixed‑ICM gap**: The analytic ICM policy changes the jam frequency by an average of 14.08 % compared with the benchmark, showing that pricing differences directly alter strategy.  
- **Empirical superiority**: SCO’s policy earns $214.33 more prize equity per hand than solver‑built opponents and is favored in 2,433 of 2,838 matched units, outperforming both LLMs and non‑modeling threshold players.

## Methodology  
The authors fix the opponent policies (including any LLM or threshold player) and treat them as constant. Using a three‑player jam/fold tournament with a $1 M prize pool, they compute continuation values for every reachable state via the finite model. An optimizer then selects the best current‑hand action for each seat, freezing the resulting policy. This fixed‑ICM comparison isolates the effect of only the pricing component, allowing direct evaluation of SCO’s advantage.

## Results  
Across 2,838 state–seat entries, the mean absolute value error between analytic ICM and SCO is $9,036. The SCO strategy adds $214.33 to average prize equity per hand and is selected in 2,433 matched units. Moreover, the jam frequency is increased by 14.08 % relative to the fixed‑ICM benchmark, confirming that different pricing leads to substantially altered decision rates.

## Significance  
The study reveals that ICM’s omission of action order and elimination pressure makes it an inadequate objective for tournament strategy construction. SCO demonstrates a concrete value‑to‑policy chain where improved continuation pricing yields higher equity and more rational play, highlighting the need for richer models beyond simple stack‑size evaluation.

## Related Concepts  
Independent Chip Model (ICM), Strategic‑Continuation Optimization (SCO), continuation values, finite tournament model, solver‑based opponent policies, large language model (LLM) strategies, jam/fold tournaments, prize equity, action order, elimination pressure.
