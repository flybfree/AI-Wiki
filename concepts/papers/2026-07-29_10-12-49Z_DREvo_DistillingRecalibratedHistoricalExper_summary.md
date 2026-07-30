# Summary: 2026-07-29_10-12-49Z_DREvo_DistillingRecalibratedHistoricalExperiencefo.md
Saved: 2026-07-29 20:31
Source: 2026-07-29_10-12-49Z_DREvo_DistillingRecalibratedHistoricalExperiencefo.md
Model: None

---

## Summary  
The paper tackles two persistent problems in harness self‑evolution: (1) the inability of accumulated historical experience to be dynamically reassessed for relevance to the current harness, and (2) the lack of explicit mechanisms that translate valid past evidence into concrete search directions. To overcome these issues, the authors introduce DREvo—a novel framework that combines function‑level evidence anchoring, state‑dependent evidence recalibration, and role‑conditioned search intent distillation—to guide evolution under a limited budget.

## Key Contributions  
- [Finding 1] Identify two limitations in existing methods: lack of dynamic reassessment of whether historical experience remains valid for the current harness, and lack of explicit mechanisms for translating valid historical experience into actionable search directions.  
- [Finding 2] Propose DREvo framework that integrates three components: function‑level evidence anchoring, state‑dependent evidence recalibration, and role‑conditioned search intent distillation to determine which historical evidence remains valid and where the harness should evolve next.  
- [Finding 3] Demonstrate smoother evolution trajectories, achieve the highest accuracy on all five benchmarks, and deliver average gains of 16.2 % on domain reasoning tasks and 14.2 % on agentic tasks over evaluated baselines.

## Methodology  
The authors analyze historical trial data to decide which evidence is still valid for the present harness state; they then recalibrate that evidence based on any changes in the system’s state; finally, they distill search intent conditioned on the role of each component to produce actionable next‑step recommendations. This iterative pipeline operates within a constrained evolution budget, ensuring that each iteration builds on reliable past experience.

## Results  
Under evaluation on five benchmarks (including domain reasoning and agentic tasks), DREvo consistently outperforms all baselines: it yields the highest accuracy scores, with an average improvement of 16.2 % on reasoning benchmarks and 14.2 % on agentic benchmarks. Moreover, the evolution trajectories are smoother, experiencing fewer sharp drops in performance between iterations.

## Significance  
This work advances harness self‑evolution by providing a reliable, data‑driven guidance mechanism that reduces reliance on expert labor and enables scalable AI agents to continuously improve without manual intervention. The smoother evolution and higher accuracy demonstrate the practical benefits of systematically validating and translating historical experience into future search actions.

## Related Concepts  
- Harness: a set of instructions guiding an LLM agent’s behavior.  
- Self‑evolution: iterative improvement of a harness using accumulated trial data.  
- Function‑level evidence anchoring: linking past successes to current function performance.  
- State‑dependent evidence recalibration: adjusting the relevance of historical evidence as the system state evolves.  
- Role‑conditioned search intent distillation: mapping role expectations into concrete next‑step search directions.
