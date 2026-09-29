---
title: From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents
url: http://arxiv.org/abs/2609.34132v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_02-11-56Z_FromAttackSuccesstoAttackSeverity_CounterfactualMe.md
generated_at: 2026-09-28 23:18
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the severity of persistent-memory attacks on LLM agents, arguing that current metrics focusing solely on attack success overlook the magnitude of downstream harm caused by malicious memory injections. The authors introduce Counterfactual Memory Regret (CMR) to quantify this severity as the increase in expected loss relative to clean memory and propose MemHarm, a method that optimizes for CMR using sparse semantic edits evaluated through offline paired-loss feedback. Experimental results demonstrate that CMR-guided attacks achieve significantly higher downstream damage than success-optimized attacks while maintaining high success rates across diverse agent benchmarks.

## Key Takeaways
- The study formalizes attack severity using Counterfactual Memory Regret (CMR), defined as the paired increase in expected downstream loss compared to clean memory, establishing a distinct objective beyond binary success metrics that captures the lasting impact of malicious memory writes on agent behavior.
- MemHarm is introduced as an attack framework that predeclares a finite class of sparse, grounded semantic edits and selects candidates by evaluating them through the normal agent memory interface using offline paired-loss feedback, thereby certifying selections that maximize CMR within the defined support.
- Evaluation across two agent benchmarks reveals that CMR-guided selection yields substantially larger downstream loss than attack

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34132v1)
