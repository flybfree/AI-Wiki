# Summary: 2026-08-02_20-49-59Z_BiKAN_RestoringCollapsedBasisofBinaryKolmogorov__A.md
Saved: 2026-08-04 00:23
Source: 2026-08-02_20-49-59Z_BiKAN_RestoringCollapsedBasisofBinaryKolmogorov__A.md
Model: None

---

## Summary  
This paper introduces BiKAN (Binary Kolmogorov–Arnold Network), a novel architecture designed to restore the collapsed function space inherent in binary KAN layers, where activations are restricted to {-1, +1}, causing all even powers to collapse to 1 and odd powers to x, resulting in an elementwise polynomial basis that lacks expressive power. The core issue, termed Spatial Orthogonality Collapse, is mitigated by integrating degree-2 Walsh characters into each binary layer, which generate explicit pairwise coordinates through fixed circular channel rolls and learned projections using XNOR-popcount operations. This approach preserves the binary nature of activations while enabling richer feature interactions without introducing multipliers or learning-based routing. The method ensures that the network retains its computational efficiency and hardware compatibility across diverse platforms.

## Key Contributions  
- [Finding 1] BiKAN resolves Spatial Orthogonality Collapse by augmenting binary KAN layers with degree-2 Walsh characters, which generate pairwise parity information through fixed circular channel rolls, thereby restoring a non-redundant function space.  
- [Finding 2] The method uses learned binary projections to mix these parities via XNOR-popcount operations, enabling feature mixing without multipliers or routing, thus maintaining the binary activation constraint while improving expressivity.  
- [Finding 3] BiKAN achieves superior accuracy over conventional widening and parity-based methods on multiple benchmarks, with a significant advantage in parameter efficiency and hardware performance.

## Methodology  
The authors approach the problem by analyzing how binary activations restrict polynomial functions to only constant and linear terms, eliminating higher-order interactions. To counteract this collapse, they introduce degree-2 Walsh characters—specific binary patterns that encode pairwise parity information through fixed circular channel rolls. These channels produce consistent parity outputs across inputs, which are then combined using learned binary projections implemented via XNOR-popcount operations, a lightweight arithmetic operation common in W1A1 networks. This design avoids the need for multipliers or complex routing, preserving the network’s binary nature and computational simplicity while enabling richer feature combinations.

## Results  
BiKAN demonstrates strong performance across multiple datasets: achieving 99.48% on MNIST, 84.38% on CIFAR-10, and 55.81% on CIFAR-100 with an equal ~11.9M-parameter budget. Experiments show that removing parity reduces accuracy by 1.23 points over five paired seeds (p=0.003), with the gain increasing as network width decreases, and accuracy improving monotonically with more parity planes added. Compared to conventional widening, BiKAN outperforms it by 3.09 points (p<10⁻⁴) at the same parameter budget. Hardware evaluations on Zynq-7020 FPGA show DSP usage reduced from 164 to 72 and compute-core latency cut from 401 ms to 54.8 ms, while a power-of-two-aware dense design achieves zero-DSP inference with only a 0.03-point accuracy loss.

## Significance  
BiKAN is significant because it addresses a fundamental limitation in binary neural networks—structural collapse due to restricted function spaces—without sacrificing expressivity or computational efficiency. By restoring pairwise coordinates through simple, hardware-friendly operations, the method enables high-accuracy classification on standard benchmarks while minimizing resource usage. This is especially valuable for embedded systems where DSP and power constraints are critical.

## Related Concepts  
Binary KAN (Kolmogorov–Arnold Network), Spatial Orthogonality Collapse, Walsh characters, XNOR-popcount operations, W1A1 networks, parity planes, feature mixing, parameter efficiency, hardware-efficient neural networks.
