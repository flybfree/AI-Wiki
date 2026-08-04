# Summary: 2026-08-02_11-52-46Z_DoesMachine_know_interpersonalpragmatics_Evidencef.md
Saved: 2026-08-03 23:26
Source: 2026-08-02_11-52-46Z_DoesMachine_know_interpersonalpragmatics_Evidencef.md
Model: None

---

## Summary  
The paper investigates whether Transformer‑based models can learn emoji pragmatics in Arabic digital discourse, focusing on MARBERT’s ability to capture interpersonal pragmatic functions (IPFs). It contributes a computational framework for modeling face‑management and relational communication through the use of emojis. The study provides empirical evidence that MARBERT achieves high accuracy on unseen data, showing strong performance beyond conventional sentiment analysis.

## Key Contributions  
- [Finding 1] MARBERT learns five IPFs—Politeness, Respect, Solidarity, Empathy, and Encouragement—with overall accuracy of 93%, micro‑F1 = 0.61, macro‑F1 = 0.56.  
- [Finding 2] Politeness and Respect are identified more accurately than Solidarity, indicating differences in explicitness and contextual dependence of these functions.  
- [Finding 3] The mixed‑method approach combining statistical analysis with speech act theory yields interpretable insights into how emoji serve pragmatic purposes.

## Methodology  
A corpus of 8,504 unique emoji‑posted messages was collected from Facebook via Python and manually annotated to label the five IPFs. MARBERT, a Transformer model fine‑tuned on this annotated data, was evaluated using standard classification metrics (accuracy, micro‑F1, macro‑F1) and interpretive analysis grounded in politeness theory, speech act theory, and rapport management theory.

## Results  
The model achieved 93 % accuracy, micro‑F1 = 0.61, macro‑F1 = 0.56 on a held‑out test set. Function‑level evaluation revealed Politeness (≈84 %) and Respect (≈78 %) highest scores, while Solidarity was lower (≈62 %). These results demonstrate that MARBERT captures explicit pragmatic cues but struggles with implicit social meanings.

## Significance  
This work bridges NLP and interpersonal communication research by showing Transformers can model emoji pragmatics, offering a computational lens for studying face‑saving strategies in Arabic digital interaction. It also highlights the gap between learned patterns and highly implicit social meanings, informing future multimodal models.

## Related Concepts  
Emoji pragmatics; Interpersonal pragmatic functions (IPFs); Face management; Speech act theory; Politeness theory; Rapport management; Transformer fine‑tuning; Digital discourse analysis.
