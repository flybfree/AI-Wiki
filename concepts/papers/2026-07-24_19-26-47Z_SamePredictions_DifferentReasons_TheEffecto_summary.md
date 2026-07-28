# Summary: 2026-07-24_19-26-47Z_SamePredictions_DifferentReasons_TheEffectofQuanti.md
Saved: 2026-07-27 23:24
Source: 2026-07-24_19-26-47Z_SamePredictions_DifferentReasons_TheEffectofQuanti.md
Model: None

---

## Summary  
The paper investigates how post‑training quantization (PTQ) impacts the interpretability of deep convolutional neural networks, showing that while classification accuracy may stay stable, model explanations can change dramatically. It evaluates five CNN architectures at INT8 and INT4 precision using both spatial attention (Grad‑CAM) and input‑level attribution (LIME). The study introduces a multi‑metric framework to compare full‑precision and quantized models across binary classification tasks.

## Key Contributions  
- Finding 1: Quantization does not guarantee preservation of model explanations; accuracy is not a reliable proxy for interpretability stability.  
- Finding 2: DenseNet161 exhibits strong feature consistency across both precision levels, whereas EfficientNet‑B0 shows significant degradation in input‑level attribution despite good spatial attention and classification performance at INT8.  
- Finding 3: The three comparative metrics (Pearson correlation, SSIM, top‑20% IoU) together reveal distributional and structural variations that highlight which aspects of explanations are affected.

## Methodology  
The authors systematically compare full‑precision and quantized models on two binary datasets. They employ a dual interpretability framework combining Grad‑CAM for spatial attention analysis with LIME for input‑level feature attribution. Interpretability is measured using Pearson correlation coefficient, Structural Similarity Index (SSIM), and top‑20% IoU to capture both distributional and structural differences in model explanations, complemented by deletion/insertion faithfulness analyses.

## Results  
Classification accuracy remains comparable across precision levels, but the metrics show that DenseNet161 maintains high interpretability similarity, while EfficientNet‑B0 exhibits a notable drop in input‑level attribution scores. Spatial attention (Grad‑CAM) is relatively stable for both models at INT8, indicating that some aspects of explanation are preserved.

## Significance  
These findings matter because they warn developers that quantized models may be less trustworthy when interpretability is critical, such as in medical imaging or autonomous systems where understanding model decisions is required. The study underscores the need to consider architecture selection alongside quantization strategy for high‑interpretability applications.

## Related Concepts  
post‑training quantization (PTQ), Grad‑CAM, LIME, static quantization, feature attribution, interpretability, explainability, CNN architectures (VGG19, ResNet18, EfficientNet‑B0, DenseNet161, MobileNetV2), binary classification datasets.
