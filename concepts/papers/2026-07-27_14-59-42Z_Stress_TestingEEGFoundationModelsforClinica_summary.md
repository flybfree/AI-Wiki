# Summary: 2026-07-27_14-59-42Z_Stress_TestingEEGFoundationModelsforClinicalDecodi.md
Saved: 2026-07-27 21:41
Source: 2026-07-27_14-59-42Z_Stress_TestingEEGFoundationModelsforClinicalDecodi.md
Model: None

---

## Summary  
The paper investigates how pretrained EEG foundation models perform across clinical decoding tasks and datasets, focusing on dataset identity and robustness to negative controls. It benchmarks six models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, BIOT) on five tasks using frozen linear probes with various splits. The study reveals that model conclusions can be heavily influenced by evaluation unit, dataset shift, comparator strength, and targeted controls.

## Key Contributions  
- [Finding 1] Frozen REVE achieves an AUROC of 0.568 for Korean dementia detection (CAUEEG), which is lower than classical features (0.769) but still outperforms a randomly initialised encoder (0.570). The ordering persists on a patient‑disjoint held‑out split, confirming dataset‑specific degradation.  
- [Finding 2] Dataset identity is fully decoded from frozen embeddings via PCA (AUROC 1.000 at PCA‑50; 0.9998 after band restriction and per‑epoch z‑scoring), indicating that the model’s representation carries information about which dataset it was trained on.  
- [Finding 3] A randomly initialised encoder outperforms pretrained REVE (0.659 vs 0.570) on the same task, demonstrating that initialization matters more than architecture for this application.

## Methodology  
The authors benchmark six EEG foundation models across five clinical tasks using frozen linear probes. They evaluate robustness with three split strategies: leave‑one‑subject‑out, subject‑grouped, and explicitly identified recording‑level splits. Positive controls include random initialisation, random features, label permutation, scrambled‑label fine‑tuning, and projection sensitivity; negative controls comprise Gaussian random projection and PCA of the embeddings.

## Results  
On Korean dementia (CAUEEG), frozen REVE reaches 0.568 AUROC versus 0.769 for classical features; a patient‑disjoint split yields 0.565 vs 0.768, showing persistent dataset bias. Randomly initialised encoder outperforms REVE (0.659 vs 0.570). In Alzheimer’s disease, Gaussian random projection and PCA of embeddings perform similarly to classical features at the subject level. The clearest controlled positive is cross‑subject ictal detection on CHB‑MIT (n=23), where REVE reaches 0.793 AUROC—9.2 percentage points above a randomly initialised encoder.

## Significance  
These findings underscore that conclusions drawn from EEG foundation models are highly sensitive to evaluation unit, dataset shift, comparator strength, and the presence of targeted negative controls. They call for rigorous validation across diverse datasets and explicit testing against strong negative baselines to avoid over‑interpreting model performance.

## Related Concepts  
EEG foundation models, pretrained embeddings, frozen linear probes, dataset identity decoding, AUROC, ictal detection, negative controls, Gaussian projection, PCA, random initialisation.
