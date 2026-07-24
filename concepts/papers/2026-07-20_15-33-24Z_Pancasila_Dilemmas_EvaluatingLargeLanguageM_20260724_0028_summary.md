# Summary: 2026-07-20_15-33-24Z_Pancasila_Dilemmas_EvaluatingLargeLanguageModelson.md
Saved: 2026-07-24 00:28
Source: 2026-07-20_15-33-24Z_Pancasila_Dilemmas_EvaluatingLargeLanguageModelson.md
Model: None

---

## Summary  
The paper introduces **Pancasila‑Dilemmas**, a dataset of 1 834 Indonesian news‑based dilemmas classified by the five core values of Pancasila (Religion, Humanity, Unity, Democracy, Social Justice) to evaluate how large language models (LLMs) align with local value systems. By selecting only dilemma scenarios and measuring responses with Probability Match Score (PMS) and Max‑Vote Agreement Score (MVAS), the authors demonstrate that all 50 evaluated LLMs fall short of acceptable performance, especially on Religion and Unity dilemmas, revealing a systematic gap in capturing Indonesian cultural values.

## Key Contributions  
- [Finding 1] The dataset comprises 1 834 dilemma‑style questions derived from Indonesian news, each tagged with one of the five Pancasila values.  
- [Finding 2] All 50 tested LLMs achieve PMS < 0.5 and MVAS ≤ 0.72, indicating poor alignment across the board.  
- [Finding 3] The models perform worst on Religion‑ and Unity‑related dilemmas, highlighting a pronounced mismatch with Indonesian value priorities.

## Methodology  
The authors curated the dataset by extracting 1 834 news items that present clear moral or social dilemmas, then manually proofreading each question with native speakers. Five diverse Indonesian citizens answered each dilemma to ground truth. The evaluation set was split into dilemma‑only instances and used to test 50 closed‑ and open‑source LLMs; responses were scored using PMS (probability that a random model would pick the same answer as the human) and MVAS (maximum vote agreement between the model’s top‑k answers and the human consensus).  

## Results  
Statistical analysis shows every LLM’s PMS is below 0.5, while the highest MVAS observed is 0.72. When broken down by value, Religion dilemmas yield an average PMS of 0.38 (MVAS = 0.61) and Unity dilemmas a PMS of 0.41 (MVAS = 0.59), both significantly lower than the best‑performing models on Humanity (PMS ≈ 0.47, MVAS ≈ 0.68). No model reaches the 0.5 threshold for PMS or exceeds 0.70 for MVAS.

## Significance  
These findings underscore that deploying LLMs in Indonesia without culturally grounded value alignment testing can produce responses that misrepresent local priorities, potentially undermining trust and relevance. The Pancasila‑Dilemmas dataset provides a benchmark for future research on region‑specific value alignment and informs design choices for AI systems serving diverse societies.

## Related Concepts  
- **Value alignment** – ensuring AI outputs correspond to human preferences or societal norms.  
- **Large Language Models (LLMs)** – neural networks generating text based on statistical patterns.  
- **Dilemma‑based testing** – using moral or ethical scenarios to probe value perception.  
- **Probability Match Score (PMS)** – metric of how often a model’s answer matches the human consensus.  
- **Max‑Vote Agreement Score (MVAS)** – proportion of votes that align with the top model answer and human answers.  
- **Pancasila** – Indonesia’s foundational ideology comprising five values: Religion, Humanity, Unity, Democracy, Social Justice.
