# Summary: 2026-08-03_10-56-46Z_SCOPE_EntanglementFrontierEscapeforSource_FreeClas.md
Saved: 2026-08-04 00:46
Source: 2026-08-03_10-56-46Z_SCOPE_EntanglementFrontierEscapeforSource_FreeClas.md
Model: None

---

## Summary  
The paper tackles the challenge of source‑free class unlearning by showing that any fixed projection eraser must pay a retain cost equal to the energy consumed along the forget‑discriminant subspace, which is the theoretical floor for such erasers. It proves that this tension can be escaped only when the erasure is conditioned on the input, allowing the projector to suppress the unwanted subspace without harming retained classes. The authors introduce Spectral Conditional Projective Erasure (SCOPE), a single‑gate operation that conditions the projection solely on the frozen head’s weight scores for the forget class and achieves this escape with no gradient or retain data. This work establishes a new frontier in source‑free erasers, demonstrating that conditioning is both necessary and sufficient to reach optimal performance.

## Key Contributions  
- [Finding 1] Fixed projection erasers incur a retain cost at least equal to the retain‑readout energy along the forget‑discriminant subspace.  
- [Finding 2] Escaping this cost requires conditioning the erasure on the input, making representation‑level erasers incompatible with conditional projections.  
- [Finding 3] SCOPE realizes this escape with a single gate, requiring no retain data or gradient training and delivering orders of magnitude lower computational cost than retraining.

## Methodology  
SCOPE builds upon the frozen head’s weight distribution to condition a projective erasure on whether the input is from a forget class. The projection matrix multiplies the input by a scalar that is zero only when the corresponding head weight is below a threshold, thereby collapsing the forget‑discriminant subspace for those inputs while leaving other classes untouched. Because the condition is static and derived analytically, SCOPE avoids any training step and can be applied as a post‑hoc gate in inference.

## Results  
Theoretical analysis predicts that SCOPE’s retain cost matches the lower bound across all benchmark settings. Empirically, on five object, face, and speaker datasets spanning convolutional and transformer backbones, SCOPE outperforms every previously reported source‑free eraser, including trained methods, for all forget‑set sizes. At the hardest configuration it exceeds all unlearners in both accuracy and computational efficiency.

## Significance  
This work resolves a longstanding theoretical bottleneck in source‑free class unlearning, proving that conditioning is essential to achieve optimal performance. Practically, SCOPE offers a lightweight, trainable‑free solution that dramatically reduces latency compared with retraining or fine‑tuning, making large‑scale unlearning feasible without sacrificing representational fidelity.

## Related Concepts  
- Source‑free class unlearning  
- Feature‑space erasure  
- Retain‑readout energy  
- Forget‑discriminant subspace  
- Spectral conditional projection  
- Projector gate  
- Conditional erasure
