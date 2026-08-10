# Summary: 2026-08-07_12-26-03Z_CapacityConfoundsandCoverageGuaranteesinAdaptiveSu.md
Saved: 2026-08-09 22:56
Source: 2026-08-07_12-26-03Z_CapacityConfoundsandCoverageGuaranteesinAdaptiveSu.md
Model: None

---

## Summary  
The paper investigates whether adaptive capacity allocation in sub‑model federated learning (FL) can reliably estimate client data heterogeneity from the server’s observed updates. Using HAS‑FL as a test framework, the authors demonstrate that such estimates are heavily confounded by device capacity rather than actual label‑distribution differences. They also reveal a hidden failure mode where uniform allocation below full width leaves uncovered parameters at random initialization, degrading global model performance. Finally, they compare adaptive policies with matched‑budget baselines and find that random allocation performs identically to uniform allocation on image benchmarks while consuming more capacity. The core contribution is that parameter coverage—not intelligent allocation—protects accuracy in constrained FL scenarios.

## Key Contributions  
- [Finding 1] Update‑divergence estimates of client heterogeneity are dominated by device capacity, not data signal, across multiple datasets and seeds.  
- [Finding 2] A simple coverage guarantee eliminates a failure mode where capped clients leave uncovered parameters at random initialization.  
- [Finding 3] Matched‑budget analysis shows adaptive allocation offers no advantage over uniform allocation on image tasks and is the weakest strategy on naturally partitioned text data.

## Methodology  
The authors employ HAS‑FL, an adaptive capacity‑allocation framework that allocates sub‑model width based on estimated client heterogeneity. To validate their findings they generate reproducible partitions of ground‑truth label distributions, compute divergence between observed updates and true label distributions using two corrected estimators, and compare three allocation policies: (1) uniform width assignment, (2) random allocation to a fixed average budget, and (3) adaptive allocation via HAS‑FL. Coverage is measured by the fraction of global parameters that receive at least one update from each client.

## Results  
Statistical analysis shows strong negative correlation between estimate values and device capacity after controlling for data, indicating a capacity confound. When every client is capped below full width, uncovered parameters remain initialized randomly and cause progressive degradation of global model accuracy—a phenomenon removed by the coverage guarantee. Experimentally, adaptive allocation consumes more capacity than uniform allocation on image benchmarks, while on the text benchmark it yields the lowest performance among all three strategies.

## Significance  
The study underscores that in sub‑model FL, parameter coverage is the primary driver of accuracy rather than sophisticated heterogeneity estimation or capacity budgeting. Future system designs must separate true data heterogeneity signals from capacity effects to avoid hidden failures and ensure robust learning across heterogeneous devices.

## Related Concepts  
- Sub‑model federated learning (FL)  
- Capacity allocation / budgeting  
- Data heterogeneity estimation  
- Global model aggregation  
- Coverage guarantee  
- HAS‑FL framework  
- Parameter initialization bias  
- Matched‑budget analysis
