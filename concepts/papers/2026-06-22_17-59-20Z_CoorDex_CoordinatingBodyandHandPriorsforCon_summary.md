title: "Summary: 2026-06-22_17-59-20Z_CoorDex_CoordinatingBodyandHandPriorsforContinuous.md"
# Summary: 2026-06-22_17-59-20Z_CoorDex_CoordinatingBodyandHandPriorsforContinuous.md
Saved: 2026-06-23 00:01
Source: 2026-06-22_17-59-20Z_CoorDex_CoordinatingBodyandHandPriorsforContinuous.md
Model: None

---


## Summary  
CoorDex is a learning pipeline that converts high‑dimensional body and hand control into a coordinated latent residual policy, enabling continuous dexterous loco‑manipulation while the humanoid is moving. The method trains privileged motion‑tracking teachers for both the whole body and the 20‑DoF WUJI hand, distills them into proprioception‑conditioned priors, and then uses frozen priors as an action space for downstream reinforcement learning. This architecture preserves natural whole‑body motion while improving finger‑level contact reliability. The result is a system that can perform non‑stop tasks such as bottle grasping, carrying, fridge‑door opening, and cube pick‑and‑turn on the move.

## Key Contributions  
- [Finding 1] CoorDex introduces a coordinated latent residual policy that composes body and hand priors, preserving natural whole‑body motion while improving finger‑level contact reliability.  
- [Finding 2] The method uses privileged motion‑tracking teachers to distill proprioception‑conditioned latent priors from high‑DoF demonstrations, enabling high‑dimensional dexterous control.  
- [Finding 3] Ablations show that joint‑space PPO, monolithic hand control, and joint‑space residual prediction all fail under the same reward budget, whereas the latent‑prior interface succeeds.

## Methodology  
The authors begin with simulated whole‑body and hand demonstrations of humanoid loco‑manipulation. They train two teachers: one that tracks body motion and another that predicts finger trajectories. These teachers are distilled into latent priors that are conditioned on proprioceptive state (e.g., joint angles). The priors are frozen and serve as the action space for downstream residual reinforcement learning; residual heads generate task‑specific corrections while leaving the priors intact.

## Results  
Experiments on a Unitree G1 equipped with a 20‑DoF WUJI hand demonstrate successful execution of non‑stop bottle grasping, carrying, fridge‑door opening, and cube pick‑and‑turn. Ablation results indicate that the latent‑prior interface and coordinated residual structure are essential for high‑DoF contact‑rich tasks; alternative approaches such as joint‑space PPO, monolithic hand control, or joint‑space residual prediction cannot achieve comparable performance within the same reward budget.

## Significance  
This work bridges whole‑body locomotion and fine‑grained dexterous control, allowing continuous humanoid manipulation without stopping—a capability critical for real‑world service robots. By showing that learned priors can act as a bridge between high‑DoF body motion and low‑DoF hand actions, CoorDex opens the door to more natural, task‑rich interactions in mobile humanoids.

## Related Concepts  
latent priors, residual learning, privileged motion tracking, proprioception conditioning, dexterous loco‑manipulation, continuous humanoid manipulation, latent‑prior interface.
