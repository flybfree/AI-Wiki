# Summary: 2026-08-06_15-33-18Z_Audio_to_ScoreTranscriptionusingPre_trainedFeature.md
Saved: 2026-08-06 20:47
Source: 2026-08-06_15-33-18Z_Audio_to_ScoreTranscriptionusingPre_trainedFeature.md
Model: None

---

## Summary  
The paper introduces the SheetSage‑A2S dataset, a 61‑hour collection of pop‑music clips with kernel score encodings, and proposes an audio‑to‑score (A2S) system that leverages pre‑trained MuQ features together with data augmentation to improve performance on both classical and popular music. By combining these techniques, the authors achieve a 4.98 % symbol error rate on the Quartets collection for classical music and a 20.92 % SER on their new dataset, setting a strong benchmark for A2S research. The work also makes the model code publicly available.

## Key Contributions  
- **SheetSage‑A2S Dataset**: First large‑scale collection of popular‑music clips with kernel score encodings (61 h, 9,468 clips).  
- **MuQ Feature Extraction**: Utilizes a pre‑trained audio feature model to provide robust, domain‑agnostic descriptors.  
- **Data Augmentation + SER Improvement**: Combines augmentation strategies to boost generalisation and reduces symbol error rates on both classical (4.98 %) and popular music (20.92 %).

## Methodology  
The authors first preprocess each clip using MuQ to obtain a 32‑dimensional feature vector, then apply standard data‑augmentation pipelines such as pitch shifting, time stretching, and random cropping to enlarge the training set. These augmented features are fed into a convolutional neural network that predicts kernel scores sequentially, with attention mechanisms to focus on relevant audio segments.

## Results  
On the Quartets classical music benchmark, the proposed model reaches 4.98 % symbol error rate, outperforming the state‑of‑the‑art 15.3 % SER achieved by transformer‑based approaches. On the newly released SheetSage‑A2S dataset for popular music, it attains a 20.92 % SER, establishing a clear performance gap over existing methods and serving as a strong reference point.

## Significance  
This work bridges a long‑standing gap between classical A2S research and the rapidly growing interest in pop‑music transcription. By providing a comprehensive dataset and a model that works across genres, it enables future studies to evaluate and improve A2S systems with realistic data diversity.

## Related Concepts  
- Kernel score encoding  
- Data augmentation for audio  
- Pre‑trained music feature extraction (MuQ)
