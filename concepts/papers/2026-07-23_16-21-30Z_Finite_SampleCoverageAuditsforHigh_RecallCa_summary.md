# Summary: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Saved: 2026-07-24 02:54
Source: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Model: None

---

## Summary  
The paper tackles the problem of certifying that a high‑recall candidate generation stage does not miss too many relevant items, using only finite‑sample audit labels drawn from the excluded pool. It proves that auditing must include labels from this region because any bound on missed mass cannot be derived from inside‑only samples. The authors then develop an exact toolkit for converting audit results into recall guarantees and stress‑testing candidate generators under declared perturbation mechanisms.

## Key Contributions  
- [Finding 1] No procedure that uses only labels from the included pool can certify any non‑trivial bound on the missed mass; the audit must sample the excluded pool.  
- [Finding 2] Any valid finite‑sample audit that certifies fewer than *m* missed relevant items with high probability when none are present, even if adaptive and permitting full labeling of the included pool, must inspect on the order of *N₀/m* labels from the excluded pool.  
- [Finding 3] Excluded‑pool auditing is minimax rate‑optimal for missed‑mass certification in the zero‑miss regime.

## Methodology  
The authors formulate the audit problem as a finite‑sample coverage task with two disjoint pools: the candidate (included) set and its complement (excluded). They first prove impossibility of internal‑only audits via combinatorial arguments, then derive lower bounds on the number of excluded labels required to certify missed mass. Building on these theoretical limits, they construct an exact toolkit that uses binomial and hypergeometric inversion rather than asymptotic approximations. The toolkit can (i) compute confidence intervals for missed relevant items, (ii) convert those counts into recall estimates via a two‑pool design, (iii) certify simultaneously against any pre‑specified family of nested candidate generators, and (iv) produce stress‑test certificates that hold under declared perturbation mechanisms. All guarantees are valid only when the candidate generator, its generating family, and the audit rule are fixed before label examination.

## Results  
Theoretical results include: (i) impossibility of non‑trivial internal audits; (ii) a tight lower bound of ≈ N₀/m excluded labels for certifying m missed items in the zero‑miss regime; (iii) an exact finite‑sample toolkit that yields confidence intervals and recall conversions without asymptotic approximations; (iv) stress‑test certificates that remain valid under any declared perturbation mechanism. The lower bounds are shown to be asymptotically tight up to constant factors, confirming the optimality of excluded‑pool auditing.

## Significance  
This work bridges finite‑sample audit theory with high‑recall candidate generation pipelines, providing a principled method for selecting low‑burden generators that meet strict missed‑mass targets. By guaranteeing that audit labels are drawn from the excluded pool and by delivering exact conversion to recall, the toolkit reduces downstream loss of relevant items and improves overall pipeline efficiency.

## Related Concepts  
Finite‑sample coverage audits, minimax rate optimality, binomial/hypergeometric inversion, nested candidate generators, stress‑test certificates, zero‑miss regime, recall conversion.
