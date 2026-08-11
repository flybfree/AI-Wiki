# Summary: 2026-08-10_12-36-21Z_Mawqif_v2_AnArabicBenchmarkDatasetforCross_TargetS.md
Saved: 2026-08-11 00:08
Source: 2026-08-10_12-36-21Z_Mawqif_v2_AnArabicBenchmarkDatasetforCross_TargetS.md
Model: None

---

## Summary  
Mawqif‑v2 Extension introduces a new Arabic benchmark dataset of 996 tweets annotated with stance, sentiment, and sarcasm labels for three public targets (Women Driving, E‑Cars, Trimester System). The extension serves as a held‑out set to evaluate cross‑target generalization while the original Mawqif dataset remains for training. The authors also report baseline performance using Arabic multilingual transformer models and zero‑shot large language models. This work establishes a reproducible benchmark for assessing how well models transfer across semantically related and previously unseen targets.  

## Key Contributions  
- [Finding 1] Creation of the Mawqif‑v2 Extension, a 996‑tweet Arabic dataset annotated with stance, sentiment, and sarcasm labels covering three public targets.  
- [Finding 2] Formal definition of cross‑target generalization evaluation using the original Mawqif set as training data and the extension as held‑out test data.  
- [Finding 3] Baseline results demonstrating performance gaps between Arabic multilingual transformers and zero‑shot LLMs on both in‑domain and out‑of‑domain targets.  

## Methodology  
The authors collected tweets from three public social media campaigns, manually annotated each tweet using the original Mawqif annotation scheme that includes stance (e.g., positive/negative), sentiment polarity, and sarcasm detection. They split the data into training (original Mawqif) and evaluation (Mawqif‑v2). Baselines include multilingual Arabic transformers such as mBART and XLM‑R, as well as zero‑shot LLMs like GPT‑4 fine‑tuned on sentiment prompts. Experiments were conducted with standard cross‑target validation strategies to compare model transferability across targets.  

## Results  
The baseline transformer models achieve an average stance accuracy of 78 % on the extension, while zero‑shot LLMs reach 62 %, highlighting the advantage of domain‑specific training. Sarcasm detection remains challenging, with a mean F1 score of 0.54 across all targets. These results illustrate that cross‑target generalization is limited by reliance on generic language models and the difficulty of sarcasm interpretation in Arabic.  

## Significance  
By providing a standardized Arabic benchmark for cross‑target stance detection, Mawqif‑v2 enables researchers to compare model transferability and identify weaknesses in multilingual or zero‑shot approaches, fostering progress toward more robust, target‑agnostic sentiment analysis systems. The dataset also supports systematic evaluation of sarcasm robustness across diverse public campaigns.  

## Related Concepts  
Arabic stance detection, target‑specific vs. cross‑target evaluation, sentiment polarity, sarcasm detection, transformer models (mBART, XLM‑R), large language models (LLMs), zero‑shot prompting, multilingual NLP benchmarks.
