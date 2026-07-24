# Summary: 2026-07-16_05-00-49Z_Gate_ZeroGrowth_AGeometricFrameworkforFunction_Pre.md
Saved: 2026-07-23 23:45
Source: 2026-07-16_05-00-49Z_Gate_ZeroGrowth_AGeometricFrameworkforFunction_Pre.md
Model: None

---

## Summary  
Gate‑Zero Growth (GZ) is a novel function‑preserving operator that adds new residual blocks via a zero‑initialised gate to enable continual learning without degrading performance on previously learned tasks. The method guarantees rank separation in the functional Jacobian, meaning old directions remain unchanged while new directions are flat at the growth point and only the gate introduces first‑order variation. This geometric control limits function drift to \(O(\|\boldsymbolα\|^2)\) and Jacobian leakage to \(O(\|\boldsymbolα\|_\infty)\). Experiments on a 300 M → 857 M Transformer show that GZ achieves near‑zero forgetting (\(\Delta_A < 0.1\)) under both Isolation and Freeze‑Nothing operating points, outperforming non‑FP baselines such as \(G_{\text{stack}}\) by orders of magnitude.

## Key Contributions  
- [Finding 1] Gate‑Zero Growth provides a function‑preserving (FP) operator that enforces rank separation in the functional Jacobian during continual learning.  
- [Finding 2] The method yields controlled forgetting and leakage: function drift is \(O(\|\boldsymbolα\|^2)\) and Jacobian leakage is \(O(\|\boldsymbolα\|_\infty)\).  
- [Finding 3] Empirical results demonstrate that GZ reduces domain forgetting to below 0.1 on a WikiText‑103 → BookCorpus transfer, while comparable non‑FP methods suffer an order‑of‑magnitude larger degradation.

## Methodology  
The authors introduced Gate‑Zero Growth as a zero‑initialised gate that injects new residual blocks into the network during continual learning. By applying a transversality condition to the functional Jacobian, they prove that old training directions are untouched, new weight directions become flat at the growth point, and only the gate direction contributes first‑order variation. This geometric analysis underlies the controller’s ability to activate latent capacity safely. The framework is shown to be compatible with various adapter styles (LoRA, ReZero, zero‑init adapters), establishing GZ as a canonical instance of shared local geometry for safe capacity activation.

## Results  
On a 300 M → 857 M Transformer adapted from WikiText‑103 to BookCorpus, Gate‑Zero Growth achieves near‑zero forgetting (\(\Delta_A < 0.1\)) under both Isolation and Freeze‑Nothing operating points. In contrast, the non‑FP control \(G_{\text{stack}}\) exhibits an order‑of‑magnitude larger forgetting. The geometric analysis also validates that LoRA, ReZero, and zero‑init adapter constructions inherit similar rank‑separation properties, confirming the universality of GZ’s behavior across these methods.

## Significance  
Gate‑Zero Growth offers a theoretically grounded alternative to traditional continual learning techniques by guaranteeing function preservation through controlled capacity growth. This reduces catastrophic forgetting, improves downstream task performance, and provides a unified geometric view that can guide future research on safe adaptation in deep networks.

## Related Concepts  
- Function‑preserving continual learning (FP‑CL)  
- Rank separation in the functional Jacobian  
- Jacobian leakage analysis  
- Isolation operating point  
- Freeze‑Nothing operating point  
- LoRA, ReZero, zero‑init adapters  
- Isolated vs. joint frontiers  
- Capacity activation and safe growth mechanisms
