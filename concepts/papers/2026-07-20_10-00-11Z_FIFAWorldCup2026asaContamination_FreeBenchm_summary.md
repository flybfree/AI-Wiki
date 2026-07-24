# Summary: 2026-07-20_10-00-11Z_FIFAWorldCup2026asaContamination_FreeBenchmarkforL.md
Saved: 2026-07-24 00:18
Source: 2026-07-20_10-00-11Z_FIFAWorldCup2026asaContamination_FreeBenchmarkforL.md
Model: None

---

## Summary  
The paper introduces **WC2026‑Agents**, a contamination‑free benchmark that evaluates large language models (LLMs) as autonomous forecasting agents on the 104 matches of the upcoming FIFA World Cup 2026. By pairing four frontier LLMs with the pre‑match betting market, the study measures not only prediction accuracy but also how agents allocate virtual bets and reflect on their reasoning after each match is played. The benchmark reveals that despite identical top picks in most games, raw accuracy masks deeper differences in decision quality, calibration, and self‑knowledge among the models.

## Key Contributions  
- **Finding 1:** Four frontier LLMs (Claude Opus 4.8, ChatGPT GPT‑5.5, Gemini 3.1 Pro, Grok Expert Mode) issue an identical top pick in 92 % of matches and none improves the market’s Brier score; a naïve flat stake on the market favorite consistently outperforms all agents.  
- **Finding 2:** Agents’ betting return‑on‑investment (ROI) ranges from –18 % to +10 %; they are unprofitable when they “fade” the market, and the proportion of forecasts that cite the market odds varies widely (12 %–100 %). Self‑reported error rates on wrong picks span 36 % to 86 %.  
- **Finding 3:** The benchmark quantifies three axes—calibration, decision quality, and self‑knowledge—that frontier models differ along even when their predictions are the same.

## Methodology  
The authors constructed a search‑act‑reflect loop for each match: an LLM gathers evidence via a web tool, commits to a 1X2 (team A win / draw / team B win) distribution and places a virtual $100 bet, then reflects only after the final score is known. Because all matches occur after the models’ training cutoffs, the dataset is contamination‑free by construction. The benchmark includes four LLM agents plus the pre‑match betting market as a fifth competitor; odds are collected per match to serve as an economically grounded baseline.

## Results  
The release contains 416 forecasts and 414 reflections with verbatim reasoning, ground‑truth scores (including penalty shootouts), odds, and a reproducible evaluation suite. Raw accuracy hides: the four agents agree on the top pick in 92 % of matches, none beats the market’s Brier score, and a flat stake on the market favorite yields higher returns than any agent. Decision‑making metrics show ROI between –18 % and +10 %, all agents lose when they ignore the market, and self‑reported error rates vary from 36 % to 86 %.

## Significance  
WC2026‑Agents demonstrates that frontier LLMs can be evaluated on a contamination‑free real‑world forecasting task, exposing hidden deficiencies in calibration, decision quality, and self‑awareness. The benchmark shows that models may produce identical predictions yet differ dramatically in how they act with money and report errors, offering a rigorous yardstick for autonomous forecasting agents.

## Related Concepts  
contamination‑free benchmark, autonomous forecasting agents, Brier score, betting markets, ROI (return on investment), calibration, decision quality, self‑knowledge, self‑assessment.
