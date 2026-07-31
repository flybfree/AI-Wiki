# Summary: 2026-07-30_17-59-35Z_PAC_MAN_Perception_AwareCBF_RLforWhole_BodySafetyi.md
Saved: 2026-07-30 22:24
Source: 2026-07-30_17-59-35Z_PAC_MAN_Perception_AwareCBF_RLforWhole_BodySafetyi.md
Model: None

---

## Summary  
The paper introduces PAC‑MAN, a perception‑aware CBF‑RL framework that integrates control‑barrier safety with real‑time onboard sensing for whole‑body humanoid dodgeball. It enables the robot to perceive only a ball as segmentation‑masked depth from a head camera while using CBF guidance at training time to enforce clearance across all body links and adversarial motion priors. The approach demonstrates that barrier structure is perception dependent, with Joint‑CBF performing best when accurate ball states are available.

## Key Contributions  
- [Finding 1] PAC‑MAN couples control‑barrier safety constraints with deployment‑realistic onboard sensing, allowing a lightweight policy to operate on limited visual input.  
- [Finding 2] The barrier structure (Joint‑CBF) yields optimal evasion performance only when the ball’s state is accurately observable; it degrades under fixed‑camera observations unless supplemented by a gimbal or runtime filter.  
- [Finding 3] A zero‑shot Link‑CBF policy can be deployed on the Unitree G1 in real world, tolerating imperfect perception and achieving 95 % success across thrown balls.

## Methodology  
The authors train a CBF‑RL agent to maximize clearance while minimizing motion energy, using an adversarial motion prior that encourages evasive reflexes. During training the robot receives full body‑link clearance data; at inference it only sees ball depth from a head‑mounted camera via semantic segmentation. The policy is then evaluated on a controlled any‑link contact benchmark with seeded throws and a deployment loop where the robot walks back to its station between throws.

## Results  
On the controlled benchmark, PAC‑MAN’s policy reaches within a few points of a privileged state oracle that uses only the onboard camera, indicating strong safety. Joint‑CBF outperforms other configurations when ball tracking is precise; under fixed‑camera conditions it recovers with an added gimbal or filter. In the real‑world Unitree G1 test, the lightweight Link‑CBF policy succeeds on 95 % of throws despite imperfect perception and varied ball types.

## Significance  
This work bridges theoretical CBF safety with practical perception constraints in humanoid robots, showing that whole‑body safety can be achieved without expensive hardware. The findings highlight the importance of perceptual observability for barrier design and provide a scalable template for other embodied tasks requiring dynamic safety.

## Related Concepts  
CBF‑RL (Control‑Barrier Framework reinforcement learning), control‑barrier safety, perception‑aware policy, segmentation‑masked depth, adversarial motion prior, whole‑body safety, unitree G1, zero‑shot deployment, joint‑CBF, link‑CBF.
