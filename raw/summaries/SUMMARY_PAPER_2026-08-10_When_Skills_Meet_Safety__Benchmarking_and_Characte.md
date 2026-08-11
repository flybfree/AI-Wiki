---
title: When Skills Meet Safety: Benchmarking and Characterizing the Adaptive Jailbreak Robustness of Skill-Merged LLMs
url: http://arxiv.org/abs/2608.08542v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_07-41-06Z_WhenSkillsMeetSafety_BenchmarkingandCharacterizing.md
generated_at: 2026-08-10 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SkillSafe-Bench, a benchmark that evaluates skill‑merged large language models on static refusal scores, adaptive jailbreak robustness, and capability retention using a strict two‑judge AND rule. The study finds that safety alignment is shallow and can be bypassed by adaptive attacks, especially on certain model bases such as Qwen and Gemma. It also reveals that merging does not always degrade safety uniformly across models.

## Key Takeaways
- Static refusal tests fail to predict adaptive jailbreak success; merges on fragile bases are jailbroken 60‑76% of the time while others remain robust.  
- The effect of merging is base‑conditional, and a geometric signal—overlap between task vectors and safety subspaces—explains same‑recipe safety erosion without retraining.  
- SubSafe-Merge projects this overlap away to restore capability while removing the safety erosion.

## Context
Current alignment practices rely on static checks that ignore how models respond to dynamic attacks, leading to a false sense of security for merged systems. This work highlights a gap between theoretical safety and real‑world robustness in adaptive settings.

## Implications
For practitioners, the findings stress the need for ongoing adaptive evaluation when integrating new skills into aligned LLMs. Industry adoption must incorporate such benchmarks to prevent hidden vulnerabilities that could compromise user trust and system integrity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08542v1)
