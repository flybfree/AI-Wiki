# Summary: 2026-07-20_11-17-19Z_WhenaNameIsNotaName_ABenchmarkDatasetandDistilledR.md
Saved: 2026-07-24 00:22
Source: 2026-07-20_11-17-19Z_WhenaNameIsNotaName_ABenchmarkDatasetandDistilledR.md
Model: None

---

## Summary  
The paper tackles the problem of Bangla homographs where a single word simultaneously functions as a personal name and a culturally loaded common noun, causing low‑resource large language models (LLMs) to default to the common meaning. It introduces the Culturally Entangled Homograph (CEH) benchmark with 1 516 expert‑verified sentences, each containing two readings annotated with cultural categories and reasoning explanations. Experiments reveal that open‑ and closed‑source LLMs exhibit a systematic dominant‑meaning bias, ignoring name senses, especially in Bangla‑specific models that fail under all prompting regimes. Contrastive chain‑of‑thought prompting and distilled cultural explanations can markedly reduce this bias without additional training.

## Key Contributions  
- Finding 1: Models systematically default to the common‑noun sense of Bangla homographs, overlooking personal names.  
- Finding 2: A dedicated Bangla model fails under every prompting regime we test, indicating language‑specific pretraining alone does not confer cultural grounding.  
- Finding 3: Contrastive chain‑of‑thought prompting and distilled cultural explanations reduce dominant‑meaning bias from up to 100 % to under 5 %, enabling small (1–3B) models to reason correctly.

## Methodology  
The authors constructed the CEH dataset by curating sentences in which a Bangla word appears twice, each occurrence representing either a name or a culturally loaded noun. Every reading is labeled with its cultural category and accompanied by a concise reasoning justification that explains why the model should choose one sense over the other. The evaluation compares open‑source and closed‑source LLMs across multiple prompting setups, including contrastive chain‑of‑thought prompts that require models to generate explanations before selecting the correct reading. Cultural explanations are distilled into short textual snippets used as prompts for small language models.

## Results  
Experiments show a systematic dominant‑meaning bias where models select the common noun in 95–100 % of cases, while the Bangla‑specific model consistently fails (0 % correct). Using contrastive chain‑of‑thought prompting improves performance to about 85 %. Distilling cultural explanations further reduces bias to under 5 %, and fine‑tuning or prompting with these distilled snippets enables small models (1–3B parameters) to achieve >95 % accuracy on the CEH benchmark.

## Significance  
This work demonstrates that cultural knowledge is not automatically captured by language pretraining, especially for low‑resource languages like Bangla. By providing a benchmark and showing that reasoning prompts can substitute for extensive training, it offers a scalable approach to improve model performance without large datasets or fine‑tuning. The study also highlights the importance of culturally entangled lexical items in NLP evaluation.

## Related Concepts  
Homographs, cultural grounding, low‑resource language models, chain‑of‑thought prompting, contrastive learning, distilled explanations, bias mitigation, Bangla (Bengali) language processing.
