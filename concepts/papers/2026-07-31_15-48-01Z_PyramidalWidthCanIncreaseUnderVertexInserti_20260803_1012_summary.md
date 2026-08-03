# Summary: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Saved: 2026-08-03 10:12
Source: 2026-07-31_15-48-01Z_PyramidalWidthCanIncreaseUnderVertexInsertion.md
Model: None

---

## Summary
This paper addresses a longstanding open conjecture in discrete geometry proposed by Lacoste-Julien and Jaggi in 2015 regarding the behavior of pyramidal width under vertex insertion. The authors provide a definitive counterexample demonstrating that the pyramidal width of a polytope can indeed increase when a new vertex is added, provided that all original vertices remain vertices of the resulting structure. By constructing a specific configuration of six integer points in three-dimensional space, they prove that the conjecture does not hold universally. This work resolves the theoretical question by showing that pyramidal width is not monotonic with respect to vertex addition, thereby correcting a previously held assumption in the field.

## Key Contributions
- **Disproof of Monotonicity Conjecture**: The primary contribution is the rigorous disproof of the Lacoste-Julien and Jaggi conjecture, which posited that pyramidal width cannot increase when a vertex is added to a polytope while preserving existing vertices.
- **Exact Counterexample Construction**: The authors present an explicit, exact counterexample involving six integer points in $\mathbb{R}^3$. This concrete instance serves as a definitive boundary case where the geometric property behaves contrary to previous theoretical expectations.
- **Verification Framework**: The paper introduces a dependency-free exact verifier that certifies the face lattices using integer supporting hyperplanes and evaluates facial distances through finite rational calculations, ensuring the result is mathematically rigorous and reproducible.

## Methodology
The authors approached this problem by leveraging the established equivalence between pyramidal width and facial distance within polytope theory. To construct the counterexample, they defined two specific polytopes, $P$ and $Q$, where $Q$ is formed by adding a vertex to $P$. They meticulously selected six integer coordinates for the vertices to ensure computational precision and avoid floating-point errors. The methodology involved certifying the face lattices of both polytopes using integer supporting hyperplanes, which guarantees that the combinatorial structure is accurately represented. Subsequently, they evaluated every facial distance associated with these structures through finite rational calculations. This approach allowed them to compute the exact squared pyramidal widths for both $P$ and $Q$, facilitating a direct comparison without approximation errors.

## Results
The experimental and theoretical results confirm that vertex insertion can increase pyramidal width. Specifically, for the constructed polytopes where all five vertices of $P$ remain vertices in $Q$, the squared pyramidal width of $P$ is calculated as $\frac{48}{353}$, while the squared pyramidal width of $Q$ is $\frac{36}{133}$. Consequently, the pyramidal width increases by a factor of approximately $1.410886779$, derived from the square root of the ratio $1059/532$. This quantitative result definitively shows that the geometric complexity, as measured by pyramidal width, can expand rather than contract or remain stable during vertex insertion operations.

## Significance
This finding is significant because it corrects a fundamental misunderstanding in discrete geometry and optimization theory regarding the stability of polytope properties under modification. It implies that algorithms relying on the assumption of non-increasing pyramidal width may need re-evaluation, particularly in contexts involving dynamic polytope updates or incremental vertex additions. Furthermore, it highlights the subtle and non-intuitive nature of high-dimensional geometric structures, emphasizing the need for rigorous exact verification over heuristic assumptions.

## Related Concepts
- Pyramidal Width
- Facial Distance
- Polytope Vertex Insertion
- Discrete Geometry
- Lacoste-Julien and Jaggi Conjecture
- Integer Supporting Hyperplanes
- Face Lattice Certification
