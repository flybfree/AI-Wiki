# Summary: 2026-07-28_02-57-19Z_SecDrift_MeasuringSector_ConditionedSecurityDrifti.md
Saved: 2026-07-28 22:28
Source: 2026-07-28_02-57-19Z_SecDrift_MeasuringSector_ConditionedSecurityDrifti.md
Model: None

---

## Summary  
The paper introduces **SecDrift**, a benchmark designed to measure sector‑conditioned security drift in AI‑generated code, focusing on how prompts conditioned on industry contexts affect static‑analysis vulnerability rates. By evaluating seven large language models across eight CISA critical‑infrastructure sectors and nine CWE categories, the authors find that most observed differences are artifacts of specific vulnerability types rather than genuine sector effects.

## Key Contributions  
- [Finding 1] Industry prompts appear more secure (14.0 % vs. 11.4 %) but the gap is not statistically significant.  
- [Finding 2] The non‑significant gap disappears when CWE‑502 and CWE‑22 are excluded, indicating a composition artifact that reverses the trend (+0.4 pp).  
- [Finding 3] Mixed‑effects logistic regression confirms sector identity is not a moderator; only those two vulnerability types show detectable condition effects.

## Methodology  
The authors designed SecDrift as a benchmark measuring static‑analysis vulnerability rates under domain‑specific prompts versus neutral baselines. They used seven LLMs (six producing analyzable code) across eight CISA critical infrastructure sectors and nine CWE categories, with five replicates (5,355 evaluations). A 5‑dimension transformation kept the task fixed while substituting only industry terminology; a matched baseline holds the task constant.

## Results  
Out of eight sectors, none show statistically distinguishable drift from baseline (|h| < 0.15). The pooled pattern reflects generic industry‑framing specificity rather than critical‑infrastructure identity. Model selection has a large and consistent effect: vulnerability rates range from 11.6 % to 16.1 %, persisting across conditions.

## Significance  
SecDrift reveals that the observed security differences are largely artifacts of specific CWE categories, not genuine sector‑conditioned drift. It also demonstrates that model choice is a more reliable lever for improving code safety than prompt framing. The framework and data enable reproducibility in assessing AI‑generated code security under domain constraints.

## Related Concepts  
- Static analysis vulnerability rates  
- Sector‑conditioned prompting  
- CISA critical infrastructure sectors  
- CWE (Common Weakness Enumeration) categories  
- Mixed‑effects logistic regression  
- Placebo testing
