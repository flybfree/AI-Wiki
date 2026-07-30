# Summary: 2026-07-29_04-55-14Z_Audio_AnchoredFusionofMulti_RatioDiTReconstruction.md
Saved: 2026-07-29 21:34
Source: 2026-07-29_04-55-14Z_Audio_AnchoredFusionofMulti_RatioDiTReconstruction.md
Model: None

---

## Summary  
The paper proposes an audio‑anchored fusion framework that leverages multi‑ratio DiT reconstruction residuals to improve cross‑domain deepfake detection. It freezes a Diffusion Transformer (DiT) trained only on bona fide speech, extracts residual maps at masking ratios 0.5, 0.75 and 0.9, and integrates them with the projected WavLM auditory representation without gating. The approach yields competitive EER/DCF scores on both ASVspoof 5 Eval (supervised) and ITW Full (unsupervised), outperforming a separately optimized WavLM‑ResNet18 baseline.

## Key Contributions  
- Multi‑ratio DiT reconstruction residuals provide domain‑sensitive evidence that complements the frozen auditory representation.  
- Audio‑anchored fusion integrates the projected WavLM features with scalar‑gated additive correction, avoiding gate‑based attenuation.  
- Experimental results demonstrate lower EER/DCF than a separately optimized WavLM‑ResNet18 reference and competitive performance under cross‑domain transfer.

## Methodology  
The authors train DiT exclusively on authentic speech utterances, then freeze the model as a reconstruction probe. Using three masking ratios (0.5, 0.75, 0.9) they generate explicit residual maps that encode how well the diffusion process can reconstruct each segment of the audio. The frozen WavLM representation is projected into the fusion sum and the residuals are added as scalar corrections; no attention gates modulate this addition. The fused signal is evaluated on ASVspoof 5 Eval (supervised) and ITW Full (unsupervised) to assess detection performance.

## Results  
Seed‑42 runs achieve 6.5442 % EER / 0.18456 min‑DCF on ASVspoof 5 Eval and 13.8372 % / 0.36921 on ITW Full; three‑seed means are 6.8885 (0.3308 %) and 15.3328 (2.0719 %). When auxiliary supervision is added, the competitive fusion improves to a mean ITW EER of 25.2968 %. These results show that the reconstruction residuals contribute meaningfully to detection accuracy.

## Significance  
The work shows that reconstruction residuals can serve as complementary evidence to auditory embeddings, enabling non‑competitive cross‑domain transfer without relying on gated attention mechanisms. This opens a promising path for robust deepfake detection across varying generators and recording conditions.

## Related Concepts  
Diffusion Transformer (DiT), WavLM, residual maps, multi‑ratio masking, audio‑anchored fusion, cross‑domain evaluation, EER/DCF metrics.
