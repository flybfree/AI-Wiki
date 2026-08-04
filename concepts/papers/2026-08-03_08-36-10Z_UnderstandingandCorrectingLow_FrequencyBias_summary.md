# Summary: 2026-08-03_08-36-10Z_UnderstandingandCorrectingLow_FrequencyBiasinEEGFo.md
Saved: 2026-08-04 00:28
Source: 2026-08-03_08-36-10Z_UnderstandingandCorrectingLow_FrequencyBiasinEEGFo.md
Model: None

---

## Summary  
The paper investigates a persistent low‑frequency bias that appears in the representations learned by diverse EEG foundation models despite increasing data scale or model capacity. By linking this bias to the natural $1/f^α$ spectral structure of EEG and the network’s tendency to prioritize low‑frequency components, the authors show that masked autoencoders amplify the imbalance when reconstruction loss is dominated by high‑power low‑frequency signals. They propose FAME—a frequency‑balanced masked autoencoding framework—that standardizes reconstruction targets within each EEG band and gives equal weight to all bands, thereby correcting the bias. The study demonstrates that this correction yields more spectrally balanced representations and state‑of‑the‑art performance on 24 of 41 downstream tasks in OmniEEG‑Bench.

## Key Contributions  
- **Finding 1:** A low‑frequency bias persists across EEG foundation models, dataset sizes, model capacities, and pretraining objectives.  
- **Finding 2:** The bias arises from the interaction between EEG’s $1/f^α$ spectral shape and neural networks’ preference for low‑frequency components, amplified by $\ell_2$ reconstruction loss in masked autoencoders.  
- **Finding 3:** FAME introduces a frequency‑balanced masked autoencoding framework that equalizes supervision across EEG bands, correcting the bias.

## Methodology  
The authors first conducted an empirical analysis of representation distributions from various EEG foundation models, confirming that low‑frequency components dominate regardless of training conditions. They then examined how the $\ell_2$ reconstruction objective in masked autoencoders skews loss toward high‑power low‑frequency signals. To remedy this, they designed FAME: a framework that masks specific frequency bands, reconstructs them independently using band‑specific targets, and aggregates losses with equal weight per band. This approach standardizes supervision across the EEG spectrum, ensuring each band contributes equally to learning.

## Results  
FAME was evaluated on 41 downstream tasks from OmniEEG‑Bench. Compared to baseline models, FAME achieved state‑of‑the‑art performance on 24 tasks and consistently outperformed them on the remaining 17. Additionally, internal analysis showed that FAME’s representations were more spectrally balanced, with reduced variance between high‑frequency and low‑frequency components across all bands.

## Significance  
Balanced spectral supervision is crucial for learning transferable EEG representations; without it, models remain trapped in a low‑frequency trap despite abundant data. FAME provides a practical correction that can be integrated into existing pretraining pipelines, potentially improving performance across diverse downstream applications and reducing the need for massive additional training resources.

## Related Concepts  
- Low‑frequency bias in neural representations  
- $1/f^α$ spectral structure of EEG signals  
- Masked autoencoder (MAE) architecture  
- $\ell_2$ reconstruction loss  
- Frequency‑balanced masking and band‑specific supervision  
- Spectral balance across EEG bands
