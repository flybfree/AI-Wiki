# Summary: 2026-07-22_09-32-28Z_WhenDoesKnowledgeDistillationHurt_Reliability_Awar.md
Saved: 2026-07-24 01:39
Source: 2026-07-22_09-32-28Z_WhenDoesKnowledgeDistillationHurt_Reliability_Awar.md
Model: None

---

## Summary  
The paper investigates when knowledge distillation (KD) harms model performance in low‑resource language summarization tasks. It shows that standard KD often degrades validation loss on a large fraction of training samples and only marginally improves ROUGE‑L scores. To remedy this, the authors introduce reliability‑aware distillation methods that evaluate per‑sample usefulness before applying teacher signals. The contributions include empirical findings of harmful samples, two new algorithms (CHAD and EWAD+CPDP), and cross‑language evaluation results.

## Key Contributions  
- Finding 1: Approximately 51.3 % of training samples in BanSum Bangla are estimated to actively harm validation loss under standard KD.  
- Finding 2: CHAD improves ROUGE‑L by +0.0173 over baseline, while EWAD+CPDP improves it by +0.0219, both far exceeding the negligible gain of standard KD (+0.0003).  
- Finding 3: EWAD+CPDP outperforms a fine‑tuned Qwen 2.5‑3B model despite using only 60 M parameters.

## Methodology  
The authors first measure per‑sample KD usefulness by aligning gradients between the student and validation loss, creating a counterfactual judgment that is learned into a lightweight gate (CHAD). For EWAD+CPDP they combine token‑level entropy weighting with adaptive distillation from a second teacher using a capacity‑proportional geometric constraint, ensuring complementary information.

## Results  
On BanSum Bangla, CHAD yields +0.0173 ROUGE‑L and EWAD+CPDP +0.0219, while standard KD gains only +0.0003. Across 15 languages in XL‑Sum, EWAD+CPDP beats the CE‑only baseline on 10/15 languages; performance correlates with complementary teacher signals and degrades where coverage is saturated.

## Significance  
This work demonstrates that blind knowledge distillation can be detrimental, especially for low‑resource tasks, and provides a principled way to select useful teacher information. The methods enable high‑quality compression without large models, supporting efficient summarization in under‑represented languages.

## Related Concepts  
- Knowledge Distillation (KD)  
- Reliability‑aware training  
- Counterfactual judgment  
- Gradient alignment  
- Entropy weighting  
- Capacity‑proportional geometric constraint  
- Low‑resource language summarization
