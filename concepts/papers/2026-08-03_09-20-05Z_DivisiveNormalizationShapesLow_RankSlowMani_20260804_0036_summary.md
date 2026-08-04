# Summary: 2026-08-03_09-20-05Z_DivisiveNormalizationShapesLow_RankSlowManifoldsfo.md
Saved: 2026-08-04 00:36
Source: 2026-08-03_09-20-05Z_DivisiveNormalizationShapesLow_RankSlowManifoldsfo.md
Model: None

---

## Summary  
The paper investigates how continuous variables are maintained in working memory and shows that a biologically inspired normalization mechanism, divisive normalization, enables robust low‑rank slow manifolds without explicit factorization. It proposes the Recurrent Divisive Normalization Network (RDNN) to achieve this. The authors demonstrate via dynamical systems analysis and gradient dynamics that this constraint yields stable manifold learning. Their findings reveal that subtractive inhibition alone is insufficient for time‑varying inputs.

## Key Contributions  
- [Finding 1] Divisiive normalization enables convergence to high‑fidelity slow manifolds in continuous working memory tasks.  
- [Finding 2] Gradient scaling from divisive normalization during BPTT reduces parameter updates, leading to effective rank compression and low‑dimensional subspace dynamics.  
- [Finding 3] Ablations show subtractive inhibition cannot prevent manifold shattering under time‑varying inputs; divisive normalization is mathematically essential.

## Methodology  
The authors model working memory as a dynamical system using recurrent networks with divisive normalization, where each neuron’s output is normalized by the sum of its activity across neurons. They analyze gradient flow during Backpropagation Through Time (BPTT) to understand how this normalization influences parameter updates. Experiments involve canonical continuous‑variable tasks (e.g., maintaining a slowly changing value) and measure manifold fidelity via trajectory reconstruction.

## Results  
Theoretical analysis shows that divisive normalization yields slow manifold dynamics with low‑rank structure, avoiding shattering. Numerical experiments confirm high‑fidelity memory retention across time steps, while gradient magnitude is suppressed in active regimes, consistent with rank compression. Ablation results demonstrate that without divisive normalization, the network rapidly loses manifold stability.

## Significance  
These findings bridge biology and machine learning by identifying a simple, biologically plausible mechanism that stabilizes continuous representations, offering an alternative to explicit low‑rank factorization that suffers from fine‑tuning fragility. It suggests that natural neural computation can naturally enforce low‑dimensionality without engineering constraints.

## Related Concepts  
- Continuous attractor networks  
- Slow manifolds  
- Divisive normalization  
- Recurrent RNNs (GRU/LSTM)  
- Backpropagation Through Time (BPTT)  
- Gradient scaling  
- Low‑rank factorization
