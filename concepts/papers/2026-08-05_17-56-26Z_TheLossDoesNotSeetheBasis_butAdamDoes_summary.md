# Summary: 2026-08-05_17-56-26Z_TheLossDoesNotSeetheBasis_butAdamDoes.md
Saved: 2026-08-05 22:35
Source: 2026-08-05_17-56-26Z_TheLossDoesNotSeetheBasis_butAdamDoes.md
Model: None

---

## Summary  
The paper investigates why gradient descent on a factored model $W=UV^\top$ is implicitly biased toward low‑rank solutions while Adam does not, attributing the difference to the loss’s gauge symmetry $(U,V)\mapsto (UQ,VQ)$. It derives a structure theorem that links low‑rank recovery to optimizers that are gauge‑equivariant and shows which update rules satisfy this condition. The authors also test nine optimization strategies on underdetermined matrix‑sensing tasks and analyze transformer training behavior, revealing that Adam separates two gauge‑equivalent initializations at the first step but leaves per‑head weight invariants $W_Q^\top W_K$ 56 % apart in Frobenius distance. Experimental results show gradient descent reduces held‑out error by 43–44 % on hyperspectral datasets at low sampling density and effective rank, whereas Adam’s bias persists.

## Key Contributions  
- [Finding 1] Gradient descent is implicitly biased toward low‑rank solutions due to the loss’s gauge symmetry, whereas Adam avoids this bias.  
- [Finding 2] A structure theorem characterizes gradient flow’s low‑rank mechanism as requiring gauge‑equivariant optimizers; only gradient descent, momentum, shared‑scalar Adam, Muon and Shampoo satisfy it.  
- [Finding 3] Gradient descent cuts held‑out error by 43–44 % on hyperspectral data at the lowest sampling density and effective rank, while Adam’s per‑head invariants diverge.

## Methodology  
The authors trace the bias to the loss’s gauge symmetry and derive a transfer theorem that maps gradient‑flow properties onto common‑scalar flows. They characterize memoryless equivariant update rules as exactly the Gram‑determined left preconditioners and evaluate nine optimizers (gradient descent, momentum, shared‑scalar Adam, Muon, Shampoo, RMSProp, etc.) by measuring recovery error on underdetermined matrix‑sensing tasks. Additional transformer experiments measure per‑head weight invariants to quantify divergence.

## Results  
Gradient descent achieves a 43–44 % reduction in held‑out error compared with Adam at low sampling density and effective rank, indicating strong low‑rank recovery. Adam’s per‑head Frobenius distance between $W_Q^\top W_K$ matrices is about 56 %, a gap that cannot be closed by any rotation. A one‑parameter family of Gram‑determined left preconditioners restores the low‑rank bias monotonically, confirming that anisotropy—not initialization—is the cause.

## Significance  
Basis choice is not merely a tuning detail; it determines which interpolant an optimizer selects and thus influences model capacity and generalization. Understanding gauge‑equivariance clarifies why some optimizers recover low‑rank structure while others do not, guiding more principled design of learning algorithms for factorized models.

## Related Concepts  
- Gauge symmetry  
- Gradient flow  
- Gauge‑equivariant optimization  
- Gram‑determined left preconditioners  
- Common‑scalar flows  
- Matrix sensing  
- Transformers  
- Hyperspectral learning  
- Low‑rank recovery bias
