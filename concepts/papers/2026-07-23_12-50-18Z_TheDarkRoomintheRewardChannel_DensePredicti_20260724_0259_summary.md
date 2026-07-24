# Summary: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Saved: 2026-07-24 02:59
Source: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Model: None

---

## Summary  
The paper investigates why dense per‑step prediction rewards, when paired with group‑normalized RL (GRPO), cause GRPO‑trained language models to catastrophically fail on long‑horizon tasks. By training Qwen‑1.7B/4B/8B on ALFWorld with a “dark room” reward channel that forces the agent to maximize next‑step prediction accuracy, every run converges to an absorbing state where task success is zero despite perfect observation prediction. The authors identify three core findings: (i) removing only GRPO’s standard deviation normalization rescues performance, indicating that bounded rewards become unbounded pressure in all‑fail groups; (ii) a variance‑profile criterion can retroactively predict which arms will collapse and even forecast outcomes for unobserved arms; and (iii) the reward channel is neutral while an auxiliary loss channel yields a ~20‑point gain, proving that signal delivery mechanisms matter more than the dense signal itself.  

## Key Contributions  
- [Finding 1] Dense prediction rewards under GRPO induce a “dark room” pathology: agents achieve near‑perfect observation prediction but zero task success and fixed episode length equal to the horizon.  
- [Finding 2] A single‑factor ablation shows that eliminating only the std normalization of GRPO restores baseline performance, and a two‑line proposition explains why z‑scored advantages remain invariant in all‑fail groups, turning bounded shaping into unbounded pressure.  
- [Finding 3] The variance‑profile criterion predicts collapses, carries preregistered predictions for arms that have not yet run, and is compatible with existing reward‑channel successes, while an auxiliary loss channel provides a measurable benefit over the neutral reward channel.  

## Methodology  
The authors train GRPO on Qwen language models using ALFWorld as a benchmark environment. They employ dense per‑step supervision by rewarding the model for correctly predicting its next observation, which is then normalized within each RL group via standard deviation scaling. To diagnose the collapse, they perform single‑factor ablations (removing only the std normalization) and construct a variance‑profile metric that quantifies how quickly within‑group reward variance decays as mastery increases. A controlled signal‑delivery matrix varies only the consumption mechanism of the dense prediction reward, while an auxiliary loss channel is added to compare gains. All experiments are single‑seeded; seed replication and group‑size controls are preregistered for future verification.  

## Results  
The baseline setup drives every run into a degenerate absorbing state: observation prediction accuracy reaches 1.0, task success drops to 0%, and episode length is pinned at the horizon. Removing only GRPO’s std normalization eliminates the collapse, yielding performance comparable to random search. The variance‑profile criterion correctly predicts which arms will suffer from all‑fail groups and even forecasts outcomes for previously unobserved arms. In the signal‑delivery matrix, the auxiliary loss channel improves task success by roughly 20 points relative to the neutral reward channel, while a shuffled‑gold placebo matches the true gold arm, confirming that the gap is not due to label leakage.  

## Significance  
These findings clarify why dense supervision can be detrimental in RL, offering a diagnostic framework (variance profiling) for identifying unsafe signal amplification and guiding the design of auxiliary loss mechanisms. The work bridges theoretical insights about z‑scored advantages with practical engineering solutions, potentially preventing similar collapses in future LLM‑driven reinforcement learning systems.  

## Related Concepts  
- GRPO (Group‑Normalized Policy Optimization)  
- Dense prediction rewards  
- Within‑group variance and its decay profile  
- Z‑scoring of advantages  
- Reward channel design  
- Auxiliary loss functions  
- RL policy collapse (“dark room”)
