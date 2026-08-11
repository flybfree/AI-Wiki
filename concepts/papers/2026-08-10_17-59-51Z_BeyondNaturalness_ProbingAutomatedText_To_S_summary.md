# Summary: 2026-08-10_17-59-51Z_BeyondNaturalness_ProbingAutomatedText_To_SpeechEv.md
Saved: 2026-08-11 00:03
Source: 2026-08-10_17-59-51Z_BeyondNaturalness_ProbingAutomatedText_To_SpeechEv.md
Model: None

---

## Summary  
The authors aim to move beyond the conventional “naturalness” judgment in automated Text‑to‑Speech (TTS) evaluation by analysing speech perception on ten linguistically grounded dimensions. They create a dimension‑level meta‑evaluation benchmark that quantifies how well different TTS evaluators capture these specific aspects of speech quality. The study demonstrates that existing MOS predictors and Audio‑Large Language Model judges fail to reflect the full spectrum of perceptual cues, revealing systematic weaknesses in current automated assessment methods.

## Key Contributions  
- [Finding 1] Mean Opinion Score (MOS) predictors collapse onto acoustic signal quality, indicating they cannot distinguish non‑acoustic linguistic errors.  
- [Finding 2] Audio‑LLM judges exhibit selective detection that depends on the prompt used and does not generalize across all ten perceptual dimensions.  
- [Finding 3] Neither class of evaluators reliably captures a breadth of linguistically structured speech errors, suggesting a need for more nuanced assessment.

## Methodology  
The researchers decompose “naturalness” into an annotation schema comprising ten distinct perceptual dimensions such as prosody, phoneme accuracy, and intelligibility. Using this schema they generate a dataset of 860 TTS utterances annotated by trained linguist raters who evaluate each utterance on the full set of dimensions. The benchmark then benchmarks four MOS predictors (e.g., frequency‑based models) and four Audio‑LLM judges (trained on audio‑text pairs) to measure their performance across these dimensions.

## Results  
Experimental results show that MOS predictors achieve high scores only when acoustic fidelity is high, confirming their reliance on signal quality rather than linguistic nuance. Audio‑LLM judges produce variable outputs: they excel at detecting certain prosodic cues under specific prompts but ignore other dimensions such as phoneme errors or rhythm deviations. Overall reliability of both classes drops sharply when evaluating the full spectrum of linguistic errors, underscoring a lack of holistic assessment.

## Significance  
By exposing the limited scope of existing TTS evaluation tools, this work pushes the field toward more interpretable, linguistically informed metrics that can guide system design and improve user experience. The publicly released dataset, annotation schema, and code enable researchers to build targeted evaluations that align with human perception rather than relying on a single “naturalness” label.

## Related Concepts  
- Naturalness (conventional TTS quality metric)  
- Mean Opinion Score (MOS) predictors  
- Audio‑Large Language Model (Audio‑LLM) judges  
- Linguistically grounded perceptual dimensions  
- Dimension‑level meta‑evaluation benchmark  
- Linguistic speech errors (phoneme, prosody, rhythm)
