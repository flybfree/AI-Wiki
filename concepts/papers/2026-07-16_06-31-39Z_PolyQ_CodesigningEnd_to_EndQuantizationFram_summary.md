# Summary: 2026-07-16_06-31-39Z_PolyQ_CodesigningEnd_to_EndQuantizationFrameworkfo.md
Saved: 2026-07-23 23:45
Source: 2026-07-16_06-31-39Z_PolyQ_CodesigningEnd_to_EndQuantizationFrameworkfo.md
Model: None

---

## Summary  
PolyQ is a CPU‑oriented compiler/quantization co‑design that enables fractional‑bit quantization for large language models on CPUs while respecting a user‑specified average‑bit budget. It assigns per‑channel bit‑widths from {2,3,4,8,16} and uses compile‑time model compilation to permute channels into homogeneous blocks, generate SIMD‑ and LUT‑compatible kernels, and merge compatible permutations across operators while keeping layout regularization off the runtime path. This turns fine‑grained budget fitting into a practical fractional‑bit deployment method for CPU‑only inference.

## Key Contributions  
- Provides a practical fractional‑bit deployment method for CPU‑only inference using activation‑aware channel‑wise bit allocation.  
- Demonstrates stable quality scaling from 3–6 bits with perplexity improvements up to 32.1 % over prior methods at a 3‑b target, showing that fractional‑bit deployment does not degrade performance.  
- Compiler layout regularization reduces activation reorder traffic by up to 70.8 %, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy/token overhead stays below 2 % relative to an optimized LUT‑based back‑end.

## Methodology  
The authors propose PolyQ, which first allocates per‑channel bit‑widths based on a user‑specified average budget. A compile‑time model compiler then permutes channels into bit‑homogeneous blocks, generates SIMD‑ and LUT‑compatible kernels, merges compatible permutations across operators, and ensures that layout regularization is eliminated from the runtime path.

## Results  
Experiments on Falcon‑H1‑3B, Llama2‑13B, Qwen3‑32B on WikiText‑2 show perplexity improvements of 2.4–32.1 % at a 3‑b budget. Activation reorder traffic is reduced by up to 70.8 %, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy/token overhead stays below 2 % relative to an optimized LUT‑based back‑end.

## Significance  
Fractional‑bit CPU deployment is practical, predictable, and energy‑efficient across diverse edge targets (workstation, laptop, mobile). PolyQ enables scalable on‑device LLMs without sacrificing quality or incurring large overheads, making high‑performance inference feasible on ubiquitous CPUs.

## Related Concepts  
quantization, activation‑aware bit allocation, channel‑wise quantization, compiler co‑design, SIMD kernels, LUT‑based back‑ends, fractional‑bit deployment, CPU‑only LLM inference.
