# Summary: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Saved: 2026-08-04 00:44
Source: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Model: None

---

## Summary  
The paper investigates why generic large language models (LLMs) fail to perform predictive analytics on tabular data when used in a single‑pass inference setting that supplies the full training and test sets as a prompt. It systematically tests five plausible hypotheses—noise, CSV formatting, numeric tokenisation, limited query points, and input dimensionality—and finds that most are falsified. The decisive factor is dimensionality: as the number of features grows, LLM accuracy deteriorates while classical baselines remain flat or improve.

## Key Contributions  
- Dimensionality is the primary factor limiting LLM performance; accuracy systematically decreases with increasing input dimension.  
- In low‑dimensional regimes (two dimensions) the LLM’s predictions resemble a local distance‑based method, achieving up to 91.6 % grid agreement, but beyond that it diverges sharply from any classical model, even when those models are augmented with noise.  
- The failure mode is not due to data corruption or tokenisation quirks; instead, the LLM’s capability dissolves in a dimension‑dependent way that no noisy classical learner can mimic.

## Methodology  
The authors evaluate five hypotheses (noise, CSV format, numeric tokenisation, number of test points per query, dimensionality) by running controlled experiments with a frontier LLM in its purest inference regime—no tools, no fine‑tuning, just a single generation pass over the full data. They compare this approach against 252 configured classical models and sweep random linear projections across thirty‑one benchmark datasets to quantify how accuracy changes with dimensionality.

## Results  
Across the dimension sweep, the LLM’s accuracy declines as dimensionality grows, whereas all nine classical baselines stay flat or improve. In two dimensions the LLM matches a local distance method up to 91.6 % grid agreement; for higher dimensions no classical model—even with tuned, dimension‑dependent noise—reproduces its predictions.

## Significance  
These findings reveal a fundamental limitation of LLMs on tabular prediction: their performance collapses as the feature space expands, a problem that older baselines handle gracefully. The work underscores the need for specialized foundation models tailored to tables and highlights why generic language‑model tools remain ineffective in this common workload.

## Related Concepts  
Large language models, tabular prediction, dimensionality, local distance methods (e.g., k‑NN), classical machine‑learning baselines, tokenisation of numbers, CSV format, noise‑corrupted learners.
