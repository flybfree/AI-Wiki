---

title: "HaorFloodAlert: Deseasonalized ML Ensemble for 72-Hour Flood Prediction in Bangladesh Haor Wetlands"
url: http://arxiv.org/abs/2605.20167v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-19_17-51-46Z_HaorFloodAlert_DeseasonalizedMLEnsemblefor72_HourF.md
generated_at: "2026-06-11 10:43"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces HaorFloodAlert, a deseasonalized machine‑learning ensemble that predicts flood probability for the Sunamganj haor wetlands within 72 hours. The model combines random forest and XGBoost with a SAR‑derived upstream indicator from Assam’s Barak River, achieving high accuracy on real Sentinel‑1 events.

## Key Takeaways
- The seasonal bias caused by temperature is removed, improving forecast reliability without relying on calendar months as a cheat code.  
- A three‑tier alert pipeline and a BRRI‑calibrated boro rice damage estimator are integrated to operationalize the predictions for flood response.  
- Otsu‑thresholded SAR change detection validates at 84–91 percent spatial match, providing about 36 hours lead time.

## Context
Machine learning ensembles that incorporate remote sensing data are increasingly used for early warning systems in flood‑prone regions. This work demonstrates how a simple preprocessing step—deseasonalization—can boost model performance and make predictions more actionable.

## Implications
Practitioners can deploy HaorFloodAlert to reduce crop loss and improve disaster preparedness without complex seasonal adjustments. The approach offers a scalable template for other wetland flood prediction tasks worldwide.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.20167v1)
