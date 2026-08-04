# Summary: 2026-08-03_07-54-56Z_FOCUS_FP4OptimizationviaCoupled_RelaxationandDual_.md
Saved: 2026-08-03 23:44
Source: 2026-08-03_07-54-56Z_FOCUS_FP4OptimizationviaCoupled_RelaxationandDual_.md
Model: None

---

## Summary  
Large language models (LLMs) are limited by their massive size and high inference cost, especially when deployed on accelerators that support FP4 quantization formats such as MXFP4 and NVFP4. Existing post‑training quantization methods tightly couple the quantization and dequantization scales to discrete hardware constraints, which restricts accuracy and leaves optimization space unused. This paper introduces **FOCUS**, an end‑to‑end scale‑learning framework that decouples these scales through Coupled‑Relaxation Scaling (CRS) and further refines them with Dual‑Granularity Scaling (DGS). By learning a full‑precision coefficient for CRS and applying DGS at sub‑block granularity, FOCUS achieves state‑of‑the‑art FP4 accuracy without adding inference overhead.  

## Key Contributions  
- [Finding 1] The proposed **FOCUS** framework enables post‑training quantization with learnable scale optimization for FP4 formats, opening an untapped optimization space that is not required by hardware constraints.  
- [Finding 2] **Coupled‑Relaxation Scaling (CRS)** introduces a learnable full‑precision coefficient that relaxes the tight coupling between quantization and dequantization scales while preserving hardware compliance.  
- [Finding 3] **Dual‑Granularity Scaling (DGS)** refines the quantization scale at finer sub‑block granularities, allowing local adaptation to weight distributions for improved accuracy.  

## Methodology  
FOCUS operates as a post‑training quantization pipeline that learns both the scaling factor and its derivative through an end‑to‑end optimization process. CRS replaces the fixed hardware‑driven coefficient with a trainable variable, enabling the model’s scale to adapt independently of the discrete format. DGS then applies this refined scale at a granularity finer than the block level, allowing each sub‑block to have a slightly different scaling factor that matches its local weight statistics. The training objective minimizes a combination of accuracy loss and scale variance, ensuring that the learned scales keep the model within the MXFP4 or NVFP4 range while maximizing performance.  

## Results  
Experiments across multiple LLM families on standard benchmarks demonstrate that FOCUS consistently reaches state‑of‑the‑art FP4 accuracy under both MXFP4 and NVFP4 formats. Importantly, the framework introduces **no additional inference overhead**, confirming that the learned scales are fully compatible with hardware execution paths. The authors release code and quantized models at https://github.com/tencent/AngelSlim for reproducibility.  

## Significance  
By decoupling quantization and dequantization scales through CRS and DGS, FOCUS unlocks a significant amount of optimization potential that was previously constrained by hardware‑specific scaling rules. This leads to smaller model footprints, lower energy consumption, and higher accuracy—key advantages for deploying LLMs at scale in resource‑constrained environments such as edge devices or mobile platforms.  

## Related Concepts  
FP4 quantization, MXFP4 format, NVFP4 format, post‑training quantization, scale optimization, coupled relaxation scaling (CRS), dual granularity scaling (DGS), hardware constraints, end‑to‑end learning, sub‑block granularity adaptation.
