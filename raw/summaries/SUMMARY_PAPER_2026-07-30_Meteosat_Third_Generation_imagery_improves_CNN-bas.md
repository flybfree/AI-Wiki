---
title: Meteosat Third Generation imagery improves CNN-based SSI retrieval
url: http://arxiv.org/abs/2607.28093v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-05-34Z_MeteosatThirdGenerationimageryimprovesCNN_basedSSI.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper evaluates a multi-imager and multi-resolution CNN that combines MSG SEVIRI and MTG FCI imagery with solar geometry features to retrieve 10‑minute surface solar irradiance over Estonia. The hybrid model reduces RMSE by 8.2 W m⁻² under overcast skies compared with the SEVIRI‑only approach, while showing no significant gain on partly cloudy or clear days relative to SARAH‑3 physics based product.  

## Key Takeaways  
- The hybrid SEVIRI‑FCI CNN model improves SSI retrieval accuracy by 8.2 W m⁻² under overcast conditions, demonstrating that higher resolution MTG FCI imagery benefits machine learning when clouds dominate irradiance.  
- Under cloudy or partly cloudy skies the model’s performance does not differ statistically from a SEVIRI‑only CNN, indicating spatial resolution alone cannot replace physics based methods in those regimes.  
- Compared with SARAH‑3, the hybrid model achieves skill scores of 35 % under overcast conditions and 21 % overall, but still underperforms SARAH‑3 on clear skies.  

## Context  
This study contributes to the growing effort to integrate satellite imagery with machine learning for renewable energy monitoring. By quantifying the trade‑off between spatial resolution gains and cloudy sky limitations, it highlights a nuanced view of model performance that is essential for reliable forecasting.  

## Implications  
For photovoltaic operators relying on automated SSI retrieval, the findings suggest focusing on hybrid models that leverage both high‑resolution imagery and clear‑sky physics when clouds are prevalent. Practitioners should also recognize that clear‑sky conditions remain a challenge for purely data‑driven approaches, guiding future research toward multimodal fusion strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28093v1)
