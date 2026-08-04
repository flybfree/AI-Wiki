# Summary: 2026-08-02_15-42-14Z_CanLanguageModelsIdentifyShadowTradingTargets_AnNL.md
Saved: 2026-08-04 00:12
Source: 2026-08-02_15-42-14Z_CanLanguageModelsIdentifyShadowTradingTargets_AnNL.md
Model: None

---

## Summary  
This paper investigates whether natural‑language processing (NLP) can replicate the ex ante identification of “economically linked” firms that the U.S. Securities and Exchange Commission (SEC) presumes insiders already know when evaluating shadow‑trading liability. By applying a two‑stage LLM pipeline to Item 7 of SEC 10‑K filings, the authors score semantic similarity across thirty mergers‑and‑acquisitions events spanning five industries and test whether those scores predict abnormal stock returns on announcement days. The results show that while the model can surface Incyte as a plausible peer in the single case with a known outcome, it fails to detect any systematic relationship between similarity and market impact across the full sample. This work therefore challenges the empirical premise of shadow‑trading enforcement and raises constitutional questions about the SEC’s surveillance infrastructure.

## Key Contributions  
- [Finding 1] The NLP pipeline successfully identifies Incyte among the closest peers for the Panuwat fact pattern, providing a sanity check on the known case.  
- [Finding 2] Across thirty M&A events, the similarity scores show no statistically significant association with abnormal returns (within‑event rank correlation = +0.07; mean per‑event Spearman = +0.05, CI [-0.08, +0.18]; p = 0.37).  
- [Finding 3] A case‑level reading yields a mixed picture: 14 events support the shadow‑trading hypothesis, 12 contradict it, and 4 are ambiguous.

## Methodology  
The authors constructed a two‑stage LLM pipeline that first extracts Item 7 (Management’s Discussion and Analysis) from SEC 10‑K filings, then computes semantic similarity between each filing and the counterpart of its paired M&A event. This similarity score is later correlated with abnormal stock returns observed on the announcement day across thirty events covering five industries.

## Results  
The within‑event rank correlation between similarity scores and abnormal returns is +0.07 (permutation p = 0.37), indicating a non‑significant trend. The mean per‑event Spearman correlation is +0.05 with a 95% confidence interval of [-0.08, +0.18], which excludes any moderate relationship. Case‑level analysis shows 14 events support the hypothesis, 12 contradict it, and 4 are ambiguous; Incyte also falls outside the SEC’s typical $2B–$10B mid‑cap band on the day before its announcement.

## Significance  
These findings undermine the empirical basis of shadow‑trading enforcement theory, suggesting that NLP cannot reliably identify economically linked firms ex ante. Consequently, the paper raises concerns about the constitutional legitimacy of the SEC’s financial surveillance infrastructure and its reliance on post‑hoc market surveillance rather than pre‑emptive identification.

## Related Concepts  
shadow trading, material nonpublic information (MNPI), insider trading liability, NLP, semantic similarity, M&A events, abnormal returns, SEC 10‑K Item 7, mid‑cap oncology category, constitutional questions.
