# Summary: 2026-08-05_12-37-31Z_Guideline_as_Oracle_Zero_AnnotationTrainingofanOph.md
Saved: 2026-08-05 20:35
Source: 2026-08-05_12-37-31Z_Guideline_as_Oracle_Zero_AnnotationTrainingofanOph.md
Model: None

---

## Summary  
The paper proposes **Guideline‑as‑Oracle (GAO)**, a framework that leverages the American Academy of Ophthalmology’s clinical guidance to train an ophthalmic telephone triage agent without any human annotation. By converting these 70‑row rule tables into a dataset of 3,000 multi‑turn dialogues and using eight construction strategies to map rules onto conversational content, GAO achieves zero‑annotation training while preserving privacy. The resulting model, GAO‑Triage, improves both agreement with an operational reference and emergent‑case recall compared with existing systems.

## Key Contributions  
- **Finding 1:** GAO compiles the AAO guidance into a compact 70‑row rule table that serves as the sole instance‑level supervision source for training, eliminating the need for costly expert dialogue annotation.  
- **Finding 2:** The authors catalog eight construction strategies (e.g., cited‑row tier assignment, one‑fact boundary pairs, metadata‑only repair) and characterize their evidential status—labeling mechanism, null, confounded, or evaluated only as a package—to understand how rule conversion influences model learning.  
- **Finding 3:** GAO‑Triage, fine‑tuned on a 9B backbone, raises agreement from 61.7% to 74.1% (exact McNemar p = 0.0046) and emergent‑case recall from 9.5% to 69.0%, while the model remains robust across seeds and patient simulators; label repair also resolves a late‑training safety degradation, whereas permuting label‑dialogue assignments collapses performance to a constant‑routine predictor.

## Methodology  
The authors approached the problem by first extracting the AAO guidance into an operational rule table (70 rows). They then generated 3,000 multi‑turn medical dialogues using eight construction strategies that map each rule to conversational utterances. Human labeling was reserved exclusively for evaluation on a 201‑case reference set. A 9B language model was fine‑tuned on this zero‑annotation corpus, and the system was benchmarked against seven general‑purpose triage models.

## Results  
Fine‑tuning GAO‑Triage yields significant gains: agreement with the operational reference improves from 61.7% to 74.1% (exact McNemar p = 0.0046), and emergent‑case recall jumps from 9.5% to 69.0%. These improvements persist across two random seeds and a patient simulator. None of the seven competing systems dominate GAO‑Triage on both metrics, and the model requires no frontier model at inference time. Moreover, label repair coincides with the disappearance of a late‑training safety degradation.

## Significance  
GAO demonstrates that zero‑annotation training is feasible for medical dialogue agents when rule‑based supervision is available, dramatically reducing annotation costs while respecting patient privacy. The results show that the signal driving performance lies in how guidelines are assigned to dialogues rather than superficial surface form, offering a scalable path toward reliable ophthalmic triage.

## Related Concepts  
Guideline‑as‑Oracle (GAO), zero‑annotation training, medical telephone triage, rule table conversion, fine‑tuning of large language models, emergent‑case recall, exact McNemar test, safety degradation, constant‑routine predictor.
