# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:25
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper addresses a long-standing conjecture in discrete geometry proposed by Lacoste-Julien and Jaggi in 2015 regarding the behavior of pyramidal width under vertex insertion. The authors present a definitive counterexample demonstrating that the pyramidal width of a polytope can indeed increase when a new vertex is added, provided that all original vertices remain vertices of the resulting structure. By constructing a specific configuration of six integer points in three-dimensional space, they prove that adding a single point can expand the geometric complexity measured by this metric. This finding fundamentally challenges previous assumptions about the monotonicity of pyramidal width in polyhedral combinatorics.

## Key Contributions
- **Disproof of Monotonicity Conjecture**: The primary contribution is the rigorous disproof of the 2015 conjecture that pyramidal width cannot increase during vertex insertion. This establishes a new boundary condition for understanding how geometric metrics behave under polytope modification.
- **Exact Counterexample Construction**: The authors provide an explicit, minimal counterexample involving six integer points in $\mathbb{R}^3$. This concrete instance serves as a definitive reference point for future research into polytope geometry and metric stability.
- **Verification Methodology**: A significant contribution is the development of a dependency-free exact verifier. This tool certifies both the face lattices via integer supporting hyperplanes and evaluates facial distances through finite rational calculations, ensuring the result is mathematically irrefutable.

## Methodology
The authors approached the problem by constructing two specific polytopes, $P$ and $Q$, where $Q$ is formed by adding a vertex to $P$. They defined $P$ as the convex hull of five vertices ($v_0$ through $v_4$) and $Q$ as the convex hull of these same five vertices plus a sixth vertex ($v_5$). To ensure the validity of the counterexample, they verified that all five original vertices of $P$ remained extreme points (vertices) in $Q$. The core of their method relied on the equivalence between pyramidal width and facial distance. They utilized integer supporting hyperplanes to certify the face lattices of both polytopes exactly. Finally, they computed the pyramidal width for both structures using finite rational arithmetic to avoid floating-point errors, thereby providing an exact proof rather than a numerical approximation.

## Results
The computational results show that while $P$ has a pyramidal width squared of $\frac{48}{353}$, the modified polytope $Q$ has a pyramidal width squared of $\frac{36}{133}$. Comparing these values reveals that the pyramidal width increases by a factor of approximately $1.410886779$ (specifically $\sqrt{1059/532}$). This quantitative increase confirms that the geometric property in question is not monotonic under vertex insertion, directly contradicting the prior theoretical expectation.

## Significance
This result is significant because it corrects a fundamental misunderstanding in the field of discrete geometry and polyhedral combinatorics. It implies that algorithms or theoretical bounds relying on the assumption of decreasing or stable pyramidal width during refinement may be flawed. Furthermore, it highlights the complex and non-intuitive nature of high-dimensional geometric metrics, urging researchers to re-evaluate stability assumptions in computational geometry and optimization problems involving polytope modifications.

## Related Concepts
- Pyramidal Width
- Polytope Geometry
- Vertex Insertion
- Facial Distance
- Convex Hulls
- Discrete Geometry
- Counterexamples in Mathematics
