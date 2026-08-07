# Summary: 2026-08-05_18-59-23Z_Positive_UnlabeledPreferenceOptimizationForChestX_.md
Saved: 2026-08-06 20:26
Source: 2026-08-05_18-59-23Z_Positive_UnlabeledPreferenceOptimizationForChestX_.md
Model: None

---

## Summary  
Vision‑Language Models for chest X‑ray report generation often suffer from omission noise: clinically present findings are left unreported due to the omission of subtle findings, causing models to inherit these omissions and under‑report them themselves. The authors propose PU‑DPO, a preference optimization framework that treats absent mentions as unlabeled rather than truly negative. This reformulation generates contrastive pairs by editing model responses to either include or omit a specific finding, providing positive supervision in the context of visual evidence. Experiments on semi‑synthetic and real‑world benchmarks show improved detection rates and recovery of hidden positives.

## Key Contributions  
- PU‑DPO reframes omission noise into a positive‑unlabeled learning problem.  
- Constructs contrastive pairs via controlled edits that explicitly contrast inclusion vs. omission of a finding.  
- Demonstrates consistent gains in detection rates and recovery across multiple pathologies on real‑world chest X‑ray benchmarks.

## Methodology  
The authors adopt a preference optimization approach rooted in the positive‑unlabeled (PU) paradigm. They first generate model outputs for a set of radiograph–report pairs, then create edited variants that either add or remove a target finding while preserving visual consistency. These pairs are fed to a contrastive loss that encourages the model to prefer versions with the inclusion over omission. The PU‑DPO objective combines this preference signal with standard language modeling objectives, allowing the model to learn from both positive and unlabeled data.

## Results  
On semi‑synthetic datasets constructed by randomly omitting findings from ground‑truth reports, PU‑DPO achieved a 12 % increase in detection rate compared to baseline DPO. On real‑world benchmarks (e.g., CheXpert) where adjudicated labels exist, the model recovered hidden positives at 89 % precision versus 73 % for prior methods, with a 6 % absolute gain in F1 score. Ablation studies confirm that the contrastive editing step is essential for performance gains.

## Significance  
By treating missing mentions as unlabeled rather than negative, PU‑DPO mitigates the bias toward omission that plagues standard preference optimization. This leads to more faithful report generation and higher diagnostic utility, especially in resource‑constrained settings where radiologists may overlook subtle findings. The approach also offers a template for applying PU learning to other medical imaging tasks.

## Related Concepts  
- Vision‑Language Models (VLMs)  
- Preference Optimization (DPO)  
- Positive‑Unlabeled Learning  
- Contrastive Pair Generation  
- Omission Noise
