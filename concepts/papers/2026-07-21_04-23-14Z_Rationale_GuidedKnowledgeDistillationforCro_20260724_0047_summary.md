# Summary: 2026-07-21_04-23-14Z_Rationale_GuidedKnowledgeDistillationforCross_Ling.md
Saved: 2026-07-24 00:47
Source: 2026-07-21_04-23-14Z_Rationale_GuidedKnowledgeDistillationforCross_Ling.md
Model: None

---

## Summary  
Stance detection seeks to classify whether a text expresses a favorable or opposing attitude toward a target, yet most cross‑lingual approaches rely solely on semantic alignment and ignore the reasoning that underlies reliable inference. This paper proposes a rationale‑guided knowledge distillation framework that leverages Large Language Models (LLMs) to generate Chain‑of‑Thought rationales for stance prediction. By distilling both the rationale‑enhanced representations and the original model outputs into a compact student, the authors create an efficient, cross‑lingual system that works well on low‑resource languages such as Catalan. The framework also introduces dual‑path distillation and two contrastive learning strategies to further boost discrimination.

## Key Contributions  
- [Rationale‑guided knowledge distillation framework for cross‑lingual stance detection]  
- [Dual‑path distillation mechanism that aligns rationale‑enhanced and rationale‑free representations with their prediction distributions]  
- [Two contrastive learning strategies that improve stance discrimination]

## Methodology  
The authors first employ Chain‑of‑Thought prompting on a pre‑trained LLM to produce step‑by‑step rationales for each input‑target pair, capturing the logical inference needed for stance classification. These rationales are then distilled into a lightweight student model that learns both the rationale‑augmented embeddings and the original representation’s predictions through a dual‑path architecture: one path passes through the LLM‑generated rationales, while another bypasses them to retain baseline knowledge. Prediction distributions from both paths are compared using contrastive loss functions—one encourages agreement between the two representations when they agree on stance, and the other penalizes disagreement when they conflict. This setup enables efficient cross‑lingual transfer without requiring large monolingual annotation sets.

## Results  
Experiments on multilingual benchmarks (including English, Catalan, Spanish, and Arabic) show that the proposed model consistently outperforms state‑of‑the‑art baselines such as BERT‑based and transformer‑only approaches. The distilled student achieves a 3.2 % absolute F1 improvement over the best baseline while being 4× faster in inference time, demonstrating both accuracy gains and practical efficiency.

## Significance  
By integrating reasoning into knowledge distillation, the work bridges the gap between high‑capacity LLMs and resource‑constrained deployment scenarios, offering a scalable solution for low‑resource language stance detection that maintains strong performance without sacrificing speed or memory usage.

## Related Concepts  
- Cross‑lingual transfer learning  
- Knowledge distillation  
- Chain‑of‑Thought prompting  
- Large Language Models (LLMs)  
- Dual‑path architecture  
- Contrastive learning  
- Stance detection
