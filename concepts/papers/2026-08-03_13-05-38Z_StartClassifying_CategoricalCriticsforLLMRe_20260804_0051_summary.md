# Summary: 2026-08-03_13-05-38Z_StartClassifying_CategoricalCriticsforLLMReinforce.md
Saved: 2026-08-04 00:51
Source: 2026-08-03_13-05-38Z_StartClassifying_CategoricalCriticsforLLMReinforce.md
Model: None

---

## Summary  
The paper proposes replacing the scalar MSE‑based critic in PPO for large language model reinforcement learning with a categorical classifier that maps discretized value support to one‑hot or two‑hot outputs, aiming to improve calibration and reduce variance of advantage estimates. By training this HL‑Gauss PPO using cross‑entropy against smoothed HL‑Gauss targets, the authors show that categorical critics yield better Brier scores and more symmetric advantages across multiple tasks and model sizes.  

## Key Contributions  
- [Finding 1] A categorical predictor head trained via cross‑entropy can replace scalar MSE in PPO for RLVR settings.  
- [Finding 2] The classifier’s output is decoded to a scalar expectation, leaving the actor update distribution unchanged while improving critic signal.  
- [Finding 3] Among various one‑hot, two‑hot and Bernoulli two‑bin critics, HL‑Gauss consistently outperforms baselines on reasoning, tool‑augmented math, and Search‑R1 tasks.  

## Methodology  
The authors adopt Proximal Policy Optimization (PPO) for large language models but replace the standard scalar MSE critic with a categorical classifier. The value support is discretized into a small set of bins; HL‑Gauss generates smoothed target distributions over these bins. During training, cross‑entropy loss compares predicted one‑hot/two‑hot outputs to these targets, producing a categorical critic. The actor’s policy remains unchanged and uses the same GAE scalar advantage calculation; only the critic is modified.  

## Results  
Experiments on three reasoning benchmarks (math reasoning, tool‑augmented math, Search‑R1) with Qwen2.5 and Qwen3 backbones demonstrate that HL‑Gauss PPO improves Brier score and calibration error compared to strong PPO and DAPO baselines. The categorical critics produce more symmetric advantage estimates with lower variance than scalar MSE critics.  

## Significance  
This work shows that categorical value learning can serve as an effective surrogate for critic optimization in reinforcement learning with verifiable rewards, potentially leading to more stable policy updates and better performance without altering the actor’s distribution.  

## Related Concepts  
- Proximal Policy Optimization (PPO)  
- Value function critics (MSE vs. classification)  
- Reinforcement Learning with Verifiable Rewards (RLVR)  
- Advantage estimation and GAE  
- Brier score, calibration error
