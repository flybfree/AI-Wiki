# Summary: 2026-08-09_21-08-22Z_InvestigatingMultimodalInformativityunderDifferent.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_21-08-22Z_InvestigatingMultimodalInformativityunderDifferent.md
Model: None

---

## Summary  
The paper investigates how referential information conveyed through gestures in video‑mediated dialogue is interpreted under varying partner visibility conditions, aiming to improve multimodal dialogue models beyond transcript reliance. It contributes technical advances in modeling gesture‑speech fusion and insights into pragmatic effects of visibility on interaction.  

## Key Contributions  
- [Finding 1] Gesture alone can predict the intended referent in a video‑mediated communication game, demonstrating that nonverbal cues carry meaningful information.  
- [Finding 2] Multimodal fusion (gesture + speech) is most beneficial when the transcript‑based model is uncertain, showing synergy between modalities.  
- [Finding 3] Training‑only alignment of learned multimodal representations with the referent image further enhances performance, indicating a practical improvement to model training pipelines.  

## Methodology  
The authors construct three models: one using only the speech transcript, another using only skeletal gesture data, and a third that fuses both modalities. Participants engage in a video‑mediated referential communication game where they must point to an object described by their partner’s speech while performing gestures. The models are evaluated on their ability to correctly identify the intended referent across multiple interaction rounds under conditions of full visibility, partial visibility, and hidden partner.  

## Results  
The gesture‑only model achieves higher accuracy than the transcript‑only model, especially when visual cues are available. Fusion models outperform both single‑modal baselines when the transcript is ambiguous or noisy. Alignment training reduces error rates by up to 12 % compared with unaligned fusion models. Human interaction data reveal that visibility influences gesture production and informativeness, while speech and multimodal performance show entrainment across rounds, but gestures do not.  

## Significance  
These findings advance the technical modeling of human multimodal dialogue by showing how nonverbal information can compensate for transcript gaps and how model training can be optimized with referent‑aligned data. They also provide empirical evidence that visibility shapes pragmatic behavior in video communication, informing applications such as assistive technologies and social robotics.  

## Related Concepts  
- Multimodal fusion, referential communication, gesture informativeness, partner visibility, speech entrainment, training alignment, human interaction data, video‑mediated dialogue.
