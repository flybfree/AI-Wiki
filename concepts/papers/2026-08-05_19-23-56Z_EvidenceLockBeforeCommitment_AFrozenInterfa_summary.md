# Summary: 2026-08-05_19-23-56Z_EvidenceLockBeforeCommitment_AFrozenInterfaceDegra.md
Saved: 2026-08-06 21:49
Source: 2026-08-05_19-23-56Z_EvidenceLockBeforeCommitment_AFrozenInterfaceDegra.md
Model: None

---

## Summary  
The paper investigates how LLM‑as‑judge evaluation degrades when evidence is persisted across multiple calls, showing that freezing intermediate records reduces agreement with human preferences and increases answer‑order inconsistency. It compares four judging protocols on three datasets using Claude Sonnet 4.5 and GPT‑5 to quantify the impact of evidence locking versus structured elicitation.

## Key Contributions  
- Finding 1: Evidence locking (persisting evidence across calls) reduces agreement with human preferences by 4–6 percentage points compared to standard pairwise judging.  
- Finding 2: Evidence locking increases answer‑order inconsistency by 8–10 points relative to structured one‑call judging, indicating a loss of coherence.  
- Finding 3: Pointwise locking is also harmful, while structured evidence elicitation remains close to standard judging.

## Methodology  
The authors designed four judgment protocols: (1) standard pairwise judging where each call receives only the two candidate answers; (2) structured one‑call judging where criteria and evidence are extracted in a single call before decision; (3) two‑call evidence locking where evidence is recorded in the first call and used exclusively in the second; (4) three‑call pointwise locking where each criterion is locked separately. They applied these protocols to 24,000 judgments across HelpSteer3, FeedbackQA, and CoVal using Claude Sonnet 4.5 and GPT‑5.

## Results  
Across all datasets, evidence locking (two‑call and pointwise) lowered agreement with human preferences by 4–6% and raised answer‑order inconsistency by 8–10 points compared to structured one‑call judging. Standard pairwise judging performed best, while structured evidence elicitation stayed near that level. The degradation was consistent across both models and all three datasets.

## Significance  
These findings highlight a critical flaw in “evidence lock” designs: persisting intermediate records can mislead the model’s decision process, undermining alignment with human judgments and introducing systematic inconsistency. The results caution against treating evidence as a static artifact rather than a dynamic guide during evaluation.

## Related Concepts  
- LLM‑as‑judge evaluation  
- Evidence persistence vs. source answer reliance  
- Structured elicitation of criteria  
- Answer‑order consistency  
- Human preference alignment
