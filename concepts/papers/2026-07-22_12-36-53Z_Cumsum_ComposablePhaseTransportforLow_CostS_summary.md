# Summary: 2026-07-22_12-36-53Z_Cumsum_ComposablePhaseTransportforLow_CostStreamin.md
Saved: 2026-07-24 01:50
Source: 2026-07-22_12-36-53Z_Cumsum_ComposablePhaseTransportforLow_CostStreamin.md
Model: None

---

## Summary  
The paper proposes a streaming‑native temporal layer called cumsum‑composable phase transport that enables low‑cost keyword spotting while preserving the compact recurrent state of state‑space models. By projecting acoustic frames to complex channels, applying learned unitary rotations, accumulating a finite window with prefix differences, and updating via a gated residual, the method achieves exact batched training using ordinary cumulative sums and exact online inference with one prefix update per frame. The approach is designed to be simple, memory‑efficient, and compatible with streaming data pipelines.

## Key Contributions  
- [Finding 1] Cumsum‑composable phase transport provides a low‑cost temporal primitive that can be used for streaming keyword spotting without sacrificing accuracy.  
- [Finding 2] The unitary rotation constraint guarantees well‑conditioned prefix terms, allowing exact cumulative sums and minimal memory footprint.  
- [Finding 3] Experimental results show the method matches or exceeds state‑of‑the‑art baselines (e.g., MelCNNMaxPool) while using fewer parameters and delivering faster training and lower single‑example latency.

## Methodology  
The authors adopt a state‑space sequence model architecture that maintains a compact recurrent state across frames. Each frame is first mapped to complex channels, then transported by a learned unitary rotation which preserves the norm of the representation. A finite‑window prefix difference is accumulated using ordinary cumulative sums, and this prefix term is combined with the current frame via a gated residual update. Because the inverse rotations are orthogonal (norm = 1), the prefix terms remain stable even when only a short window or block readout supplies memory, enabling exact online inference per frame.

## Results  
On Google Speech Commands v2 with 12 labels, the cumsum‑phase transport model attains 97.3 % test accuracy, matching a 51.6K‑parameter tied model and reaching 96.8 % with a 24.8K tied model—both outperforming the 25.6K MelCNNMaxPool baseline (97.1 %). In a matched cumsum versus scan benchmark, the method yields 94.82 % accuracy compared to 94.33 % for the scan baseline. Training is 1.07× faster and single‑example latency drops from 7.09 ms to 5.01 ms on a Tesla T4.

## Significance  
Cumsum‑composable phase transport offers a simple, low‑cost temporal layer that can be integrated into streaming keyword spotting pipelines with negligible extra memory or compute overhead. Its unitary transport ensures numerical stability and exact cumulative sums, while the gated residual update preserves model expressiveness. These advantages translate to faster training, reduced latency per frame, and competitive accuracy, making it a practical choice for real‑time speech applications.

## Related Concepts  
state‑space models, unitary rotations, prefix sums, cumulative sums, phase transport, gated residual networks, MelCNNMaxPool, streaming keyword spotting, batch training, online inference.
