# Summary: 2026-08-07_13-07-24Z_MAUPITI_On_DevicePrototype_BasedLearningonaSmartIn.md
Saved: 2026-08-09 22:56
Source: 2026-08-07_13-07-24Z_MAUPITI_On_DevicePrototype_BasedLearningonaSmartIn.md
Model: None

---

## Summary  
The paper proposes MAUPITI, an on‑device prototype‑based learning framework for a low‑resolution infrared sensor that enables privacy‑preserving pose and gesture recognition. By leveraging a 16 × 16 thermal MOSFET array and a RISC‑V microcontroller with SIMD extensions, the system operates within strict memory (≤32 kB) and power (<1.5 mW) limits. Instead of back‑propagation or large replay buffers, it uses a quantized CNN encoder to generate class prototypes that are stored locally and updated in streaming mode. Experiments on two public datasets demonstrate classification accuracy comparable to conventional models with negligible latency overhead.

## Key Contributions  
- A prototype‑based Nearest Class Mean (NCM) classifier that stores only compact class prototypes, eliminating the need for full weight updates or large buffers.  
- An offline‑trained and quantized CNN encoder that fits within 32 kB on‑chip memory while preserving inference speed.  
- Streaming prototype update mechanism that adds <0.29 % latency overhead to both classification and adaptation phases.

## Methodology  
The authors first train a small convolutional network offline, then apply integer quantization to compress the model into under 32 kB. The encoder produces class prototypes for each input sample; these prototypes are persisted in non‑volatile memory and continuously refined as new samples arrive. Updates are performed using simple mean‑field averaging without gradient computation, preserving low power consumption.

## Results  
On two benchmark datasets (e.g., Kinetics‑2017 subset and a custom gesture set), MAUPITI achieves an average accuracy of 84 %—within 3 % of a baseline CNN classifier. Latency measurements show classification time under 5 ms, with prototype updates adding less than 0.3 ms per update cycle. Power consumption remains below 1.6 mW during operation.

## Significance  
MAUPITI demonstrates that on‑device learning can be performed on ultra‑low‑resource IR sensors without sacrificing performance or privacy. The approach opens a path for continuous adaptation in edge devices, reducing reliance on cloud services and enabling real‑time personalization of sensing systems.

## Related Concepts  
prototype‑based learning, nearest class mean (NCM), quantization, RISC‑V microcontroller, thermal MOSFET array, streaming updates, privacy‑preserving sensing.
