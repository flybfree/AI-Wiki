# Summary: 2026-09-02_16-19-54Z_SafeEvolve_Harness_PolicyCo_EvolutionfromAgentExpe.md
Saved: 2026-09-02 23:41
Source: 2026-09-02_16-19-54Z_SafeEvolve_Harness_PolicyCo_EvolutionfromAgentExpe.md
Model: None

---

## Summary  
The paper introduces **SafeEvolve**, a framework that jointly evolves both the harness and the policy of LLM‑based agents through experience‑driven co‑evolution to achieve safety alignment. It bridges runtime control with intrinsic safety by converting trajectory‑level safety evidence into reversible, component‑level updates across prompts and hierarchical skills while bootstrapping policies via a two‑stage SFT‑RL paradigm. This continual loop turns safety experience into an evolved runtime harness and improved policy behavior. The approach yields a stronger safety–utility tradeoff than existing baselines.

## Key Contributions  
- [Finding 1] Harness‑policy co‑evolution using on‑policy safety experience creates auditable, reversible component‑level updates.  
- [Finding 2] Two‑stage SFT‑RL bootstraps the policy to leverage evolved harness artifacts and then refines it with verifier‑decomposed rewards.  
- [Finding 3] The framework achieves a stronger safety–utility tradeoff than existing methods on benchmark agents.

## Methodology  
The authors collect on‑policy trajectories, extract safety evidence at trajectory level, and feed it into a harness that updates prompts and hierarchical skill modules via bounded component adjustments. For the policy side, they first fine‑tune the model with harness‑use data (SFT) to generate an initial behavior, then apply reinforcement learning where rewards are decomposed by verifier components to encourage safe multi‑step actions.

## Results  
On Qwen3.5‑4B, SafeEvolve reduces ASR on AgentDojo by a factor of three and raises benign utility from 59.79 % to 61.86 %, outperforming baselines in both safety and utility metrics.

## Significance  
By integrating harness evolution with policy learning, the work moves beyond static alignment toward dynamic, experience‑driven safety that scales across tasks, reducing reliance on external updates and enabling continual improvement.

## Related Concepts  
Harness, policy co‑evolution, SFT‑RL, verifier‑decomposed rewards, trajectory‑level evidence, component‑level updates, runtime harness artifacts, safety–utility tradeoff.
