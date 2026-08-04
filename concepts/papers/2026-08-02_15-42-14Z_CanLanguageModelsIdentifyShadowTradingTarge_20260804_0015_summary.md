# Summary: 2026-08-02_15-42-14Z_CanLanguageModelsIdentifyShadowTradingTargets_AnNL.md
Saved: 2026-08-04 00:15
Source: 2026-08-02_15-42-14Z_CanLanguageModelsIdentifyShadowTradingTargets_AnNL.md
Model: None

---

## Summary  
The paper investigates whether natural‑language processing can replicate the SEC’s ex ante identification of “economically linked” firms that are alleged to be shadow‑trading targets, thereby testing a theory of insider‑trading liability. It builds a two‑stage LLM pipeline that scores semantic similarity between Item 7 disclosures and M&A events across five industries, then measures how those scores relate to abnormal stock returns on announcement days. The empirical test shows no statistically significant link between disclosed similarity and market impact, casting doubt on the SEC’s enforcement premise. Moreover, a case‑level analysis reveals mixed support for shadow trading in only 14 of 30 events, with Incyte highlighted as an outlier due to its size classification.  

## Key Contributions  
- [Finding 1] The LLM pipeline can automatically compute semantic similarity scores between Item 7 sections and M&A events across a diverse set of filings.  
- [Finding 2] No robust statistical association is found between those similarity scores and abnormal returns on announcement days (within‑event rank correlation +0.07, p = 0.37; mean per‑event Spearman +0.05, CI [-0.08, +0.18]).  
- [Finding 3] Case‑level examination shows that only 14 of the 30 events support shadow trading, 12 contradict it, and 4 are ambiguous, with Incyte falling outside the SEC’s mid‑cap band complicating categorisation.  

## Methodology  
The authors constructed a two‑stage language model pipeline: first, they extracted Item 7 (Management’s Discussion and Analysis) text from 30 recent M&A events spanning five industries; second, they fed these texts into an LLM to generate similarity scores that capture semantic overlap with the counterpart filing. The scores were then correlated with abnormal returns measured on the announcement day using a standard statistical framework.  

## Results  
Across the full dataset, the within‑event rank correlation between similarity and abnormal return is +0.07 (permutation p = 0.37), indicating no meaningful link; the mean per‑event Spearman correlation is +0.05 with a 95 % confidence interval of [-0.08, +0.18]. At the case level, 14 events support shadow trading, 12 contradict it, and 4 are ambiguous. Notably, Incyte was excluded from the “mid‑cap oncology” category because its pre‑announcement price fell outside the $2 B–$10 B range, challenging the SEC’s typology.  

## Significance  
These findings undermine the empirical premise that insiders can reliably identify shadow‑trading targets ex ante using public disclosures, suggesting that the SEC’s reliance on mass market surveillance may be more reactive than predictive. The results also raise constitutional questions about the scope of financial surveillance authority when algorithmic tools are employed to enforce securities law.  

## Related Concepts  
- Shadow Trading  
- Material Nonpublic Information (MNPI)  
- Economic Linkage  
- NLP and LLM pipelines  
- Semantic Similarity Scoring  
- SEC Enforcement Theory  
- Abnormal Returns  
- M&A Event Analysis  
- Mid‑cap Stock Band  
- Constitutional Authority of Financial Surveillance
