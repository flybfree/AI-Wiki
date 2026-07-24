# Summary: 2026-07-21_07-30-08Z_QScheduler_AdaptiveGradientSamplingforZeroth_Order.md
Saved: 2026-07-24 00:32
Source: 2026-07-21_07-30-08Z_QScheduler_AdaptiveGradientSamplingforZeroth_Order.md
Model: None

---

## Summary  
Zeroth‑Order (ZO) optimization enables on‑device learning by estimating gradients from forward passes alone, eliminating the need for back‑propagation and large memory buffers. The paper’s core contribution is an adaptive algorithm called QScheduler that automatically tunes the number of gradient samples q during training to balance noise reduction against computational cost. By dynamically adjusting q based on training progress, QScheduler eliminates the costly hyperparameter search required for fixed‑q strategies. Experiments demonstrate that QScheduler yields performance comparable to well‑tuned static‑q configurations while operating entirely within the memory and compute limits of an INT8‑quantized NPU.

## Key Contributions  
- [Finding 1] QScheduler is the first adaptive algorithm that modifies q in real time based on training dynamics, removing the need for offline hyperparameter optimization.  
- [Finding 2] It provides a proof‑of‑concept of INT8 quantized zeroth‑order training on the STM32N6’s Neural‑ART NPU, showing feasibility on a microcontroller‑class hardware platform.  
- [Finding 3] QScheduler matches or exceeds the accuracy and efficiency of the best fixed‑q configurations for ResNet18 and MobileNetV2 without requiring prior q tuning.

## Methodology  
The authors employ zeroth‑order gradient estimation, where each forward pass yields a noisy gradient estimate. The number of samples q is a hyperparameter that influences both gradient variance and compute cost. QScheduler monitors training loss or validation accuracy; if the metric plateaus early, it reduces q to save resources, while if performance improves, it increases q for finer gradients. This feedback loop adjusts q every few epochs, allowing the model to converge with minimal overhead.

## Results  
On EuroSAT and STL‑10 benchmarks, QScheduler achieves ResNet18 accuracies of 92.5 % (vs. 93.0 % for optimal fixed‑q) and MobileNetV2 F1 scores of 78.6 % (vs. 79.1 %). The adaptive schedule reduces average compute per epoch by ~12 % compared with the best static q, while memory usage stays under 4 MiB on the NPU’s INT8 pipeline. Training completes within the device’s limited runtime budget without additional hardware.

## Significance  
By enabling accurate ODL on ultra‑low‑power microcontrollers, QScheduler opens a pathway for AI inference and learning at the edge where back‑propagation is infeasible. It lowers the barrier to deploying deep models in constrained environments such as IoT sensors or automotive ECUs, where power, cost, and size are critical constraints.

## Related Concepts  
- Zeroth‑order optimization (ZO)  
- On‑device learning (ODL)  
- INT8 quantization  
- Neural‑ART NPU  
- Gradient sampling  
- Adaptive hyperparameter tuning
