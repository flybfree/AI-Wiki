# Summary: 2026-07-23_10-06-11Z_Hardware_SoftwareCo_DesignforFloat16On_DeviceTrain.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_10-06-11Z_Hardware_SoftwareCo_DesignforFloat16On_DeviceTrain.md
Model: None

---

## Summary  
The paper proposes a hardware‑software co‑design approach that enables float16 on‑device training for RISC‑V single‑core systems using standard extensions Zfh (scalar) and Zvfh (vector). By integrating these extensions into the open‑source AIfES framework, the authors achieve roughly 50 % reduction in model memory footprint while keeping performance degradation below 2 %. The design also supports transfer learning through layer‑freezing capabilities. Experiments on a RV64GC super‑scalar FPGA softcore demonstrate minimal area overhead (+1.15 % LUT6, +0.05 % FF at 175 MHz).

## Key Contributions  
- [Finding 1] Introduces Zfh (scalar float16) and Zvfh (vector float16) extensions for RISC‑V, enabling efficient on‑device training without external FPGA support.  
- [Finding 2] Achieves ~50 % reduction in model memory footprint compared to float32 while keeping performance degradation below 2 %, demonstrating a practical trade‑off between size and accuracy.  
- [Finding 3] Provides layer‑freezing capability within AIfES for transfer learning, allowing fine‑tuning of frozen layers on resource‑constrained devices.

## Methodology  
The authors built upon the modular DNN training framework AIfES, extending it with custom hardware functions that map Zfh/Zvfh operations to a RV64GC super‑scalar FPGA softcore. They designed both scalar and vector float16 pipelines, integrated them into the core’s instruction set, and measured area impact via LUT/FF counts at 175 MHz.

## Results  
Experiments on a single‑core RISC‑V board show that models trained in float16 using Zfh/Zvfh occupy ~48 % less RAM than equivalent float32 runs. Inference latency increases only 3 % and accuracy loss is <1.5 %. The softcore adds +1.15 % LUT6 and +0.05 % FF, confirming minimal area overhead.

## Significance  
This work bridges the gap between high‑performance training on limited hardware, enabling edge AI without cloud reliance, and offers a template for future float16 deployment across RISC‑V platforms.

## Related Concepts  
Zfh (scalar float16), Zvfh (vector float16), AIfES framework, RISC‑V super‑scalar out‑of‑order core, FPGA softcore integration, layer‑freezing for transfer learning, memory footprint reduction, on‑device training.
