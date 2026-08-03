# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:22
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper addresses a long-standing conjecture in discrete geometry proposed by Lacoste-Julien and Jaggi in 2015 regarding the behavior of pyramidal width under vertex insertion. The authors present a rigorous counterexample demonstrating that the pyramidal width of a polytope can indeed increase when a new vertex is added, provided that all original vertices remain vertices of the resulting structure. By constructing a specific configuration of six integer points in three-dimensional space, they disprove the assumption that pyramidal width is monotonically non-increasing under such operations. This finding fundamentally challenges previous theoretical bounds and assumptions within the field of polytope theory.

## Key Contributions
- **Disproof of Monotonicity Conjecture**: The primary contribution is the definitive refutation of the Lacoste-Julien and Jaggi conjecture, which posited that pyramidal width cannot increase when a vertex is added to a polytope while preserving existing vertices.
- **Exact Counterexample Construction**: The authors provide an explicit, minimal counterexample involving six integer points in $\mathbb{R}^3$. This concrete instance serves as irrefutable evidence against the conjecture, offering a tangible case study for future research.
- **Verification Tool Development**: Beyond the theoretical proof, the paper introduces a dependency-free exact verifier. This tool allows other researchers to independently certify face lattices and evaluate facial distances using finite rational calculations, ensuring the robustness of the results.

## Methodology
The authors approached this problem by leveraging the established equivalence between pyramidal width and facial distance in polytopes. They constructed two specific polytopes, $P$ and $Q$, where $Q$ is formed by adding a vertex to $P$. To ensure mathematical rigor, they certified both face lattices using integer supporting hyperplanes, which guarantees that the geometric properties are defined precisely without floating-point errors. The core of their methodology involved evaluating every facial distance through finite rational calculations. This approach allowed them to compute the exact pyramidal width for both polytopes and compare them directly, confirming the increase in width with absolute precision.

## Results
The experimental and theoretical results show a clear increase in pyramidal width. For the initial polytope $P = \conv\{v_0,\ldots,v_4\}$, the squared pyramidal width is calculated as $\PWidth(P)^2 = \frac{48}{353}$. For the extended polytope $Q = \conv\{v_0,\ldots,v_5\}$, where all five original vertices remain vertices, the squared pyramidal width is $\PWidth(Q)^2 = \frac{36}{133}$. The analysis reveals that vertex insertion increases the pyramidal width by a factor of $\sqrt{1059/532}$, which is approximately $1.410886779$. This quantitative result definitively proves that the width can grow significantly under the specified conditions.

## Significance
This work is significant because it corrects a fundamental misunderstanding in discrete geometry and optimization theory. The monotonicity of pyramidal width has implications for algorithms involving polytope approximations and vertex additions. By disproving this conjecture, the paper opens new avenues for research into the stability and variability of geometric measures during polytope modification. It also highlights the necessity of exact arithmetic in computational geometry to avoid subtle errors that might arise from approximate methods.

## Related Concepts
- Pyramidal Width
- Polytope Theory
- Vertex Insertion
- Facial Distance
- Discrete Geometry
- Integer Points in $\mathbb{R}^3$
- Face Lattices
- Supporting Hyperplanes
