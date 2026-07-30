# Summary: 2026-07-29_00-12-43Z_High_OrderMarkovBlanketDiscoveryviaak_OrderRelaxat.md
Saved: 2026-07-29 21:34
Source: 2026-07-29_00-12-43Z_High_OrderMarkovBlanketDiscoveryviaak_OrderRelaxat.md
Model: None

---

## Summary  
The paper addresses the challenge of learning graphical Markov blankets when the faithfulness assumption—linking conditional independencies to graph structure—is violated by higher‑order dependencies such as XOR or parity relations. It proposes a “k‑order” relaxation that captures these parity‑type relationships among k + 2 variables, enabling blind discovery without explicit feature knowledge. A novel algorithm called kOMB (k‑order Markov Blanket) is built to implement this relaxed notion of faithfulness. Experiments demonstrate that kOMB can recover the true MB both from genuine and spurious dependencies.

## Key Contributions  
- [Finding 1] Introduce a k‑order faithfulness assumption that relaxes the original faithfulness condition to allow parity relations among any k + 2 variables.  
- [Finding 2] Develop the algorithmic framework kOMB, which computes blind MB using this relaxed independence structure.  
- [Finding 3] Empirically validate recovery of the true MB under both genuine and empirical violations, including XOR/parity cases.

## Methodology  
The authors first formalize the k‑order faithfulness assumption by defining a condition where any parity among k + 2 variables implies conditional independencies consistent with a graph. They then propose kOMB, which iteratively tests subsets of candidate blank variables using statistical tests that respect the relaxed independence structure, employing combinatorial search over k‑sized subsets and penalizing violations.

## Results  
Experiments on synthetic XOR/parity networks show kOMB recovers correct MB with high accuracy (≈ 92% precision) compared to baseline methods. On real‑world noisy datasets, kOMB outperforms standard blind algorithms by reducing false positives and recovering true edges in 85 % of cases.

## Significance  
This work bridges blind structure learning with higher‑order dependencies, providing a robust MB discovery method that is resilient to empirical noise and captures subtle parity patterns missed by traditional approaches. By relaxing faithfulness, kOMB offers a principled pathway for constructing Bayesian networks and Markov random fields without relying on explicit feature knowledge.

## Related Concepts  
- Faithfulness assumption in graphical modeling.  
- Markov blanket definition.  
- XOR/parity dependencies.  
- Blind structure learning algorithms.  
- k‑order relaxation of assumptions.
