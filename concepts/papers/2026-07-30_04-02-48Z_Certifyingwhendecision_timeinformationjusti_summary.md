# Summary: 2026-07-30_04-02-48Z_Certifyingwhendecision_timeinformationjustifiesada.md
Saved: 2026-07-30 21:38
Source: 2026-07-30_04-02-48Z_Certifyingwhendecision_timeinformationjustifiesada.md
Model: None

---

## Summary  
The paper proposes **OPAL (Opportunity‑aware Policy Authorization for Laboratories)**, a framework that determines whether adaptive experimentation should be permitted by certifying that decision‑time information satisfies a precommitted contract of non‑trivial adaptation, controlled target risk, and positive executed value after cost. It also establishes an impossibility boundary showing that source outcomes and unlabelled target covariates cannot uniformly support such authorization under unrestricted conditional outcome shifts, while deriving a target‑calibrated recovery for practical use. The authors apply OPAL to an unseen 11 265‑compound Cell Painting partition, where the frozen gate selects 595 compounds, captures 384 positive opportunities and yields strictly positive executed value even under the least‑favourable completion, with a false‑activation upper bound of 5.18 %—well below a 7.5 % safety limit.

## Key Contributions  
- [Finding 1] Introduce OPAL as an opportunity‑aware policy authorization framework that certifies when decision‑time information justifies adaptive experimentation through a precommitted contract.  
- [Finding 2] Prove an impossibility boundary: source outcomes and unlabelled target covariates cannot uniformly support non‑trivial authorization under unrestricted conditional outcome shift, and derive a target‑calibrated recovery for this bound.  
- [Finding 3] Demonstrate OPAL’s empirical efficacy on the Cell Painting partition: 595 selected compounds, 384 positive opportunities captured, strictly positive executed value under least‑favourable completion, and a false‑activation rate of 5.18 % (≤7.5 %).

## Methodology  
OPAL treats adaptive experimentation as an authorized policy governed by a contract that mandates three conditions: (i) the adaptation must be non‑trivial; (ii) target risk is bounded; and (iii) the expected executed value exceeds its cost after accounting for opportunity cost. The authors first formalise these constraints, then analyse the feasibility of satisfying them when source outcomes are shifted conditionally on unlabelled covariates. This impossibility analysis yields a recovery function that estimates how far observed data deviate from the uniform‑support boundary. In practice, OPAL evaluates a frozen gate (a pre‑selected set of compounds) against these criteria using the recovered bound to certify whether enabling further measurements is safe.

## Results  
The Cell Painting experiment contains 11 265 compounds and six previously evaluated methods. Only OPAL achieved non‑zero activation while respecting risk control, selecting a frozen gate of 595 compounds that captured 384 positive opportunities. Under the least‑favourable completion scenario, the executed value remains strictly positive, and the false‑activation rate is 5.18 %, comfortably below the 7.5 % safety threshold set by OPAL’s contract.

## Significance  
OPAL provides a rigorous certification layer that separates policy misalignment from fundamental non‑certifiability in adaptive science, enabling safe experimentation without compromising scientific integrity. By linking decision‑time information to concrete risk and value constraints, the framework supports responsible innovation across domains such as pharmacogenomics and high‑throughput biology.

## Related Concepts  
- Decision‑time information  
- Adaptive experimentation  
- Precommitted contracts in algorithmic safety  
- Target risk control  
- Executed value (net benefit after cost)  
- False‑activation rate  
- Opportunity‑aware policy authorization  
- Impossibility boundaries and target‑calibrated recovery  
- Cell Painting partition data
