# Summary: 2026-07-28_11-00-28Z_Matrix_FreePhotoacousticImageReconstructionviaSens.md
Saved: 2026-07-28 22:43
Source: 2026-07-28_11-00-28Z_Matrix_FreePhotoacousticImageReconstructionviaSens.md
Model: None

---

## Summary  
Photoacoustic tomography (PAT) fuses optical absorption contrast with ultrasound spatial resolution, yet reconstructing the pressure field from sparse sensor measurements is an ill‑posed inverse problem that traditionally requires the system matrix at inference. This work introduces the Sensor Attention Network (SAN), a transformer architecture that treats each full time series as a token and maps raw measurements directly to the image without forming or inverting the H‑matrix. By bypassing the costly matrix computation, SAN enables real‑time reconstruction suitable for clinical PAT. The network is trained using an analytical k‑space H‑matrix and benchmarked against standard solvers on matched geometry.

## Key Contributions  
- [Finding 1] SAN reconstructs images from sparse PAT data without explicitly forming the system matrix, leveraging tokenized time series as input to a self‑attention transformer.  
- [Finding 2] The network achieves superior reconstruction fidelity (SSIM 0.522, PSNR 22.09 dB, NMSE 0.233) compared with ISTA, split‑Bregman TV, and LISTA on held‑out data.  
- [Finding 3] SAN reduces reconstruction time by at least an order of magnitude because inference is matrix‑free.

## Methodology  
The authors construct an analytical k‑space H‑matrix for a matched geometry to serve as the ground truth for training. They augment this dataset with vessel weighting and generate 488 samples, then train SAN on these examples using a sensor‑token self‑attention architecture that directly maps raw measurements to reconstructed images. Evaluation is performed on 46 held‑out samples against ISTA, split‑Bregman total variation (SBTV), and learned ISTA (LISTA).

## Results  
The mean per‑sensor Pearson correlation is 0.919 ± 0.049, with an energy‑normalized mismatch reduced by 49% using k‑space apodization and Gaussian temporal damping. SAN outperforms all baselines: highest SSIM (0.522), PSNR (22.09 dB) and lowest NMSE (0.233). Paired t‑tests and Wilcoxon signed‑rank tests confirm superiority over LISTA on PSNR, NMSE, and Pearson correlation at p < 1e‑8, and over ISTA and SBTV across all metrics. Reconstruction time is reduced by roughly tenfold.

## Significance  
SAN provides a matrix‑free, real‑time reconstruction pathway for PAT that preserves high image quality while dramatically lowering computational load, making it feasible to deploy on clinical devices or edge processors where latency is critical.

## Related Concepts  
Photoacoustic tomography, compressive sensing, iterative reconstruction (ISTA), split Bregman total variation (SBTV), learned ISTA (LISTA), transformer self‑attention, tokenization of time series, sensor attention network, k‑space H‑matrix, apodization, Gaussian temporal damping.
