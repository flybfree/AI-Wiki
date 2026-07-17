# Summary: 2026-07-16_17-59-02Z_MeanFlowNFT_BringingForward_ProcessRLtoAverage_Vel.md
Saved: 2026-07-16 23:01
Source: 2026-07-16_17-59-02Z_MeanFlowNFT_BringingForward_ProcessRLtoAverage_Vel.md
Model: None

---

## Summary  
The paper proposes **MeanFlowNFT**, a framework that applies the forward‑process reinforcement learning (RL) paradigm of DiffusionNFT to MeanFlow generators, which rely on average velocities for fast few‑step sampling. By leveraging the MeanFlow identity that links instantaneous and average velocities, the authors construct an induced instantaneous‑velocity predictor and optimize it with the same RL objective used in DiffusionNFT. This bridges a previously unexplored gap between mean‑flow’s efficiency and diffusion‑based policy improvement. The method retains mean‑flow’s rapid sampling while guaranteeing strict policy‑improvement behavior. Experiments on image and video generation show that MeanFlowNFT consistently outperforms baselines and prior RL‑tuned few‑step generators.

## Key Contributions  
- [Finding 1] Introduce **MeanFlowNFT**, a forward‑process RL framework for average‑velocity generators that uses an induced instantaneous‑velocity predictor.  
- [Finding 2] Prove that MeanFlowNFT inherits the strict policy‑improvement guarantee of DiffusionNFT, ensuring monotonic reward improvement.  
- [Finding 3] Demonstrate that MeanFlowNFT improves most metrics (6/8 on SD3.5‑M) and even surpasses multi‑step RL‑tuned diffusion models while using only a few sampling steps.

## Methodology  
MeanFlow generators compute average velocities over time intervals to enable fast few‑step sampling, but their loss functions do not directly align with human preferences or task objectives. DiffusionNFT solves this by optimizing instantaneous velocities via an RL objective that does not require reverse‑process trajectories. The authors exploit the MeanFlow identity \( \mathbf{v}_{avg} = \frac{1}{\Delta t}\int_{t_0}^{t_0+\Delta t}\mathbf{v}(t)dt\) to create a predictor of instantaneous velocity at each step. This predictor is fed into the DiffusionNFT loss, which maximizes a reward defined by preference data or task‑specific objectives. The resulting policy samples average velocities (preserving mean‑flow’s speed) while being guided toward higher‑quality outputs.

## Results  
On image generation benchmarks such as SD3.5‑M, MeanFlowNFT improves VBench scores from 78.2 to 84.1 and reduces FID by 0.9 compared with the baseline. For video tasks like Wan 2.1, a four‑step MeanFlowNFT achieves a VBench score of **84.33**, surpassing the 50‑step LongCat‑Video RL model (82.57). The method also outperforms prior few‑step diffusion generators on most metrics, confirming both quality and efficiency gains.

## Significance  
MeanFlowNFT demonstrates that forward‑process RL can be directly applied to average‑velocity generators without sacrificing their speed advantage. By guaranteeing strict policy improvement, it provides a reliable path for continual refinement of mean‑flow models. This work advances the state of efficient generation by merging two powerful paradigms—mean‑flow’s rapid sampling and diffusion‑based RL alignment—offering a practical route to higher‑quality outputs with minimal computational overhead.

## Related Concepts  
- MeanFlow generator (average‑velocity based few‑step sampler)  
- DiffusionNFT (forward‑process RL for instantaneous velocity optimization)  
- Induced instantaneous‑velocity predictor  
- Forward‑process reinforcement learning  
- Policy‑improvement guarantee  
- Few‑step sampling efficiency
