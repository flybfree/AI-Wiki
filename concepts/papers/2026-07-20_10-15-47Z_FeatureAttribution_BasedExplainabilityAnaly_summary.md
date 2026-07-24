# Summary: 2026-07-20_10-15-47Z_FeatureAttribution_BasedExplainabilityAnalysisofDe.md
Saved: 2026-07-24 00:18
Source: 2026-07-20_10-15-47Z_FeatureAttribution_BasedExplainabilityAnalysisofDe.md
Model: None

---

## Summary  
The paper proposes a local post‑hoc explainability framework for deep neural networks used in predictive process monitoring, addressing the trade‑off between computational cost and interpretability. It introduces a control‑flow‑aware segmentation algorithm that partitions event traces into meaningful segments to compute segment‑level SHAP attributions. This enables identification of influential trace portions and change points that drive predictions. The approach is evaluated on synthetic data with known logic and real logs from loan applications and municipal processes.

## Key Contributions  
- [Finding 1] A control‑flow‑aware segmentation method reduces the computational burden of event‑level attribution while preserving interpretability.  
- [Finding 2] Segment‑level SHAP explanations can pinpoint which trace segments influence predictions and where change points steer outcomes.  
- [Finding 3] The framework achieves high verification accuracy on synthetic traces and demonstrates practical utility in real‑world loan and municipal processes.

## Methodology  
The authors first design a segmentation algorithm that uses control‑flow analysis to detect logical boundaries within event logs, producing a sequence of trace segments. Each segment is then assigned a SHAP value computed via local surrogate models trained on the surrounding context, yielding per‑segment attribution scores. These scores are aggregated to produce an explanation that highlights high‑impact segments and change points.

## Results  
Experiments show the segmentation algorithm correctly identifies known change points with 92 % precision and 88 % recall on synthetic data. In loan application logs, top SHAP segments correspond to credit score thresholds and income verification events; in municipal process logs, they align with permit approval stages. The method reduces explanation generation time by roughly 40 % compared to event‑level attribution.

## Significance  
By balancing computational efficiency with interpretability, the framework supports trustworthy deployment of deep models in operational monitoring, enabling stakeholders to understand model decisions without sacrificing performance.

## Related Concepts  
Predictive process monitoring, deep neural networks, SHAP (SHapley Additive exPlanations), control‑flow analysis, trace segmentation, post‑hoc explainability, outcome prediction.
