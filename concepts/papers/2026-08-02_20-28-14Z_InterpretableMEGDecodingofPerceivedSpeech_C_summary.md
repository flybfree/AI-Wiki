# Summary: 2026-08-02_20-28-14Z_InterpretableMEGDecodingofPerceivedSpeech_Cortical.md
Saved: 2026-08-04 00:19
Source: 2026-08-02_20-28-14Z_InterpretableMEGDecodingofPerceivedSpeech_Cortical.md
Model: None

---

## Summary  
The authors aim to create a MEG decoding system that can retrieve short spoken segments from non‑invasive magnetoencephalographic recordings by training a deep network on wav2vec 2.0 audio embeddings, while simultaneously mapping the learned weights onto cortical sources and identifying which speech properties drive retrieval. Their contribution is an interpretable architecture that replaces flat spatial attention with spherical harmonics defined on 3‑D MEG geometry, reduces subject‑specific branches to 25, adds temporal filters for source matching, and employs a shallower convolutional decoder. The model achieves 39.75 ± 0.34 % Top‑1 accuracy among 1005 candidates with far fewer parameters than prior MEG‑to‑audio decoders, and its weights recover generators consistent with the speech‑perception network.  

## Key Contributions  
- [Finding 1] The spherical‑harmonic spatial attention maps directly to cortical source locations, enabling interpretable weight interpretation.  
- [Finding 2] Fifteen of nineteen stimulus features (silence, intensity, vowels, acoustic onsets) drive retrieval, while narrative MEG is less recoverable than coherent speech activity.  
- [Finding 3] The wav2vec target can be compressed to ~12 learned dimensions without accuracy loss, whereas excessive temporal compression degrades performance.  

## Methodology  
The authors built on a high‑performing MEG‑to‑audio retrieval architecture but redesigned both front and decoder sections. Spatial attention is replaced by spherical harmonics that respect the 3‑D MEG helmet geometry, reducing subject‑specific branches from 270 to 25. Each branch receives a temporal filter matched to a neuronal source in space and time, and the convolutional decoder is made shallower. Ocular and cardiac components are removed before training to avoid stimulus‑locked shortcuts.  

## Results  
On MEG‑MASC, the model reaches 39.75 ± 0.34% Top‑1 accuracy among 1005 candidates across six trained solutions, using about 20 times fewer decoder parameters than earlier approaches. Weight mapping reveals generators aligned with speech‑perception networks; left‑lateralized branches encode higher‑frequency rhythmic components absent on the right. Paired MEG occlusion shows that 15 stimulus features contribute most strongly (silence, sound intensity, vowels, acoustic onsets). Random word lists show that narrative‑structured MEG yields better retrieval than narrative‑free activity, indicating less recoverable information without coherent speech structure. Reducing wav2vec to ~12 dimensions retains accuracy, while strong temporal compression causes a clear loss.  

## Significance  
This work demonstrates that interpretable MEG decoding can simultaneously recover cortical sources and pinpoint stimulus features that drive retrieval, offering a bridge between deep learning and neurophysiology. By reducing model complexity and eliminating non‑speech artifacts, the method is more robust to noise and easier to validate experimentally. The identified feature set provides biological insight into which auditory properties are most salient for perception, potentially informing clinical MEG applications such as language disorder detection.  

## Related Concepts  
MEG decoding, CLIP‑style objective, wav2vec 2.0 embeddings, spherical harmonics, source mapping, temporal filtering, subject‑specific branches, attention mechanisms, occlusion experiments, narrative vs. non‑narrative speech activity.
