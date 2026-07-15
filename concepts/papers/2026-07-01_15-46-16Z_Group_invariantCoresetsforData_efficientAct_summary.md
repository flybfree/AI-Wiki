title: "Summary: 2026-07-01_15-46-16Z_Group_invariantCoresetsforData_efficientActiveLear.md"
# Summary: 2026-07-01_15-46-16Z_Group_invariantCoresetsforData_efficientActiveLear.md
Saved: 2026-07-01 21:01
Source: 2026-07-01_15-46-16Z_Group_invariantCoresetsforData_efficientActiveLear.md
Model: None

---


## Summary  
Active learning seeks to minimize labeling effort by selecting the most informative unlabeled instances. Standard coreset methods treat each sample independently, which can waste queries on transformed copies of the same instance and ignore known data symmetries. The authors introduce GRINCO, a group‑invariant coreset framework that operates in the quotient space induced by a transformation group, thereby selecting entire orbits rather than individual points. By combining quotient‑space k‑center selection with an orbit‑averaged loss and deriving a generalization bound, GRINCO achieves higher label efficiency when redundancy is present.

## Key Contributions  
- [Finding 1] Propose GRINCO, a group‑invariant coreset method that selects on orbits instead of raw samples.  
- [Finding 2] Use canonical representatives or learned orbit‑separating invariant embeddings to define practical quotient metrics and combine them with k‑center selection and an orbit‑averaged loss.  
- [Finding 3] Derive a generalization bound linking excess orbit‑averaged risk to quotient‑space coverage, label uncertainty, and intra‑orbit variability.

## Methodology  
The problem is approached by first identifying the transformation group that generates redundant instances (e.g., rotations). The authors construct a quotient space where each orbit represents a single equivalence class. Acquisition is performed in this quotient space using k‑center selection on representative points or learned invariant embeddings, ensuring that selected orbits cover diverse regions of the data manifold. Training proceeds via an orbit‑averaged loss that averages over all members of a sampled orbit, preserving invariance while allowing efficient computation.

## Results  
Experiments on synthetic scale‑invariant datasets and real image benchmarks with rotation‑induced redundancy demonstrate that GRINCO improves orbit coverage compared to conventional coreset baselines. The method also achieves stronger label efficiency, especially when group‑induced redundancy is substantial. Theoretical analysis confirms the derived bound holds across both settings.

## Significance  
GRINCO matters because it leverages known symmetries of data to reduce wasted labeling queries and improve active learning performance. By operating on quotient spaces rather than raw samples, it mitigates redundancy and yields more representative training sets, which is crucial for high‑dimensional or expensive labeling tasks.

## Related Concepts  
Group invariants, quotient space, k‑center selection, orbit‑averaged loss, generalization bound, active learning, coresets.
