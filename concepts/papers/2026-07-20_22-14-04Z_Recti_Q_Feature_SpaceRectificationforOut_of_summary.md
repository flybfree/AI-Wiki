# Summary: 2026-07-20_22-14-04Z_Recti_Q_Feature_SpaceRectificationforOut_of_Distri.md
Saved: 2026-07-24 00:27
Source: 2026-07-20_22-14-04Z_Recti_Q_Feature_SpaceRectificationforOut_of_Distri.md
Model: None

---

## Summary  
The paper addresses the Quantization‑Induced Robustness Gap observed when post‑training quantization (PTQ) of large vision models on edge devices degrades robustness under out‑of‑distribution conditions while preserving in‑distribution accuracy. It proposes Recti‑Q, a lightweight feature‑space rectification framework that mitigates this degradation with minimal overhead.

## Key Contributions  
- Finding 1: PTQ causes substantial robustness loss under deployment‑relevant distribution shifts (e.g., sensor noise, severe weather) despite negligible ID accuracy loss.  
- Finding 2: Recti‑Q recovers significant robustness by applying feature‑space rectification using only source data, matching or exceeding FP32 performance on ImageNet‑C and PACS benchmarks.  
- Finding 3: Recti‑Q adds <1 % parameter overhead (as low as 6 KB) and negligible compute cost while preserving >99 % of PTQ memory savings.

## Methodology  
The authors freeze the quantized backbone and train a small classifier‑head LoRA adapter using only source data, enabling teacher‑free training. The rectification operates in feature space, adjusting the representation to improve robustness without retraining the entire model.

## Results  
Across ImageNet‑C and PACS benchmarks, 4‑bit PTQ models show pronounced robustness degradation; Recti‑Q mitigates this loss, achieving performance comparable to FP32 models with only a 6 KB overhead. Memory savings remain >99 %, compute cost is negligible, and OTA resilience patching is enabled.

## Significance  
This work bridges the gap between quantization efficiency and real‑world deployment reliability, allowing edge robots to operate reliably in unpredictable environments while maintaining ultra‑low memory footprints.

## Related Concepts  
- Post‑training quantization (PTQ)  
- Quantization‑induced robustness gap  
- Feature‑space rectification  
- LoRA (Low‑Rank Adaptation)  
- Out‑of‑distribution detection
