# Summary: 2026-07-23_05-56-04Z_FromaWord_LevelDictionarytoSentence_LevelSemantics.md
Saved: 2026-07-24 02:32
Source: 2026-07-23_05-56-04Z_FromaWord_LevelDictionarytoSentence_LevelSemantics.md
Model: None

---

## Summary  
The paper addresses the limitation of word‑level lexicons in measuring grievance across languages, proposing that static term matching should be replaced by contextual models that read full sentences and paragraphs. Experiments on a five‑language evaluation set show that reading the surrounding text improves detection of implicit or quoted grievances, raising average precision from 0.14 to 0.20 where the dictionary is silent. The study also reveals a construction bias in existing lexicon evaluations: every “random” label corresponds to a lexicon‑negative item, collapsing macro‑AUROC to 0.5. The authors release their code and benchmark for reproducibility.

## Key Contributions  
- [Finding 1] Contextual models outperform word‑level dictionaries by significantly increasing average precision on lexicon‑negative text from 0.14 to 0.20 across five languages.  
- [Finding 2] Reading the full post rather than just the target sentence improves detection of implicit and cross‑sentence grievances, highlighting the importance of broader context.  
- [Finding 3] The existing Grievance Dictionary evaluation is biased: every “random” label corresponds to a lexicon‑negative item, collapsing macro‑AUROC to 0.5.

## Methodology  
The authors keep the dictionary’s 22‑construct ontology but replace term matching with contextual language models trained on multilingual data; training uses multilingual BERT embeddings to capture cross‑linguistic semantics. They evaluate these models on a non‑circular benchmark that stratifies items into unconditional‑random, lexicon‑positive, and lexicon‑negative categories across five languages.

## Results  
Experiments show that context reading yields the largest gains where the dictionary is silent, particularly for quoted or implicit grievances. Average precision improves from 0.14 to 0.20 on lexicon‑negative samples; macro‑AUROC rises from 0.686 to about 0.75. The benchmark confirms that “random” labels are all negative, exposing a construction flaw.

## Significance  
These findings demonstrate that grievance detection is more reliable when context is considered and that existing lexicon evaluations are misleading due to circularity. They provide a methodological path for fairer multilingual threat monitoring systems.

## Related Concepts  
- Grievance Lexicons (e.g., Grievance Dictionary)  
- Contextual Language Models (BERT, multilingual variants)  
- AUROC, Average Precision  
- Construction Bias in Evaluation
