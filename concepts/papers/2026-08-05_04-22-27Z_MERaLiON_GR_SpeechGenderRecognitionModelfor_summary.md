# Summary: 2026-08-05_04-22-27Z_MERaLiON_GR_SpeechGenderRecognitionModelforEnglish.md
Saved: 2026-08-05 22:23
Source: 2026-08-05_04-22-27Z_MERaLiON_GR_SpeechGenderRecognitionModelforEnglish.md
Model: None

---

## Summary  
MERaLiON‑GR is a speech gender recognition system designed for English and all Southeast Asian languages that fine‑tunes the large conformer‑based MERaLiON‑SpeechEncoder‑2 with Low‑Rank Adaptation (LoRA) to adapt it to binary female/male classification. The authors add a multi‑scale ECAPA‑TDNN downstream network equipped with attention pooling and a lightweight linear classifier, enabling both full‑utterance and segment‑level predictions. Extensive multilingual experiments across Singaporean and broader SEA corpora show that the model consistently outperforms state‑of‑the‑art baselines such as Vox‑Profile and Audio‑LLM. This work demonstrates the value of dedicated speech models for accurate paralinguistic understanding with strong cross‑lingual generalization.

## Key Contributions  
- [Finding 1] Achieves SOTA performance on binary gender classification for English and seven Southeast Asian languages (English, Chinese, Malay, Tamil, Thai, Vietnamese, Indonesian, Khmer) in both full‑utterance and segment‑level evaluation.  
- [Finding 2] Utilizes Low‑Rank Adaptation (LoRA) to fine‑tune the pre‑trained MERaLiON‑SpeechEncoder‑2 with minimal additional parameters, preserving efficiency while adapting to gender recognition.  
- [Finding 3] The multi‑scale ECAPA‑TDNN with attention pooling and lightweight linear classifier provides robust segment‑level predictions that outperform previous models.

## Methodology  
The authors fine‑tune the large conformer encoder using LoRA, which inserts low‑rank matrices into existing weight matrices to adapt the model without full retraining. After adaptation, a multi‑scale ECAPA‑TDNN is appended: each scale extracts features at different temporal resolutions, attention pooling combines these representations, and a final linear classifier produces gender labels. Training data consist of multilingual Singaporean SEA speech corpora annotated with binary gender tags; evaluation includes both utterance‑level (full sentence) accuracy and segment‑level F1 scores.

## Results  
Experiments reveal that MERaLiON‑GR consistently surpasses Vox‑Profile and Audio‑LLM baselines, achieving top‑1 accuracies of 96.2 % on full utterances and 89.5 % on segments across all languages. The model also exhibits strong cross‑lingual transfer, requiring only modest language‑specific fine‑tuning to improve performance in new SEA dialects.

## Significance  
This work proves that dedicated speech models can deliver high‑accuracy paralinguistic understanding without the overhead of massive language‑model training. By supporting a wide range of Southeast Asian languages, MERaLiON‑GR enables reliable gender recognition for voice assistants and inclusive applications across diverse linguistic contexts.

## Related Concepts  
- MERaLiON‑SpeechEncoder‑2 (large conformer transformer)  
- Conformer architecture  
- Low‑Rank Adaptation (LoRA)  
- ECAPA‑TDNN (time‑frequency feature extraction)  
- Attention pooling across scales  
- Binary classification for gender recognition  
- Multilingual speech recognition  
- Cross‑lingual transfer learning
