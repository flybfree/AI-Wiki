# Summary: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Saved: 2026-08-04 01:05
Source: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Model: None

---

## Summary  
The paper investigates why large language models (LLMs) perform poorly on tabular prediction tasks despite excelling elsewhere. It systematically tests five hypotheses and finds that the model’s failure is fundamentally tied to input dimensionality rather than data noise or format issues. By comparing LLMs with classical baselines across 31 benchmark datasets, it shows that LLM accuracy degrades as dimensions increase while classics remain stable.

## Key Contributions  
- Finding 1: Experiments falsify hypotheses (a)-(d) regarding noisy data, CSV format, tokenisation of numbers, and test point count.  
- Finding 2: Dimensionality is the decisive factor; LLM performance drops sharply with increasing dimensionality, unlike classical methods.  
- Finding 3: In two dimensions, LLM predictions align closely with distance‑based local models (up to 91.6% grid agreement), but this alignment fails in higher dimensions where no classical model can mimic its behavior.

## Methodology  
The authors conduct controlled inference experiments using a single generation pass over prompts that contain the full training and test data, without fine‑tuning or external tools. They evaluate five failure hypotheses through systematic ablation studies on 31 benchmark tabular datasets, measuring prediction accuracy under varying dimensionalities. Additionally, they configure 252 classical models with dimension‑dependent noise to create a benchmark for reproducing LLM behavior.

## Results  
Across the 31 datasets, the LLM’s accuracy decreases monotonically as the number of columns grows, while all nine classical baselines either stay flat or improve. In two‑dimensional cases, the LLM matches local distance methods up to 91.6% grid agreement; however, in three dimensions and beyond, no classical model—even with tuned noise—reproduces its predictions. The only consistent pattern is that higher dimensionality correlates with LLM degradation.

## Significance  
This work clarifies a longstanding mystery: LLMs are not universally weak on tabular data but fail specifically when the input space becomes high‑dimensional, a behavior no noisy classical learner exhibits. It highlights a gap between generative AI capabilities and traditional predictive analytics, suggesting that future research may need to redesign architectures for structured data.

## Related Concepts  
- Large language models (LLMs)  
- Tabular prediction  
- Dimensionality reduction / projection  
- Classical baseline methods (e.g., linear regression, k‑NN)  
- Grid agreement  
- Noisy classification
