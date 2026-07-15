title: "Summary: 2026-07-01_15-25-21Z_GSRQ_Gain_ShapeResidualQuantizationforSub_1_bitKVC.md"
# Summary: 2026-07-01_15-25-21Z_GSRQ_Gain_ShapeResidualQuantizationforSub_1_bitKVC.md
Saved: 2026-07-01 21:00
Source: 2026-07-01_15-25-21Z_GSRQ_Gain_ShapeResidualQuantizationforSub_1_bitKVC.md
Model: None

---


## Summary  
The paper addresses the storage bottleneck of KV caches in large language models by proposing Gain‑Shape Residual Quantization (GSRQ), a quantization scheme that pushes codebook entries toward sub‑1‑bit precision. It identifies a flaw in standard ℓ₂ K‑means where centroid shrinkage degrades angular fidelity, and introduces Gain‑Shape K‑means to preserve directionality while matching or improving distortion. GSRQ integrates this improved K‑means into a residual quantization pipeline for KV caches. Experiments on LLaMA‑3‑8B show substantial gains in accuracy across LongBench tasks at 1‑bit compared with baselines.  

## Key Contributions  
- Finding 1: Standard ℓ₂ K‑means suffers from centroid shrinkage that reduces angular alignment, harming directional preservation.  
- Finding 2: Gain‑Shape K‑means (GSKM) mitigates this issue by preserving directionality and matching or improving ℓ₂ distortion.  
- Finding 3: GSRQ, built on GSKM, achieves a 22.2 percentage‑point accuracy boost for LongBench tasks at 1‑bit quantization.  

## Methodology  
The authors first analyze the high‑dimensional nature of residual vectors in KV caches and show that Euclidean centroid averaging leads to shrinkage. They replace the standard K‑means with GSKM, which uses gain‑weighted updates to maintain vector orientation. GSRQ then applies this refined codebook learning within a residual quantization framework, encoding only the residuals after initial integer coding.  

## Results  
On LLaMA‑3‑8B, GSRQ outperforms VQLLM and other sub‑1‑bit baselines across all LongBench tasks. At 1‑bit, average accuracy rises from 11.34 to 33.54 points (a 22.20 pp gain). The improvement persists at higher bit rates, confirming robustness.  

## Significance  
By solving the angular fidelity problem in residual quantization, GSRQ enables practical sub‑1‑bit KV cache storage without sacrificing model performance, directly addressing a critical bottleneck for extended‑context LLMs.  

## Related Concepts  
- Key‑Value (KV) cache memory  
- Residual Quantization (RQ)  
- K‑means codebook learning  
- Euclidean centroid shrinkage  
- Gain‑Shape K‑means (GSKM)  
- Sub‑1‑bit quantization
