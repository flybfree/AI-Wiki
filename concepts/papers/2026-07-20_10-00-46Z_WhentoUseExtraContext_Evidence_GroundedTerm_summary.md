# Summary: 2026-07-20_10-00-46Z_WhentoUseExtraContext_Evidence_GroundedTerminology.md
Saved: 2026-07-24 00:18
Source: 2026-07-20_10-00-46Z_WhentoUseExtraContext_Evidence_GroundedTerminology.md
Model: None

---

## Summary  
The paper investigates why injecting full‑document context into every streaming segment of simultaneous speech translation is often unnecessary and proposes an Evidence‑Grounded Terminology Adaptation (EGTA) framework that extracts only the most relevant terms for each streaming state. By building a document terminology memory and selecting compact candidate words conditioned on the current audio‑text stream, EGTA adapts both ASR and decoder decision spaces without requiring full‑model fine‑tuning. The authors demonstrate that this targeted adaptation yields measurable gains in translation quality across technical‑talk datasets.  

## Semantic links
- [[concepts/audio-speech/audio-speech-hub.md|Audio and Speech Hub]] — 3 title terms overlap; 73 backlinks; 3 summary/topic terms overlap
- [[concepts/papers/2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforV_summary.md|Summary: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md]] — 3 title terms overlap; 14 summary/topic terms overlap; semantic match 0.13
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 2 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** Diagnostic experiments reveal that the benefit of extra context comes primarily from paper‑specific terminology recovery rather than a uniform semantic enhancement.  
- **Finding 2:** EGTA constructs a document terminology memory, selects compact candidate terms based on the current streaming state, and adapts both ASR (speech‑side) and decoder decision spaces using only those selected terms.  
- **Finding 3:** The framework improves BLEU (+1.05/+0.59), XCOMET‑XL (+0.019/+0.006), named‑entity recall (+79 %/+73 %), and acronym recall (+0.099/+0.171) on En→Zh and En→De in MCIF‑dev, while maintaining consistent gains across latency settings without full‑model fine‑tuning.  

## Methodology  
The authors first conducted diagnostic experiments to isolate the source of context benefits, confirming that only terminology alignment matters. They then designed EGTA as a lightweight adaptation layer: (1) a persistent document terminology memory stores all unique terms; (2) at each streaming step, a compact set of candidate terms is chosen by conditioning on the current audio‑text state; (3) this set triggers adaptive updates to both ASR and decoder models, allowing the system to “remember” only the needed words. The method can be embedded in cascaded, end‑to‑end, or generation‑only SimulST pipelines without retraining the full model.  

## Results  
On MCIF‑dev, EGTA‑RG boosts BLEU by 1.05 (en→zh) and 0.59 (en→de), XCOMET‑XL by 0.019 and 0.006, named‑entity recall by 79 % and 73 %, and acronym recall by 0.099 and 0.171 respectively. Latency evaluations show that EGTA consistently improves XCOMET‑XL, named‑entity recall, and acronym recall across all latency settings. External validation on ACL60/60‑dev confirms similar terminology‑recall gains without any additional fine‑tuning. Shuffled‑memory controls and activation audits further prove that improvements stem from evidence‑grounded term alignment rather than generic prompting.  

## Significance  
EGTA demonstrates that simultaneous speech translation can achieve substantial quality gains by focusing on a small, context‑relevant set of terms, thereby reducing latency and computational cost compared with full‑document context injection or model fine‑tuning. This targeted adaptation is especially valuable for technical talks where precise terminology is critical yet streaming constraints limit heavy processing.  

## Related Concepts  
Simultaneous Speech Translation (SimulST), Evidence‑Grounded Terminology Adaptation (EGTA), document terminology memory, streaming state conditioning, ASR/speech‑side adaptation, decoder‑space adaptation, BLEU score, XCOMET‑XL metric, named‑entity recall, acronym recall.
