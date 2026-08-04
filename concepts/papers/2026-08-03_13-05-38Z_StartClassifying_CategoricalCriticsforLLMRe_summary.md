# Summary: 2026-08-03_13-05-38Z_StartClassifying_CategoricalCriticsforLLMReinforce.md
Saved: 2026-08-03 23:55
Source: 2026-08-03_13-05-38Z_StartClassifying_CategoricalCriticsforLLMReinforce.md
Model: None

---

## Summary  
The paper proposes a new training objective for the critic component of Proximal Policy Optimization (PPO) when applied to large language models in reinforcement learning with verifiable rewards (RLVR). Instead of using a scalar mean‑squared‑error (MSE) head, it replaces the critic with a categorical classifier that predicts discrete value bins from a discretized support. The classifier is trained via cross‑entropy against smoothed HL‑Gauss targets, and its output is decoded to a scalar expectation for GAE/PPO updates. Experiments on multiple reasoning benchmarks show that this categorical critic consistently outperforms standard PPO and DAPO baselines, indicating that classification‑based learning can serve as an effective surrogate for value estimation in RLVR.

## Key Contributions  
- [Finding 1] A categorical predictor trained with cross‑entropy against HL‑Gauss targets yields a scalar expectation that improves the PPO critic signal compared to scalar MSE.  
- [Finding 2] Ablation studies (one‑hot, two‑hot, Bernoulli two‑bin critics) reveal that neither larger output head nor binary classification alone explains the gains; the improvement is specific to the HL‑Gauss discretization and smoothing strategy.  
- [Finding 3] On reasoning prefixes, tool‑augmented math, Search‑R1, and both Qwen2.5/Qwen3 backbones, HL‑Gauss PPO improves Brier score, calibration error, and produces more symmetric, lower‑variance advantages than strong baselines.

## Methodology  
The authors replace the standard scalar MSE critic head in PPO with a categorical classifier that maps discretized value support to class probabilities. The classifier is trained by cross‑entropy loss against smoothed HL‑Gauss target functions, which provide a more realistic distribution of returns. During inference, the predicted class probabilities are decoded into a scalar advantage estimate using GAE or PPO’s standard update rule; the actor network remains unchanged. This approach avoids distributional assumptions inherent in MSE while preserving the same gradient flow for the policy.

## Results  
Across multiple reasoning tasks and both Qwen2.5 and Qwen3 language models, HL‑Gauss PPO consistently outperforms strong PPO and DAPO baselines. The categorical critic reduces Brier score and calibration error, producing advantages that are more symmetric and exhibit lower variance. These gains persist even when the output head is constrained to one‑hot, two‑hot, or Bernoulli two‑bin configurations, confirming that the improvement stems from the specific HL‑Gauss discretization rather than merely a larger classifier.

## Significance  
Categorical value learning offers a practical alternative to scalar MSE for PPO critics in RLVR settings where rewards are sparse and binary. By leveraging classification objectives, the method improves calibration and reduces variance without altering the actor dynamics, which is crucial for large‑scale language model training. This work opens avenues for more robust reinforcement learning pipelines that can handle verifiable reward signals.

## Related Concepts  
- Proximal Policy Optimization (PPO)  
- Reinforcement Learning with Verifiable Rewards (RLVR)  
- Scalar mean‑squared‑error (MSE) critic head  
- Categorical predictor / classification‑based value learning  
- HL‑Gauss discretization and smoothing strategy  
- GAE (Generalized Advantage Estimation)
