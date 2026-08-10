# Summary: 2026-08-07_10-16-25Z_PTQ4SNN_Membrane_AwarePost_TrainingQuantizationfor.md
Saved: 2026-08-09 22:53
Source: 2026-08-07_10-16-25Z_PTQ4SNN_Membrane_AwarePost_TrainingQuantizationfor.md
Model: None

---

## Summary  
The paper introduces PTQ4SNN, a membrane‑aware post‑training quantization framework for spiking neural networks (SNNs) that tackles the problem of retaining floating‑point recurrent membrane states after weight quantization. It proposes two novel techniques—a channel‑wise Unified Scale Bridge and mixed‑precision bit allocation—to preserve spike decisions while using only a small calibration set. The method works on projection‑LIF pairs and is compatible with both convolutional SNNs and spike‑driven Transformers without retraining. Experiments show that PTQ4SNN maintains accuracy under W4 quantization when membrane precision is reduced to roughly 4 bits.

## Key Contributions  
- [Finding 1] The Unified Scale Bridge constrains the membrane scale as s_mem,c = s_w,c × 2^k_c, adapting to channel‑specific distributions and enabling shift‑compatible conversion.  
- [Finding 2] Mixed‑Precision Bit Allocation assigns 2/4/8‑bit precision to membrane channels based on firing activity and quantization sensitivity within an average bit budget.  
- [Finding 3] Joint post‑training quantization of weights and recurrent membranes is achieved with minimal calibration data, avoiding the need for retraining.

## Methodology  
The authors approached the problem by recognizing that recurrent membrane states are typically kept in floating point after weight quantization, which can degrade spike timing and accumulate errors. They introduced a channel‑wise Unified Scale Bridge that maps each membrane’s scale to its corresponding weight scale using a power‑of‑two factor, guaranteeing compatibility across quantizations. Subsequently, Mixed‑Precision Bit Allocation dynamically allocates bit widths per channel, prioritizing high‑activity or sensitive channels while respecting an overall budget. The framework operates on existing projection‑LIF pairs and can be applied to both convolutional SNNs and spike‑driven Transformers without any architectural changes.

## Results  
Experiments on static classification, event‑based classification, and semantic segmentation demonstrate that PTQ4SNN retains model accuracy comparable to full‑precision models under W4 quantization while using only about 4 bits for membrane precision. The method reduces memory consumption significantly compared with conventional quantization schemes and preserves spike timing fidelity across the network.

## Significance  
This work advances the deployment of SNNs on low‑bit, edge‑compatible hardware by enabling accurate inference without sacrificing spiking behavior. By preventing errors that arise from quantizing membrane dynamics, PTQ4SNN leads to more reliable neuromorphic systems where power and energy are critical constraints.

## Related Concepts  
- Spiking Neural Networks (SNNs)  
- Post‑training quantization  
- Recurrent membrane states  
- Unified Scale Bridge  
- Mixed‑precision bit allocation  
- Calibration sets  
- Projection‑LIF pairs  
- W4 quantization  
- Event‑based inference
