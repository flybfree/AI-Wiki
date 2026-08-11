# Summary: 2026-08-08_17-59-00Z_LearningunderOpponentUnawarenessinLinear_Quadratic.md
Saved: 2026-08-10 23:05
Source: 2026-08-08_17-59-00Z_LearningunderOpponentUnawarenessinLinear_Quadratic.md
Model: None

---

## Summary  
The paper investigates learning in infinite‑horizon linear‑quadratic stochastic games where players lack information about opponents, observing only a common state and their own action history. It analyzes an asynchronous decentralized ε‑greedy iterated least‑squares (ILS) process for each player. Despite the absence of system parameters, we prove that learning converges almost surely to the complete‑information Nash equilibrium. The convergence rate is characterized analytically.

## Key Contributions  
- Convergence proof: Asymptotic almost sure convergence to Nash equilibrium under opponent unawareness.  
- Rate characterization: Provides explicit bound on convergence speed depending on ε and stochastic dynamics.  
- Empirical validation: Numerical experiments on dynamic Cournot with sticky prices show reduced profits, lower surplus, higher concentration when price stickiness is high; public output revelation speeds up learning.

## Methodology  
The authors model the game as a linear‑quadratic stochastic process where each player’s state is x_i(t) and action u_i(t). They assume asynchronous updates: at discrete times a randomly selected player runs an ε‑greedy iterated least‑squares algorithm that minimizes a quadratic loss based on its own history. The common state s(t) is observed by all, but no opponent actions are revealed. The analysis uses martingale convergence theory and stochastic approximation to derive almost sure convergence.

## Results  
Theoretical results establish that the sequence of strategies converges to the Nash equilibrium with probability one, at a rate O(ε log n). Simulations on a two‑firm Cournot model with sticky prices confirm that high stickiness depresses firm profits and total surplus, increasing market concentration. Introducing a public variable aggregating output reduces these losses and accelerates convergence.

## Significance  
This work bridges algorithmic learning theory and industrial applications, showing that even when firms cannot infer competitors’ moves, decentralized learning can still achieve equilibrium outcomes. The identified welfare trade‑offs under price stickiness highlight the importance of information sharing for market efficiency.

## Related Concepts  
- Linear‑quadratic stochastic games  
- Nash equilibrium convergence  
- ε‑greedy iterated least‑squares (ILS) algorithm  
- Asynchronous decentralized learning  
- Price stickiness in Cournot competition
