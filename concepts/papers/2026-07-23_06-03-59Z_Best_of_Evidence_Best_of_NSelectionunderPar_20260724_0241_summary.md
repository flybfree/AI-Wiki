# Summary: 2026-07-23_06-03-59Z_Best_of_Evidence_Best_of_NSelectionunderPartialVer.md
Saved: 2026-07-24 02:41
Source: 2026-07-23_06-03-59Z_Best_of_Evidence_Best_of_NSelectionunderPartialVer.md
Model: None

---

## Summary  
Best‑of‑Evidence (BoE) tackles the limitation of Best‑of‑N (BoN), which assumes that an entire candidate response can be verified with a reliable proxy score. In many vision‑language tasks, only partial evidence—such as a specific span, value, or relation—is verifiable, and the same claim may appear in multiple candidates with conflicting stances. BoE introduces an inference‑time selection framework that reuses a fixed candidate pool, encodes reusable claims via signed factor graphs, and allocates a limited budget of evidence actions to improve final choice. The method recovers BoN’s zero‑budget behavior while allowing selective use of partial verification, offering both theoretical analysis and practical gains.

## Key Contributions  
- [Finding 1] A formal model for selection under partial verification using signed candidate–factor graphs that captures reusable claims across candidates.  
- [Finding 2] An O(log K) versus Θ(K) query separation theorem showing that shared factor queries can dramatically reduce the number of evidence actions needed, with K being the pool size.  
- [Finding 3] Empirical results demonstrating BoE’s ability to improve fixed‑pool selection and rescue BoN failures on four medical VQA benchmarks when evidence is reliable, contrastive, and decision‑relevant.

## Methodology  
The authors treat each candidate as a node in a factor graph where edges represent reusable claims. Each claim carries a sign indicating which candidates support it versus contradict it. The controller decides which evidence actions (e.g., querying specific spans) to execute within a budget, updating the graph’s state and recomputing a score‑based selector that balances evidence cost against candidate preference.

## Results  
Theoretical analysis proves that residual evidence capacity caps any improvement beyond O(log K). Experiments on medical VQA datasets show BoE outperforms BoN by 3–7 % in fixed‑pool settings and reduces the number of queries needed to achieve comparable accuracy. The method also highlights channel‑quality and candidate‑generation limits that prevent universal gains.

## Significance  
BoE bridges a critical gap between theoretical selection under partial verification and practical model deployment, enabling more efficient use of limited evidence resources while preserving BoN’s simplicity in the zero‑budget case.

## Related Concepts  
- Best‑of‑N (BoN) selection  
- Factor graphs for claim reuse  
- Partial verification in VQA  
- Evidence budget allocation  
- O(log K) query separation
