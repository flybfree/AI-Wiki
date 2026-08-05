# Summary: 2026-08-02_05-42-58Z_KING_Embodiment_AwareKinematicGraphNeuralNetworkfo.md
Saved: 2026-08-03 21:34
Source: 2026-08-02_05-42-58Z_KING_Embodiment_AwareKinematicGraphNeuralNetworkfo.md
Model: None

---

## Summary  
This paper introduces KING, a graph neural network that unifies kinematic representations for both wheeled and legged robots by embedding embodiment‑specific structures into a common graph. The primary goal is to enable a single model to estimate odometry using proprioceptive sensors without requiring separate training per robot. By learning from diverse URDF descriptions, KING provides robust generalization across different joint counts and ground‑contact elements such as wheels or feet.  

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- Unified representation: Both wheel kinematics (continuous rotation) and leg kinematics (jointed articulation) can be expressed as a single graph neural network, eliminating the need for separate models.  
- Embodiment‑aware training: KING is trained on a heterogeneous dataset containing multiple robot URDFs, allowing it to learn a shared parameterization that works across different numbers of joints and contact points.  
- Accurate odometry with few‑shot adaptation: Using only an embodiment description (URDF) and onboard encoders/IMU, the model achieves sub‑meter error and can be adapted to a new robot after just one minute of data.  

## Methodology  
The authors construct a kinematic graph where each node corresponds to a joint, wheel, or foot, and edges encode geometric constraints such as distance, angle, and contact. A Graph Neural Network aggregates these constraints to predict the robot’s pose from proprioceptive measurements. The network is trained end‑to‑end on simulated trajectories that include diverse URDFs, with the URDF serving both as a topological embedding and as a source of training data.  

## Results  
In experiments on real wheeled and legged robots, KING estimates odometry with a mean absolute error of 0.8 m, outperforming baseline model‑based methods by more than twofold. The few‑shot adaptation protocol reduces retraining time from hours to under one minute while maintaining performance, as shown in ablation studies across three robot families.  

## Significance  
This work matters because it decouples the kinematic representation from the specific embodiment, enabling a universal odometry estimator that can be applied to any robot without extensive dataset collection. By leveraging few‑shot learning, KING accelerates research and deployment of autonomous mobile platforms, reducing the cost and time associated with model adaptation.  

## Related Concepts  
- Graph Neural Networks (GNN)  
- Kinematic graph  
- URDF  
- Proprioceptive odometry  
- Few‑shot learning  
- Wheel vs leg embodiment
