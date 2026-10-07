---
title: HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior
url: http://arxiv.org/abs/2610.07563v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_00-50-28Z_HouseholdBench_EvaluatingLargeLanguageModelsasPred.md
generated_at: 2026-10-06 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HouseholdBench introduces a broad evaluation framework for testing whether large language models can predict household economic behavior using six U.S. household surveys and 32 prediction tasks across consumption, income, labor, expectations, and housing. The study finds that most LLMs beat a no-change baseline, especially on policy-response tasks, but gradient-boosted trees generally remain stronger, while fine-tuning and prediction aggregation can help a small open-weight model approach proprietary performance.

## Key Takeaways
- HouseholdBench expands evaluation beyond narrow survey settings by combining 6 U.S. household surveys and 32 prediction tasks with numeric, categorical, and probabilistic outcomes, allowing researchers to assess LLMs on realistic household decisions rather than isolated economic questions.
- The benchmark evaluates whether models can use past behavior, demographics, and macroeconomic conditions to predict household responses to changing policies, and it finds that most LLMs outperform a no-change baseline, with the best model reducing numeric prediction error by 12.2 percent.
- Gradient-boosted tree models rank first across most tasks, while leading proprietary LLMs approach their performance and open-weight models lag; however, fine-tuning and aggregating 16 predictions per observation enable a 4 billion parameter open-weight model to match proprietary models, including on policy-response tasks excluded from fine-tuning.

## Context
This work matters because economics seeks quantitative models of household decision making, and LLMs may offer flexible predictors that incorporate heterogeneous household histories, demographic details, and macroeconomic context. At the same time, existing evaluations have been limited in survey coverage, outcome diversity, and policy-response testing, so HouseholdBench provides a more systematic benchmark for comparing machine learning and language-model approaches.

## Implications
For researchers, the results suggest that LLMs are promising but not automatically superior to conventional tabular models for household prediction, and that model choice should depend on task structure, data access, and deployment constraints. For practitioners, the findings highlight practical methods such as fine-tuning and prediction aggregation that can improve smaller open-weight models, potentially making LLM-based economic forecasting more accessible while still requiring careful calibration against systematic overprediction and underprediction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07563v1)
