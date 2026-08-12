# Summary: 2026-08-07_21-41-16Z_DoLLMRecommendersKnowWhenThey_reHallucinating_Audi.md
Saved: 2026-08-11 22:29
Source: 2026-08-07_21-41-16Z_DoLLMRecommendersKnowWhenThey_reHallucinating_Audi.md
Model: None

---

## Summary  
The paper investigates whether LLM recommenders can self‑detect when they hallucinate and how their verbalized confidence scores are calibrated. It audits four zero‑shot recommender models across three catalogs, measuring both out‑of‑domain (hallucination) rates and confidence calibration. The study finds that the models are systematically under‑confident even on perfect recommendations, revealing a mismatch between confidence expression and true probability. These findings challenge existing assumptions about confidence in LLM hallucination detection.

## Key Contributions  
- Finding 1: Hallucination rates vary by catalog (0–8.4 %) but are low; however, the models’ confidence is miscalibrated even when OOD=0.  
- Finding 2: All four LLMs exhibit under‑confidence on recommended items, averaging 67–86, indicating they do not express high probability for correct items.  
- Finding 3: A conformal abstention threshold based on verbalized confidence reduces hallucination marginally but incurs substantial coverage loss.

## Methodology  
The authors evaluate each recommender (Mistral Large, Llama‑3.3‑70B, GPT‑OSS‑120B, Claude Sonnet 4.6) on twelve catalog‑popularity cells using MovieLens‑25M, Amazon Reviews 2023 Toys, and Yelp Open Dataset. They compute OOD@10 (hallucination rate), Expected Calibration Error (ECE), Brier score, and reliability; they also generate confidence scores via a generic “Just Ask” prompt. The calibration is assessed by comparing predicted probabilities to observed correctness.

## Results  
Hallucination rates are 0–8.4 % across catalogs; ECE ranges up to 0.223 even with zero OOD, indicating severe miscalibration. Confidence scores average 67–86 and are accurate 92–100 %. Conformal thresholds reduce hallucination by at most 0.7 pp but increase coverage loss from 4 to 21 %.

## Significance  
The study shows that confidence calibration is a critical metric for recommender reliability, yet current practices ignore it; under‑confidence may mask errors and lead to unsafe recommendations.

## Related Concepts  
Hallucination (out‑of‑domain generation), confidence calibration (ECE, Brier score), conformal prediction, catalog‑anchored elicitation, zero‑shot recommendation.
