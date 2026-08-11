# Summary: 2026-08-10_05-24-39Z_WhenLatentsForgetPixels_RestoringFidelityinDiffusi.md
Saved: 2026-08-10 23:37
Source: 2026-08-10_05-24-39Z_WhenLatentsForgetPixels_RestoringFidelityinDiffusi.md
Model: None

---

## Summary  
The paper addresses a persistent weakness in diffusion‑transformer based image super‑resolution: latent representations obtained from VAE compression discard fine‑grained pixel evidence, causing hallucinations that are not anchored to the original low‑resolution (LR) image. The authors introduce Pixel‑Grounded Super‑Resolution (PGSR), a framework that preserves LR‑observed pixels before VAE encoding and reuses them during restoration, thereby restoring visual fidelity while retaining perceptual quality. By conditioning both the latent trajectory and the decoder on explicit pixel cues, PGSR mitigates the “latent forgets pixels” problem without retraining large pretrained models. The approach is lightweight, compatible with existing DiT backbones, and scales efficiently to high‑resolution outputs.

## Key Contributions  
- [Finding 1] A novel Pixel‑Grounded Super‑Resolution (PGSR) framework that extracts pre‑VAE pixel evidence from the LR image and reuses it at both the conditioning and decoding stages.  
- [Finding 2] Condition‑Side Trajectory Guidance, which fuses LR‑derived pixel evidence with the latent LR condition to steer the diffusion trajectory toward faithful reconstruction.  
- [Finding 3] Decoder‑Side Pixel Grounding, which injects multi‑scale pixel features into a frozen VAE decoder to enforce visual consistency with the original observation.

## Methodology  
The authors adopt a representation‑level view of generative super‑resolution: first, they generate an upsampled LR image and extract its pixel embeddings before feeding it through a VAE encoder. The latent output is then conditioned on both the compressed code (as in standard diffusion) and the original pixel evidence via the Condition‑Side Trajectory Guidance module. At generation time, the frozen VAE decoder receives these pixel cues through Decoder‑Side Pixel Grounding, ensuring that high‑frequency details are not lost. To keep training efficient, only lightweight restoration modules—local‑window attention layers—are trained; the latent autoencoder and main flow‑matching backbone remain untouched.

## Results  
Experimental evaluation on standard SR benchmarks shows PGSR outperforms prior latent diffusion methods in both realism and fidelity metrics (PSNR, SSIM) while maintaining perceptual quality. The trade‑off between realism and fidelity is markedly improved: hallucinated details are reduced by up to 38 % compared with baseline models, and visual inspection reveals a higher proportion of correctly grounded textures and edges. Ablation studies confirm that the two key modules (Condition‑Side Guidance and Decoder‑Side Grounding) are essential for achieving these gains.

## Significance  
PGSR demonstrates that preserving pixel evidence throughout the latent pipeline is critical for high‑fidelity generative super‑resolution, addressing a longstanding limitation of diffusion transformers. By integrating lightweight modules into existing pretrained models, it offers a practical path to more faithful image restoration without prohibitive computational cost.

## Related Concepts  
- Diffusion Transformer (DiT) – a latent diffusion model that operates on compressed VAE representations.  
- Variational Autoencoder (VAE) compression bottleneck – the loss of fine‑grained spatial information during encoding/decoding.  
- Pixel‑grounded super‑resolution – a strategy that retains original pixel cues to guide generation.  
- Local‑window attention – an efficient attention variant for high‑resolution diffusion tasks.
