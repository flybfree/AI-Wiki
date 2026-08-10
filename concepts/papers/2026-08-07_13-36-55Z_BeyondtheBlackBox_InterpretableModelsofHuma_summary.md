# Summary: 2026-08-07_13-36-55Z_BeyondtheBlackBox_InterpretableModelsofHumanRandom.md
Saved: 2026-08-09 22:57
Source: 2026-08-07_13-36-55Z_BeyondtheBlackBox_InterpretableModelsofHumanRandom.md
Model: None

---

## Summary  
The paper investigates whether human randomisation failures in O’Neill’s zero‑sum card game can be explained by transparent, interpretable models rather than the black‑box predictions of deep learning. It seeks to identify which behavioural patterns—such as repeat or avoid strategies and management of recent action histories—that capture the predictive signal while remaining explainable. Using a large dataset of 84 060 decisions from 2 802 pairs, the authors compare naive, behavioral, interpretable ML, and deep models. The key insight is that these simple frequency‑based rules are sufficient to predict outcomes without complex architectures.

## Key Contributions  
- Finding 1: Human randomisation failures in O’Neill’s game can be captured by simple frequency‑based rules rather than LSTM predictions.  
- Finding 2: Repeat or avoid behaviour, especially tracking of one's own recent actions, explains most variance in the data.  
- Finding 3: Adding a nested frequency‑tracking extension does not improve out‑of‑sample performance, indicating diminishing returns.

## Methodology  
The authors benchmarked various models against interpretable alternatives and deep learning, using LASSO diagnostics to select features, then extended the EWA specifications with a nested frequency tracking model. They evaluated both in‑sample and out‑of‑sample predictive power to assess explanatory capacity and practical utility.

## Results  
Interpretable models outperformed black‑box LSTMs on out‑of‑sample prediction, with repeat/avoid strategies accounting for roughly 80 % of the variance. The nested frequency extension added negligible improvement, suggesting that the basic rule set is already highly effective.

## Significance  
Demonstrates that human strategic behaviour in this game is largely transparent and can be captured by lightweight statistical rules, challenging reliance on opaque deep models for behavioural analysis and highlighting the value of interpretable machine learning for social science research.

## Related Concepts  
Mixed strategy equilibrium, black‑box sequence models (LSTMs), interpretable machine learning, LASSO diagnostics, EWA specifications, frequency tracking, zero‑sum card game.
