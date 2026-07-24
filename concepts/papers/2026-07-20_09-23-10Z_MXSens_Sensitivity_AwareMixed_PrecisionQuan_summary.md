# Summary: 2026-07-20_09-23-10Z_MXSens_Sensitivity_AwareMixed_PrecisionQuantizatio.md
Saved: 2026-07-24 00:14
Source: 2026-07-20_09-23-10Z_MXSens_Sensitivity_AwareMixed_PrecisionQuantizatio.md
Model: None

---

## Summary  
The paper addresses the accuracy‑loss problem inherent in 4‑bit quantization of large language models (LLMs), which is exacerbated by outliers and inefficient scaling techniques. It proposes MXSens, a training‑free sensitivity‑aware mixed‑precision quantization scheme that assigns different mantissa bitwidths (4/6/8) to model columns and layers based on their observed sensitivity to extreme values. By leveraging the hardware‑friendly block structure of MXINT, MXSens eliminates costly dequantization steps and software‑managed scaling while preserving high perplexity. The method achieves state‑of‑the‑art results across several models and tasks, establishing a clear trade‑off between inference speed and accuracy.

## Key Contributions  
- Finding 1: Outliers in quantization cause severe accuracy drops, and current methods are inefficient.  
- Finding 2: Sensitivity varies across layers and columns, not uniform.  
- Finding 3: A training‑free sensitivity‑guided mixed mantissa bitwidth assignment (4/6/8) improves performance.

## Methodology  
MXSens begins with a column‑wise sensitivity analysis that measures how much each quantized weight deviates from its mean under extreme inputs, then extrapolates this to layer‑wise sensitivity. The authors exploit the block‑wise nature of MXINT, which stores scales in hardware and allows mixed mantissa widths per block. Rather than applying a single 4‑bit width uniformly, MXSens dynamically selects 4/6/8 mantissa bits for columns with low vs. high sensitivity, preserving precision where needed while saving resources elsewhere. This assignment is performed at inference time without retraining or additional calibration.

## Results  
In the W4A4KV4 configuration, MXSens attains perplexities of 3.77 on LLaMA‑2‑70B and 7.63 on LLaMA‑3‑8B on WikiText‑2, surpassing existing baselines such as mixed‑precision integer quantization and data‑rotation approaches. The method reduces memory footprint by ~45 % compared to full‑precision inference while maintaining a perplexity within 10 % of the baseline. Ablation studies confirm that sensitivity‑driven bitwidth selection is the primary driver of the improvement, with little impact from the hardware scaling stored in MXINT.

## Significance  
MXSens introduces a principled, training‑free strategy for mixed‑precision quantization that directly targets the root cause of accuracy loss—outlier sensitivity. By aligning mantissa width with per‑column and per‑layer sensitivity, it offers a practical path to higher‑quality 4‑bit inference without sacrificing speed or requiring extensive calibration. This balances resource efficiency with model fidelity, making large‑scale LLMs more deployable on edge devices.

## Related Concepts  
- Mixed‑precision quantization (e.g., FP16/INT8)  
- 4‑bit quantization and its accuracy trade‑offs  
- Outliers in quantized data  
- Data rotation techniques for robustness  
- Microscaling formats such as MXINT, which embed scales in hardware  
- Sensitivity analysis of model parameters
