# Summary: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Saved: 2026-07-24 03:11
Source: 2026-07-23_16-21-30Z_Finite_SampleCoverageAuditsforHigh_RecallCandidate.md
Model: None

---

## Summary  
The paper tackles the problem of certifying how many relevant items are missed by an initial high‑recall candidate generation stage, where those missed items cannot be recovered later in a pipeline. It proves that any finite‑sample audit must draw labels from the excluded pool, not only from the candidates, and derives a matching lower bound on the number of such audits needed to certify a small missed mass with high probability. Building on this theoretical foundation, the authors present an exact finite‑sample toolkit based on binomial and hypergeometric inversion that can certify missed mass, convert it to recall, handle multiple candidate generators simultaneously, and generate stress‑test certificates.  

## Key Contributions  
- [Finding 1] No procedure that uses only labels from inside the candidate set can certify any non‑trivial bound on the missed relevant mass; audits must sample the excluded pool where unrecovered items reside.  
- [Finding 2] Any valid audit that certifies fewer than m missed relevant items with high probability when none are present, even if adaptive and allowed to label the entire included pool, must inspect on the order of N₀/m excluded‑pool labels, establishing that excluded‑pool auditing is minimax rate‑optimal in the zero‑miss regime.  
- [Finding 3] An exact finite‑sample toolkit using binomial and hypergeometric inversion can certify missed mass, convert it to recall via a two‑pool design, certify pre‑specified families of nested candidate generators simultaneously, and produce stress‑test certificates against declared perturbation mechanisms.  

## Methodology  
The authors formalize the missed‑mass certification as a finite‑sample problem, first showing impossibility of internal‑only audits through combinatorial arguments. They then prove a matching lower bound by analyzing the worst‑case scenario where no relevant items are present, demonstrating that inspecting ≈ N₀/m excluded labels is necessary and sufficient for optimal performance. The toolkit leverages exact inversion formulas (binomial and hypergeometric) rather than asymptotic approximations, enabling precise probability calculations, conversion of missed mass to recall through a two‑pool design, simultaneous certification across multiple candidate generators, and generation of stress‑test certificates that validate the audit rule against declared perturbation mechanisms. All guarantees are valid when the candidate generator, its pre‑specified family, and the audit rule are fixed before label examination.  

## Results  
Theoretical results show that in the zero‑miss regime, excluded‑pool auditing achieves a rate of O(N₀/m), which is optimal under any protocol. The exact toolkit provides closed‑form certificates for missed mass, enabling conversion to recall and simultaneous verification across nested candidate generators. It also generates stress‑test certificates that can be paired with observable review burden to select the least burdensome pre‑specified generator meeting a target missed‑mass level. These results hold under the fixed‑protocol assumption, providing rigorous guarantees without reliance on asymptotic approximations.  

## Significance  
This work matters because it supplies a mathematically sound method for auditing high‑recall pipelines, ensuring that critical relevant items are not lost to later stages. By proving excluded‑pool audits are minimax optimal and delivering exact finite‑sample tools, the authors enable scalable systems to certify missed mass with minimal label cost, thereby reducing review burden while maintaining performance guarantees. The approach is applicable across many domains where early filtering decisions have irreversible consequences, such as information retrieval, medical triage, and recommendation systems.  

## Related Concepts  
finite‑sample coverage audits, candidate generation, recall, missed mass, excluded pool, minimax rate‑optimal, binomial inversion, hypergeometric inversion, two‑pool design, stress‑test certificates
