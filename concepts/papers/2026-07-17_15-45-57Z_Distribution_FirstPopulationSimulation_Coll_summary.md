# Summary: 2026-07-17_15-45-57Z_Distribution_FirstPopulationSimulation_Collapse_Ca.md
Saved: 2026-07-23 23:57
Source: 2026-07-17_15-45-57Z_Distribution_FirstPopulationSimulation_Collapse_Ca.md
Model: None

---

## Summary  
This paper addresses a critical failure in the current paradigm of using independent large language model (LLM) agents to simulate population responses, demonstrating that such models systematically collapse into a single modal distribution regardless of input structure or seed variation. The authors introduce a "distribution-first" approach—calibrating each agent to match the true underlying response distribution derived from real survey microdata—using Verbalized Sampling (VS), which corrects both under- and over-dispersion without requiring extensive training. This method is evaluated on non-WEIRD data from Turkey, revealing that while the population-level distribution can be preserved, individual agent behavior remains distorted due to recall limitations and structural biases. The study concludes with a budget-aware router that assigns calibrated distributions at O(1) cost, achieving high accuracy without sacrificing realism.

## Key Contributions  
- [Finding 1] N independent LLM agents grounded on real World Values Survey respondents fail to reproduce the population's response distribution, exhibiting an 85% collapse with concentration increasing from 0.36 to 0.69 and entropy dropping from 1.46 to 0.77, with a TVD of 0.44; this collapse is strongly correlated (r=0.55) with single-answer survey structure.  
- [Finding 2] Verbalized Sampling (VS), which fixes the field's chronic under-dispersion by adjusting sampling weights, universally overshoots into over-dispersion (SD-ratio increasing from 0.4–0.56 to 1.26–1.37), indicating a structural flaw in how VS handles variance across model families like Qwen, where p=0.002 and d=6.2 confirms significance.  
- [Finding 3] Survey fidelity transfers weakly to agentic behavior: in a booking task, the cheapest-default persona dominates (80% of responses) regardless of income, with comfort choice only rising from 0% to 7% to 32%, showing that agents prioritize cost over preference.

## Methodology  
The authors used real microdata from 2,414 World Values Survey respondents across four scenarios and five seeds per scenario. They generated N independent LLM agents using a distribution-first approach: first calibrating the true response distribution via Verbalized Sampling (VS), then assigning this calibrated distribution to each agent at O(1) cost through a budget-aware router. The verifier used was deterministic and construct-validated, ensuring that only outputs matching the target distribution were accepted. To test robustness, they conducted placebo memorization attacks and an election backtest to measure recall contamination.

## Results  
The collapse (85%) is reproducible across seeds and models, with high correlation to single-answer structure. VS corrects under-dispersion but introduces over-dispersion, increasing SD-ratio from 0.4–0.56 to 1.26–1.37. In the booking task, the cheapest-default persona dominates (80%), with comfort choice only reaching 32% at highest income. The router’s honest AUC is 0.805, significantly lower than the ideal 1.0 of a code-derived oracle. Placebo attacks and election backtests show that while aggregate strength is preserved, subgroup and individual claims are contaminated by recall errors and underdetermination.

## Significance  
This research reveals a fundamental flaw in treating each LLM agent as an independent population simulator, exposing how model outputs can systematically misrepresent real-world distributions. The distribution-first approach offers a more honest calibration that respects both statistical fidelity and computational efficiency, paving the way for responsible synthetic-population modeling without false realism claims.

## Related Concepts  
- Distribution-First Calibration: Assigning true response distributions to agents at low cost.  
- Verbalized Sampling (VS): A method to correct sampling weights in survey data.  
- Collapse and Entropy: Statistical measures of distribution concentration.  
- TVD (Total Variation Distance): Quantifies divergence between two probability distributions.  
- Recall Contamination: Error introduced when agents recall incorrect or incomplete population behavior.
