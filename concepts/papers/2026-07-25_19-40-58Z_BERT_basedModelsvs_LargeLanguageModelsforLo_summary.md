# Summary: 2026-07-25_19-40-58Z_BERT_basedModelsvs_LargeLanguageModelsforLow_Resou.md
Saved: 2026-07-27 20:14
Source: 2026-07-25_19-40-58Z_BERT_basedModelsvs_LargeLanguageModelsforLow_Resou.md
Model: None

---

## Summary  
The paper aims to compare BERT‑based models fine‑tuned on Marathi NER data with general‑purpose Large Language Models (LLMs) for low‑resource named entity recognition in Marathi. It contributes that the fine‑tuned MahaBERT‑v2 variants achieve higher F1 scores than both the existing baseline and all evaluated LLMs, demonstrating task‑specific language models outperform LLMs in this setting.

## Key Contributions  
- Fine‑tuning MahaBERT‑v2 on multiple MahaNER dataset variants yields state‑of‑the‑art performance (F1 0.88–0.91) for Marathi NER.  
- General‑purpose LLMs such as Gemini, LLaMA‑3.3‑70B and Gemma perform significantly worse (F1 0.57–0.69), confirming their limited efficacy in low‑resource language tasks.  
- The study empirically validates that task‑specific, domain‑focused models remain superior to LLMs for Marathi NER.

## Methodology  
The authors fine‑tuned MahaBERT‑v2 on several variants of the MahaNER dataset and compared them against the existing MahaNER baseline and three large language models (Gemini, LLaMA‑3.3‑70B, Gemma) on a Marathi NER test set using precision, recall, and F1 metrics.

## Results  
Fine‑tuned MahaBERT variants achieved F1 scores ranging from 0.88 to 0.91, which surpass the baseline model’s score of 0.8843. In contrast, LLM‑based approaches yielded F1 scores between 0.57 and 0.69, showing a clear performance gap. All metrics confirm that fine‑tuned BERT models outperform LLMs across all evaluation criteria.

## Significance  
This work underscores that specialized architectures trained on limited but relevant data can outperform massive, general‑purpose LLMs in low‑resource NLP tasks, guiding resource allocation and model design for under‑represented languages like Marathi. It highlights the continued importance of language‑focused models when high‑quality annotated corpora are scarce.

## Related Concepts  
Named Entity Recognition (NER), low‑resource language processing, BERT fine‑tuning, Large Language Models (Gemini, LLaMA‑3.3‑70B, Gemma), task‑specific vs. general‑purpose models, F1 score.
