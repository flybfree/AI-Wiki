# Summary: 2026-07-27_12-53-22Z_MXAttention_Data_FreeOptimalScalingandPre_Normaliz.md
Saved: 2026-07-27 21:37
Source: 2026-07-27_12-53-22Z_MXAttention_Data_FreeOptimalScalingandPre_Normaliz.md
Model: None

---

## Summary  
The paper addresses the quadratic attention bottleneck in diffusion video generation and proposes MXAttention, a data‑free quantization method for MXFP4 attention that mitigates clipping‑underflow scaling and normalization errors. It introduces Universal Optimal Scaling (UOS) to compute a distribution‑independent Qmax=7.25 without calibration or search, and Pre‑Normalization Quantization (PNQ) to quantize unnormalized softmax exponentials before row‑wise summation, preserving normalization by construction. Experiments on Wan2.2 and HunyuanVideo demonstrate that MXAttention closes at least 95% of the VBench Imaging Quality gap between OCP MXFP4 and FP16 while substantially improving frame‑level similarity. The method preserves FP16‑level generation quality with less than 0.01 absolute degradation on all reported VBench metrics.  

## Key Contributions  
- UOS provides a distribution‑independent optimal scaling boundary Qmax=7.25 that can be derived analytically without calibration or search.  
- PNQ eliminates the row‑wise normalization error introduced by quantizing softmax exponentials after summation, preserving normalization mathematically.  
- MXAttention achieves a 95% reduction in the VBench Imaging Quality gap between OCP MXFP4 and FP16 while maintaining generation quality.  

## Methodology  
The authors analyze the periodic structure of power‑of‑two microscaling to derive an optimal scaling boundary analytically, eliminating the need for calibration or search. They then implement Pre‑Normalization Quantization by quantizing unnormalized softmax exponentials before performing row‑wise summation, which mathematically guarantees that normalization is preserved.  

## Results  
On Wan2.2 and HunyuanVideo, MXAttention reduces the VBench quality gap from 5% to under 0.5%, improves frame‑level similarity, and shows less than 0.01 absolute degradation on all VBench metrics compared with OCP MXFP4. The method’s performance is competitive with strong NVFP4 baselines while adding negligible overhead when fused into the attention pipeline.  

## Significance  
This work enables efficient inference in diffusion video generation models without sacrificing image quality, addressing a critical bottleneck for real‑time deployment. By preserving FP16‑level visual fidelity, MXAttention supports higher‑resolution and longer‑duration video generation at lower computational cost.  

## Related Concepts  
MXFP4 attention, quantization, scaling boundaries, softmax normalization, VBench, power‑of‑two microscaling, data‑free optimization.
