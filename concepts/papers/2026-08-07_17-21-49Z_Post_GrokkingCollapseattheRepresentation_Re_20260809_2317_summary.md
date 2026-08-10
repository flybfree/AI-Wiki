# Summary: 2026-08-07_17-21-49Z_Post_GrokkingCollapseattheRepresentation_ReadoutIn.md
Saved: 2026-08-09 23:17
Source: 2026-08-07_17-21-49Z_Post_GrokkingCollapseattheRepresentation_ReadoutIn.md
Model: None

---

## Summary  
The paper investigates why Muon‑trained transformers experience a sudden loss of performance after grokking, attributing the failure to an instability at the representation‑readout interface that is not captured by the standard training objective. By systematically varying training configurations and freezing specific model groups, the authors demonstrate that the collapse occurs only when both the embedding and readout components are unfrozen, revealing a joint artifact that cannot be mitigated by orthogonalizing or normalizing the Moons. The study shows that the task‑aligned family can still solve the problem in isolation, while the full model collapses to sub‑threshold performance across multiple seeds and hardware settings. This work identifies a previously unnoticed interface failure as a critical barrier to reliable grokking.

## Key Contributions  
- [Finding 1] The post‑grokking collapse is localized to the representation‑readout interface, identified only through an invertible map that the loss does not select.  
- [Finding 2] Freezing either the embedding or readout group eliminates the failure, whereas freezing both groups causes it, indicating a dependency on their interaction.  
- [Finding 3] The collapse is independent of Fourier filtering and power‑distribution metrics, suggesting that circuit design changes are not the root cause.

## Methodology  
The authors performed a controlled ablation study across nine training configurations defined by (a+b) mod 113, varying modulus, width, training fraction, subtraction vs. addition, and depth. They trained Muon models with AdamW embeddings and readout heads, measured performance on the test set after grokking, and systematically froze either the embedding or readout groups to isolate their contribution. Gradient magnitudes, step‑size elasticity, and parameter update rates were recorded at each checkpoint. The study also compared Fourier filtering of circuit outputs to detect residual errors.

## Results  
Across five seeds, four configurations fell below the threshold, achieving an average of 27.59 % accuracy; two moduli, two widths, subtraction, depth, and training fractions all triggered collapse. After solving the training set, gradients dropped to ~10⁻⁶, AdamW step‑size elasticity was +1.5 while Muon’s was –0.03, and Muon updates moved 8× faster per parameter. Freezing embeddings or readouts alone prevented failure (no sub‑threshold evaluations), whereas unfrozen arms recorded 137–321 failures. Removing normalization/orthogonalization reduced effective conjugate pairs from 326 to 4, causing terminal collapse. Fourier filtering separated circuit failure from masking; the task‑aligned family achieved 100 % on its own, while full models reached 45.85 % in circuit failure and 99.9 % after rescaling.

## Significance  
Identifying a representation‑readout interface instability resolves a major obstacle to reliable grokking of Moons, enabling consistent high performance across diverse training regimes. The findings highlight that optimization dynamics can be fragile even when the model’s architecture appears correct, prompting new design considerations for future transformer variants.

## Related Concepts  
- Grokking: rapid convergence after solving a training set.  
- Representation‑readout interface: point where hidden states are projected to output heads.  
- AdamW optimizer: adaptive learning rates with weight decay.  
- Fourier filtering: analysis of circuit outputs in transformers.  
- Conjugate pairs: representation space structure used by Moons.
