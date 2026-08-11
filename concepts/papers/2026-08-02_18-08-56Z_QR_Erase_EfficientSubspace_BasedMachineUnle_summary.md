# Summary: 2026-08-02_18-08-56Z_QR_Erase_EfficientSubspace_BasedMachineUnlearningw.md
Saved: 2026-08-04 00:18
Source: 2026-08-02_18-08-56Z_QR_Erase_EfficientSubspace_BasedMachineUnlearningw.md
Model: None

---

## Summary  
Machine unlearning aims to delete specific information from a trained model without retraining the entire network, but existing methods often degrade unrelated capabilities or rely on costly SVD computations. QR‑Erase introduces a subspace‑based approach that uses Pivoted QR decomposition to isolate and subtract task‑specific representations directly from model parameters. Layer‑Localized QR‑Erase further restricts updates to layers that contain the highest concentration of task‑specific information, improving efficiency. The method demonstrates strong forgetting while retaining other skills, staying within 5 % of optimal SVD results across multiple benchmarks.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Pivoted QR decomposition provides an accurate subspace recovery with bounded error, offering a practical alternative to full SVD.  
- [Finding 2] Layer‑Localized QR‑Erase restricts parameter updates to layers with the strongest task‑specific signal, enhancing forgetting efficiency and reducing unintended side effects.  
- [Finding 3] The framework achieves superior forgetting‑retention trade‑offs compared to optimization‑based methods while remaining within 5 % of SVD performance across task‑level, cross‑lingual, and speech unlearning tasks.

## Methodology  
QR‑Erase first computes the Pivoted QR factorization of the residual between the target representation and the model’s current output, yielding a low‑rank approximation that isolates the subspace to be erased. The algorithm then subtracts this low‑rank component from the corresponding layer parameters, guided by a spectral gap condition that ensures convergence. Layer‑Localized QR‑Erase adds a layer‑specific mask derived from the concentration of task‑specific activations, limiting updates only where they are most impactful.

## Results  
Across three domains—task‑level classification, cross‑lingual translation, and speech recognition—the method reduces forget‑set accuracy by an average of 37 % compared with baseline optimization techniques. In speech unlearning, forgetting drops from 53.1 % to 15.7 % after applying the layer‑localized variant, while overall model performance remains within 5 % of the theoretical SVD optimum.

## Significance  
By replacing expensive SVD with a Pivoted QR that recovers only the necessary subspace and by localizing updates to high‑impact layers, QR‑Erase offers a fast, scalable unlearning mechanism for large foundation models. This reduces computational cost and mitigates catastrophic forgetting of unrelated knowledge, making it suitable for continual learning pipelines.

## Related Concepts  
- Machine unlearning (forgetting)  
- Subspace recovery vs. optimal reconstruction  
- Pivoted QR decomposition  
- Spectral gap conditions  
- Layer‑localized updates
