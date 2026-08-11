# Summary: 2026-08-10_17-59-51Z_BeyondNaturalness_ProbingAutomatedText_To_SpeechEv.md
Saved: 2026-08-11 00:19
Source: 2026-08-10_17-59-51Z_BeyondNaturalness_ProbingAutomatedText_To_SpeechEv.md
Model: None

---

## Summary  
The paper seeks to move beyond the conventional Mean Opinion Score (MOS) evaluation of Text‑to‑Speech (TTS) by proposing a linguistically grounded annotation schema that isolates ten distinct perceptual dimensions of naturalness. By constructing the first dimension‑level meta‑evaluation benchmark—comprising 860 utterances rated by trained linguist raters—the authors evaluate how well existing MOS predictors and Audio Large Language Model (Audio‑LLM) judges capture these specific linguistic aspects. The study reveals that conventional metrics collapse onto acoustic quality, while AI judges are selective and prompt‑dependent, failing to generalize across the full spectrum of linguistic dimensions.

## Key Contributions  
- [Finding 1] A linguistically grounded annotation schema with ten perceptual dimensions is introduced as the first dimension‑level meta‑evaluation benchmark for TTS.  
- [Finding 2] MOS predictors collapse onto acoustic signal quality rather than reflecting broader linguistic aspects of naturalness.  
- [Finding 3] Audio‑LLM judges exhibit selective, prompt‑dependent detection that does not generalize across all dimensions.

## Methodology  
The authors assembled a dataset of 860 TTS utterances annotated by linguist raters using the ten‑dimensional schema. They compared four standard MOS predictors and four Audio‑LLM models on this benchmark to assess their ability to evaluate each linguistic dimension independently.

## Results  
MOS predictors showed strong correlations with acoustic quality metrics such as pitch stability and energy variance but weak or negligible correlations with linguistic dimensions like phonotactic errors, prosodic flow, and lexical stress. In contrast, Audio‑LLM judges performed variably: they excelled on specific prompts related to certain dimensions yet produced inconsistent scores across the schema, indicating a lack of generalisation.

## Significance  
By decoupling naturalness into interpretable linguistic components, this work enables targeted improvements in TTS systems and provides a framework for future research that can diagnose where evaluation tools fall short. The publicly released dataset, annotation schema, and code facilitate reproducible, dimension‑aware studies.

## Related Concepts  
Naturalness, Mean Opinion Score (MOS), Audio Large Language Model (Audio‑LLM), linguistic grounding, perceptual dimensions, meta‑evaluation benchmark, linguist raters, phonotactic errors, prosody, lexical stress.
