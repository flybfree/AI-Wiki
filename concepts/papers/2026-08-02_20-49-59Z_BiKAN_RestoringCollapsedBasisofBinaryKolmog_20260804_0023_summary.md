# Summary: 2026-08-02_20-49-59Z_BiKAN_RestoringCollapsedBasisofBinaryKolmogorov__A.md
Saved: 2026-08-04 00:23
Source: 2026-08-02_20-49-59Z_BiKAN_RestoringCollapsedBasisofBinaryKolmogorov__A.md
Model: None

---

## Summary  
The paper addresses the collapse of binary Kolmogorov–Arnold Networks (KANs) where activations are restricted to {‑1, +1}, causing a structural failure known as Spatial Orthogonality Collapse that eliminates higher‑order polynomial features. BiKAN proposes augmenting each binary layer with degree‑2 Walsh characters to restore pairwise coordinate information without learned routing or multipliers. This restores the effective function space and enables high‑accuracy classification on standard benchmarks.

## Key Contributions  
- [Finding 1] The authors identify Spatial Orthogonality Collapse as a fundamental limitation of binary KANs, where even powers collapse to constants and odd powers reduce to linear terms.  
- [Finding 2] BiKAN restores pairwise coordinates by integrating fixed circular channel rolls that generate parity bits, using XNOR‑popcount operations to mix them within the W1A1 architecture.  
- [Finding 3] Experiments show Parity planes improve accuracy by up to 3.09 points over conventional widening (p<10⁻⁴) and enable zero‑DSP inference on FPGA, outperforming parity reduction in accuracy.

## Methodology  
The authors start with a standard binary KAN layer where activations are limited to {‑1, +1}, causing the elementwise polynomial basis to collapse. To mitigate this, they embed degree‑2 Walsh characters—fixed circular shifts of the input that produce pairwise parity patterns. These parity planes are combined using XNOR and popcount logic, which mirrors the existing W1A1 path’s combinatorial structure. The resulting BiKAN architecture replaces learned routing with explicit parity generation, preserving the binary nature while reintroducing second‑order features.

## Results  
On CIFAR‑10, Parity planes reduce accuracy loss to 1.23 points across five seeds (p=0.003), with gains larger for narrower networks and monotonic improvement as more planes are added. At a fixed ~11.9M parameters, BiKAN beats conventional widening by 3.09 points (p<10⁻⁴). On MNIST, CIFAR‑10, and CIFAR‑100, BiKAN achieves 99.48%, 84.38%, and 55.81% respectively. FPGA deployment shows DSP usage cut from 164 to 72 and latency reduced to 54.8 ms; a zero‑DSP dense variant incurs only a 0.03‑point accuracy loss.

## Significance  
This work demonstrates that structural collapse in binary networks can be repaired without sacrificing performance, offering a path toward efficient hardware deployment of KANs. By leveraging fixed parity planes and XNOR operations, BiKAN provides a scalable solution that aligns with the constraints of low‑power FPGA inference.

## Related Concepts  
- Binary Kolmogorov–Arnold Networks (binary KAN)  
- Spatial Orthogonality Collapse  
- Walsh characters  
- Parity planes  
- W1A1 path  
- XNOR‑popcount operations  
- DSP usage, compute‑core latency
