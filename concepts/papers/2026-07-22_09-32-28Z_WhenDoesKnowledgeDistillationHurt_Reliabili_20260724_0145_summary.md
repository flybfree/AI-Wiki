# Summary: 2026-07-22_09-32-28Z_WhenDoesKnowledgeDistillationHurt_Reliability_Awar.md
Saved: 2026-07-24 01:45
Source: 2026-07-22_09-32-28Z_WhenDoesKnowledgeDistillationHurt_Reliability_Awar.md
Model: None

---

## Summary  
The paper investigates when knowledge distillation harms performance in low‑resource language summarization by measuring per‑sample effects on validation loss. It shows that standard KD yields only a negligible ROUGE‑L gain while approximately 51 % of training samples are estimated to actively hurt the student model. To address this, the authors propose two reliability‑aware distillation methods—CHAD and EWAD+CPDP—that selectively retain beneficial teacher signals and discard harmful ones. These approaches achieve substantial ROUGE‑L improvements over both baseline and large teacher models while using only a modest parameter budget.

## Key Contributions  
- [Finding 1] Standard KD improves ROUGE‑L by only +0.0003 on BanSum Bangla but harms ~51 % of training samples.  
- [Finding 2] CHAD and EWAD+CPDP achieve substantial ROUGE‑L gains (+0.0173 and +0.0219 respectively) over standard KD.  
- [Finding 3] EWAD+CPDP outperforms a fine‑tuned Qwen 2.5‑3B model on BanSum, demonstrating high quality with far fewer parameters.

## Methodology  
The authors analyze the per‑sample impact of distillation by measuring gradient alignment between teacher and validation loss to identify samples that would increase student loss. CHAD trains a lightweight gate that generalizes this counterfactual judgment across the full training set. EWAD+CPDP combines token‑level entropy weighting with a capacity‑proportional geometric constraint derived from an incompatible teacher, allowing both methods to generalize their harmfulness detection.

## Results  
On BanSum Bangla, CHAD yields +0.0173 ROUGE‑L while standard KD gains only +0.0003; EWAD+CPDP improves ROUGE‑L by +0.0219 and beats a 50× larger Qwen 2.5‑3B model. Across 15 typologically diverse XL‑Sum languages, EWAD+CPDP outperforms the CE‑only baseline on 10 of them; its performance correlates with complementary teacher signals and weakens when both teachers saturate or share weak language coverage.

## Significance  
The work reveals that knowledge distillation can be detrimental in low‑resource settings and introduces a principled way to select beneficial samples, enabling high‑quality compression without large models. This advances reliability‑aware model training for summarization and provides a template for other sequence‑to‑sequence tasks where teacher signals may mislead.

## Related Concepts  
- Knowledge Distillation  
- ROUGE‑L  
- Counterfactual Harm‑Aware Distillation (CHAD)  
- Entropy‑weighted Adaptive Distillation with Capacity‑Proportional Geometric Constraint (EWAD+CPDP)  
- Low‑resource language summarization  
- Cross‑entropy baseline
