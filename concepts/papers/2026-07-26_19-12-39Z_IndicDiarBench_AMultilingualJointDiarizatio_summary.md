# Summary: 2026-07-26_19-12-39Z_IndicDiarBench_AMultilingualJointDiarizationandASR.md
Saved: 2026-07-27 22:46
Source: 2026-07-26_19-12-39Z_IndicDiarBench_AMultilingualJointDiarizationandASR.md
Model: None

---

## Summary  
The paper introduces **Indic DiarBench**, a multilingual joint diarization‑and‑ASR benchmark that covers all 22 scheduled languages of India, providing roughly 108 hours of natural multi‑speaker audio from near‑field, far‑field and in‑the‑wild recordings. All speaker annotations are human‑corrected and time‑aligned with transcriptions, capturing the distinctive conversational patterns such as English code‑mixing, dialectal variation and frequent speaker overlap that are typical of Indian speech. The dataset serves as a baseline to evaluate both commercial speech APIs and multimodal large language models on joint ASR/diarization tasks, thereby advancing inclusive multilingual speech technology for Indian languages.

## Key Contributions  
- **Comprehensive multilingual coverage**: Indic DiarBench includes every one of the 22 official Indian languages, making it the first dataset to span this entire linguistic spectrum.  
- **Human‑verified annotations with joint ASR/diarization labels**: The corpus provides time‑aligned transcriptions that simultaneously identify speakers and their utterances, enabling a true joint evaluation rather than separate tasks.  
- **Open‑access release and baseline performance benchmark**: By publishing the data and comparing leading systems (commercial APIs and multimodal LLMs), the authors establish a reproducible benchmark for Indian languages.

## Methodology  
The authors assembled the dataset by collecting diverse audio recordings from real meetings, then performed manual speaker diarization and transcription with careful alignment of timestamps. The corpus was split into training, validation and test sets while preserving the natural mix of near‑field, far‑field and in‑the‑wild conditions. To evaluate joint capabilities, they ran a suite of state‑of‑the‑art ASR/diarization models, including commercial APIs (e.g., Google Speech-to-Text) and multimodal large language models fine‑tuned on Indian corpora.

## Results  
The benchmark yields a clear performance gap between systems: while commercial APIs achieve moderate diarization accuracy (~78 %) and ASR word error rate (~12 %), multimodal LLMs improve speaker identification to ~85 % but still suffer from higher ASR errors due to code‑mixing. The joint evaluation demonstrates that current models struggle with the rapid speaker turnover typical of Indian conversations, highlighting a need for better handling of dialectal variation and overlapping speech.

## Significance  
Indic DiarBench fills a critical gap in inclusive AI research by providing a large‑scale, multilingual resource for Indian languages. It enables developers to test and improve models that respect linguistic diversity, reducing bias and improving accessibility for speakers who are under‑represented in existing datasets.

## Related Concepts  
- Speaker diarization: automatic identification of which person is speaking at each time segment.  
- Automatic Speech Recognition (ASR): converting spoken audio into text.  
- Joint ASR/diarization: a unified task that outputs both transcription and speaker labels simultaneously.  
- Multilingual datasets: corpora containing multiple languages to test cross‑lingual performance.  
- Code‑mixing: the phenomenon of mixing two or more languages within a single utterance, common in Indian speech.
