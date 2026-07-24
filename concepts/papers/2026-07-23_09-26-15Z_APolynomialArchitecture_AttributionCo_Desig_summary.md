# Summary: 2026-07-23_09-26-15Z_APolynomialArchitecture_AttributionCo_DesignFramew.md
Saved: 2026-07-24 02:35
Source: 2026-07-23_09-26-15Z_APolynomialArchitecture_AttributionCo_DesignFramew.md
Model: None

---

## Summary  
The paper introduces APEX, a polynomial architecture‑attribution co‑design framework that makes the Aumann–Shapley attribution integral for graph neural networks (GNNs) exact by preserving a bounded multivariate polynomial form of model scores. By employing PolyGIN—a GIN‑style network whose message‑passing, normalization and transformation steps maintain this polynomial structure—the authors guarantee that the derivative along any attribution path has degree at most \(2^{L}-1\) for an architecture with \(L\) polynomial blocks. This theoretical bound enables Gauss–Legendre quadrature to evaluate the path integral exactly (up to floating‑point precision) using only \(2^{L-1}\) deterministic points, yielding both feature‑level and node‑level explanations while preserving completeness of attribution. The framework therefore bridges exact theory with practical GNN inference.

## Key Contributions  
- [Finding 1] PolyGIN maintains a bounded multivariate polynomial form for scalar model scores across all message‑passing steps in the network.  
- [Finding 2] The derivative along an attribution path is limited to degree \(2^{L}-1\), allowing exact quadrature evaluation with \(2^{L-1}\) points.  
- [Finding 3] APEX reduces the number of evaluations required for path integration compared with standard baselines while preserving full attribution fidelity.

## Methodology  
The authors designed PolyGIN as a GIN‑style architecture where each polynomial transformation block applies an operation that preserves the polynomial nature of the output. By analyzing how successive message‑passing and normalization steps affect the degree of the scalar score, they derive the bound \(2^{L}-1\). This bound justifies using Gauss–Legendre quadrature, which is exact for polynomials up to a certain order, to compute the Aumann–Shapley path integral. Feature attributions are obtained by integrating the model score along the attention path and then aggregated into node‑level scores, ensuring that the explanation remains complete.

## Results  
Experiments on both synthetic graphs (e.g., citation networks) and real‑world datasets (e.g., Cora, PubMed) demonstrate that PolyGIN retains competitive predictive performance relative to standard GNNs. The APEX framework achieves higher attribution fidelity than baselines such as Integrated Gradients and DeepLIFT, while requiring substantially fewer evaluation points—often a factor of two or more reduction in computational cost. Ablation studies confirm that the exact quadrature scheme is the primary source of the improved efficiency.

## Significance  
Exact Aumann–Shapley attribution is valuable because it provides theoretically sound, complete explanations without relying on finite‑sample approximations. By embedding this guarantee into a polynomial GNN architecture, APEX offers a practical pathway to interpretable GNN predictions, reducing both interpretability gaps and inference overhead in real applications.

## Related Concepts  
Aumann–Shapley attribution, Integrated Gradients, path integral formulation, Gauss–Legendre quadrature, GIN (Graph Isomorphism Network), polynomial networks, feature‑level vs. node‑level explanations, APEX framework.
