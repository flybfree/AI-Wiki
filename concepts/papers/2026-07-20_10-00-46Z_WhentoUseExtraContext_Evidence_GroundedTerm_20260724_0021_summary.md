# Summary: 2026-07-20_10-00-46Z_WhentoUseExtraContext_Evidence_GroundedTerminology.md
Saved: 2026-07-24 00:21
Source: 2026-07-20_10-00-46Z_WhentoUseExtraContext_Evidence_GroundedTerminology.md
Model: None

---

## Summary  
The paper investigates how to incorporate extra context into simultaneous speech translation (SimulST) without overwhelming the streaming pipeline, noting that full‑document injection is often too coarse. It discovers that the most beneficial gains arise from recovering paper‑specific terminology rather than providing uniform semantic enrichment. To address this, the authors propose EGTA – an Evidence‑Grounded Terminology Adaptation framework that creates a document terminology memory and selects compact candidate terms conditioned on the current streaming state. This adaptation is applied to both ASR/speech‑side decision spaces and the decoder side without requiring full model fine‑tuning.

## Key Contributions  
- Finding 1: Diagnostic experiments reveal that context benefits primarily stem from paper‑specific terminology recovery, not generic semantic enhancement.  
- Finding 2: EGTA builds a document terminology memory, selects compact candidate terms based on the streaming state, and adapts ASR/speech‑side and decoder decision spaces using only those selected terms.  
- Finding 3: On MCIF‑dev, EGTA‑RG improves BLEU by +1.05/+0.59, XCOMET‑XL by +0.019/+0.006, named‑entity recall by +79 %/+73 %, and acronym recall by +0.099/+0.171 for English→Chinese and English→German translations.

## Methodology  
The authors approach the problem by constructing a lightweight document terminology memory that stores all unique terms from the target talk. During streaming, they generate candidate term sets conditioned on the current acoustic‑linguistic context, then inject only these candidates into both ASR and decoder models. The adaptation can be integrated in three SimulST configurations—cascaded, end‑to‑end, or generation‑only—without any full‑model fine‑tuning, preserving latency while targeting terminology recovery.

## Results  
Experimental results show consistent gains across all latency settings on the MCIF‑dev evaluation suite. BLEU scores rise by 1.05 (average) and 0.59 (best), XCOMET‑XL improves by 0.019 and 0.006, named‑entity recall increases by 79 % and 73 %, and acronym recall improves by 0.099 and 0.171 for both language pairs. External validation on ACL60/60‑dev confirms terminology‑recall improvements without additional fine‑tuning, while shuffled‑memory controls and activation audits demonstrate that the benefits are tied to evidence‑grounded alignment rather than generic prompting.

## Significance  
This work provides a principled, evidence‑based method for using extra context in SimulST, reducing unnecessary computational load and improving translation quality specifically for technical talks. By focusing on terminology recovery and supporting multiple model architectures, EGTA offers a scalable solution that can be deployed without full retraining, making high‑quality simultaneous translation more practical for real‑world applications.

## Related Concepts  
Simultaneous Speech Translation (SimulST), Extra Context injection, Terminology Memory, Evidence‑Grounded Adaptation, Cascaded/End‑to‑End/Generation‑Only configurations, BLEU score, XCOMET‑XL metric, Named‑Entity Recall, Acronym Recall.
