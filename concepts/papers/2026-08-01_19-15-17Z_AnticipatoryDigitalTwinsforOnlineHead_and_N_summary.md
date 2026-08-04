# Summary: 2026-08-01_19-15-17Z_AnticipatoryDigitalTwinsforOnlineHead_and_NeckAdap.md
Saved: 2026-08-03 21:29
Source: 2026-08-01_19-15-17Z_AnticipatoryDigitalTwinsforOnlineHead_and_NeckAdap.md
Model: None

---

## Summary  
The paper proposes anticipatory digital twins to predict treatment‑day anatomy for online adaptive proton therapy, reducing the need for repeated CT scans. It leverages a pretrained foundation‑model deformable registration network without patient‑specific training. The framework uses cross‑patient motion transfer from planning and quality‑assurance CTs to synthesize predicted CTs (pdCTs). This enables personalized online replanning with improved accuracy. The approach addresses the clinical bottleneck of repeated CT acquisition, which is time‑consuming and expensive, and aligns with the growing interest in AI‑driven medical imaging.

## Key Contributions  
- Founding 1: pdCTs improve normalized cross‑correlation by 22.8% compared to static planning CT, demonstrating superior spatial alignment and reduced registration error.  
- Founding 2: Dice scores for OARs increase by 20.2%, indicating better organ protection and reduced risk of toxicity due to more accurate dose distribution.  
- Founding 3: CT number error decreases by 23.4%, showing reduced dose uncertainty and improved treatment planning precision.

## Methodology  
The authors built a digital‑twin framework using a pretrained foundation‑model deformable registration network, which was trained on a large multimodal dataset to capture generic anatomical deformation patterns. First, they align a prior patient's planning CT to the target frame and carry its QACT into that frame; second, they estimate the change between planning and QACT in the prior, then apply it to the target's own planning CT to generate pdCTs with propagated contours. This two‑step registration decouples patient‑specific motion estimation from cross‑patient motion transfer.

## Results  
Using 88 HN patients (planning CT + three QACTs), the method achieved higher registration quality than static planning CT. Normalized cross‑correlation improved by 22.8%, Dice for OARs improved by 20.2%, and CT‑number error reduced by 23.4%. Gains were most pronounced for patients undergoing substantial tumor shrinkage, while stable anatomy yielded modest improvements.

## Significance  
By anticipating anatomy changes, the method reduces patient burden, cost, and treatment delay, enabling true online adaptive proton therapy without repeated imaging. It also improves dose safety by better aligning the Bragg peak to critical structures, which is especially important for pediatric patients.

## Related Concepts  
Anticipatory digital twins, foundation‑model deformable registration network, cross‑patient motion transfer, predicted CT (pdCT), online adaptive proton therapy, quality‑assurance CT (QACT), Bragg peak, organ‑at‑risk dosimetry, AI‑driven registration.
