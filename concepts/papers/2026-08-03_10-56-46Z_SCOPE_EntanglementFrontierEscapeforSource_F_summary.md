# Summary: 2026-08-03_10-56-46Z_SCOPE_EntanglementFrontierEscapeforSource_FreeClas.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_10-56-46Z_SCOPE_EntanglementFrontierEscapeforSource_FreeClas.md
Model: None

---

## Summary  
The paper tackles the challenge of source‑free class unlearning by showing that any fixed projection eraser must incur a non‑zero retain cost because forget and retain classes share a representation. It proves this tension forms a theoretical frontier, and conditioning the erasure on the input can escape it entirely. The authors introduce Spectral Conditional Projective Erasure (SCOPE), a single‑gate operation that achieves source‑free unlearning with negligible retain loss. Experimental results across multiple benchmarks demonstrate that SCOPE matches the predicted lower bound and outperforms all existing erasers, even trained unlearners.

## Key Contributions  
- [Finding 1] The forget‑retain conflict creates a frontier: any fixed projection eraser must pay at least the retain‑readout energy along the forget‑discriminant subspace.  
- [Finding 2] Conditioning the erasure on the input can bypass this cost, enabling source‑free class unlearning without retraining.  
- [Finding 3] Spectral Conditional Projective Erasure (SCOPE) realizes this conditional escape with a single gate, closed‑form, no retain data or gradient training.

## Methodology  
The authors analyze the representational overlap between forget and retain classes, derive a lower bound on the retain cost for any projection eraser, and propose SCOPE as a spectral conditioning of the projection that depends only on the frozen head’s weight scores. The method is implemented as a single linear transformation applied to the input representation, eliminating the need for gradient‑based training or retain data.

## Results  
Across five object, face, and speaker benchmarks spanning two modalities (convolutional and transformer backbones) and varying forget‑set sizes, SCOPE achieves the predicted minimal retain cost on every benchmark. It consistently outperforms all source‑free erasers, including trained unlearners, at both easy and hardest settings.

## Significance  
SCOPE provides an efficient, scalable technique for class erasure that avoids costly retraining, dramatically reducing computational overhead while respecting the theoretical frontier of representation‑level unlearning. This work advances the field by bridging theory and practice in source‑free learning.

## Related Concepts  
source‑free class unlearning; feature‑space erasers; projection‑based unlearning; spectral conditioning; retain‑readout energy; forget‑discriminant subspace; frontiers of optimization; single‑gate operations.
