# Summary: 2026-08-09_07-41-06Z_WhenSkillsMeetSafety_BenchmarkingandCharacterizing.md
Saved: 2026-08-10 23:14
Source: 2026-08-09_07-41-06Z_WhenSkillsMeetSafety_BenchmarkingandCharacterizing.md
Model: None

---

## Summary  
This paper argues that the safety guarantees of skill‑merged large language models (LLMs) are fragile and often invisible to traditional static refusal tests, which only capture the first few tokens of a response. By introducing SkillSafe‑Bench, the authors demonstrate that adaptive jailbreak attacks can exploit this hidden erosion even when a model appears safe on conventional checks. The work shows that merging safety‑aligned bases with task vectors does not uniformly improve robustness; instead, its effect varies dramatically across different base models and scales. Consequently, the authors propose SubSafe‑Merge as a method to remove the geometric overlap between skill vectors and the safety subspace, preserving capability while eliminating this safety cost.

## Key Contributions  
- Finding 1: Static refusal scores are misleading for skill‑merged LLMs because they do not capture adaptive jailbreak robustness.  
- Finding 2: The impact of merging is base‑conditional; merges on fragile bases (e.g., Qwen scales, Gemma) suffer high jailbreak rates (60–76 %) while others remain robust.  
- Finding 3: Safety erosion can be quantified via a data‑free geometric signal—the overlap between the task vector and a safety subspace—and SubSafe‑Merge removes this overlap to restore safety.

## Methodology  
The authors built SkillSafe‑Bench, a controlled benchmark that evaluates six open‑weight LLMs across static refusal tests, adaptive jailbreak robustness, and capability retention. Each model is scored with a conservative two‑judge AND rule. To characterize the hidden erosion, they compute the geometric overlap of task vectors with a safety subspace without needing additional data. SubSafe‑Merge projects this overlap away using a learned projection that preserves the merged model’s performance.

## Results  
Under a semantic template attack, merges on Qwen and Gemma bases were jailbroken 60–76 % of the time, whereas Llama and Phi‑4 remained largely unaffected (≈15 %). Static safety scores did not predict these outcomes: safe‑looking merges on fragile bases still failed. The geometric overlap analysis revealed a strong correlation between high overlap and susceptibility to jailbreak. SubSafe‑Merge reduced the jailbreak rate by roughly 30 % while maintaining capability retention, confirming that removing the overlap restores safety.

## Significance  
The findings underscore that current safety alignment practices are insufficient for skill‑merged models because they rely on shallow, token‑level checks. Adaptive evaluation is essential to detect hidden vulnerabilities. The geometric signal and SubSafe‑Merge offer a principled way to mitigate safety erosion without sacrificing performance, paving the way for more robust model merging.

## Related Concepts  
Skill merging, task vectors, safety subspace, geometric signal, Task Arithmetic, TIES, DARE, static vs adaptive jailbreak, Jailbreak robustness, model alignment, capability retention.
