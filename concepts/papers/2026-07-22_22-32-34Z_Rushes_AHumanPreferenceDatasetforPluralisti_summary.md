# Summary: 2026-07-22_22-32-34Z_Rushes_AHumanPreferenceDatasetforPluralisticAlignm.md
Saved: 2026-07-24 02:17
Source: 2026-07-22_22-32-34Z_Rushes_AHumanPreferenceDatasetforPluralisticAlignm.md
Model: None

---

## Summary  
Rushes is a new dataset that captures how individual users make sequential choices within AI‑generated branching narratives. The authors demonstrate that human engagement exhibits structured, non‑random patterns with low choice entropy, and they position Rushes as a benchmark for evaluating pluralistic alignment in generative systems. By comparing simple matrix‑factorization baselines to state‑of‑the‑art large language models (including GPT‑5), the study reveals an “Engagement Gap” where advanced models perform worse than baseline popularity measures. The work also releases open code and data to support future research on sequential decision‑making.

## Key Contributions  
- [Finding 1] Rushes contains 44,226 decision events from 8,167 unique users across six games, providing a richly personal, time‑ordered log of revealed preferences.  
- [Finding 2] User choices show low entropy and measurable personalized signals (≈37.7 % explained by SVD), highlighting that engagement is not uniform but follows structured trajectories.  
- [Finding 3] Front‑end LLMs such as GPT‑5 achieve only 34.23 % event‑level prediction accuracy, falling short of the popularity baseline (36.4 %), exposing a gap in current alignment methods.

## Methodology  
The authors built Rushes through an interactive game interface where each narrative branch presents a small explicit candidate set; users select one option and the system records the full set, their choice, and the evolving context. This yields per‑user, time‑ordered trajectories with persistent identifiers, enabling analysis of sequential engagement rather than static judgments.

## Results  
- Dataset size: 44,226 events, 8,167 users, six games.  
- Classical SVD model captures a personalized signal of 37.7 % variance reduction.  
- Frontier LLMs (e.g., GPT‑5) achieve 34.23 % accuracy on event‑level choice prediction.  
- Popularity baseline scores 36.4 %, indicating that SOTA models default to majority preferences rather than adapting to individual paths.

## Significance  
Rushes provides a concrete benchmark for pluralistic alignment, showing that current RLHF‑style objectives are insufficient for modeling heterogeneous, context‑dependent engagement. The documented Engagement Gap underscores the need for methods that respect individualized trajectories and can outperform simple popularity baselines in sequential decision tasks.

## Related Concepts  
- Pluralistic alignment: designing systems that accommodate diverse user preferences.  
- Revealed preferences: inferred from actual actions rather than explicit surveys.  
- Engagement Gap: performance disparity between advanced models and baseline expectations.  
- Matrix factorization (SVD): a classic technique for uncovering personalized latent factors in preference data.  
- Sequential decision‑making: modeling choices as ordered events within evolving contexts.
