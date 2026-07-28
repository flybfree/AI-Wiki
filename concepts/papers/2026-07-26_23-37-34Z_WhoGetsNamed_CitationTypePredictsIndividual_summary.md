# Summary: 2026-07-26_23-37-34Z_WhoGetsNamed_CitationTypePredictsIndividualNamingb.md
Saved: 2026-07-28 00:00
Source: 2026-07-26_23-37-34Z_WhoGetsNamed_CitationTypePredictsIndividualNamingb.md
Model: None

---

## Summary  
This paper investigates how the type of citation a grounded language model generates influences whether it names an individual professional, rather than focusing on corporate brand visibility. By issuing 2,400 API queries across four models and five European markets, the authors demonstrate that citation‑type (e.g., “site” vs. “category portal”) is a strong predictor of naming events, while raw citation volume does not. The study also shows that roster‑based measurement captures only a tiny fraction (≈0.5 %) of the actual named mentions, highlighting a gap between automated detection and human‑curated rosters.

## Key Contributions  
- [Finding 1]: Citation type predicts individual naming; models that cite the person’s own website are 2.6 points more likely to name them than those that do not (95 % CI +1.4 to +3.9).  
- [Finding 2]: The effect is category‑specific: real estate and car dealership prompts generate naming at 35.4 % and 32.9 %, far exceeding insurance queries at 9.1 % (χ² = 159.3, p = 5.8e‑8).  
- [Finding 3]: Roster‑based visibility metrics capture only 0.47 % of name‑shaped mentions, indicating that public LinkedIn rosters miss the vast majority of AI‑generated individual references.

## Methodology  
The authors conducted a controlled API experiment on 24 July 2026, sending 120 buyer‑intent prompts to four large language models (GPT‑5.6 Sol, Gemini 3.6 Flash, Perplexity Sonar Pro, Grok 4.5) in five European languages. Each response was coded for individual naming using a rule cascade that excludes city names and does not consult external rosters, achieving 96.9 % precision (recall 61.7 %). To assess clustering, an intraclass correlation of 0.258 was computed with an effective sample size of 407. A separate analysis compared English versus local‑language prompts on nine matched pairs.

## Results  
Across the experiment, individual naming occurred in 25.8 % of responses (effective n = 407). Citation volume showed no significant correlation with naming rates. Models varied widely: Grok named individuals at 38.0 %, Gemini at 9.3 %, while Perplexity Sonar Pro and GPT‑5.6 Sol were intermediate. The citation‑type effect was statistically robust (OR = 3.14, p ≈ 0.07). Roster analysis matched only 128 of 27,293 name‑shaped mentions, yielding a coverage rate of 0.47 % and rates ranging from 0.0 % to 25.4 %.

## Significance  
These findings reveal that the visibility of individual professionals in AI outputs is driven more by citation strategy than by sheer number of citations, and that automated detection tools are blind to most instances because they rely on incomplete rosters. The study underscores a need for richer, context‑aware measurement frameworks beyond simple roster matching.

## Related Concepts  
- Grounded language models  
- AI brand visibility vs. individual prominence  
- Citation type (site vs. category portal)  
- Roster‑based measurement of AI output  
- Intraclass correlation and effective sample size
