# Summary: 2026-07-23_19-52-58Z_Khondo_AMultimodalBenchmarkforDocumentPacketSplitt.md
Saved: 2026-07-26 21:30
Source: 2026-07-23_19-52-58Z_Khondo_AMultimodalBenchmarkforDocumentPacketSplitt.md
Model: None

---

## Summary  
Khondo (Bangla for split/segment) presents the first multimodal, vision‑native benchmark for document packet splitting in the Bangla language. Unlike earlier English OCR‑text datasets, Khondo supplies bilingual (Bangla–English) page images and ground‑truth boundaries across five concatenation schemes and 14 administrative domains. Zero‑shot evaluation of large multimodal language models shows they can cluster pages into their source documents but often fail to reconstruct the original page order when packets are shuffled. The authors isolate ordering as the dominant difficulty, with English packets recovering more reliably than Bangla ones.

## Key Contributions  
- [Finding 1] Khondo introduces a comprehensive multimodal benchmark that is both bilingual and vision‑native for Bangla document packet splitting.  
- [Finding 2] Zero‑shot MLLMs perform well on clustering but struggle to restore the original page order in shuffled packets.  
- [Finding 3] The analysis demonstrates that ordering, not merely clustering, is the primary challenge; English packets are ordered more reliably than Bangla ones.

## Methodology  
The authors constructed a dataset containing 14 administrative domains with five concatenation schemes ranging from sequential to fully shuffled layouts. Ground‑truth boundaries, domain types, and page order are provided for each packet. To evaluate models, they performed zero‑shot testing of large multimodal language models (MLLMs) using two controlled analyses: varying the prompt instruction and then varying the packet language. This setup isolates whether ordering or clustering is affected by instruction wording or language choice.

## Results  
Zero‑shot MLLMs cluster pages into their source documents with moderate accuracy, but page‑order reconstruction is consistently poor, especially for Bangla packets. When prompts explicitly request “in original order,” performance improves modestly, yet English packets still outperform Bangla ones. The controlled analyses confirm that ordering dominates the difficulty and that language is a secondary factor.

## Significance  
Khondo establishes page‑order reconstruction as a key open problem in vision‑based, low‑resource document understanding and provides a controlled benchmark for measuring progress toward solving it. By exposing the systematic gap between clustering and ordering, the dataset guides future research on multimodal models that can handle both tasks simultaneously.

## Related Concepts  
- Document packet splitting  
- Multimodal learning (vision + language)  
- Zero‑shot evaluation  
- MLLMs (Large Multimodal Language Models)  
- Low‑resource language processing  
- Page ordering vs. clustering  
- Vision‑native versus OCR‑text approaches
