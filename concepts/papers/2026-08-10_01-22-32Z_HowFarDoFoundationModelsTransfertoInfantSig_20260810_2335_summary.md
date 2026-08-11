# Summary: 2026-08-10_01-22-32Z_HowFarDoFoundationModelsTransfertoInfantSignals_AC.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_01-22-32Z_HowFarDoFoundationModelsTransfertoInfantSignals_AC.md
Model: None

---

## Summary  
The paper investigates how well frozen foundation models trained on one infant cry dataset can be transferred to another, aiming to expose hidden biases in single‑corpus evaluation and propose a unified approach. It audits four cry corpora using leakage checks and a five‑class need ontology, comparing encoder outputs across datasets. Findings reveal negative transfer in many cases and that fine‑tuning yields better performance than frozen probes. The work also introduces a practical recipe for noisy small corpora and releases tools.

## Key Contributions  
- Negative transfer is prevalent across datasets, with an average negative‑transfer ratio of 0.19–0.35 and significant in 18 of 30 directed cell pairs.  
- Frozen encoder outputs saturate at modest label budgets while stabilized fine‑tuning improves performance, especially at 5‑10 shots; domain‑adaptive pretraining outperforms it there but not beyond 50 shots.  
- Joint training under a unified need ontology yields up to 37 F1 points higher than naive merging of unmapped labels.

## Methodology  
The authors screened four cry corpora for leakage via byte‑level and embedding‑level deduplication plus within‑corpus train‑test near‑duplicate audit. They used a unified five‑class need ontology mapping each clip’s observed behavior to a semantic need, created shared task formulations, evaluated four frozen encoders and a handcrafted baseline under this ontology.

## Results  
Within‑domain macro‑F1 varied 0.57–0.80 for the same encoder; cross‑corpus transfer was negative on average; 349 content‑identical clip groups had conflicting metadata labels across corpora; positive effect size observed when transferring to the noisiest corpus after near‑duplicate removal; fine‑tuning beats frozen probes, especially at 5–10 shots.

## Significance  
The audit reveals that single‑corpus evaluation masks transfer issues and noisy label conflicts, offering a unified ontology and pipeline to enable reliable cross‑dataset learning for infant signals. It provides a practical recipe for small noisy corpora and demonstrates the value of joint training with proper ontology mapping.

## Related Concepts  
Foundation models; infant cry corpora; negative transfer; fine‑tuning; domain‑adaptive pretraining; need ontology; shared‑label joint training; leakage audit; macro‑F1; near‑duplicate removal.
