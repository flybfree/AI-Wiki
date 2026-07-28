# Summary: 2026-07-26_07-29-47Z_NovelClaimorDéjàVu_Rethinking_Contamination_Free__.md
Saved: 2026-07-27 20:18
Source: 2026-07-26_07-29-47Z_NovelClaimorDéjàVu_Rethinking_Contamination_Free__.md
Model: None

---

## Summary  
This paper investigates the hidden problem of “contamination” in multimodal automated fact‑checking (MAFC) benchmarks that rely on static, outdated data. By constructing a dynamic benchmark called ClaimReview2025Q4 that contains claims published after large language models’ knowledge cut‑off dates, the authors show that many such claims are still vulnerable to contamination and can inflate evaluation scores. The study demonstrates that while dynamic evaluation reduces contamination risk, it does not eliminate it entirely.

## Key Contributions  
- Finding 1: Dynamic evaluation reduces but does not eliminate contamination risks, as 17.09 %–29.30 % of post‑cut‑off claims remain potentially contaminated.  
- Finding 2: Many newly published claims can be verified either directly or by synthesizing multiple pieces of public knowledge available before the cut‑off.  
- Finding 3: Contamination can induce statistically significant inflation in MAFC performance, increasing Macro‑F1 by up to 11.34 points and distorting system rankings.

## Methodology  
The authors compare contamination risks between two benchmark sets: the static AVeriTeC benchmark (which depends on LLM internal knowledge) and their newly constructed dynamic ClaimReview2025Q4 benchmark, which includes claims published after LLMs’ knowledge cut‑off. They systematically sample post‑cut‑off claims to assess whether they can be answered using only pre‑cut‑off public data, identify cases where contamination occurs, and measure the impact on MAFC metrics.

## Results  
Experiments reveal 16 distinct findings; three are highlighted above. Overall, dynamic evaluation cuts contamination by roughly half compared with static benchmarks, yet residual contamination persists. Macro‑F1 scores improve by up to 11.34 points when contamination is ignored, indicating that SOTA models appear stronger under contaminated conditions.

## Significance  
Understanding and controlling contamination is crucial for trustworthy automated fact‑checking because inflated metrics mislead stakeholders about real performance. By exposing the limits of “contamination‑free” assumptions, this work guides researchers to design more realistic evaluation protocols and promotes fairness in model ranking.

## Related Concepts  
- Multimodal Automated Fact-Checking (MAFC)  
- Contamination in benchmark data  
- Knowledge cut‑off dates for LLMs  
- Dynamic vs. static benchmarks  
- Macro‑F1 metric
