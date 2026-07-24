# Summary: 2026-07-22_12-36-53Z_Cumsum_ComposablePhaseTransportforLow_CostStreamin.md
Saved: 2026-07-24 01:50
Source: 2026-07-22_12-36-53Z_Cumsum_ComposablePhaseTransportforLow_CostStreamin.md
Model: None

---

## Summary  
The paper introduces a streaming‑native temporal layer called cumsum‑composable phase transport that enables keyword spotting to be trained and inferred using ordinary cumulative sums while preserving low latency. By projecting acoustic frames into complex channels, applying learned unitary rotations (phase transport), accumulating a finite window with prefix differences, and updating via a gated residual, the model achieves exact batched training and a single‑frame online inference update per frame. The approach yields competitive accuracy on streaming speech datasets with far fewer parameters than conventional CNN baselines.

## Key Contributions  
- [Finding 1] Cumsum‑composable phase transport allows exact batched training using simple cumulative sums, eliminating the need for expensive scan kernels.  
- [Finding 2] Online inference requires only one prefix update per incoming frame, keeping memory usage minimal and latency low.  
- [Finding 3] The unitary rotation constraint ensures that inverse rotations have unit norm, which stabilizes the prefix representation and prevents numerical conditioning issues.

## Methodology  
The authors design a streaming‑native temporal layer that first maps each acoustic frame to a complex channel space, then applies a learned unitary rotation (phase transport) to encode temporal information. Prefix differences are accumulated over a finite window, producing a compact prefix vector that serves as the model’s state. A gated residual update combines this prefix with new frame features, yielding a low‑dimensional representation suitable for downstream classification. Training exploits ordinary cumulative sums, while inference updates only the most recent prefix, making the system fully online.

## Results  
On Google Speech Commands v2 (12 labels) the mel+cumsum model reaches 97.3 % test accuracy, tied with a 51.6K‑parameter and a 24.8K‑parameter variant that achieve 97.3 % and 96.8 %, respectively—outperforming the 25.6K MelCNNMaxPool baseline (97.1 %). In a matched benchmark against scan‑style models, cumsum+window yields 94.82 % versus 94.33 % for scan, training 1.07× faster and reducing single‑example latency from 7.09 ms to 5.01 ms on a Tesla T4 GPU.

## Significance  
This work demonstrates that streaming keyword spotting can be performed with a compact, low‑cost temporal primitive that leverages exact cumulative sums and unitary phase transport. The resulting models are smaller (≈25K parameters) yet achieve state‑of‑the‑art accuracy, while training and inference speed up dramatically, enabling real‑time deployment on edge devices.

## Related Concepts  
state‑space sequence models, unitary rotations, prefix differences, cumulative sums, gated residual networks, streaming inference, Mel spectrograms, keyword spotting, low‑latency audio processing.
