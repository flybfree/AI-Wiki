# Summary: 2026-07-22_22-32-34Z_Rushes_AHumanPreferenceDatasetforPluralisticAlignm.md
Saved: 2026-07-24 02:17
Source: 2026-07-22_22-32-34Z_Rushes_AHumanPreferenceDatasetforPluralisticAlignm.md
Model: None

---

## Summary  
The paper introduces **Rushes**, a dataset of human engagement in interactive narrative games, designed to study how users make sequential choices among small candidate sets. By analyzing 44,226 decision events from 8,167 unique players across six games, the authors demonstrate that user preferences exhibit structured, low‑entropy patterns and that state‑of‑the‑art large language models underperform simple baselines on event‑level prediction, revealing a persistent **Engagement Gap**.  

## Key Contributions  
- [Finding 1] Rushes is a dataset of 44,226 decision events from 8,167 users across six games, capturing personalized sequential engagement.  
- [Finding 2] User choices exhibit low choice entropy relative to a uniform baseline, indicating structured patterns.  
- [Finding 3] State‑of‑the‑art LLMs like GPT‑5 achieve only 34.23 % event‑level prediction accuracy versus the Popularity Baseline at 36.4 %, showing a robust Engagement Gap.  

## Methodology  
The authors collect data via a game interface where AI‑generated branching narratives present a small candidate set at each decision point; users select one option, and the system logs the full context, the chosen choice, and a persistent user identifier, producing time‑ordered trajectories for later analysis.  

## Results  
Model predictions are evaluated on event‑level choice accuracy. Classical matrix factorization (SVD) captures 37.7 % personalized signal; frontier LLMs achieve 34.23 %; the Popularity Baseline is 36.4 %. The Engagement Gap persists across models, indicating that single, population‑level objectives are insufficient to capture heterogeneous, context‑dependent engagement signals.  

## Significance  
This dataset and analysis reveal that modern alignment methods optimize for majority preferences rather than individual trajectories, limiting personalization in generative systems; Rushes provides a benchmark to evaluate pluralistic alignment and sequential decision‑making.  

## Related Concepts  
- Pluralistic Alignment: aligning models with diverse user preferences.  
- Sequential Decision‑Making: modeling choices over time.  
- Engagement Gap: performance disparity between advanced and simple baselines.  
- Matrix Factorization (SVD): capturing personalized latent factors.
