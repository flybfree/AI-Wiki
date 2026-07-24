# Summary: 2026-07-20_10-00-11Z_FIFAWorldCup2026asaContamination_FreeBenchmarkforL.md
Saved: 2026-07-24 00:21
Source: 2026-07-20_10-00-11Z_FIFAWorldCup2026asaContamination_FreeBenchmarkforL.md
Model: None

---

## Summary  
The paper introduces WC2026‑Agents, a contamination‑free benchmark for evaluating large language models as autonomous forecasting agents using real future FIFA World Cup matches where the models perform identical search‑act‑reflect loops and place virtual $100 bets. It pairs four frontier LLMs with the pre‑match betting market to measure not only prediction accuracy but also decision quality and self‑knowledge. The study reveals that despite producing the same top pick in 92 % of matches, none of the agents achieve a Brier score better than the market, and all exhibit negative return‑on‑investment when betting. This work provides a reproducible dataset and evaluation suite for benchmarking autonomous forecasting systems.

## Key Contributions  
- Finding 1: Four frontier LLMs produce identical top predictions (win/draw/loss) in 92 % of matches, yet none achieve a Brier score better than the market.  
- Finding 2: All agents exhibit negative return‑on‑investment when betting, with returns ranging from –18 % to +10 %, indicating that following the market is more profitable.  
- Finding 3: The proportion of forecasts that cite the market odds varies widely (12 %–100 %), and self‑reported error rates on wrong picks range from 36 % to 86 %.

## Methodology  
The authors constructed a benchmark by simulating each of the 104 World Cup matches with four state‑of‑the‑art LLMs—Claude Opus 4.8, ChatGPT (GPT‑5.5), Gemini 3.1 Pro, and Grok Expert Mode—running an identical search‑act‑reflect loop: they query a web tool for evidence, commit to a 1X2 outcome distribution and a virtual $100 bet, then reflect after the match using only the final score. The betting market provides per‑match 1X2 odds as a fifth competitor, forming an economically grounded baseline. Forecasts and reflections are recorded verbatim; ground truth includes scores, penalties, and odds.

## Results  
The evaluation shows that all four models issue the same top pick in 92 % of games, but their Brier scores never exceed those of the market. Return‑on‑investment is negative for every agent except one modest positive case (+10 %). The share of forecasts referencing market odds spans a large range (12–100 %), and self‑reported error rates on incorrect picks are high (36–86 %). A naive flat stake on the market favorite outperforms all agents.

## Significance  
This benchmark demonstrates that raw prediction accuracy is misleading; autonomous forecasting agents can be systematically misaligned with economic incentives. By measuring calibration, decision quality, and self‑knowledge, it offers a more holistic view of LLM performance in real‑world forecasting tasks.

## Related Concepts  
- Contamination‑free benchmark  
- Search‑act‑reflect loop  
- Brier score  
- Return‑on‑investment (ROI)  
- Market odds as baseline competitor  
- Calibration and error rate  
- Autonomous forecasting agents
