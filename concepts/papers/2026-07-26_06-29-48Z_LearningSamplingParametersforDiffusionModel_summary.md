# Summary: 2026-07-26_06-29-48Z_LearningSamplingParametersforDiffusionModels.md
Saved: 2026-07-27 20:15
Source: 2026-07-26_06-29-48Z_LearningSamplingParametersforDiffusionModels.md
Model: None

---

## Summary  
Diffusion‑based text‑to‑image models rely on a set of inference‑time parameters—prompt, negative prompt, guidance scale, and noise schedule—that are usually fixed for an entire generation, limiting their adaptability to individual prompts or denoising timesteps. The authors propose LeSAMP, a reinforcement‑learning framework that learns prompt‑conditioned, timestep‑varying sampling policies from human preference data and a vision language model judge. By treating parameter selection as a learning problem, LeSAMP can generate more appropriate schedules than manual baselines. Experiments on Flux.1 and Stable Diffusion 3.5 show up to 73 % win rates using VLM‑as‑a‑judge, confirming the benefit of learned policies.

## Key Contributions  
- [Finding 1] LeSAMP introduces a reinforcement‑learning approach that directly optimizes sampling schedules for each prompt and timestep.  
- [Finding 2] The model leverages human preference scores and VLM‑as‑a‑judge to provide reliable reward signals, improving over static baselines.  
- [Finding 3] Learned policies achieve up to 68 % win rate on human evaluations and 73 % using VLM‑based metrics, demonstrating strong performance gains.

## Methodology  
LeSAMP formulates the selection of sampling parameters as a reinforcement‑learning task: given a user prompt, a large language model emits candidate schedules for guidance scale, negative prompt, noise schedule, etc. A reward function is derived from human preference comparisons and VLM‑based image quality judgments. The policy network is trained to maximize cumulative reward across multiple denoising timesteps, allowing per‑prompt and per‑timestep adaptation.

## Results  
On Flux.1 the LeSAMP model outperformed three baselines with a 68.12 % win rate using human preference scores; on Stable Diffusion 3.5 it reached 73.37 % using VLM‑as‑a‑judge. In a user study, participants preferred LeSAMP outputs over baseline generations in 59.46 % of cases, confirming real‑world relevance.

## Significance  
By automating the choice of inference parameters, LeSAMP complements existing post‑training methods and offers a scalable way to enhance diffusion model fidelity without retraining the core network. This work opens avenues for personalized, context‑aware image generation that can adapt to diverse user preferences and generation stages.

## Related Concepts  
- Diffusion models  
- Sampling schedules (denoising timesteps)  
- Reinforcement learning for policy optimization  
- Human preference modeling  
- VLM‑as‑a‑judge (vision language model evaluation)
