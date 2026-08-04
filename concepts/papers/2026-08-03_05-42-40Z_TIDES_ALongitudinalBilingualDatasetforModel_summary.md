# Summary: 2026-08-03_05-42-40Z_TIDES_ALongitudinalBilingualDatasetforModelingMult.md
Saved: 2026-08-03 23:37
Source: 2026-08-03_05-42-40Z_TIDES_ALongitudinalBilingualDatasetforModelingMult.md
Model: None

---

## Summary  
TIDES (Team Interaction Dynamics and English‑Korean Speech) presents a high‑resolution longitudinal dataset that records 12 university project teams over an entire semester, capturing 75 971 bilingual utterances from in‑person meetings. The authors introduce socio‑structural annotations that track interaction types, emergent roles, and development stages to enable modeling of team evolution. By fine‑tuning a large language model on this data, they achieve a notable boost in next‑speaker prediction over simple baselines and performance close to state‑of‑the‑art zero‑shot models while using far less training material. However, human evaluations reveal that the improved prediction does not always translate into more natural or preferred utterances.

## Key Contributions  
- [Finding 1] TIDES is a longitudinal bilingual dataset of 75 971 utterances from 12 university project teams over one semester, providing a realistic record of multi‑party social dynamics.  
- [Finding 2] Fine‑tuning on TIDES improves next‑speaker prediction by 13.8 percentage points (64.53% vs. bigram baseline) and yields performance within 2.1 pp of the best zero‑shot models on the AMI Meeting Corpus while using ~42 % less data.  
- [Finding 3] Human evaluations show that the fine‑tuned model is generally less preferred than vanilla models, indicating a potential mismatch between prediction accuracy and perceived naturalness.

## Methodology  
The authors collected in‑person meeting recordings from university project teams, transcribed them into English and Korean, and annotated each utterance with socio‑structural tags (e.g., interaction type, role emergence). They then fine‑tuned a large language model on this bilingual corpus using the next‑speaker prediction task. The evaluation employed both automated metrics (accuracy) and human preference studies to assess naturalness.

## Results  
Automatically, TIDES yields a 13.8 pp gain over bigram baselines (64.53% accuracy). Compared with the published state of the art on AMI Meeting Corpus, TIDES achieves performance within 2.1 pp while requiring only ~42 % less training data. Human preference tests indicate that fine‑tuned models are less liked than vanilla models, suggesting improved prediction does not always improve perceived coherence.

## Significance  
TIDES bridges the gap between short‑term lab experiments and long‑term real‑world team dynamics, offering a resource for studying how socio‑structural factors evolve over time. Its fine‑tuned model demonstrates that richer modeling can boost predictive performance with less data, yet it also highlights the need to align technical improvements with human judgments of naturalness in multi‑party generation.

## Related Concepts  
Longitudinal datasets, bilingual corpora, next‑speaker prediction, socio‑structural annotations, zero‑shot models, multi‑party interaction modeling.
