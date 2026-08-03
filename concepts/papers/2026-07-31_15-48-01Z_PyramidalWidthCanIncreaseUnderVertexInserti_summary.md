# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:11
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper addresses a longstanding open problem in discrete geometry by providing a definitive counterexample to the conjecture proposed by Lacoste-Julien and Jaggi in 2015 regarding the behavior of pyramidal width under vertex insertion. The authors demonstrate that contrary to previous expectations, the pyramidal width of a polytope can strictly increase when a new vertex is added, provided that all original vertices remain extreme points of the resulting structure. By constructing a specific configuration of six integer points in three-dimensional space, the study establishes that adding a single vertex can significantly alter the geometric properties related to facial distances. This work not only resolves the conjecture but also highlights the complex and non-monotonic nature of polytope expansion metrics.

## Key Contributions
- **Disproof of Conjecture**: The primary contribution is the rigorous disproof of the Lacoste-Julien and Jaggi conjecture, which posited that pyramidal width is non-increasing under vertex insertion for full-dimensional polytopes where old points remain vertices.
- **Exact Counterexample Construction**: The authors provide an explicit, minimal counterexample consisting of six integer points in $\mathbb{R}^3$, proving that pyramidal width can increase by a specific factor of approximately $1.410886779$.
- **Verification Framework**: The paper introduces a dependency-free exact verifier that certifies the face lattices using integer supporting hyperplanes, ensuring that the theoretical results are computationally verifiable and free from floating-point errors.

## Methodology
The authors approached this problem by leveraging the established equivalence between pyramidal width and facial distance in polytopes. Instead of relying on approximate numerical methods, they utilized a purely algebraic and combinatorial approach. They constructed two specific polytopes, $P$ and $Q$, where $Q$ is formed by adding one vertex to $P$. To ensure the validity of their counterexample, they certified both face lattices using integer supporting hyperplanes. This allowed them to evaluate every facial distance through finite rational calculations, thereby avoiding any potential inaccuracies associated with floating-point arithmetic. The verification process was automated into a dependency-free exact verifier to accompany the theoretical proof.

## Results
The main result is the calculation of pyramidal widths for two specific polytopes defined by integer coordinates in $\mathbb{R}^3$. For polytope $P$, formed by five vertices, the square of the pyramidal width is calculated as $\frac{48}{353}$. For polytope $Q$, which includes an additional sixth vertex while retaining all original vertices, the square of the pyramidal width is $\frac{36}{133}$. The comparison reveals that $\PWidth(Q)^2 > \PWidth(P)^2$, demonstrating an increase in pyramidal width. Specifically, the width increases by a factor of $\sqrt{1059/532}$, which is approximately $1.410886779$. This quantitative result serves as concrete evidence against the monotonicity conjecture.

## Significance
This research is significant because it corrects a fundamental misunderstanding in the field of discrete geometry and optimization related to polytope expansion. By disproving the conjecture, it opens new avenues for understanding how geometric metrics behave under structural changes. It also impacts the theoretical foundations of algorithms that rely on pyramidal width or facial distance as stability or complexity measures. The introduction of exact verification methods provides a robust template for future research in computational geometry, ensuring that theoretical claims are backed by rigorous, error-free proofs.

## Related Concepts
- Pyramidal Width
- Facial Distance
- Polytope Vertex Insertion
- Discrete Geometry
- Convex Hulls
- Integer Points in $\mathbb{R}^3$
- Face Lattices
- Supporting Hyperplanes
