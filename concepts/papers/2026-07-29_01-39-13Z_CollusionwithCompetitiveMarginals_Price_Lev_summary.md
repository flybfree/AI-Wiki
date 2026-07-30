# Summary: 2026-07-29_01-39-13Z_CollusionwithCompetitiveMarginals_Price_LevelAudit.md
Saved: 2026-07-29 21:34
Source: 2026-07-29_01-39-13Z_CollusionwithCompetitiveMarginals_Price_LevelAudit.md
Model: None

---

## Summary  
The paper argues that algorithmic collusion can be profitable even when individual agents’ marginal prices remain competitive, and that standard price‑level audit methods are blind to such collusion by construction. It shows that tests based on single‑agent data cannot detect the hidden coupling of bid components because their power equals the false‑positive rate regardless of sample size. The authors provide three empirical findings: (1) residual correlation in language‑model bids, (2) temperature dependence of the effect, and (3) high dependence in Ethereum auction data. These results demonstrate that detection is not a matter of power but of design.

## Key Contributions  
- [Finding 1] The theoretical result that any single‑agent audit has power equal to its false‑positive rate for all coupling strengths up to comonotonicity, making the methodology blind by construction.  
- [Finding 2] Empirical evidence in language‑model deployments showing a statistically significant residual correlation between two deployments of the same model across developers.  
- [Finding 3] Real‑world Ethereum auction data reveal that the honest population exhibits extreme dependence, requiring audit thresholds far above typical false‑positive rates.

## Methodology  
The authors first construct a theoretical model where each bidding agent’s bid is a sum of a competitive component and an unexplained component shared across agents. They then analyze any test that uses only one agent’s price history, proving its detection power equals the false‑positive rate independent of sample size or coupling strength. Empirically they apply this framework to (i) 20 language‑model models with three deployment prompts each, (ii) temperature‑scaled sampling in those deployments, and (iii) 24 days of Ethereum block‑building auction data.

## Results  
Theoretical: For any coupling up to comonotonicity, the audit’s power is exactly its false‑positive rate. Empirical: (1) residual correlation of +0.053 between two deployments of a single model, 95% CI [0.030,0.078]; (2) p=0.002 for monotonic decline in coupling as temperature rises; (3) honest bidder pairs have dependence such that a 5% false‑positive rate screen sits above +0.50 to +0.81, 20–32 times the family‑wise threshold.

## Significance  
This work reframes algorithmic collusion detection from a statistical power issue to a design flaw: auditors cannot uncover profitable conspiracies that leave each agent’s marginal price competitive. The findings have regulatory implications because they show that even sophisticated, out‑of‑sample audits are blind, and that the real problem is not under‑powered tests but the inability of single‑agent metrics to capture multi‑identity collusion.

## Related Concepts  
- Algorithmic collusion; marginal price; competitive law; unexplained bid component; false‑positive rate; comonotonicity; Herfindahl index; temperature scaling; Ethereum auction data.
