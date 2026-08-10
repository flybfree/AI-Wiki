# Summary: 2026-08-07_07-44-35Z_FastLapSum_ExactDifferentiableTop_katMillionScale.md
Saved: 2026-08-09 22:46
Source: 2026-08-07_07-44-35Z_FastLapSum_ExactDifferentiableTop_katMillionScale.md
Model: None

---

## Summary  
The paper proposes Fast LapSum, an exact‑budget soft top‑k primitive that remains fully differentiable end‑to‑end while solving the problem in linear time after sorting. Unlike previous methods such as DFTopK that relax normalization constraints, Fast LapSum preserves the precise selection mass of k and can handle millions to hundreds of millions of scores with negligible overhead. The authors demonstrate that the solver processes 10⁶, 10⁷ and 10⁸ scores in 0.41 ms, 1.15 ms and 5.23 ms respectively, enabling exact soft top‑k at million‑scale. This makes sparse routing, retrieval and large‑scale optimization tractable for modern deep learning models.

## Key Contributions  
- [Finding 1] Fast LapSum is the first method that provides an **exact‑budget soft top‑k** primitive while preserving a precise selection mass of k.  
- [Finding 2] The GPU solver runs in **linear time after sorting**, achieving sub‑millisecond performance even for 10⁸ scores.  
- [Finding 3] It employs **probabilistic bracketing** to sort only the uncertain middle band, reducing computational cost and allowing exact soft top‑k at million‑scale.

## Methodology  
Fast LapSum combines a linear‑time threshold computation with an analytical vector–Jacobian product. The algorithm first computes a hard threshold to isolate scores that definitely belong to the top‑k set, then uses a probabilistic bracketing strategy to sort only the uncertain middle region of kernel‑noised scores. This hybrid approach eliminates the need for full sorting of all elements and leverages the exactness of the selection mass throughout the training loop.

## Results  
Experimental evaluation shows that Fast LapSum processes 10⁶, 10⁷ and 10⁸ scores in 0.41 ms, 1.15 ms and 5.23 ms respectively, delivering an order‑of‑magnitude speedup over state‑of‑the‑art methods. The exact soft budget of ~0.02 % of an image’s pixels is used to generate megapixel sparse adversarial examples with a speed advantage comparable to or better than existing approaches. Moreover, the primitive enables training a fully differentiable sparse image coder from scratch, confirming its utility in large‑scale optimization problems.

## Significance  
By delivering exact soft top‑k at million scale without sacrificing differentiability, Fast LapSum unlocks new possibilities for token routing, expert activation and memory selection in deep learning. Its sub‑millisecond GPU solver enables real‑time integration into training pipelines, reducing the computational bottleneck that previously limited sparse computation to small datasets or low‑precision settings.

## Related Concepts  
- Top‑k operation (hard vs. soft)  
- Soft relaxation of top‑k constraints  
- DFTopK (previous linear‑time method with relaxed normalization)  
- Linear‑time sorting algorithms  
- Vector–Jacobian product for exact gradients  
- Probabilistic bracketing for uncertain regions
