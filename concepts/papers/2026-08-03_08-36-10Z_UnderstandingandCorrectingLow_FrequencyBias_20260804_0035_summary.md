# Summary: 2026-08-03_08-36-10Z_UnderstandingandCorrectingLow_FrequencyBiasinEEGFo.md
Saved: 2026-08-04 00:35
Source: 2026-08-03_08-36-10Z_UnderstandingandCorrectingLow_FrequencyBiasinEEGFo.md
Model: None

---

## Summary  
The authors investigate why increasing the amount of EEG data or model capacity does not consistently boost downstream performance, and they discover a persistent low‑frequency bias that persists across different dataset sizes, model capacities, and pretraining objectives. This bias is traced to the interaction between EEG’s characteristic $1/f^α$ spectral structure and neural networks’ tendency to over‑emphasize low‑frequency components, which is further amplified by the $\ell_2$ loss in masked autoencoders that heavily penalizes high‑power low‑frequency signals. To remedy this, they introduce FAME—a frequency‑balanced masked autoencoding framework that reconstructs time‑frequency activity within predefined EEG bands and treats each band’s reconstruction equally. The proposed method aims to produce spectrally balanced representations suitable for transfer learning.

## Key Contributions  
- **Finding 1:** A persistent low‑frequency bias remains in EEG foundation models regardless of data scale, model capacity, or pretraining objective.  
- **Finding 2:** This bias stems from the $1/f^α$ spectral nature of EEG and is exacerbated by $\ell_2$ reconstruction loss that disproportionately penalizes high‑power low‑frequency components.  
- **Finding 3:** FAME, a frequency‑balanced masked autoencoding framework, standardizes reconstruction targets per band and equalizes band‑specific losses to achieve balanced supervision across the spectrum.

## Methodology  
The authors first conduct an empirical analysis of representation distributions from diverse EEG foundation models, confirming that low‑frequency components dominate the learned features. They then explain how the $\ell_2$ loss magnifies this imbalance by giving disproportionate weight to high‑power low‑frequency signals relative to their reconstruction error. The proposed FAME framework addresses the issue by defining a set of standard EEG bands (e.g., delta, theta, alpha, beta, gamma). During training, each band’s activity is masked in the input while the corresponding band’s time‑frequency representation is reconstructed independently. Crucially, all band losses are given equal weight, ensuring that no single frequency range dominates the overall objective.

## Results  
The authors evaluate FAME on 41 downstream tasks from the OmniEEG‑Bench benchmark. Compared with standard masked autoencoders, FAME learns more spectrally balanced representations and reaches state‑of‑the‑art performance on 24 of those tasks, demonstrating improved generalization across a wide range of applications.

## Significance  
Balancing spectral supervision is essential for developing transferable EEG foundation models that can generalize to unseen tasks and datasets. By mitigating low‑frequency bias, FAME enables more robust and reliable representations, which are critical for real‑world neurophysiological analysis and AI‑driven medical diagnostics.

## Related Concepts  
- $1/f^α$ spectral power law in EEG data  
- Masked autoencoding and foundation models  
- Frequency‑balanced training objectives  
- Spectral representation learning
