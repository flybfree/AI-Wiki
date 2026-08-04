# Summary: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Saved: 2026-08-04 00:05
Source: 2026-08-03_15-52-51Z_WhyLargeLanguageModelsFailatTabularPrediction.md
Model: None

---

## Summary  
The paper investigates why generic large language models (LLMs) perform poorly on tabular prediction tasks despite excelling at many other NLP challenges. By treating the LLM as a single‑pass inference engine that receives the entire training and test data in CSV form, the authors systematically test five plausible failure hypotheses. Their controlled experiments falsify most of these ideas except one: the impact of input dimensionality. The study shows that LLMs maintain high accuracy only when tabular inputs have few dimensions, while classical baselines remain stable or improve as dimension grows. This work bridges a long‑standing gap between foundation models and tabular analytics.

## Key Contributions  
- [Finding 1] Experiments rule out noisy/non‑linearly separable data and the linearised CSV format as primary obstacles to LLM performance on tables.  
- [Finding 2] The LLM’s accuracy deteriorates sharply with increasing dimensionality, a behavior that classical models do not replicate even when augmented with dimension‑dependent noise.  
- [Finding 3] In low dimensions (two) the LLM mimics local distance methods up to ~91.6 % grid agreement, but in higher dimensions no classical model—no matter how tuned—can reproduce its predictions.

## Methodology  
The authors adopt a “pure inference” regime: feed the full dataset into an LLM via a single prompt and collect predictions without fine‑tuning or external tools. To test hypotheses they (i) sweep random linear projections of thirty‑one benchmark tabular datasets, (ii) compare the LLM’s output to 252 configured classical models, and (iii) evaluate grid agreement in two dimensions versus higher‑dimensional spaces. All tests are conducted under identical hardware and preprocessing conditions.

## Results  
Across the thirty‑one datasets, the LLM’s accuracy declines as dimensionality rises, while every classical baseline stays flat or improves. In two‑dimensional cases the LLM matches a local distance method with 91.6 % grid agreement; however, for three dimensions and beyond no classical model—even when equipped with tuned noise—can reproduce the LLM’s predictions, indicating that the LLM’s decision surface is fundamentally different.

## Significance  
These findings explain why LLMs, despite their general intelligence, consistently lag behind fifty‑year‑old baselines on tabular prediction tasks. The degradation is tied to dimensionality rather than data quality or tokenisation quirks, highlighting a critical limitation of generic foundation models in a domain where classical algorithms have long been reliable.

## Related Concepts  
- Large language models (LLMs)  
- Tabular data and predictive analytics  
- Dimensionality reduction / linear projections  
- Tokenisation of numeric values  
- Grid agreement as a metric for local distance methods  
- Foundation models vs. classical baselines
