# Summary: 2026-07-19_16-01-11Z_TAPAS_Throughput_adaptivePerceptionforAutonomousSy.md
Saved: 2026-07-24 00:12
Source: 2026-07-19_16-01-11Z_TAPAS_Throughput_adaptivePerceptionforAutonomousSy.md
Model: None

---

## Summary  
Autonomous systems must allocate perception resources dynamically to meet varying throughput demands caused by scene complexity, yet existing methods assume a fixed frame‑per‑second (FPS) target and static model‑to‑cluster mapping. TAPAS (Throughput‑adaptive Perception for Autonomous Systems) proposes an RL‑driven strategy that fuses scene‑complexity awareness with a dynamic model‑to‑cluster mapping to deliver the required throughput while minimizing energy consumption on edge platforms such as Jetson Orin NX.

## Key Contributions  
- **Adaptive FPS allocation**: The system estimates an appropriate FPS target based on real‑time scene complexity, eliminating over‑ or under‑provisioning.  
- **Dynamic model‑to‑cluster mapping**: A reinforcement learning (RL) agent with a Reward Reasoning Model (RRM) and GRU orchestrates heterogeneous perception tasks to deliver the needed throughput at minimum energy.  
- **Robust performance on unseen data**: TAPAS maintains high throughput met rates and significant energy savings even on datasets not used during training, such as the nuScenes benchmark.

## Methodology  
TAPAS employs a reinforcement‑learning framework where an RRM provides a reward signal that encodes scene complexity, while a GRU processes temporal observations to predict the optimal FPS target. The predicted target is then mapped to clusters of perception models, allowing the system to switch between lightweight and heavyweight algorithms as needed. Experiments were conducted on Jetson Orin NX hardware using KITTI test sequences and an unseen nuScenes dataset.

## Results  
On KITTI’s test sequences, TAPAS achieves a throughput met rate of 93‑100 % while saving 76 % energy compared with baseline approaches. On the novel nuScenes dataset, it sustains a 97 % throughput met rate and reduces energy consumption by 64 % relative to state‑of‑the‑art methods.

## Significance  
By decoupling perception resource allocation from static assumptions, TAPAS enables autonomous agents to operate efficiently across diverse environments, extending battery life and reducing computational load without sacrificing navigation quality. This adaptability is crucial for real‑world deployment where scene conditions change rapidly.

## Related Concepts  
Throughput‑adaptive perception, scene complexity awareness, dynamic model‑to‑cluster mapping, reinforcement learning, Reward Reasoning Model (RRM), GRU, Jetson Orin NX, KITTI dataset, nuScenes dataset, SOTA approaches.
