# Summary: 2026-08-09_14-50-28Z_Scale_to_Dialogue_Low_BurdenElicitationofDailyPrem.md
Saved: 2026-08-10 23:23
Source: 2026-08-09_14-50-28Z_Scale_to_Dialogue_Low_BurdenElicitationofDailyPrem.md
Model: None

---

## Summary  
The paper proposes **Scale-to-Dialogue**, a conversational system that reduces the burden of daily premenstrual symptom tracking by eliciting symptoms in natural dialogue rather than static forms. It treats ordinal severity ratings as an active retrieval problem and uses small language models to map participant statements to six‑level labels. The approach integrates evidence detection with deterministic scoring via Qwen2.5-1.5B-Instruct, achieving high agreement while cutting question count by half. This work demonstrates that active cluster‑level elicitation can produce reliable daily symptom assessments.

## Key Contributions  
- Active cluster‑level elicitation yields a quadratic weighted kappa of 0.976 with six fixed items and 0.913 with three joint questions, indicating high reliability.  
- Adaptive open‑first policies require fewer questions (3.92–5.98) but produce lower agreement than fixed strategies, highlighting the trade‑off between efficiency and accuracy.  
- Participant‑cluster bootstrap analysis estimates a kappa difference of -0.062 between three‑cluster and six‑item strategies, quantifying the impact of clustering on measurement precision.

## Methodology  
The authors collected 3,320 participant‑days from the mcPHASES dataset covering cramps, mood swing, fatigue, sleep issues, stress, and bloating on a six‑level ordinal scale. Six participants were used for development; 36 formed a frozen evaluation with 360 participant‑days and 2,160 labels. A ModernBERT evidence gate identifies expressed symptoms, while Qwen2.5-1.5B-Instruct outputs deterministic severity scores. The system either asks fixed six items or three joint cluster questions, employing open‑first adaptive policies that ask as few as four questions.

## Results  
Fixed six‑item questioning achieved 97.45 % agreement within one severity level and 80.94 % recall for moderate‑or‑higher symptoms while halving the number of questions. Three joint symptom‑cluster questions reached 91.3 % kappa, 97.45 % intraclass agreement on single levels, and 80.94 % recall with 50 % fewer queries. Adaptive policies required 3.92–5.98 questions but showed lower κ (≈0.90). Bootstrap analysis gave a κ difference of -0.062 (95 % CI –0.076 to –0.048) between three‑cluster and six‑item strategies.

## Significance  
By converting symptom tracking into low‑burden conversational elicitation, Scale-to-Dialogue enables daily monitoring without cumbersome forms, supporting continuous premenstrual health data collection and enabling timely clinical insights.

## Related Concepts  
ordinal severity scales, quadratic weighted kappa, Large Language Models (Qwen2.5-1.5B-Instruct), evidence gating, adaptive questioning, participant‑cluster analysis, McPHASES dataset, conversational administration, symptom clusters.
