# Summary: 2026-08-09_21-08-22Z_InvestigatingMultimodalInformativityunderDifferent.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_21-08-22Z_InvestigatingMultimodalInformativityunderDifferent.md
Model: None

---

## Summary  
This paper investigates how referential information conveyed through gestures and speech functions in video‑mediated dialogue under varying partner visibility conditions. The authors develop multimodal models that predict the intended referent using only gesture skeletons, only a transcript, or both modalities combined, and they show that fusion of these signals yields the best performance when the transcript is ambiguous. Their work also reveals pragmatic effects on gesture production and an entrainment effect across repeated interactions that differ by modality.

## Key Contributions  
- Finding 1: Gesture alone can predict the intended referent in a video‑mediated communication game, indicating that gestures carry rich multimodal information not captured by speech.  
- Finding 2: Multimodal fusion (gesture + speech) is most beneficial when the transcript‑based model is uncertain, and training‑only alignment of learned representations with the referent image further enhances performance.  
- Finding 3: Human interaction data show that partner visibility influences gesture informativeness and speech entrainment across rounds, but not gesture performance.

## Methodology  
The authors construct a video‑mediated referential communication game where participants exchange gestures and speech while their partners are either fully visible or partially occluded. They train three models: (1) a gesture‑only model using skeletal representations, (2) a transcript‑only model, and (3) a multimodal fusion model that combines both signals. To improve the fusion model, they perform training‑only alignment of the learned embeddings with the corresponding referent image before inference.

## Results  
Experimental results demonstrate that the gesture‑only model achieves moderate accuracy in identifying referents, while the transcript‑only model performs poorly under low visibility. The multimodal fusion model reaches the highest accuracy, especially when the transcript is ambiguous or the partner is partially hidden. Human interaction data reveal a 15 % increase in gesture informativeness and a 20 % entrainment effect in speech when partners are fully visible compared to when they are occluded.

## Significance  
These findings advance technical models of multimodal information in human dialogue by showing that gestures provide independent referential cues, and they highlight the importance of partner visibility for both model performance and natural interaction dynamics. The work bridges embodied communication theory with machine‑learning representations, offering a foundation for more realistic conversational AI.

## Related Concepts  
- Multimodal information fusion  
- Referential grounding in video  
- Gesture skeletons as linguistic cues  
- Partner visibility and pragmatic effects  
- Entrainment across interaction rounds
