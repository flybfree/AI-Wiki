# Summary: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Saved: 2026-07-24 03:04
Source: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Model: None

---

## Summary  
The paper tackles the problem of certifying, in a finite‑sample setting, how many “missed relevant” items remain after an initial high‑recall stage of candidate generation. It proves that any non‑trivial bound on this missed mass must be based on labels drawn from the excluded pool, and it shows that the optimal audit size scales as \(N_0/m\) where \(m\) is the desired missed‑mass target. The authors also introduce an exact finite‑sample toolkit built on binomial and hypergeometric inversion to certify missed mass, convert it to recall via a two‑pool design, handle nested generator families simultaneously, and produce stress‑test certificates that can be paired with review burden.

## Key Contributions  
- Finding 1: No procedure using only labels from inside the candidate set can certify any non‑trivial bound on the missed mass; auditing must sample the excluded pool.  
- Finding 2: Any valid audit that certifies fewer than \(m\) missed relevant items with high probability when none are present, even if adaptive and permitting full labeling of the included pool, must inspect on the order of \(N_0/m\) excluded‑pool labels; excluded‑pool auditing is minimax rate‑optimal in the zero‑miss regime.  
- Finding 3: An exact finite‑sample toolkit using binomial/hypergeometric inversion certifies missed mass, converts it to recall through a two‑pool design, certifies pre‑specified nested candidate generators simultaneously, and generates stress‑test certificates that can be paired with observable review burden.

## Methodology  
The authors model the high‑recall stage as a binary outcome for each item: either it is correctly retained (included in the candidate set) or it is missed. They argue that unrecovered relevant items can only reside in the excluded pool, because all items inside the pool are already accepted. Using combinatorial counting they derive a lower bound on the number of excluded‑pool labels required to certify zero misses with high probability, and then match this bound to an upper bound obtained by constructing an adaptive audit that samples only the excluded pool. The exact toolkit replaces asymptotic approximations with binomial/hypergeometric inversion, allowing precise computation of the probability that a given number of excluded labels suffices to guarantee no missed relevant items.

## Results  
The theoretical analysis yields a matching lower and upper bound: any optimal finite‑sample audit must inspect roughly \(N_0/m\) excluded‑pool labels. The toolkit provides exact certificates for missed mass, enabling conversion to recall via a two‑pool design. It also supports simultaneous certification of multiple nested candidate generators and produces stress‑test certificates that align with declared perturbation mechanisms. When paired with the review burden measured on the included pool, the method selects the least burdensome pre‑specified generator that meets the targeted missed‑mass level.

## Significance  
These results give provable guarantees for high‑recall pipelines, reducing wasted effort by focusing audits exclusively on the excluded pool where unrecovered relevant items can lie. The exact toolkit offers a flexible framework applicable across families of generators and perturbation mechanisms, improving reliability in machine‑learning evaluation processes without relying on asymptotic approximations.

## Related Concepts  
high‑recall candidate generation, missed mass, finite‑sample validity, audit sampling, binomial/hypergeometric distributions, minimax rate optimality, two‑pool design, stress‑test certificates, review burden.
