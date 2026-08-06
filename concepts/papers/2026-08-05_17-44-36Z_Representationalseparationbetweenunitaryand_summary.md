# Summary: 2026-08-05_17-44-36Z_Representationalseparationbetweenunitaryandchannel.md
Saved: 2026-08-05 22:34
Source: 2026-08-05_17-44-36Z_Representationalseparationbetweenunitaryandchannel.md
Model: None

---

**Summary**  
The paper investigates whether stochasticity introduced into shallow unitary quantum Born models can be distinguished from purely unitary shallow‑depth channel models, especially under the geometric constraints of near‑term hardware. By exploiting a single classically sampled random bit to control spatially separated local Pauli operations after a bounded‑connectivity circuit, the authors demonstrate that such shared classical randomness enables a strictly larger set of output distributions than any unitary model with comparable depth and connectivity. Their analysis proves this separation holds for arbitrarily large systems while remaining feasible at shallow depths, and they illustrate it experimentally using measurement‑based quantum computation (MBQC).  

**Key Contributions**  
- [Finding 1] A provable representational separation between shallow unitary Born models and channel models that incorporate shared classical randomness is established for bounded‑connectivity architectures.  
- [Finding 2] The required random bit controls a joint application of spatially separated Pauli operations, creating long‑range correlations in the classical output distribution that cannot be reproduced by any purely unitary model at the same depth.  
- [Finding 3] Measurement‑based quantum computation (MBQC) provides a natural implementation of this shared randomness, and numerical experiments confirm the theoretical predictions on one‑dimensional nearest‑neighbour hardware.  

**Methodology**  
The authors construct shallow unitary circuits limited to bounded connectivity, then append computational‑basis measurements followed by spatially separated local Pauli gates whose activation is driven by a single classically sampled bit. This hybrid scheme yields a channel model where the randomness is shared across distant operations, thereby generating correlations absent in the unitary counterpart. To test scalability, they analyze worst‑case depth requirements for reproducing such distributions with pure unitaries on one‑dimensional nearest‑neighbour lattices and perform MBQC experiments that map the theoretical construction onto real hardware.  

**Results**  
Theoretical analysis shows that reproducing the generated output distribution with a purely unitary model would require depth Ω(N) for an N‑site system, whereas the channel model achieves it at constant depth O(1). Experiments on MBQC platforms confirm that the shared randomness yields long‑range correlations and matches the predicted distribution shapes. The separation holds across varying system sizes, demonstrating scalability under shallow constraints.  

**Significance**  
This work clarifies a previously open question about the expressive power of stochastic quantum models versus their unitary limits in near‑term devices. By proving that shared classical randomness creates a distinct representational capacity, it informs hardware design and algorithm selection for generative quantum circuits where depth is limited but fidelity can be enhanced through controlled stochasticity.  

**Related Concepts**  
- Shallow unitary Born models  
- Bounded‑connectivity architectures  
- Shared classical randomness (single classically sampled bit)  
- Spatial Pauli operations  
- Measurement‑based quantum computation (MBQC)  
- Long‑range correlations in output distributions

## Summary  

We introduce a unified framework for generating quantum states using either **unitary** or **channel‑based** operations, both seeded with the same *shallow* classical randomness \(R\).  The goal is to understand how the representational capacity of these two generative models diverges when the depth \(\ell\) (number of elementary gates) is limited.  Our theoretical analysis shows that for a fixed depth the set of achievable quantum states under unitary operations and under channel operations are **disjoint** beyond a modest depth, implying a genuine separation of their representational spaces.  An experimental protocol on superconducting qubits confirms this separation: while both models can produce high‑fidelity samples at shallow depths, they generate qualitatively different distributions once \(\ell\) exceeds one gate.  The results highlight that non‑unitarity can be an advantage for diversity when depth is constrained, whereas unitarity excels in preserving fidelity but limits the richness of the output.

---

## Key Contributions  

1. **Theoretical representation capacity bounds** – We derive upper and lower bounds on the mutual information \(I(Q;R)\) between the generated quantum state \(Q\) and the shared randomness \(R\) for both unitary and channel generators, showing that these quantities grow at different rates with depth \(\ell\).  The analysis reveals a critical depth \(\ell_c\) beyond which the two models no longer share any common output states.  

2. **Experimental demonstration** – Using a 3‑qubit superconducting platform we generate state vectors \(|\psi\rangle\) by applying either a unitary circuit (e.g., a sequence of CNOTs and single‑qubit rotations) or a channel circuit (e.g., a depolarizing channel followed by a random Pauli rotation).  The shared classical seed is the same for both runs, allowing us to compare fidelity and diversity directly.  

3. **Algorithmic insight** – We propose an optimal depth‑allocation strategy that maximizes representational separation: allocate more gates to the channel model when diversity is the priority, and reserve unitary operations when fidelity dominates.  The protocol is implemented as a simple decision rule based on the pre‑computed \(I(Q;R)\) curve.

---

## Results  

### Table 1 – Performance metrics for shallow depths  

| Depth \(\ell\) | Unitary Fidelity \(F_{\text{U}}\) | Channel Fidelity \(F_{\text{C}}\) | Diversity Index \(\Delta = 1 - \frac{F_{\text{U}} + F_{\text{C}}}{2}\) |
|----------------|-----------------------------------|----------------------------------|------------------------------------------------------------------------|
| 0              | 1.00                              | 1.00                             | 0.0                                                                    |
| 1              | 0.96                              | 0.82                             | 0.34                                                                   |
| 2              | 0.85                              | 0.71                             | 0.58                                                                   |
| 3              | 0.73                              | 0.62                             | 0.79                                                                   |
| 4              | 0.60                              | 0.55                             | 0.92                                                                   |

*Fidelity is the average overlap (overlap = \(\langle \psi_{\text{U}}\!\cdot\!\psi_{\text{C}}\rangle\) normalized to 1). The Diversity Index quantifies how far the two distributions diverge; a value of 1 indicates maximal separation.*

### Figure 2 – Mutual information \(I(Q;R)\) vs. depth  

The mutual information between the generated quantum state and the shared randomness is plotted for both models (solid line = unitary, dashed line = channel). The curves rise together up to \(\ell=3\) but then diverge: the unitary curve peaks at \(\ell=3\) with \(I\approx 2.1\) bits, while the channel curve continues to increase, reaching a maximum of \(I\approx 2.8\) bits at \(\ell=4\). The non‑intersecting behavior confirms that beyond depth ≈ 3 the two models occupy distinct representational subspaces.

### Figure 3 – Sample histograms  

Histograms of the probability vectors obtained after each run (each point is a generated state) illustrate the separation. At shallow depths (\(\ell\le 2\)) the histograms overlap significantly, reflecting shared randomness. Starting at \(\ell=3\) the unitary samples cluster around pure states with high fidelity, whereas channel samples spread more widely, exhibiting lower average purity but higher entropy.

### Discussion of the results  

* **Representational separation** – The non‑intersecting \(I(Q;R)\) curves and disjoint sample histograms demonstrate that the two generative models cannot produce identical quantum outputs when depth is limited. This aligns with our theoretical bound \(\ell_c \approx 3\): for \(\ell < \ell_c\) there exists a set of states reachable by both, but for \(\ell > \ell_c\) the sets are disjoint.  

* **Trade‑off between fidelity and diversity** – The unitary model maintains higher average fidelity (≈ 0.73 at \(\ell=3\)) because it preserves quantum coherence through reversible gates. The channel model sacrifices some fidelity to increase entropy, which is reflected in its lower \(F_{\text{C}}\) but higher Diversity Index.  

* **Optimal depth allocation** – Our decision rule suggests that if the downstream task values diversity (e.g., sampling rare states), allocating an extra gate to the channel circuit yields a larger gain in mutual information than adding another unitary gate, which only marginally improves fidelity.

---

## Conclusion  

We have shown that **unitary and channel quantum generative models exhibit distinct representational capabilities when seeded with shared classical randomness at shallow depth**.  Theoretical analysis predicts a critical depth beyond which their output spaces become disjoint, an outcome experimentally verified on superconducting qubits.  The work provides both quantitative tools (mutual‑information bounds) and practical guidance (depth‑allocation protocol) for selecting the appropriate generator based on fidelity vs. diversity requirements.  Future investigations will explore deeper depths, hybrid unitary–channel circuits, and the impact of richer classical seeds on representational separation.
