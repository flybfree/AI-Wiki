# Summary: 2026-07-22_18-28-38Z_AdaptiveMulti_HorizonReinforcementLearning.md
Saved: 2026-07-24 02:11
Source: 2026-07-22_18-28-38Z_AdaptiveMulti_HorizonReinforcementLearning.md
Model: None

---

## Summary  
The paper addresses the limitation of conventional reinforcement‑learning algorithms that rely on a single, fixed discount factor to balance short‑ and long‑term rewards. By introducing an adaptive multi‑horizon framework, the authors enable agents to dynamically choose among several temporal horizons, thereby capturing both immediate actions and distant goals without manual tuning. Their approach is designed for continual learning environments where tasks change over time, such as the MiniGrid benchmark. The contribution lies in a biologically inspired mechanism that mimics flexible discounting found in animal behavior.

## Key Contributions  
- [Finding 1] Adaptive selection of multiple temporal horizons improves performance across MiniGrid tasks compared with fixed‑horizon baselines.  
- [Finding 2] The method automatically determines optimal discount factors for each horizon, eliminating the need for manual tuning.  
- [Finding 3] Continual learning with task switches benefits from multi‑horizon planning, yielding higher sample efficiency and lower variance.

## Methodology  
The authors propose a hierarchical policy network that maintains a set of learned discount factors indexed by horizon length. At each time step the agent evaluates which combination of these horizons best predicts future reward trajectories using a lightweight surrogate model. The selected horizon(s) are then blended to produce an effective discount factor for the current action selection. This adaptive mechanism is implemented within the standard Q‑learning or policy‑gradient loop, allowing seamless integration with existing RL pipelines.

## Results  
Experiments on three sequentially changing MiniGrid environments show that the adaptive multi‑horizon agent achieves a mean reward increase of 12 % over fixed‑discount baselines. The variance in performance across episodes drops by 35 %, and sample efficiency improves, requiring only 40 % fewer interactions to reach comparable performance. Ablation studies confirm that removing any horizon reduces overall reward, validating the necessity of multi‑horizon flexibility.

## Significance  
By decoupling temporal discounting from manual parameter selection, this work opens a path toward continual learning systems that can adapt to evolving rewards and task structures without human intervention. The biologically inspired design also provides a theoretical bridge between artificial RL and neurobiological reward processing, offering insights into how flexible planning might underlie animal behavior.

## Related Concepts  
- Temporal discounting  
- Reinforcement learning (Q‑learning, policy gradient)  
- Multi‑horizon planning  
- Continual learning  
- MiniGrid benchmark
