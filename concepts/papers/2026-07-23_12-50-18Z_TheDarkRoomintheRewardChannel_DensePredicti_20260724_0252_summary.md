# Summary: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Saved: 2026-07-24 02:52
Source: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Model: None

---

## Summary  
The paper investigates why dense per‑step supervision—rewarding an LLM agent for predicting its next observation while the memory follows—fails catastrophically when used together with group‑normalized RL (GRPO). Experiments on Qwen3 models across ALFWorld reveal a “dark room” where agents achieve prediction accuracy of 1.0 but never succeed in the task, freezing episode length at the horizon. The authors identify that the root cause is an invariant z‑scored advantage across all‑fail groups, which turns bounded rewards into unbounded pressure and prevents annealing from working. A variance‑profile criterion can retroactively predict which arms will collapse, showing that signals whose within‑group variance decays with mastery are amplifier‑safe.  

## Key Contributions  
- [Finding 1] Dense per‑step supervision under GRPO produces a “dark room” pathology: prediction accuracy saturates while task success remains zero and episode length is pinned at the horizon.  
- [Finding 2] Removing only the standard‑deviation normalization in GRPO rescues the collapse, indicating that an invariant z‑scored advantage across groups creates unbounded pressure that halts annealing; a two‑line proposition explains this mechanism.  
- [Finding 3] A variance‑profile criterion retroactively predicts which arms will fail and which succeed, demonstrating that signals with decaying within‑group variance are amplifier‑safe and that auxiliary‑loss channels can improve performance without correct labels.  

## Methodology  
The authors trained Qwen3 (1.7B/4B/8B) on ALFWorld using GRPO with a dense prediction reward shaping the agent’s next observation. They performed a single‑factor ablation by disabling only the standard‑deviation normalization, and they built a controlled signal‑delivery matrix that varied only the consumption mechanism while keeping the signal identical. All experiments were run from single seeds; seed replication and group‑size controls are preregistered for reproducibility. The variance‑profile criterion was applied to both observed and preregistered arms to assess predictability of collapse.  

## Results  
Across all runs, agents entered a degenerate absorbing state: prediction accuracy → 1.0, task success → 0%, episode length → horizon. Disabling the GRPO std normalization restores baseline performance, confirming that the invariant z‑scored advantage is the culprit. The variance‑profile criterion correctly predicts failures for arms that had not yet run and matches observed reward‑channel successes (a compatibility check). In a signal‑delivery matrix, the reward channel shows no gain, while the auxiliary‑loss channel yields ~20 points; a shuffled‑gold placebo matches the true gold arm, proving the gap persists without correct labels.  

## Significance  
This work explains why dense supervision can be harmful in long‑horizon RL and provides a diagnostic tool (variance‑profile) to anticipate collapse before it occurs. It also shows that auxiliary loss channels can boost performance without requiring accurate reward labels, offering practical guidance for safe LLM agent design. The findings have broader implications for any scenario where signal variance drives optimization pressure.  

## Related Concepts  
GRPO, dense prediction rewards, z‑scoring, variance profile, reward channel, auxiliary loss, RL annealing, RL safety, long‑horizon task learning.
