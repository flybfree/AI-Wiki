# Summary: 2026-07-27_07-05-11Z_TheCostofKnowing_AResource_AwareProtocolforBenchma.md
Saved: 2026-07-27 22:54
Source: 2026-07-27_07-05-11Z_TheCostofKnowing_AResource_AwareProtocolforBenchma.md
Model: None

---

## Summary  
Static factuality leaderboards ignore the computational cost of generating answers, which can mislead practitioners into selecting a model that is both highly accurate and prohibitively expensive. The paper introduces MAS‑HQ (Multi‑Agent System Hallucination Quest), a resource‑aware protocol that normalizes factuality scores by the amount of compute required, thereby making trade‑offs visible. By comparing models against each other rather than scoring them in isolation, MAS‑HQ reveals when a higher raw score is outweighed by excessive token usage or latency. The study shows that competition elicits modest but consistent improvements in resource efficiency across summarization and open‑domain QA tasks.

## Key Contributions  
- [Finding 1] Static leaderboards cannot differentiate between high‑factuality models that are also very costly, leading to ranking reversals when cost is accounted for.  
- [Finding 2] MAS‑HQ introduces a normalized factuality metric (the Q‑Score) that subtracts the cost of generating answers under competitive matching, providing a fair comparison.  
- [Finding 3] Empirical experiments demonstrate that single‑agent baselines over‑optimize for raw scores while competition encourages more resource‑efficient policies, with gains stable across 100 trials.

## Methodology  
The authors wrap any existing factuality detector and compute the cost (tokens and latency) of each answer. They then normalize the factuality score by this cost to obtain a Q‑Score that reflects both accuracy and efficiency. MAS‑HQ pits two systems against each other, sweeping the sensitivity of the cost weight to explore trade‑offs. The protocol is applied to summarization and open‑domain QA benchmarks, with 100 independent trials to assess stability.

## Results  
The main experimental results show that when models compete, average token usage drops by roughly 25 % while maintaining comparable factuality scores. Single‑agent baselines exhibit a 30 % increase in tokens per query compared to competition. The Q‑Score remains discriminative for frontier systems such as Gemini‑2.5‑Pro and simulated GPT‑5, indicating that the metric captures genuine efficiency gains rather than noise.

## Significance  
This work matters because real‑world deployment budgets limit how much compute can be spent on model inference; a model that scores slightly higher but is four times more expensive may be impractical. MAS‑HQ provides a reproducible way to measure the “cost of knowing,” guiding practitioners toward balanced choices between accuracy and resource consumption.

## Related Concepts  
factuality, hallucination, static leaderboards, resource‑aware evaluation, Q‑Score, normalization, competitive learning, token cost, latency, Gemini‑2.5‑Pro, GPT‑5 preview.
