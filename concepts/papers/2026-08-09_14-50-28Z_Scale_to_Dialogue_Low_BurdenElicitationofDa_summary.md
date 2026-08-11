# Summary: 2026-08-09_14-50-28Z_Scale_to_Dialogue_Low_BurdenElicitationofDailyPrem.md
Saved: 2026-08-10 23:23
Source: 2026-08-09_14-50-28Z_Scale_to_Dialogue_Low_BurdenElicitationofDailyPrem.md
Model: None

---

## Summary  
The paper proposes a conversational system that uses a small language model to elicit daily premenstrual symptom ratings, replacing repetitive ordinal forms with an active dialogue that maps natural‑language expressions to predefined severity levels. It treats the task as an ordinal label‑recovery problem where the model identifies symptom clusters and assigns scores accordingly. A modern BERT evidence gate detects whether a symptom is expressed in the user’s text, feeding this binary signal into Qwen2.5‑1.5B‑Instruct for deterministic scoring. The approach reduces response burden while preserving diagnostic accuracy.

## Key Contributions  
- [Finding 1] Fixed six‑item questioning achieves a quadratic weighted kappa of 0.976 compared with baseline performance.  
- [Finding 2] Adaptive three joint symptom‑cluster questions reach 97.45 % agreement within one severity level, 80.94 % recall for moderate‑or‑higher symptoms, and cut the average number of questions by roughly 50 %.  
- [Finding 3] Participant‑cluster bootstrap analysis estimates a kappa difference of –0.062 (95 % CI –0.076 to –0.048) between the three‑cluster and six‑item strategies.

## Methodology  
The authors employed the mcPHASES dataset, which contains 3,320 complete participant‑days across six symptom clusters—cramps, mood swing, fatigue, sleep issues, stress, and bloating—rated on a six‑level ordinal scale. Six participants were reserved for development; 36 formed a frozen evaluation of 360 participant‑days and 2,160 item labels. A ModernBERT evidence gate determines if a symptom is expressed in the dialogue text, and this binary signal is passed to Qwen2.5‑1.5B‑Instruct, which outputs deterministic severity scores. Two experimental strategies were compared: (i) fixed six‑item questioning and (ii) adaptive three joint cluster questions with open‑first policies.

## Results  
Fixed six‑item questioning yielded a quadratic weighted kappa of 0.976. The adaptive three‑cluster strategy achieved a kappa of 0.913, 97.45 % agreement within one severity level, and 80.94 % recall for moderate‑or‑higher symptoms while requiring only 3.92–5.98 questions on average (versus ~6). Open‑first adaptive policies produced lower agreement than the corresponding fixed policies.

## Significance  
This work demonstrates that conversational administration can substantially reduce response burden in daily premenstrual symptom tracking without sacrificing diagnostic reliability, offering a scalable low‑burden alternative for routine monitoring and clinical deployment.

## Related Concepts  
Ordinal label‑recovery problem; ordinal scale; quadratic weighted kappa; modern BERT evidence gate; small language model (Qwen2.5‑1.5B‑Instruct); adaptive dialogue policies; participant‑cluster bootstrap analysis; symptom clusters; daily tracking burden reduction.
