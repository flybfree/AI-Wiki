---
title: Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.09228v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_07-51-45Z_PrivilegedSolutionsorContext_InducedTeacherBehavio.md
generated_at: 2026-08-10 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates why On‑Policy Self‑Distillation (OPSD) is often attributed to the transfer of privileged information from a teacher’s reference solution. It finds that while OPSD can improve performance, much of its benefit may stem not from the actual answer but from how the teacher behaves in response to the context created by that solution. The authors introduce On‑Policy Self‑Distillation from Other Problems (OP²SD), which swaps the paired problem‑solution reference for a different example while keeping the student rollout, teacher, and distillation objective unchanged. Experiments across three models and three mathematics benchmarks show OP²SD improves over the base model and stays competitive with OPSD.

## Key Takeaways  
- The reference solution not only provides the correct answer but also alters the context in which the teacher supervises token‑level updates.  
- OP²SD replaces the paired reference with a problem‑solution pair from another example, preserving all other components of the distillation process.  
- OP²SD yields improvements over the base model and remains competitive with OPSD, indicating that gains are not solely due to access to the reference solution.

## Context  
On‑policy self‑distillation is an emerging technique for enhancing large language models without fine‑tuning, relying on a teacher that observes student trajectories. Understanding what drives performance improvements—whether it is the true answer or the surrounding context—is crucial for designing effective distillation pipelines and avoiding overfitting to privileged data.

## Implications  
Practitioners can leverage OP²SD as an alternative reference strategy that reduces reliance on exact solution access, potentially leading to more robust training. Recognizing teacher behavior’s role in context‑induced effects may guide future research into self‑distillation methods that are less sensitive to specific problem instances.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09228v1)
