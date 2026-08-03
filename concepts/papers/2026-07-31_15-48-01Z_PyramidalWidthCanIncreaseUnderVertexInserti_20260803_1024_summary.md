# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:24
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper addresses a longstanding conjecture in discrete geometry proposed by Lacoste-Julien and Jaggi in 2015, which posited that the pyramidal width of a polytope is non-increasing when a new vertex is added, provided all original vertices remain extreme points. The author, Jinze Zhao, presents a definitive counterexample to this conjecture using a specific configuration of six integer points in three-dimensional Euclidean space ($\mathbb{R}^3$). By constructing two polytopes, $P$ and $Q$, where $Q$ is formed by adding a vertex to $P$ without altering the status of $P$'s original vertices, the study demonstrates that pyramidal width can indeed increase. This finding fundamentally challenges previous assumptions about the monotonicity of geometric complexity measures during polytope expansion.

## Key Contributions
- **Disproof of Conjecture**: The primary contribution is the rigorous disproof of the 2015 Lacoste-Julien and Jaggi conjecture regarding the non-increasing nature of pyramidal width under vertex insertion.
- **Exact Counterexample Construction**: The author constructs a precise counterexample involving six integer points in $\mathbb{R}^3$, providing concrete coordinates for vertices $v_0$ through $v_5$ that satisfy the necessary geometric conditions.
- **Computational Verification Tool**: A dependency-free exact verifier is developed and provided alongside the paper, allowing other researchers to independently certify the face lattices and facial distances of similar polytopes using integer supporting hyperplanes.

## Methodology
The authors approached this problem by leveraging the mathematical equivalence between pyramidal width and facial distance within polytope theory. Instead of relying on approximate numerical methods, the methodology emphasizes exact arithmetic to ensure rigorous proof validity. The process involved defining two specific convex hulls: $P$, formed by five vertices, and $Q$, formed by adding a sixth vertex $v_5$ to the set of vertices defining $P$. The critical step was verifying that all five original vertices of $P$ remained vertices (extreme points) in the new polytope $Q$. To achieve this, the authors certified the face lattices of both polytopes using integer supporting hyperplanes. This allowed for the evaluation of every facial distance through finite rational calculations, ensuring that the results were exact and free from floating-point errors. The proof relies on comparing the squared pyramidal widths of $P$ and $Q$ directly via these rational evaluations.

## Results
The experimental and theoretical results confirm that vertex insertion can strictly increase pyramidal width. For the constructed polytopes, the squared pyramidal width of $P$ is calculated as $\frac{48}{353}$, while for $Q$, it is $\frac{36}{133}$. Comparing these values reveals that $\PWidth(Q)^2 > \PWidth(P)^2$. Specifically, the pyramidal width increases by a factor of $\sqrt{1059/532}$, which is approximately $1.410886779$. This quantitative result provides irrefutable evidence that the geometric property in question does not behave monotonically under the specified conditions, directly contradicting the prior conjecture.

## Significance
This research is significant because it corrects a fundamental misunderstanding in discrete geometry and optimization theory regarding how polytope complexity metrics evolve. Pyramidal width is closely related to other important measures such as facial distance and condition numbers, which are critical in analyzing the performance of algorithms in linear programming and machine learning. By showing that these widths can increase upon vertex addition, the paper implies that algorithmic stability or convergence properties previously thought to be guaranteed by monotonicity may not hold. This necessitates a re-evaluation of theoretical bounds and assumptions in fields relying on polytope geometry for complexity analysis.

## Related Concepts
- Pyramidal Width
- Polytope Geometry
- Vertex Insertion
- Facial Distance
- Convex Hulls
- Discrete Geometry
- Lacoste-Julien and Jaggi Conjecture
- Integer Points in $\mathbb{R}^3$
