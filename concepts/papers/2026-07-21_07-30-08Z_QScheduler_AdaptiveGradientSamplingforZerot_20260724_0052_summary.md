# Summary: 2026-07-21_07-30-08Z_QScheduler_AdaptiveGradientSamplingforZeroth_Order.md
Saved: 2026-07-24 00:52
Source: 2026-07-21_07-30-08Z_QScheduler_AdaptiveGradientSamplingforZeroth_Order.md
Model: None

---

## Summary  
Zeroth‑Order (ZO) optimization enables on‑device learning by estimating gradients from forward passes alone, eliminating the need for back‑propagation. The number of gradient samples *q* is a key hyperparameter: too few samples yield noisy estimates that plateau early, while too many consume excessive compute and memory. QScheduler introduces an adaptive algorithm that automatically tunes *q* during training, removing the costly manual search for an optimal value. This work demonstrates the first proof‑of‑concept of INT8 quantized ZO training on a microcontroller’s Neural‑ART NPU without prior hyperparameter optimization.

## Key Contributions  
- **Adaptive gradient sampling algorithm**: QScheduler dynamically adjusts *q* based on real‑time training progress, balancing accuracy and resource usage.  
- **First demonstration of INT8 on‑device training**: The authors show that INT8 quantized ZO can run on the STM32N6 Neural‑ART NPU without requiring a pre‑tuned *q*.  
- **Performance parity with fixed‑*q** configurations: Experiments on ResNet18 and MobileNetV2 demonstrate that QScheduler matches well‑tuned fixed‑*q* results while using fewer samples.

## Methodology  
Zeroth‑Order optimization relies solely on forward passes to approximate gradients, which is ideal for memory‑constrained devices. QScheduler monitors a proxy of training progress—such as loss variance or convergence speed—and increments *q* when the estimate becomes noisy, then reduces it once stability is achieved. This adaptive loop ensures that each iteration uses only the minimum necessary samples while preserving gradient fidelity.

## Results  
The authors evaluate QScheduler on two benchmark datasets (EuroSAT and STL‑10) using ResNet18 and MobileNetV2 architectures. Across all configurations, QScheduler achieves accuracy comparable to the best fixed‑*q* settings reported in prior work. Moreover, it reduces average compute per iteration by up to 35 % compared with a high *q* baseline, while maintaining or improving final performance over low *q* methods.

## Significance  
By automating the selection of gradient samples, QScheduler removes a major bottleneck for on‑device learning: costly hyperparameter tuning. This enables real‑time training and inference on ultra‑low‑power microcontrollers, opening practical pathways to AI‑enabled edge devices without sacrificing accuracy or requiring offline optimization.

## Related Concepts  
Zeroth‑Order optimization, On‑Device Learning (ODL), INT8 quantization, Neural‑ART NPU, gradient sampling, adaptive scheduling, hyperparameter-free training.
