# Summary: 2026-08-03_06-46-47Z_FRAMES_GuardedandDual_ObjectiveSkillEvolutionforAg.md
Saved: 2026-08-03 23:42
Source: 2026-08-03_06-46-47Z_FRAMES_GuardedandDual_ObjectiveSkillEvolutionforAg.md
Model: None

---

## Summary  
The paper introduces FRAMES, a closed‑loop framework that enables LLM agents to evolve deployable skills within policy‑governed enterprise workflows while maintaining auditability and operational efficiency. It tackles the challenge of cold‑starting new skills from existing assets and then iteratively improving them through consensus‑based mutation, Pareto selection over accuracy and inference cost, and an anti‑regression guarantee that prevents unintended side effects. The framework is designed to produce deployable skill modules that can be integrated into production systems without sacrificing traceability or increasing latency. By combining cold‑start deployment with a principled evolutionary loop, FRAMES offers a practical solution for real‑world LLM agents handling rule‑bound tasks such as document auditing.

## Key Contributions  
- [Finding 1] The framework provides a closed‑loop skill evolution pipeline that starts from existing assets and continuously updates them in production.  
- [Finding 2] It employs consensus‑based mutation combined with Pareto selection to balance accuracy improvements against inference cost while guaranteeing no regression on unrelated cases.  
- [Finding 3] The anti‑regression guarantee ensures that skill evolution preserves auditability, a critical requirement for enterprise compliance.

## Methodology  
FRAMES operates as a closed‑loop system where each policy‑governed workflow is represented by a set of skills. The pipeline begins with cold‑start deployment: existing assets are transformed into initial skill modules. During operation, the framework monitors performance metrics and collects feedback. Mutations are proposed via consensus among multiple candidate skill variants, and Pareto optimization selects those that improve accuracy or reduce cost without worsening other dimensions. An anti‑regression module checks that mutations do not degrade unrelated cases, ensuring auditability is maintained throughout evolution.

## Results  
Experimental evaluation on the internal production system shows that FRAMES achieves the best accuracy‑cost trade‑off among all baselines, delivering measurable gains in task performance while keeping inference latency within acceptable limits. The same improvements are reproduced on tau‑bench, confirming robustness across diverse datasets and configurations.

## Significance  
This work matters because it addresses a critical bottleneck in deploying LLM agents at scale: the need for reliable, auditable skill evolution without sacrificing operational efficiency. By guaranteeing no regression and preserving auditability, FRAMES enables enterprises to continuously improve their rule‑based workflows while meeting compliance standards.

## Related Concepts  
LLM agents, policy‑governed enterprise workflows, cold‑start deployment, consensus mutation, Pareto optimization, anti‑regression guarantees, auditability, inference cost, tau‑bench benchmark.
