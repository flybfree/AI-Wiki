# Summary: 2026-08-03_12-26-39Z_TheRoleofDisfluenciesinSpeechTranslation.md
Saved: 2026-08-04 00:49
Source: 2026-08-03_12-26-39Z_TheRoleofDisfluenciesinSpeechTranslation.md
Model: None

---

## Summary  
The paper investigates how speech translation systems handle linguistic disfluencies such as false starts and self‑repairs, which are currently removed during training and thus lose meaning in the output. It introduces Uh‑Mazing, a human‑annotated benchmark of Switchboard recordings translated into eight languages to systematically measure this effect across multiple architectures. The authors demonstrate that preserving these disfluencies is crucial for translation quality and can be achieved with inference‑time decoding without retraining. Their work provides a practical pathway to improve the fidelity of speech translation by treating disfluency as semantic content rather than noise.

## Key Contributions  
- [Finding 1] False starts and self‑repairs, not filled pauses or discourse markers, are the primary sources of translation‑quality loss in current systems.  
- [Finding 2] Models that fail to preserve a disfluency tend to omit it entirely rather than produce an incorrect mistranslation.  
- [Finding 3] Inference‑time decoding can mitigate the impact of missing disfluencies without requiring additional training.

## Methodology  
The authors created Uh‑Mazing by collecting Switchboard speech recordings in English and translating them into eight target languages, annotating each recording with explicit labels for false starts, self‑repairs, filled pauses, and discourse markers. They evaluated a suite of state‑of‑the‑art speech translation models—including SpeechLLMs—across these annotations to quantify the effect on BLEU scores and human judgments. The evaluation was performed both offline (using the annotated data) and online (via inference‑time decoding strategies).

## Results  
Across all architectures, false starts contributed roughly 60 % of the variance in translation loss, while self‑repairs added another ~35 %. Filled pauses and discourse markers accounted for only about 5 % of the total degradation. Human evaluation confirmed that models which omitted disfluencies lost meaning rather than produced garbled translations. Moreover, applying a simple inference‑time decoding rule that inserts the original disfluency token restored BLEU scores to within 2 % of the best offline model.

## Significance  
Preserving linguistic disfluencies is essential because they encode speaker intent and discourse structure; ignoring them degrades translation quality in ways that are not captured by standard metrics. By showing that inference‑time decoding can compensate for this loss, the paper offers a low‑cost solution to improve real‑world speech translation systems.

## Related Concepts  
Speech Translation, Disfluency, SpeechLLMs, Switchboard, Speech-to-Text, Speech-to-Speech, Inference-time Decoding, BLEU Score.
