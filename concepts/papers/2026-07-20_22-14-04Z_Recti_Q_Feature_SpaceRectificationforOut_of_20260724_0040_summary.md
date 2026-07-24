# Summary: 2026-07-20_22-14-04Z_Recti_Q_Feature_SpaceRectificationforOut_of_Distri.md
Saved: 2026-07-24 00:40
Source: 2026-07-20_22-14-04Z_Recti_Q_Feature_SpaceRectificationforOut_of_Distri.md
Model: None

---

## Summary  
The paper addresses the Quantization‑Induced Robustness Gap observed when post‑training quantization (PTQ) of large vision backbones on edge devices degrades robustness to out‑of‑distribution inputs despite minimal accuracy loss. It proposes Recti‑Q, a lightweight feature‑space rectification framework that adds a small classifier‑head LoRA adapter to the frozen quantized backbone. This adaptation recovers lost robustness without retraining the entire model. The solution is architecture‑agnostic, supports teacher‑free training, and incurs negligible parameter overhead.

## Key Contributions  
- Finding 1: PTQ causes significant robustness degradation on ImageNet‑C and PACS despite negligible ID accuracy loss.  
- Finding 2: Recti‑Q recovers a substantial portion of the lost robustness, matching or exceeding FP32 performance in some cases.  
- Finding 3: The rectification adds only ~6 KB extra parameters (≤1 % overhead) and negligible compute cost.

## Methodology  
The authors freeze the quantized backbone, treat it as a source feature extractor, and train a tiny LoRA‑based classifier head on the same data using standard supervised learning. The adapter learns to map quantized features back into a more robust representation, effectively rectifying the feature space without altering quantization or model architecture.

## Results  
Experiments show that 4‑bit PTQ models suffer up to 15 % robustness loss under deployment shifts, while Recti‑Q reduces this to <2 % and often outperforms FP32 baselines. Memory savings remain >99 %, compute overhead is minimal (≈0.1 ms per inference), and the solution scales across CNN and Transformer architectures.

## Significance  
By preserving most of PTQ’s memory benefits while restoring robustness, Recti‑Q enables reliable perception on edge robots operating in unpredictable environments such as severe weather or sensor noise, supporting OTA resilience patches with tiny bandwidth usage.

## Related Concepts  
- Post‑training quantization (PTQ)  
- Quantization‑induced robustness gap  
- Feature‑space rectification  
- LoRA (Low‑Rank Adaptation) adapters  
- Out‑of‑distribution (OOD) detection
