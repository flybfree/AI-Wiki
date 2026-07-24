# Summary: 2026-07-20_19-01-12Z_CANDOR_Chance_CalibratedDiscordanceinFrozenFoundat.md
Saved: 2026-07-24 00:25
Source: 2026-07-20_19-01-12Z_CANDOR_Chance_CalibratedDiscordanceinFrozenFoundat.md
Model: None

---

## Summary  
The paper addresses a problem where frozen encoders appear blind because nearest‑neighbor discordance is biased by unequal bank sizes, leading to chance‑level performance that cannot be trusted. It proposes CANDOR, a measure with equal‑size banks symmetric under label swap, fixing the chance level at exactly 0.5. Experiments across 22 encoders and 605 k images show collapse below chance everywhere, indicating no encoder is blind but many are weak. CANDOR can be read before training to flag problematic findings.  

## Key Contributions  
- Introduces CANDOR, a discordance measure that equalizes bank sizes and fixes the chance level at one half.  
- Empirically demonstrates that collapse occurs below chance across all encoders, revealing that weakness is not due to blindness but selection bias.  
- Shows that CANDOR can be evaluated prior to training, providing an early warning of which findings a frozen encoder supports poorly.  

## Methodology  
The authors construct CANDOR by creating two equally sized banks for each image pair, ensuring the measure is invariant under swapping labels. They compute discordance as the fraction of pairs where the nearest‑neighbor from one bank has the opposite label to the other bank’s nearest neighbor. The chance level is fixed at 0.5 because the banks are symmetric. The method is applied across a diverse set of encoders and datasets to assess its calibration.  

## Results  
CANDOR corrects for the bias introduced by unequal banks, resulting in a true chance level of 0.5 across all evaluations. Collapse—where predictions align with random labels—occurs below chance everywhere, confirming that no encoder is blind. The best chest model achieves an AUROC of 84.5 but still misplaces 18.4 % of positive cases near opposite‑label films relative to its own kind. Some heads are correct on all but 2.8 % of cases where a single head misses 35.9 % of positives, indicating the deficit is selection rather than information loss. Erasure retention correlates with collapse and shows no link to objective scale, recency, or size.  

## Significance  
CANDOR provides a transparent, pre‑training assessment that can expose hidden bias in frozen encoders before they are used for decision making. By fixing the chance level and detecting collapse, it improves interpretability and trust in model outputs, especially in high‑stakes medical imaging where blindness could lead to dangerous misclassifications.  

## Related Concepts  
frozen encoder, nearest‑neighbor discordance, chance level, collapse, balanced banks, Lipschitz head margin, erasure retention, AUC, selection bias
