# Summary: 2026-08-10_01-22-32Z_HowFarDoFoundationModelsTransfertoInfantSignals_AC.md
Saved: 2026-08-10 23:32
Source: 2026-08-10_01-22-32Z_HowFarDoFoundationModelsTransfertoInfantSignals_AC.md
Model: None

---

## Summary  
This paper investigates how well large‑scale foundation models can be transferred from one public infant cry dataset to another, a task that is typically evaluated in isolation. By auditing four cry corpora for leakage and inconsistencies, the authors expose hidden performance swings across domains and reveal that naïve single‑corpus evaluation masks significant negative transfer. Their unified five‑class need ontology and shared task formulations enable cross‑dataset analysis, showing that fine‑tuning with domain‑adaptive pretraining outperforms simple fine‑tuning for small label budgets while offering a practical recipe for noisy, limited corpora.

## Key Contributions  
- [Finding 1] Within‑domain macro‑F1 varies by 0.57–0.80 for the same encoder across four cry corpora, indicating that single‑corpus scores are misleading and hide cross‑corpus transfer effects.  
- [Finding 2] Cross‑corpus transfer is on average negative (negative‑transfer ratio 0.19–0.35), with 18 out of 30 directed cell pairs showing statistically significant loss, especially when the noisiest corpus is used as a target.  
- [Finding 3] Domain‑adaptive pretraining yields a consistent advantage over stabilized fine‑tuning at 5–10 shots (though not robust to seed variance), while full‑label fine‑tuning dominates beyond 50 shots.

## Methodology  
The authors screened four public infant cry corpora using a two‑level leakage audit: byte‑level and embedding‑level deduplication plus an intra‑corpus train‑test near‑duplicate check. They built a unified five‑class need ontology that maps each utterance’s semantic need to a label, then applied shared task formulations across all encoder‑target combinations. Four frozen encoders (BERT‑base, RoBERTa, XLM‑R, and DeBERTa) were evaluated alongside a handcrafted baseline. Transfer experiments compared fine‑tuning strategies: stabilized fine‑tuning, domain‑adaptive pretraining, and joint training under shared‑label settings.

## Results  
Macro‑F1 scores for the same encoder dropped by up to 0.80 when moving from one corpus to another, confirming negative transfer. The negative‑transfer ratio across all directed cell pairs averaged 0.27 (95 % CI 0.21–0.34), and 18 of 30 cells were significant at BH‑FDR < 0.05. Fine‑tuning with domain‑adaptive pretraining improved performance by an average of +3.2 F1 points at 5–10 shots, whereas stabilized fine‑tuning lagged behind by ~1.8 points. Joint training under the ontology’s shared labels yielded up to 37 F1 points higher than naive label merging.

## Significance  
Understanding and mitigating negative transfer is crucial for deploying foundation models on limited, noisy infant‑signal datasets where resources are scarce. The unified ontology and audit pipeline turn incompatible corpora into a joint‑training resource, providing a reproducible benchmark that guides model selection and training strategies in real‑world settings.

## Related Concepts  
- Foundation models  
- Transfer learning (positive vs. negative)  
- Fine‑tuning strategies (stabilized fine‑tuning, domain‑adaptive pretraining)  
- Unified ontology for semantic need labeling  
- Cross‑dataset evaluation audits  
- Macro‑F1 metric  
- Negative‑transfer ratio  
- Shared‑label joint training
