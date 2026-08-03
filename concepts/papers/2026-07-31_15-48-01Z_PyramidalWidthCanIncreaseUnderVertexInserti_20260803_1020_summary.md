# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:20
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper presents a definitive counterexample to a long-standing conjecture in discrete geometry proposed by Lacoste-Julien and Jaggi in 2015. The original conjecture posited that the pyramidal width of a polytope is non-increasing when a new vertex is added, provided that all existing vertices remain vertices of the resulting structure. By constructing a specific configuration of six integer points in three-dimensional space, the authors demonstrate that this property does not hold universally. The study rigorously proves that under certain conditions, the insertion of a single vertex can actually increase the pyramidal width, thereby refuting the previous theoretical assumption and expanding the understanding of polytope geometry.

## Key Contributions
- **Refutation of a Conjecture**: The primary contribution is the exact disproof of the Lacoste-Julien and Jaggi conjecture regarding the monotonicity of pyramidal width under vertex insertion. This establishes that pyramidal width is not inherently stable or decreasing in this context.
- **Construction of a Minimal Counterexample**: The authors provide a concrete, minimal counterexample involving six integer points in $\mathbb{R}^3$. This specific geometric configuration serves as the foundational evidence for their theoretical claims.
- **Verification Framework**: The work introduces and utilizes a dependency-free exact verifier that certifies face lattices using integer supporting hyperplanes, ensuring the mathematical rigor of the results through finite rational calculations.

## Methodology
The authors approached the problem by constructing two specific polytopes, $P$ and $Q$, in three-dimensional Euclidean space. Polytope $P$ is defined as the convex hull of five vertices ($v_0$ through $v_4$), while polytope $Q$ includes an additional vertex ($v_5$). The methodology relies on precise coordinate selection for these integer points to ensure that all original vertices of $P$ remain extreme points (vertices) in $Q$. To validate the pyramidal width, the authors utilized the established equivalence between pyramidal width and facial distance. They certified the face lattices of both polytopes using integer supporting hyperplanes, allowing for the evaluation of every facial distance through exact finite rational arithmetic rather than approximate numerical methods.

## Results
The experimental and theoretical results show a clear increase in pyramidal width upon vertex insertion. Specifically, for the constructed polytopes, the square of the pyramidal width for $P$ is calculated as $\frac{48}{353}$, while for $Q$, it is $\frac{36}{133}$. Comparing these values reveals that the pyramidal width increases by a factor of approximately $1.410886779$ (specifically $\sqrt{1059/532}$). This quantitative result definitively contradicts the conjecture that the width should decrease or remain constant, proving that structural changes via vertex addition can expand this geometric measure.

## Significance
This finding is significant because it corrects a fundamental misunderstanding in the study of polytopes and their combinatorial properties. It impacts areas such as optimization theory and computational geometry where pyramidal width is used to analyze complexity and structure. By showing that width can increase, it suggests that adding constraints or points can sometimes complicate rather than simplify the geometric landscape, influencing future algorithms and theoretical models in discrete mathematics.

## Related Concepts
- Pyramidal Width
- Polytope Geometry
- Vertex Insertion
- Facial Distance
- Convex Hulls
- Discrete Mathematics
- Lacoste-Julien and Jaggi Conjecture
