# Summary: 2026-08-06_09-33-09Z_PredictingTaskDifficultyWithoutRollouts.md
Saved: 2026-08-06 20:35
Source: 2026-08-06_09-33-09Z_PredictingTaskDifficultyWithoutRollouts.md
Model: None

---

## Summary  
The paper tackles the challenge of estimating task difficulty from a description alone, without resorting to costly rollouts in long‑horizon environments where empirical trial‑and‑error is computationally prohibitive. By developing a rollout‑free predictor across 17 diverse agentic benchmarks, it offers a scalable way to calibrate evaluation metrics and design progressive training curricula.

## Key Contributions  
- Token‑level entropy serves as a reliable predictive signal for task difficulty.  
- Residuals between expected and observed difficulty expose hidden environment flaws such as contamination or infeasibility.  
- AUC can mask poor difficulty estimates, highlighting the need for more informative evaluation metrics.

## Methodology  
The authors gathered 17 benchmarks spanning coding, mathematics, machine‑learning, web navigation, function calling, and other domains. For each task they measured difficulty via success probability, computed token‑level entropy from the task description, and evaluated predictions using AUC. They also compared predicted versus observed difficulty to generate residuals that reveal systematic deviations.

## Results  
Empirical analysis shows a strong correlation between token entropy and difficulty (AUC ≈ 0.9), indicating that entropy captures most of the predictive information. Residual patterns point to contamination in several tasks, where predicted difficulty diverges from reality. Moreover, standard AUC‑based metrics underestimate true difficulty for certain benchmarks, underscoring their limitations.

## Significance  
Providing rollout‑free difficulty estimates reduces reliance on expensive simulations, enabling environment designers to create fair benchmarks and adaptive training schedules. The findings also reveal systematic biases in existing evaluation pipelines that can be corrected through residual analysis.

## Related Concepts  
task difficulty, rollout‑free prediction, token entropy, AUC, residuals, environment contamination, progressive curriculum learning
