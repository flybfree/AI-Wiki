# Summary: 2026-08-06_14-27-46Z_SignalorSpuriousCue_ARandomizedAuditofSurvey_Count.md
Saved: 2026-08-06 22:17
Source: 2026-08-06_14-27-46Z_SignalorSpuriousCue_ARandomizedAuditofSurvey_Count.md
Model: None

---

## Summary  
The paper investigates whether survey‑country metadata serves as a genuine signal for LLM social inference or merely as a spurious cue that can mislead models when randomly assigned. It conducts a randomized audit to test if uniform, record‑independent origins of labels reduce country‑directed uptake and improve Brier loss. The study evaluates five fixed API models across six countries on seven development‑selected targets using paired data from 14 400 item‑level probability distributions.

## Key Contributions  
- Finding 1: Disclosing that random labels were uniformly generated reduces the country‑specific direction of inference by a small but statistically significant amount (paired attenuation = 0.0003).  
- Finding 2: Verified survey‑country metadata lowers held‑out Brier loss by 0.040, indicating genuine utility beyond random noise.  
- Finding 3: Random‑label regret is zero, suggesting that using uniformly generated labels does not harm performance.

## Methodology  
The authors designed a within‑record audit where each participant’s response was paired with two label assignments—one opaque (treated as the survey country) and one disclosed‑random (uniformly generated). They measured changes in forecast direction and Brier loss across five fixed LLM models, six countries, and seven development‑selected targets. Data came from a 72‑record post‑review panel and a non‑overlapping mixed‑coverage consistency panel.

## Results  
In the primary post‑review panel, opaque labels produced country‑direction shifts of 0.214; disclosed‑random labels attenuated this to 0.0003 (95 % CI [-0.0157, 0.0166]). Verified country reduced Brier loss by 0.040 (95 % CI [0.024, 0.056]), while random‑label regret was zero. The mixed‑coverage panel retained positive disclosed‑random movement and verified utility, though attenuation remained uncertain.

## Significance  
These findings clarify that survey‑country metadata is not a reliable signal for social inference; its value depends on verification, and random labels do not degrade performance but may obscure true signals.

## Related Concepts  
LLM social inference, Brier loss, survey metadata, random labeling, within‑record audit, mixed‑coverage consistency, API model forecasting.
