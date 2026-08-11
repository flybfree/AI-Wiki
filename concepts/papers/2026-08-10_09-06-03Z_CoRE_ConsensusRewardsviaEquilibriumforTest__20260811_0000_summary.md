# Summary: 2026-08-10_09-06-03Z_CoRE_ConsensusRewardsviaEquilibriumforTest_TimeRei.md
Saved: 2026-08-11 00:00
Source: 2026-08-10_09-06-03Z_CoRE_ConsensusRewardsviaEquilibriumforTest_TimeRei.md
Model: None

---

## Summary  
The paper introduces **CoRE** (Consensus Rewards via Equilibrium), a novel framework for test‑time reinforcement learning that replaces the brittle majority‑vote reward with a graph‑based equilibrium mechanism producing graded per‑rollout rewards. By modeling the \(N\) rollouts as a network where edges encode answer agreement, reasoning similarity and generation confidence, CoRE extracts a dominant set via replicator dynamics, yielding refined pseudo‑labels, calibrated rewards and a cohesion gate without extra rollouts.

## Key Contributions  
- **Consensus Rewards via Equilibrium (CoRE)** replaces majority voting with a graph‑based equilibrium process that generates graded per‑rollout rewards.  
- A theoretical block‑value analysis shows CoRE strictly generalizes voting, recovers correct minority answers when they outnumber wrong answers by up to 75 %, and improves confidence calibration multiplicatively.  
- Empirically, across seven backbones and five benchmarks (42 model–benchmark cells), CoRE lifts the untrained base by **+21.7** points versus **+20.4** for majority‑vote TTRL; it matches voting plateau accuracy in **54–70 %** fewer steps and wins up to **+7.5** points where agreement is contestable.

## Methodology  
The authors construct a graph whose nodes are the \(N\) rollout answers. Edge weights combine three signals: (i) whether two answers agree, (ii) how similar their reasoning traces are, and (iii) each answer’s generation confidence. Replicator dynamics run on this weighted network to compute the dominant set of nodes, which becomes a refined pseudo‑label. The process also produces a per‑rollout graded reward and a cohesion gate that aggregates node strengths, all without generating additional rollouts.

## Results  
CoRE improves the untrained base by **21.7** points on average compared with **+20.4** for majority‑vote TTRL. In cases where the correct answer is a minority but still wins up to 75 % of votes, CoRE recovers it and adds up to **7.5** additional points over voting. The method reaches the voting baseline’s plateau accuracy in **54–70 %** fewer training steps, demonstrating both higher reward calibration and faster convergence.

## Significance  
Turning a simple ballot box into a calibrated, graded reward that respects reasoning similarity and confidence makes test‑time RL more robust to noisy or contested rollouts. This reduces reliance on majority voting’s brittleness, shortens the path to baseline performance, and offers a principled way to extract richer supervision from unlabeled data.

## Related Concepts  
- Test‑time reinforcement learning (TTRL)  
- Consensus mechanisms in graph theory  
- Replicator dynamics for extracting dominant opinions  
- Belief propagation across belief networks  
- Block‑value analysis of voting thresholds  
- Calibration of confidence scores
