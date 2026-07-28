# Summary: 2026-07-27_14-54-01Z_SystematicAnalysisofLargeLanguageModelsandTransfor.md
Saved: 2026-07-27 23:01
Source: 2026-07-27_14-54-01Z_SystematicAnalysisofLargeLanguageModelsandTransfor.md
Model: None

---

## Summary  
The paper systematically evaluates large language models (LLMs) and transformer‑based neural machine translation systems for English‑Tamil and Tamil‑English translation using a suite of diverse datasets (NTREX, EnTamV2, WikiMatrix, PMIndia). It compares supervised NMTs such as NLLB and mBART with few‑shot prompting on a Tamil‑capable model, measuring BLEU and chrF scores while visualising attention alignments. The study highlights how dataset quality, domain alignment, and attention mechanisms jointly influence translation performance.

## Key Contributions  
- Finding 1: Performance varies significantly across datasets; high‑quality parallel data yields higher BLEU/chrF scores.  
- Finding 2: Attention visualization reveals token‑level correspondences, improving interpretability and model debugging.  
- Finding 3: Few‑shot prompting with TamilLaMA can produce coherent translations comparable to supervised NMTs.

## Methodology  
The authors collected four datasets representing different sizes and domains of English‑Tamil and Tamil‑English pairs. They loaded supervised models (NLLB, mBART) and a few‑shot prompt scenario using the Tamil‑capable TamilLaMA model. Evaluation employed BLEU and chrF metrics; attention maps were generated for selected sentences to illustrate token alignment.

## Results  
Supervised NMTs achieved higher scores on high‑quality datasets like NTREX but struggled on low‑resource EnTamV2 and PMIndia. Attention maps showed that the model tends to align English tokens with nearby Tamil equivalents, indicating local lexical mapping. The few‑shot approach produced translations with acceptable coherence despite limited examples.

## Significance  
The work underscores that dataset quality is crucial for low‑resource language translation, demonstrates interpretability benefits of attention mechanisms, and shows that LLMs can be effective even without extensive fine‑tuning via in‑context prompting.

## Related Concepts  
Large Language Models, Transformer‑based NMT, BLEU, chrF, Attention Visualization, Few‑shot Learning, Low‑Resource Languages (Tamil), Multilingual Pretraining, In‑Context Prompting.
