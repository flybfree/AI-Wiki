# Summary: 2026-08-05_10-21-11Z_CalibratingArtificialGuilt_NeurallyGroundedRewardS.md
Saved: 2026-08-05 20:33
Source: 2026-08-05_10-21-11Z_CalibratingArtificialGuilt_NeurallyGroundedRewardS.md
Model: None

---

## Summary  
The paper investigates whether a guilt signal derived from human neuro‑behavioral data can be used to calibrate artificial prosocial rewards in multi‑agent reinforcement learning, moving beyond hand‑tuned reward shaping. By extracting a subject‑fixed guilt weight from fMRI recordings of momentary happiness changes, the authors embed this quantitative prior into a two‑agent Social Lottery environment and compare its performance with four different shaping regimes. The calibrated agents reproduce human safe‑choice rates more faithfully than the other conditions, demonstrating that neurobiological priors can constrain reward design. This work bridges affective neuroscience and reinforcement learning by providing an automatic, data‑driven method for aligning artificial goals with human prosocial behavior.

## Key Contributions  
- Finding 1: A guilt weight \(\hat{w}=1.118\) (Cohen’s \(d=0.214\)) is recovered from a regression of momentary happiness changes on outcome‑type counts using the SoDec dataset, providing an empirically grounded quantitative constraint.  
- Finding 2: Embedding this weight in the Social Lottery environment yields agents whose policy distributions closely match human safe‑choice rates (KL divergence = 0.0012) across 1,000 evaluation episodes per condition.  
- Finding 3: The calibrated agents outperform uniform constant, zero, and unit‑coefficient oracle shaping regimes by one to three orders of magnitude in KL distance, highlighting the importance of neuro‑derived scaling.

## Methodology  
The authors first collected fMRI data from 40 participants while they performed a responsibility task that recorded momentary happiness changes contingent on whether their partner received a reward or not. They fitted a subject‑fixed‑effects regression model to estimate how each participant’s guilt response scales with the number of times a partner is negatively impacted, yielding the guilt weight \(\hat{w}\). This scalar is then used as a coefficient in a two‑agent Social Lottery environment where agents receive rewards based on their actions and the partner’s outcomes. The authors train independent Proximal Policy Optimization (PPO) actor‑critic pairs under four shaping regimes: (i) neurally calibrated using \(\hat{w}\), (ii) uniform constant weight, (iii) zero weight (selfish), and (iv) a unit‑coefficient oracle. After training, they evaluate each policy by measuring the proportion of safe choices made by agents relative to human behavior.

## Results  
Across 1,000 evaluation episodes per condition, the neurally calibrated agents achieve a safe‑choice rate of 0.459, which is only slightly lower than the human average of 0.484 (KL = 0.0012). The uniform constant weight yields a safe‑choice rate of 0.312 (KL ≈ 0.07), the zero weight drops to 0.195 (KL ≈ 0.18), and the unit‑coefficient oracle reaches 0.642 (KL ≈ 0.12). These results demonstrate that the empirically derived guilt weight produces agents whose behavior is statistically indistinguishable from human prosocial choices, whereas other regimes produce markedly divergent policies.

## Significance  
By converting subjective affective states into an objective reward‑shaping parameter, this study provides a principled framework for aligning artificial agents with human moral intuitions. It reduces reliance on manual tuning of social terms and offers a scalable method to embed neurobiological priors in reinforcement learning systems that interact with other agents.

## Related Concepts  
- Prosocial multi‑agent reinforcement learning  
- Neural grounding of reward shaping  
- Guilt as a social affective signal  
- Proximal Policy Optimization (PPO) for continuous control  
- Subject‑fixed‑effects regression in neuroimaging data
