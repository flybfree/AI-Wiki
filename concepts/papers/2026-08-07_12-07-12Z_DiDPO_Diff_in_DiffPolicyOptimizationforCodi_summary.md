# Summary: 2026-08-07_12-07-12Z_DiDPO_Diff_in_DiffPolicyOptimizationforCodingAgent.md
Saved: 2026-08-09 22:55
Source: 2026-08-07_12-07-12Z_DiDPO_Diff_in_DiffPolicyOptimizationforCodingAgent.md
Model: None

---

## Summary  
Reinforcement learning with Verifiable Reward (RLVR) enables objective feedback for coding agents, yet it struggles to assign credit when a single action creates multiple changes across different code regions. This paper introduces DiDPO, a critic‑free RL method that extracts fine‑grained credit units directly from the structure of code diffs. By splitting whole diffs into semantically coherent anchors using a groupability score, DiDPO can project advantage back to individual response tokens without relying on an external critic. Experiments on long‑horizon coding benchmarks show substantial gains over strong agentic baselines.

## Key Contributions  
- [Finding 1] DiDPO constructs fine‑grained credit units directly from the structure of code diffs, enabling critic‑free RL.  
- [Finding 2] The groupability score algorithm optimally balances the semantic scope of anchors and their group mass.  
- [Finding 3] Experiments demonstrate >10 % improvement over strong baselines on Qwen2.5‑7B‑Coder, narrowing the gap with larger models.

## Methodology  
The authors decompose multi‑turn coding interactions into thought‑action steps and sample trajectories to discover code diffs. Each whole diff is partitioned into similar sub‑diffs using a groupability score that maximizes semantic coherence while minimizing group mass imbalance. These partitions become anchors, forming advantage groups that are then projected back to individual response tokens through a critic‑free mapping.

## Results  
On long‑horizon coding and reasoning benchmarks, DiDPO outperforms strong agentic RL baselines, achieving up to 10 % higher accuracy on Qwen2.5‑7B‑Coder compared with comparable methods; it also narrows the gap between smaller and larger models.

## Significance  
This work provides a principled framework for fine‑grained credit assignment in coding agents, addressing the unique challenge of simultaneous changes across code versions. By focusing on diff structure rather than outcome rewards, DiDPO unlocks more effective training and could be extended to other sequential decision‑making tasks with complex feedback.

## Related Concepts  
- Reinforcement Learning with Verifiable Reward (RLVR)  
- Diff‑in‑Diff credit assignment  
- Groupability score  
- Critic‑free RL  
- Coding agent
