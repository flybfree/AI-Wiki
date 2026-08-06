# Summary: 2026-08-05_02-38-20Z_HelpingMusicCo_CreationAgents_Listen_Well_Hierarch.md
Saved: 2026-08-05 20:28
Source: 2026-08-05_02-38-20Z_HelpingMusicCo_CreationAgents_Listen_Well_Hierarch.md
Model: None

---

## Summary  
The paper proposes a hierarchical self‑supervised world model that enables a music co‑creation agent to “listen” and generate symbolic piano‑roll data without any external labels or music‑theory vocabulary. By training a 2.55 M‑parameter Swin V2 encoder on MIDI images with JEPA‑style objectives, the system learns representations where phrase boundaries are captured at coarse levels while harmonic detail is encoded at fine levels. A conditional flow‑matching decoder reproduces target windows with F1 ≈ 0.996 and allows graphical prompting for masked inpainting. The pipeline runs on CPU in 2.8 s (Apple MPS in 0.6 s), delivering real‑time suggestions that augment rather than replace human agency.

## Key Contributions  
- [Finding 1] A hierarchical world model decodes musical properties at different spatial scales: phrase boundaries emerge from the coarsest encoder levels, while note density and harmonic detail are encoded on finer levels.  
- [Finding 2] The self‑supervised objectives (pitch‑time equivariance, masked embedding prediction, distributional regularizer) capture temporal and phrase structure without any labeled data or music‑theory vocabulary.  
- [Finding 3] Adding a small chord‑supervision head lifts joint chord recovery from .18 to .54 and key detection from .16 to .70, showing how targeted supervision can boost specific capabilities.

## Methodology  
The authors build a symbolic music world model by first encoding MIDI piano‑roll images with a Swin V2 encoder using only JEPA‑style self‑supervised objectives—no external labels are required. The hierarchical architecture ensures that coarse levels capture macro‑level temporal cues (phrases) while fine levels retain harmonic nuance. For generation, they employ a conditional flow‑matching decoder whose conditioning is derived from PCA‑reduced latent space; per‑level dropout controls how much the output can vary, enabling both pixel‑wise reconstruction and graphical prompting for masked inpainting without a dedicated inpainting sampler.

## Results  
The model contains 2.55 million parameters and achieves an F1 of 0.996 on pixel‑space reconstruction. With chord supervision, joint chord recovery improves to .54 (from .18) and key detection reaches .70 (from .16). The full pipeline runs in 2.8 seconds on a CPU and only 0.6 seconds on an Apple MPS, supporting live interactive demos where the agent suggests musical actions in real time.

## Significance  
By providing a low‑latency, self‑supervised representation that aligns with human perception of music, this work creates a collaborative co‑creation framework that respects user agency. The efficient decoding and generation pipeline enables agents to act as supportive assistants rather than autonomous creators, opening new possibilities for interactive music experiences.

## Related Concepts  
- Hierarchical world models  
- Self‑supervised representation autoencoders (e.g., JEPA)  
- Flow matching decoders with conditional conditioning  
- Symbolic music representation using MIDI piano‑roll images  
- Conditional inpainting and graphical prompting
