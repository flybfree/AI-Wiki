# Summary: 2026-07-20_15-33-24Z_Pancasila_Dilemmas_EvaluatingLargeLanguageModelson.md
Saved: 2026-07-24 00:21
Source: 2026-07-20_15-33-24Z_Pancasila_Dilemmas_EvaluatingLargeLanguageModelson.md
Model: None

---

## Summary  
This paper introduces Pancasila‑Dilemmas, a dataset of 1,834 Indonesian news‑based dilemmas classified by the five values of Pancasila (Religion, Humanity, Unity, Democracy, Social Justice) to evaluate how large language models (LLMs) align with local value systems. By measuring model responses on these culturally specific scenarios, the authors demonstrate that current LLMs perform poorly in capturing Indonesian ethical reasoning, highlighting a gap between universal‑oriented benchmarks and regionally grounded assessments.

## Key Contributions  
- [Finding 1] All evaluated LLMs achieve a Probability Match Score (PMS) below 0.5 and a Max‑Vote Agreement Score (MVAS) of 0.72, indicating systematic misalignment with the intended values.  
- [Finding 2] The models consistently underperform on dilemmas involving Religion and Unity, revealing particular weaknesses in handling culturally sensitive value conflicts.  
- [Finding 3] The Pancasila‑Dilemmas dataset is publicly released (GitHub link) as a reusable benchmark for measuring LLM value alignment against Indonesian societal norms.

## Methodology  
The authors constructed the dataset by extracting dilemmas from recent Indonesian news articles, assigning each to one of the five Pancasila values. Scenarios were selected for their inherent ethical tension and then proofread by native speakers. Five diverse Indonesian citizens answered each dilemma, providing ground‑truth responses that serve as the reference for evaluation. The 50 LLMs (both closed‑source and open‑source) were prompted to generate answers, whose probability distributions were scored using PMS and MVAS metrics.

## Results  
Across all values, every model’s PMS is under 0.5 and its MVAS is below 0.72, confirming a clear misalignment. The poorest performance occurs in Religion (PMS ≈ 0.38) and Unity (MVAS ≈ 0.61), where models often ignore or invert the prescribed values. These scores are significantly lower than typical universal‑value benchmarks, underscoring the dataset’s effectiveness at exposing regional gaps.

## Significance  
Value alignment is essential for deploying LLMs responsibly in societies that prioritize specific ethical frameworks. By grounding evaluation in Pancasila, this work provides a concrete metric to compare models against Indonesian cultural expectations and guides future research on culturally aware AI.

## Related Concepts  
Large Language Models, Value Alignment, Dilemma Scenarios, Probability Match Score (PMS), Max‑Vote Agreement Score (MVAS), Pancasila (Religion, Humanity, Unity, Democracy, Social Justice), Indonesian News Corpus.
