---
title: Caliber: Cross-Architecture Extraction-Cost Control for Score-Returning APIs
url: http://arxiv.org/abs/2608.01023v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_05-58-00Z_Caliber_Cross_ArchitectureExtraction_CostControlfo.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
Caliber is an output‑perturbation defense that treats noise selection as a calibration problem to control the trade‑off between supervision loss and query cost. The paper proves monotone agreement degradation for unique maximizers, derives a closed‑form per‑input recovery cost bound, and shows that calibrated Gaussian noise reduces surrogate error by only 0.6–1.4% on average across many models.

## Key Takeaways  
- Monotone agreement degradation occurs when clean logits have a single top scorer; the agreement drops strictly as noise scale increases, giving each target in (1/K, 1) a unique positive scale.  
- A closed‑form minimax lower bound is obtained for the number of repeated queries needed to recover the original logits, and the noise‑utility relationship fits a logistic curve either per model or shared across tasks.  
- Calibration yields mean absolute relative errors between 0.6% and 1.4%, meaning surrogate performance tracks the configured degradation while fixed‑input averaging reduces variance as expected.

## Context  
Model extraction attacks exploit returned scores for knowledge distillation, creating a need for defenses that limit information leakage without sacrificing training efficiency. Caliber’s approach provides provable bounds on query cost and accuracy loss, aligning with trends toward transparent and controllable AI security mechanisms.

## Implications  
For researchers, the per‑input recovery bound offers a clear metric to evaluate defense strength. Practitioners can adopt calibrated noise settings to balance model utility against extraction risk, supporting deployment in high‑stakes environments where data privacy is paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01023v1)
