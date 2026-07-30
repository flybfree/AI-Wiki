# Summary: 2026-07-29_16-07-37Z_ScoresAreNotDecisions_Cost_AwareStoppingforToolAcq.md
Saved: 2026-07-29 20:43
Source: 2026-07-29_16-07-37Z_ScoresAreNotDecisions_Cost_AwareStoppingforToolAcq.md
Model: None

---

## Summary  
The paper tackles the problem of how LLM agents should decide how many external tools to acquire when each tool has a different acquisition cost, showing that merely using relevance scores is insufficient. It introduces a cost‑aware marginal decision‑focused stopping (CAM‑DF) framework and its lightweight variant CAM‑DF‑lite, which directly optimizes the gap between stopping now and the best possible continuation. The objective is proved Bayes‑aligned with the true stopping target and demonstrates that score‑only rules are suboptimal under heterogeneous costs. Experiments show superior payoff on τ‑bench Retail while reducing tool exposure by 37 % without sacrificing task success.

## Key Contributions  
- **Finding 1:** Formulating tool acquisition as a cost‑aware marginal decision‑focused stopping problem over ranked tool prefixes, introducing CAM‑DF and its compact variant.  
- **Finding 2:** Proving that the objective is Bayes‑aligned with the true stopping target and that score‑only rules are suboptimal when costs differ across tools.  
- **Finding 3:** Empirically achieving state‑of‑the‑art payoff on τ‑bench Retail, reducing tool usage by 37 % while maintaining comparable task success.

## Methodology  
The authors treat each candidate prefix of a ranked tool list as an action whose cost is the acquisition price and whose payoff depends on whether stopping now yields the best continuation. They optimize a decision rule that minimizes expected regret: the sign of the gap between “stop now” and “continue” labels the optimal choice, while the magnitude weights errors by the payoff at stake. CAM‑DF‑lite computes a simple threshold on marginal value to select prefixes without fine‑tuning the underlying LLM.

## Results  
Evaluated across 1,343 tasks in five tool‑use domains, CAM‑DF outperforms predict‑then‑threshold baselines across all ranking sources and cost regimes, delivering higher payoff. In live execution it accesses 37 % fewer tools than full access while task success remains comparable.

## Significance  
This work shows that optimal tool selection must consider heterogeneous acquisition costs, offering a lightweight, interpretable plugin that improves LLM agent efficiency without altering the model; it bridges offline gap learning with real‑world deployment constraints.

## Related Concepts  
- Cost‑aware stopping  
- Marginal decision‑focused stopping (CAM‑DF)  
- Bayes‑optimal stopping  
- Heterogeneous costs  
- Tool ranking  
- Payoff‑weighted error magnitude  
- τ‑bench Retail benchmark
