# Summary: 2026-08-03_05-24-03Z_CodingAgentsasTest_SuiteAuditors_FindingWhatOffici.md
Saved: 2026-08-03 23:23
Source: 2026-08-03_05-24-03Z_CodingAgentsasTest_SuiteAuditors_FindingWhatOffici.md
Model: None

---

## Summary  
The paper proposes a coding agent that audits official test suites for bugs missed by them, building adversarial suites to expose gaps and providing certification without relying on judge verdicts. It demonstrates that such agents can uncover verified accepted‑but‑buggy submissions across AtCoder and Codeforces, improving coverage of logic bugs while maintaining high precision.

## Key Contributions  
- [Finding 1] The agent identifies **589** verified accepted‑but‑buggy submissions among AtCoder’s 20,375 audited accepted submissions.  
- [Finding 2] Extending the same certification to all five agents yields a union floor of **906** such submissions, showing robust detection across multiple models.  
- [Finding 3] The agents’ coverage matches official suites within **1.7 pp** on logic bugs and outperforms them on problems lacking official tests.

## Methodology  
The authors construct adversarial test suites by generating diverse inputs that expose edge cases missed by existing suites; they then build a certification chain where multiple independently written accepted solutions agree, brute‑force resolves disagreements, and a per‑problem validator confirms legality. This replaces reliance on judge verdicts with consensus among alternative implementations.

## Results  
The agents collectively detect **906** buggy submissions, each verified without official judge input. Separate scoring shows each agent’s false‑positive rate stays within **1.7 pp** of the official suite; on Codeforces problems without official suites, the method reproduces all baselines at every tested input budget.

## Significance  
By providing a self‑validating audit tool that fills gaps in existing test suites and reduces reliance on judge verdicts, this work improves reliability of code evaluation for LLM training and deployment.

## Related Concepts  
adversarial testing, certification chains, consensus validation, off‑the‑shelf coding agents, test‑suite adequacy, bug detection precision.
