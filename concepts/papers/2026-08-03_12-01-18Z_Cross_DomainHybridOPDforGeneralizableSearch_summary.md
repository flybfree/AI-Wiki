# Summary: 2026-08-03_12-01-18Z_Cross_DomainHybridOPDforGeneralizableSearchAgents.md
Saved: 2026-08-04 00:31
Source: 2026-08-03_12-01-18Z_Cross_DomainHybridOPDforGeneralizableSearchAgents.md
Model: None

---

## Summary  
The paper introduces a hybrid training framework for search agents that balances specialization and general intelligence, directly addressing the alignment tax where gains in specialized performance come at the cost of broader capabilities. By employing cross‑domain expert on‑policy distillation (OPD), the authors distill knowledge from multiple general‑purpose experts into a student model while preserving its overall utility. The framework is built on the Hunyuan3 architecture and jointly optimizes both search specialization and general capability, eliminating the need to trade one for the other. Experiments show that the resulting Yuanbao agent achieves strong search performance without sacrificing its general intelligence.

## Key Contributions  
- Cross‑Domain Expert On‑Policy Distillation (OPD) to distill general‑domain experts into a search‑specialized student.  
- Joint optimization of specialization and general capability, effectively mitigating the alignment tax.  
- Demonstrated that the hybrid model attains competitive search performance while consistently improving its overall generalization across tasks.

## Methodology  
The authors adopt a hybrid training pipeline where an autonomous reinforcement learning (RL) agent performs iterative searches; OPD extracts knowledge from multiple domain‑expert models using on‑policy distillation; the distilled student is fine‑tuned via RL to specialize in search tasks; and the whole process is jointly optimized with loss functions that balance specialization and general performance. This pipeline ensures that the student inherits broad capabilities while being guided toward task‑specific behavior.

## Results  
Experiments on benchmark search benchmarks reveal that the Yuanbao model outperforms baseline agents, achieving up to 12 % higher success rates in search tasks. At the same time, its general QA scores improve by roughly 8 %, indicating no adverse trade‑off. Ablation studies confirm that OPD is essential for preserving generalization, and removing it leads to a noticeable drop in both specialization and overall ability.

## Significance  
This work provides a practical solution to the longstanding specialization–generalization tradeoff, enabling assistants that excel at specific tasks without losing their utility as universal agents. The approach could be extended to other RL‑driven systems beyond search, offering a scalable method for domain‑specific adaptation while maintaining broad competence.

## Related Concepts  
- Reinforcement Learning (RL)  
- On‑Policy Distillation (OPD)  
- Cross‑Domain Knowledge Transfer  
- Alignment Tax  
- Agentic Search  
- Hunyuan3 Architecture
