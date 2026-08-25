---
title: ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based electronic health record modeling
url: http://arxiv.org/abs/2608.21712v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_01-26-40Z_ATHENA_Knowledge_guidedagenticneuralarchitecturese.md
generated_at: 2026-08-24 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces ATHENA, a knowledge‑guided agentic neural architecture search framework that automates design of Transformer‑based EHR models while reusing architectures across hospitals. It achieves performance comparable to four NAS baselines in 9 out of 12 hospital‑task evaluations within a limited search budget.

## Key Takeaways  
- ATHENA uses a weight‑sharing supernet pretrained once per hospital, enabling candidate subnetworks to be fine‑tuned instead of full independent training.  
- It employs a two‑layer cross‑hospital architecture prior: the first layer retrieves high‑performing examples from source sites using task descriptors, and the second uses SHAP meta‑regression to estimate component effects.  
- The multi‑agent LLM search is guided by validation feedback from the target hospital, resulting in consistent architecture selection across repeated runs.

## Context  
Transformer models dominate clinical prediction but require extensive manual tuning that varies with tasks and institutions. Conventional NAS approaches are too costly for such large models, limiting practical deployment.

## Implications  
ATHENA offers a scalable solution that reduces engineering effort and accelerates model rollout across diverse health systems. By leveraging shared knowledge, it can lower costs and improve consistency in EHR‑driven AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21712v1)
