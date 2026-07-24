# Summary: 2026-07-20_19-01-12Z_CANDOR_Chance_CalibratedDiscordanceinFrozenFoundat.md
Saved: 2026-07-24 00:35
Source: 2026-07-20_19-01-12Z_CANDOR_Chance_CalibratedDiscordanceinFrozenFoundat.md
Model: None

---

## Summary  
Frozen encoders are evaluated by how well a lightweight head reads the true distribution of nearby examples, yet standard discordance measures can be biased when the nearest‑neighbor banks have unequal sizes. The authors introduce CANDOR—a chance‑calibrated discordance that uses equal‑size banks and is symmetric under label swaps—so its chance level is exactly one half. Experiments across 22 encoders, 20 datasets from seven medical domains, and 605 443 images show that collapse falls below chance everywhere, indicating no encoder is blind to the underlying data distribution. This correction reverses earlier conclusions that some encoders are “blind” while still performing modestly on downstream tasks.

## Key Contributions  
- [Finding 1] The proposed CANDOR measure provides a chance‑calibrated discordance that is symmetric under label swap, guaranteeing a fixed chance level of 0.5.  
- [Finding 2] Empirical evidence across 22 encoders, 20 datasets, and 605 443 images shows collapse below chance everywhere, indicating no encoder is blind to the true distribution.  
- [Finding 3] The discrepancy between encoding performance and CANDOR metric reveals that some heads are correct on most cases but miss many due to selection bias rather than lack of information.

## Methodology  
The authors first define frozen encoders as models whose weights never change during training, leaving only a lightweight head to read latent space geometry. Standard nearest‑neighbor discordance compares the density of opposite‑label examples to that of same‑label ones, but unequal bank sizes cause the measure to reflect density rather than true geometric separation. CANDOR addresses this by constructing two banks of equal size for each label and swapping labels; the resulting discordance is invariant to label permutation, fixing its chance level at 0.5. The metric is computed on a held‑out test set before any head is trained, allowing early detection of poor support.

## Results  
CANDOR reverses earlier conclusions: collapse (the proportion of examples where the opposite‑label neighbor wins) is below chance across all evaluated encoders. For example, the best chest model achieves 84.5 AUROC for pneumothorax but still places 18.4 % of those positives nearer an opposite‑label film than its own kind in the same hospital—a clear selection artifact. The same encoder that resolves bird species at 4.5 leaves chest findings at 42.8 and glaucoma at 49.8, performing at chance or worse than random weights. Crucially, CANDOR can be read before training to flag which findings a frozen encoder supports poorly.

## Significance  
This work corrects a systematic misinterpretation of frozen encoder performance by providing an objective, label‑independent discordance metric that is calibrated to chance. It enables researchers and clinicians to identify weak encoders early, reduces reliance on downstream AUROC scores that can be misleading, and clarifies whether observed deficits stem from selection bias rather than genuine lack of information.

## Related Concepts  
frozen encoders, nearest‑neighbor discordance, chance calibration, collapse, Lipschitz heads, normalization margin, selection bias, AUROC, latent space geometry vs density.
