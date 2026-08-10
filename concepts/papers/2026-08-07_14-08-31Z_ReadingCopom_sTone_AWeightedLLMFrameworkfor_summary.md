# Summary: 2026-08-07_14-08-31Z_ReadingCopom_sTone_AWeightedLLMFrameworkforHawkish.md
Saved: 2026-08-09 23:01
Source: 2026-08-07_14-08-31Z_ReadingCopom_sTone_AWeightedLLMFrameworkforHawkish.md
Model: None

---

## Summary  
The paper introduces a weighted LLM framework for measuring the tone of Copom statements, extending iSent by assigning intensity weights to hawkish and dovish expressions and producing a bounded document‑level score between –1 and 1. It also adds a full‑document layer that evaluates forward‑guidance direction, explicitness, uncertainty level, and its temporal change. The system outputs both tone scores (e.g., +0.232 for the latest statement) and guidance‑direction scores with a strong correlation of 0.719. This work is methodological rather than predictive, focusing on transparent analysis.

## Key Contributions  
- Finding 1: A weighted LLM framework that assigns intensity weights (0‑1) to hawkish/dovish sentences, enabling a bounded document tone score between –1 and 1.  
- Finding 2: A full‑document layer that quantifies forward guidance direction, explicitness, uncertainty level, and its change across meetings.  
- Finding 3: Empirical results showing 33.3 % hawkish, 18 % dovish, 42.1 % neutral sentences; average document score +0.107 with peak +0.570 in August 2021 and latest +0.232; correlation 0.719.

## Methodology  
The authors built an LLM‑based classifier that first scans each sentence for hawkish or dovish lexical cues, assigning a continuous intensity weight; then aggregates sentence counts with average intensity to produce the document score; finally, they apply separate heuristics and statistical measures on full statements to derive guidance direction (hawkish/dovish/neutral), explicitness rating, uncertainty classification (low/central/high) and its temporal change.

## Results  
Across 80 Copom statements from August 31 2016 to August 5 2026 (1,498 sentences), the sentiment distribution is 33.3 % hawkish, 18 % dovish, 42.1 % neutral, 6.5 % out‑of‑context. The average document tone score is +0.107; the highest reading (+0.570) occurs in August 2021. The most recent statement (Aug 5 2026) scores +0.232, composed of eight hawkish, two dovish and nine neutral sentences. The guidance‑direction score correlates with tone at r = 0.719.

## Significance  
This work provides a transparent, incremental, auditable system that separates rhetorical tone from policy guidance and uncertainty, offering an open framework for future sentiment analysis without claiming predictive power over Selic decisions or DI returns.

## Related Concepts  
- Hawkish vs dovish monetary stance  
- Forward guidance (explicitness)  
- Uncertainty quantification in central‑bank communications  
- iSent sentiment classifier  
- LLM‑based text classification and weighting
