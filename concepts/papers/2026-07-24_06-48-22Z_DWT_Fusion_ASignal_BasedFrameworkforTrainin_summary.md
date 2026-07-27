# Summary: 2026-07-24_06-48-22Z_DWT_Fusion_ASignal_BasedFrameworkforTraining_FreeL.md
Saved: 2026-07-26 21:42
Source: 2026-07-24_06-48-22Z_DWT_Fusion_ASignal_BasedFrameworkforTraining_FreeL.md
Model: None

---

## Summary  
The paper proposes DWT-Fusion, a training‑free detection framework for LLM‑generated text that leverages discrete wavelet analysis of token‑level log‑probability signals. It moves beyond global language‑model statistics to exploit localized probability dynamics across multiple scales. The approach combines several wavelet configurations using calibration‑guided voting without any supervised meta‑learning. This enables robust zero‑shot detection across diverse datasets and models.  

## Key Contributions  
- DWT-Fusion introduces a signal‑based, training‑free method that uses discrete wavelet analysis of token‑level log‑probability sequences.  
- It demonstrates that multiresolution probability dynamics provide stronger detection signals than global language‑model statistics.  
- Calibration‑weighted voting fusion of multiple wavelet configurations yields significant AUROC improvements without training.  

## Methodology  
The authors generate proxy causal language models for each test model, compute token‑level log probabilities, and apply discrete wavelet transforms to obtain multiscale signal representations. These signals are used as detection features; four voting strategies (equal‑weight hard/soft, calibration‑weighted hard/soft) combine them without a meta‑classifier.  

## Results  
On HC3, M4, and MAGE with GPT‑Neo‑2.7B, Falcon‑7B, LLaMA‑3‑8B, the best single wavelet configurations achieve AUROC 0.9872, 0.8185, and 0.7138 respectively; calibration‑weighted voting improves them to 0.9919, 0.8477, and 0.7471.  

## Significance  
These results show that localized, multiscale probability signals can outperform global language‑model metrics in zero‑shot detection, offering interpretable, training‑free solutions for LLM‑generated text identification across heterogeneous settings.  

## Related Concepts  
Discrete wavelet transform, token‑level log probabilities, calibration weighting, voting fusion, zero‑shot detection, proxy causal language model.
