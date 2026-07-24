# Summary: 2026-07-20_11-17-19Z_WhenaNameIsNotaName_ABenchmarkDatasetandDistilledR.md
Saved: 2026-07-24 00:19
Source: 2026-07-20_11-17-19Z_WhenaNameIsNotaName_ABenchmarkDatasetandDistilledR.md
Model: None

---

## Summary  
The paper tackles the challenge of Bangla homographs that serve both personal names and culturally loaded common nouns, a phenomenon that relies on cultural knowledge rarely present in pretraining data. To study this issue, the authors introduce a benchmark dataset of 1,516 expert‑verified sentences containing 3,032 labelled occurrences where each word appears twice with distinct readings, each annotated with its cultural category and reasoning explanation.  

## Key Contributions  
- Finding 1: Open‑source LLMs exhibit a systematic dominant‑meaning bias, defaulting to the common‑noun sense and ignoring the name reading.  
- Finding 2: A Bangla‑specific pretrained model fails across all prompting regimes, indicating that language‑specific pretraining alone does not confer cultural grounding.  
- Finding 3: Contrastive chain‑of‑thought prompting reduces bias dramatically; distilling cultural explanations further cuts bias to under 5% and rescues the weak model.  

## Methodology  
The authors constructed a Culturally Entangled Homograph (CEH) benchmark comprising expert‑verified sentences where each homograph is presented twice, with one occurrence labelled as a name and the other as a noun. Each label includes a culturally grounded category and an explicit reasoning justification. Evaluation was performed on open‑source models, closed‑source models, and a Bangla‑specific model using various prompting strategies, including contrastive chain‑of‑thought.  

## Results  
Experiments reveal that dominant‑meaning bias reaches up to 100 % in many cases for both open‑ and closed‑source models, while the Bangla‑specific model performs poorly under every prompt. Contrastive chain‑of‑thought prompting reduces this bias from 100 % down to roughly 5 %, and distilling cultural explanations further improves performance, making the distilled (1–3B) model the strongest among small models.  

## Significance  
This work demonstrates that cultural grounding is a critical yet overlooked aspect of language understanding in low‑resource settings. By providing a benchmark and showing that reasoning over cultural knowledge can be taught without retraining, it offers a pathway to more robust LLMs for Bangla and similar culturally entangled languages.  

## Related Concepts  
- Homographs  
- Cultural grounding  
- Distributional bias  
- Chain‑of‑thought prompting  
- Contrastive learning  
- Low‑resource language models
