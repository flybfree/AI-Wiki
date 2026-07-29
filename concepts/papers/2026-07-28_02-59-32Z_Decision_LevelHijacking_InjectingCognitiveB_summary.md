# Summary: 2026-07-28_02-59-32Z_Decision_LevelHijacking_InjectingCognitiveBiasinto.md
Saved: 2026-07-28 22:28
Source: 2026-07-28_02-59-32Z_Decision_LevelHijacking_InjectingCognitiveBiasinto.md
Model: None

---

## Summary  
The paper introduces a new class of threat called decision‑level hijacking, in which an attacker can subtly alter the cognitive stance of a large language model (LLM) to influence downstream decisions without any real‑time interaction or training‑process control. It demonstrates that Bit‑Flip Attacks (BFAs) can achieve this with only a few weight bits flipped after deployment, making the manipulation stealthy and low‑cost. To fill this gap, the authors propose CogBias, a framework that injects cognitive bias via a differentiable sentiment evaluator, and BitScout, a tool to locate ultra‑sparse bit locations. The work shows that such minute perturbations can reliably shift model stances on target topics while leaving other tasks largely untouched.

## Key Contributions  
- [Finding 1] Decision‑level hijacking is feasible through sparse bit‑flip attacks that do not require live interaction or retraining.  
- [Finding 2] CogBias converts subjective preferences into optimization signals using a differentiable sentiment evaluator and a multi‑objective loss to preserve non‑target outputs.  
- [Finding 3] BitScout identifies ultra‑sparse bit locations that enable targeted cognitive intervention with minimal weight changes.

## Methodology  
The authors first formalized decision‑level hijacking as the manipulation of an LLM’s internal stance toward a specific topic. They then built CogBias, which treats subjective preferences (e.g., “this is wrong”) as differentiable loss terms that guide weight updates via a sentiment evaluator. A multi‑objective loss function simultaneously minimizes the bias injection while keeping unrelated tasks stable. BitScout employs a sparse optimization algorithm to locate the smallest set of bits whose flips produce the desired stance shift, achieving ultra‑sparse bit‑flip budgets.

## Results  
Experiments on Llama‑3.2‑3B, Mistral‑7B, and Qwen2.5‑14B show that flipping only a handful of bits (often < 0.1 % of total weights) reliably induces a stance shift on controversial factual topics such as “AI safety” or “political bias.” The impact is confined to the targeted task; other generation tasks and overall output distribution remain largely unchanged, confirming the precision of CogBias.

## Significance  
This research reveals that even microscopic perturbations to low‑level weight data can undermine high‑level value alignment in LLMs used for corporate strategy or controversial recommendation systems. It underscores a previously unaddressed vulnerability: attackers can covertly bias model judgments without triggering content filters, posing a serious risk to decision‑making processes.

## Related Concepts  
Decision‑level hijacking, cognitive bias injection, bit‑flip attacks, LLMs, value alignment, sentiment evaluator, multi‑objective loss, sparse optimization, BitScout.
