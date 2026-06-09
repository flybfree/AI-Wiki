# Summary: 2026-06-04_17-59-40Z_TempoVLA_LearningSpeed_ControllableVision_Language.md
Saved: 2026-06-05 02:02
Source: 2026-06-04_17-59-40Z_TempoVLA_LearningSpeed_ControllableVision_Language.md
Model: None

---


## Summary  
TempoVLA introduces a Vision‑Language‑Action model that can control the execution speed of a robot by conditioning on an explicit speed parameter, moving beyond the fixed‑speed policies typical in existing VLAs. The authors discover that the magnitude of each predicted action already governs how fast the robot moves, providing a direct route to controllable motion. They propose Variable‑Speed Trajectory Augmentation (VSTA) to re‑time demonstrations without altering semantics and embed this speed into the model’s conditioning mechanism. Experiments show that TempoVLA can accelerate during low‑risk phases and decelerate for high‑risk ones, while VSTA also improves default performance.

## Key Contributions  
- [Finding 1] Action magnitude directly governs robot motion speed.  
- [Finding 2] Variable‑Speed Trajectory Augmentation (VSTA) can re‑time demonstrations to any target speed with negligible motion error.  
- [Finding 3] TempoVLA integrates VSTA and a model‑side conditioning mechanism for flexible, bidirectional speed control.

## Methodology  
The authors first analyze how current Vision‑Language‑Action systems treat speed as immutable. They then design VSTA, which merges or splits actions in the trajectory according to a target speed while preserving motion semantics. This augmented data is fed into a multimodal model whose policy receives an explicit speed condition. The combined system learns to execute at desired speeds without sacrificing task accuracy.

## Results  
Simulations and real‑world manipulation tasks demonstrate that TempoVLA can smoothly accelerate or decelerate as needed, with speed control working in both directions. VSTA boosts the baseline 1× performance by better utilizing the original demonstration data. The motion error introduced by re‑timing is minimal, confirming that VSTA reliably meets the requested speed.

## Significance  
Enabling robots to adapt their execution speed dynamically improves safety and efficiency in manipulation tasks, especially when low‑risk transit phases demand rapid action while high‑risk contact stages require precise, slow motion. This work moves beyond static policies toward truly controllable multimodal agents.

## Related Concepts  
Vision‑Language‑Action models, Variable‑Speed Trajectory Augmentation (VSTA), multimodal conditioning, action magnitude as a speed proxy, large multimodal language models, dynamic speed control in robotics.

[[2026-06-04_17-59-40Z_TempoVLA_LearningSpeed_ControllableVision_Language.md]]