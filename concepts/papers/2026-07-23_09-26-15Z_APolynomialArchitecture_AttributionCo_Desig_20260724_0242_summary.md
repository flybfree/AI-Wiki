# Summary: 2026-07-23_09-26-15Z_APolynomialArchitecture_AttributionCo_DesignFramew.md
Saved: 2026-07-24 02:42
Source: 2026-07-23_09-26-15Z_APolynomialArchitecture_AttributionCo_DesignFramew.md
Model: None

---

## Summary  
The paper introduces APEX, a polynomial architecture‑attribution co‑design framework that makes the Aumann‑Shapley path integral computable exactly for graph neural networks (GNNs). By preserving a bounded multivariate polynomial form through a specialized GIN variant called PolyGIN, the authors enable Gauss–Legendre quadrature to evaluate the attribution with deterministic evaluation points and floating‑point precision. This yields feature‑level explanations that can be aggregated into node‑level scores while maintaining full completeness.

## Key Contributions  
- [Finding 1] APEX provides an exact analytical method for Aumann‑Shapley attribution in GNNs by bounding the derivative degree of the path integral.  
- [Finding 2] PolyGIN, a GIN‑style architecture with L polynomial transformation blocks, guarantees that the attribution derivative has degree at most 2^L−1.  
- [Finding 3] The framework reduces the number of quadrature evaluations to 2^{L‑1}, dramatically lowering computational cost while improving attribution fidelity over baselines.

## Methodology  
The authors first design PolyGIN, a graph neural network whose message‑passing, normalization and transformation steps keep scalar model scores (e.g., pre‑softmax logits) within a bounded multivariate polynomial. They analyze the degree of the derivative along any attribution path, showing it grows as 2^L−1 with each block. Using this bound they apply Gauss–Legendre quadrature exactly: the integral is evaluated at 2^{L‑1} deterministic points, producing feature‑level attributions that are then aggregated to node‑level scores while preserving completeness.

## Results  
Experiments on both synthetic and real‑world graph benchmarks demonstrate that PolyGIN retains competitive predictive performance compared with standard GNNs. The complete APEX framework yields higher attribution fidelity than baselines such as Integrated Gradients, and it requires far fewer evaluation points—scaling linearly with 2^{L‑1} rather than exponentially with network depth. Consequently, the number of required quadrature evaluations is substantially reduced.

## Significance  
Exact path integration for GNNs bridges theoretical attribution models with practical deployment, offering transparent explanations without sacrificing efficiency. By decoupling architectural design from numerical approximation, APEX enables researchers and practitioners to achieve high‑quality feature‑level insights while keeping computational overhead low.

## Related Concepts  
- Aumann‑Shapley attribution  
- Integrated Gradients (path‑integral method)  
- GIN (Graph Isomorphism Network) architectures  
- Polynomial form preservation in deep networks  
- Gauss–Legendre quadrature for exact integration  
- Feature‑level vs. node‑level explanations
