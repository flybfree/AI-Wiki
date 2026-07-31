# Summary: 2026-07-30_09-28-37Z_ExactActionValuesAreNotEnough_Rollout_VerifiedRein.md
Saved: 2026-07-30 20:32
Source: 2026-07-30_09-28-37Z_ExactActionValuesAreNotEnough_Rollout_VerifiedRein.md
Model: None

---

## Summary  
The paper investigates whether a frontier reasoning model can control multi‑zone VAV systems from text without building‑specific training, and whether rollout‑verified reinforcement fine‑tuning (RFT) can produce a deployable open‑weight controller. It demonstrates that while GPT‑5 yields higher electricity savings via RL, its predictions are unstable due to hidden failure in the learned critic’s within‑state ranking. The study shows that exact action values alone cannot guarantee improvement and that rollout verification does not resolve the problem without transition‑focused supervision.

## Key Contributions  
- [Finding 1] Frontier reasoning models like GPT‑5 can achieve competitive VAV control from text, surpassing baseline Guideline 36.  
- [Finding 2] Rollout‑verified reinforcement fine‑tuning (RFT) exposes a hidden failure in the critic’s within‑state ranking, where rollout scores rank actions but do not reflect true next‑state effects.  
- [Finding 3] Exact action values and rollout verification alone are insufficient; transition‑focused supervised fine‑tuning is needed before value‑based RFT to improve controller performance.

## Methodology  
The authors first evaluate a reasoning model (GPT‑5) on a physics‑based four‑zone VAV emulator over three summer days, comparing electricity consumption and compliance with Guideline 36. They then implement TD3‑guided reinforcement fine‑tuning (RFT), using deterministic rollouts to audit the learned critic’s decisions. The open‑weight controller is deployed for 200 steps, and its performance is measured against persistence and baseline.

## Results  
GPT‑5 reduced HVAC electricity by 6.2% but lowered ventilation margin; RFT with rollout verification produced no sustained improvement (sampled‑action returns unchanged) and even increased electricity use compared to baseline. The critic’s within‑state ranking correlation was r=0.9998, indicating unreliable ordering; only 5 of 10 states had correct rollout‑best selection.

## Significance  
This work highlights the gap between exact action values and real‑world control gains, showing that rollout verification can mask model failures and that transition modeling is crucial for robust RL fine‑tuning in HVAC systems.

## Related Concepts  
Multi‑zone VAV control, Model predictive control, Reinforcement learning, Deep reinforcement learning (TD3), Rollout verification, Open‑weight deployment, Text‑to‑control reasoning models, Guideline 36 compliance.
