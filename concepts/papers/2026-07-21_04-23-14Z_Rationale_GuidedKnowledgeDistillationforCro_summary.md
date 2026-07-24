# Summary: 2026-07-21_04-23-14Z_Rationale_GuidedKnowledgeDistillationforCross_Ling.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_04-23-14Z_Rationale_GuidedKnowledgeDistillationforCross_Ling.md
Model: None

---

## Summary  
The paper proposes a rationale‑guided knowledge distillation framework for cross‑lingual stance detection that leverages Chain‑of‑Thought prompting to generate rationales, distills them into a compact student model, and aligns reasoning‑enhanced representations with traditional ones. It introduces dual‑path distillation and contrastive learning strategies to improve performance across low‑resource languages such as Catalan.

## Key Contributions  
- Rationale‑guided knowledge distillation using Chain‑of‑Thought prompts to capture reasoning for cross‑lingual stance detection.  
- Dual‑path distillation mechanism aligning rationale‑enhanced and rationale‑free representations with their prediction distributions.  
- Two contrastive learning strategies that enhance stance discrimination.

## Methodology  
The authors first generate rationales via Chain‑of‑Thought prompting on a large language model, then distill these into a student model. They employ dual‑path architecture: one path uses the distilled reasoning knowledge, the other uses standard features; both feed into the same classifier. Contrastive learning is applied to align representations and prediction distributions across tasks.

## Results  
Experiments on multilingual stance detection benchmarks show consistent improvement over baselines such as BERT‑based models and prior cross‑lingual approaches. The distilled model achieves higher F1 scores, especially in low‑resource languages, with lower computational cost due to the compact student model.

## Significance  
This work bridges the gap between high‑capacity reasoning of LLMs and practical deployment by distilling them into efficient student models, enabling effective cross‑lingual stance detection where data is scarce. It reduces latency and resource usage while preserving accuracy.

## Related Concepts  
- Stance detection: identifying favorable vs opposing attitudes.  
- Cross‑lingual transfer learning: adapting knowledge from high‑resource to low‑resource languages.  
- Knowledge distillation: transferring model knowledge to smaller models.  
- Chain‑of‑Thought prompting: generating step‑by‑step reasoning.  
- Dual‑path architecture: parallel processing of different representations.  
- Contrastive learning: aligning representations via contrastive loss.
