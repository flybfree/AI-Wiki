# Summary: 2026-08-06_15-21-42Z_VisualGroundinginZero_ShotVision_LanguageControl.md
Saved: 2026-08-06 22:18
Source: 2026-08-06_15-21-42Z_VisualGroundinginZero_ShotVision_LanguageControl.md
Model: None

---

## Summary  
The paper investigates whether zero‑shot vision‑language controllers truly ground their actions in visual perception or rely on simulator dynamics and biases. It introduces an input‑ablation battery to test this claim, revealing that many models ignore visual cues and produce constant or invariant behavior despite hazardous scenes. The study demonstrates that while some deterministic perception models can estimate lead gaps with low MAE and mirror equivariance, overall performance is limited, supporting the view of VLMs as selective hazard assistants rather than monolithic controllers.  

## Key Contributions  
- [Finding 1] Direct‑action zero‑shot VLM controllers often produce image‑invariant or constant actions even when visual hazards are present.  
- [Finding 2] Deterministic perception models can estimate the lead gap with a 0.090 m MAE and exact mirror equivariance, confirming that sufficient visual information is available.  
- [Finding 3] A symmetry‑consensus guardian improves balanced accuracy on held‑out frames by selecting two models from calibration frames and freezing a 2‑of‑4 hazard vote across original and reflected views.  

## Methodology  
The authors employ an input‑ablation battery across nine direct‑action VLMs, six structured local VLMs, and a VLM‑MPC hierarchy in three simulators (two embodied, one non‑visual). They generate 32 874 scored calls, perform blind‑image controls, repeated identical inputs, lane‑axis reflection, non‑visual baselines, and pipeline integrity checks. Post‑hoc analysis uses a symmetry‑consensus guardian that selects two models from calibration frames and freezes a 2‑of‑4 hazard vote across original and reflected views to evaluate performance on held‑out data.  

## Results  
Direct‑control results are largely negative: the constant‑SLOW policy outperforms a scripted geometric controller, several models are image‑invariant or nearly constant, and longitudinal hazard recognition fails to transform LEFT/RIGHT under reflection. No local VLM meets joint longitudinal and lateral grounding criteria. The deterministic perception model estimates the lead gap with 0.090 m MAE and exact mirror equivariance. The guardian achieves 0.954 balanced accuracy (bootstrapped CI [0.895,0.990]) on 272 held‑out frames; nested leave‑one‑episode‑out recovers the same pair/threshold in all folds. Abstaining raises committed balanced accuracy to 0.973 at 0.824 coverage. Offline modular replay achieves 0.934 action agreement and exact mirror equivariance.  

## Significance  
These findings challenge the assumption that zero‑shot VLMs are full controllers, showing they are bounded and selective, acting as hazard assistants rather than monolithic agents. The empirical evidence supports input‑ablation testing to verify perception grounding and suggests practical solutions such as symmetry‑consensus guardians for robust zero‑shot control in simulation.  

## Related Concepts  
Vision‑language models (VLMs), zero‑shot control, input‑ablation experiments, visual grounding, symmetry‑consensus guardian, balanced accuracy, MAE, mirror equivariance, modular replay, hazard voting.
