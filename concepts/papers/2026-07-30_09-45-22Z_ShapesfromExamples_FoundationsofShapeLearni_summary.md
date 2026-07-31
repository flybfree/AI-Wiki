# Summary: 2026-07-30_09-45-22Z_ShapesfromExamples_FoundationsofShapeLearninginRec.md
Saved: 2026-07-30 21:46
Source: 2026-07-30_09-45-22Z_ShapesfromExamples_FoundationsofShapeLearninginRec.md
Model: None

---

## Summary  
The paper tackles the problem of learning SHACL shape expressions from a set of positive and negative example nodes, focusing on recursive shapes expressed in the ELI fragment of the SHACL core. By formulating fitting existence and most‑specific fitting as decision problems, the authors prove tight exponential‑time upper bounds for the general case while delivering polynomial‑time algorithms for well‑founded, stable, and supported shape catalogues.

## Key Contributions  
- Found a tight exponential‑time upper bound on the existence of any shape expression that fits given positive and negative node sets.  
- Developed an algorithm that computes the most specific such expression in polynomial time under conditions where the catalogue is well‑founded, stable, and supported.  
- Provided polynomial‑time algorithms for special cases where the depth of recursion is bounded or the shape components are limited.

## Methodology  
The authors treat SHACL shapes as recursive expressions built from ELI description logic constructs. They formulate fitting existence as a decision problem: given sets P (positives) and N (negatives), does there exist an expression C that validates all nodes in P and none in N? The most‑specific fit is then defined as the unique maximal C satisfying this condition. Using combinatorial analysis of recursive definitions, they derive recurrence relations for the search space, unroll them to obtain exponential bounds, and exploit structural properties (well‑foundedness, stability, support) to collapse the recursion into polynomial work.

## Results  
For the general case the existence problem admits an O(2^{|P|+|N|}) algorithmic bound, which is tight up to a constant factor. When the shape catalogue satisfies well‑foundedness and stability, the authors obtain a polynomial bound of O(|G|^{k}), where k is the maximum recursion depth, yielding an algorithm that runs in time proportional to the graph size plus the number of shape components. The most‑specific fitting computation follows similarly, achieving polynomial complexity under the same conditions.

## Significance  
These theoretical guarantees and concrete algorithms enable automated validation of complex knowledge graphs at scale, reducing reliance on manual SHACL design. By providing provable upper bounds and efficient computation methods, the work advances both the correctness of graph models and the practical deployment of recursive shape learning in real‑world applications.

## Related Concepts  
SHACL shapes, ELI fragment, recursive shape catalogue, fitting problem (existence and most specific fit), descriptive logic, well‑founded semantics, stable semantics, support semantics, exponential‑time upper bound, polynomial‑time algorithm, knowledge graph validation.
