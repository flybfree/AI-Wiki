# Summary: 2026-07-28_20-43-23Z_EarlyVerdicts_BetterBudgets_SequentialAdaptiveRoll.md
Saved: 2026-07-29 20:21
Source: 2026-07-28_20-43-23Z_EarlyVerdicts_BetterBudgets_SequentialAdaptiveRoll.md
Model: None

---

## Summary  
The paper addresses the inefficiency of rollout generation in reinforcement learning with verifiable rewards (RLVR) by noting that groups often become saturated early, leading to wasted budget on already‑decided prompts. It proposes SARA, a sequential adaptive rollout allocation algorithm that treats rollout collection as an optimal stopping problem and dynamically reallocates budget to promising new prompts while abandoning ineffective ones after a short probe. The method maintains a Beta posterior over each prompt’s success rate and uses a closed‑form predictor of group effectiveness to decide when to commit or abort. By proving abandonment reliability, expected savings, and dominance under fixed budgets, SARA reduces rollouts without sacrificing performance.  

## Key Contributions  
- [Finding 1] The early decision point of groups allows budget reallocation, avoiding waste on saturated prompts that have already decided their effectiveness.  
- [Finding 2] SARA provides a closed‑form predictor and two‑threshold SPRT rule for committing or abandoning groups without extra rollouts.  
- [Finding 3] Theoretical analysis shows abandonment reliability, expected savings, fixed‑budget yield dominance, and links effective‑group yield to the GRPO gradient norm.  

## Methodology  
SARA treats the sequential collection of rollouts as a budget‑constrained optimal stopping problem. For each prompt group it maintains a Beta posterior over its success rate and computes a closed‑form estimate of group effectiveness. When the estimator exceeds a high threshold, the group is committed; if below a low threshold, the group is abandoned after a brief probe, freeing budget for new prompts. The algorithm iteratively allocates rollouts to maximize expected reward under a fixed total budget.  

## Results  
In experiments on 1.5B and 3B language models running on a single GPU, SARA matches DPS (Deep Sample Allocation) in accuracy while using 22 % fewer rollouts, and when combined with DPS yields the highest accuracy at only 67 % fewer rollouts compared to DS oracle. Theoretical analysis confirms that abandoning saturated groups reliably reduces variance and improves the GRPO gradient norm.  

## Significance  
This work alleviates a major bottleneck in RLVR by making rollout budget allocation adaptive, enabling near‑optimal performance with dramatically reduced computational cost—critical for large‑scale language model training where rollouts are expensive.  

## Related Concepts  
RLVR (Reinforcement Learning with Verifiable Rewards), optimal stopping, Beta posterior, SPRT (Sequential Probability Ratio Test), DPS (Deep Sample Allocation), GRPO gradient norm.
