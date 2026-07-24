# Summary: 2026-07-23_17-25-08Z_DONDO_Openw2v_BERTSpeech_RecognitionBaseModelsforA.md
Saved: 2026-07-24 03:12
Source: 2026-07-23_17-25-08Z_DONDO_Openw2v_BERTSpeech_RecognitionBaseModelsforA.md
Model: None

---

## Summary  
The paper introduces DONDO, a family of open automatic speech recognition (ASR) base models for African languages built on the w2v‑BERT 2.0 self‑supervised speech encoder. It provides both monolingual and multilingual models that are fine‑tuned primarily on read speech drawn from religious texts, which offer broad, license‑clear coverage for languages lacking transcribed audio. A two‑step learning‑rate‑annealed fine‑tuning procedure is employed to adapt a shared multilingual model, and a lightweight language‑conditioning mechanism injects a one‑hot language identity as prefix frames at inference. All models are released on Hugging Face under the Apache‑2.0 license (attribution only) so they can be used freely for commercial purposes.

## Key Contributions  
- Finding 1: The w2v‑BERT 2.0 encoder enables high‑quality speech representation for African languages with limited annotated data.  
- Finding 2: Learning‑rate‑annealed fine‑tuning improves performance, especially when adapting shared multilingual models to individual languages.  
- Finding 3: A one‑hot language prefix conditioning allows a single multilingual checkpoint to serve multiple African languages at inference.

## Methodology  
The authors built DONDO by first training the w2v‑BERT 2.0 encoder on read speech from religious texts that are orthographically consistent across the target languages, ensuring reliable acoustic‑text alignment. They then fine‑tuned this shared multilingual model using a two‑step learning‑rate schedule: an initial high learning rate for rapid adaptation followed by a gradual reduction to refine predictions; additionally, they prepended a one‑hot vector representing the language as prefix frames to the acoustic features to condition the output. This lightweight mechanism avoids large parameter overhead while enabling language selection at runtime.

## Results  
Across five multilingual families covering twenty‑seven language varieties in Ghana, Sierra Leone, Nigeria, Senegal, Kenya and Zimbabwe, the annealed models achieve an average word error rate (WER) of 10–13%, which is comparable to strong monolingual baselines and reduces the gap between them. The multilingual checkpoint covers roughly one hundred million first‑language speakers, with second‑language use expanding that figure substantially. All models are publicly available on Hugging Face via the KhayaAI organization under an Apache‑2.0 license (attribution only).

## Significance  
This work provides a scalable, open foundation for ASR in African languages that lack large annotated corpora, allowing researchers and developers to build high‑quality speech recognition tools without costly data collection. By offering a multilingual checkpoint with lightweight language conditioning, it reduces deployment complexity and cost, fostering broader adoption of AI solutions across the region.

## Related Concepts  
- w2v‑BERT 2.0 self‑supervised speech encoder  
- automatic speech recognition (ASR)  
- African languages  
- orthographically consistent read speech from religious texts  
- learning‑rate annealing fine‑tuning  
- language‑conditioning via one‑hot prefix frames  
- Apache‑2.0 licensing
