# Summary: 2026-08-02_20-28-14Z_InterpretableMEGDecodingofPerceivedSpeech_Cortical.md
Saved: 2026-08-04 00:22
Source: 2026-08-02_20-28-14Z_InterpretableMEGDecodingofPerceivedSpeech_Cortical.md
Model: None

---

## Summary  
The paper aims to decode perceived speech from non‑invasive magnetoencephalographic (MEG) recordings using a deep network trained with a CLIP objective against wav2vec 2.0 audio embeddings, while making the mapping interpretable by linking network weights to specific cortical sources and stimulus features. It redesigns both the front‑end spatial attention and decoder architecture to operate on spherical harmonics defined on the three‑dimensional MEG helmet geometry and reduces subject‑specific branches. The approach eliminates ocular and cardiac components to avoid stimulus‑locked shortcuts. On the MEG‑MASC dataset, the model reaches 39.75 ± 0.34% Top‑1 accuracy with roughly twenty times fewer decoder parameters than prior approaches.  

## Key Contributions  
- The authors develop an interpretable MEG decoding architecture that maps network weights onto cortical source space.  
- They identify fifteen of nineteen stimulus features as driving retrieval, highlighting silence, sound intensity, vowels, and acoustic onsets as the most influential.  
- Their design reduces decoder parameters by about twenty‑times while maintaining high accuracy.  

## Methodology  
The authors start from a high‑performing MEG‑to‑audio retrieval model. They replace the flattened sensor spatial attention with spherical harmonics defined on 3D MEG geometry, reducing subject‑specific representation to 25 branches and adding per‑branch temporal filters aligned to source locations. Convolutional decoder depth is reduced, and ocular/cardiac components are removed before training.  

## Results  
On the MEG‑MASC dataset across six trained solutions, Top‑1 accuracy reaches 39.75 ± 0.34% with about twenty times fewer decoder parameters than previous models. Source mapping reveals left‑lateralized branches encode higher‑frequency rhythmic components absent on the right. Paired occlusion experiments confirm that narrative MEG outperforms random word lists, showing coherent speech carries more recoverable information.  

## Significance  
This work bridges deep learning and neurophysiology by providing a transparent decoding pipeline that links neural activity to specific cortical generators and stimulus properties, offering a foundation for personalized auditory perception research.  

## Related Concepts  
- MEG (magnetoencephalography)  
- wav2vec 2.0  
- CLIP objective  
- Spherical harmonics on 3D sensor geometry  
- Source space mapping of neural weights  
- Top‑1 accuracy in retrieval tasks  
- Occlusion experiments comparing narrative vs random word lists  
- Removal of ocular and cardiac artifacts
