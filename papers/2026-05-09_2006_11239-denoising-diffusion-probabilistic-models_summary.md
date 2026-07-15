---
title: "Summary: Denoising Diffusion Probabilistic Models"
date: 2026-05-09
tags: ['paper', 'research', 'ai']
---
# Summary: Denoising Diffusion Probabilistic Models


**Source**: [Original Paper](https://arxiv.org/abs/2006.11239)
Saved: 2026-05-09 23:00
Source: 2026-05-09_2006.11239-denoising-diffusion-probabilistic-models.md
Model: None

---


## Summary  
Denoising Diffusion Probabilistic Models (DDPM) propose a generative framework that learns to reverse a gradual Gaussian‑noise addition process, allowing high‑quality image synthesis by iteratively denoising random noise rather than producing an image in one shot. This approach delivers greater stability, higher fidelity, and richer diversity compared with earlier GAN‑based methods.

## Key Contributions  
- DDPM defines a probabilistic generative framework where the forward process adds Gaussian noise step‑by‑step and the reverse process learns to remove it.  
- The model generates high‑fidelity images by iteratively denoising noisy representations over 100–1000 steps, achieving state‑of‑the‑art image quality.  
- DDPM’s stability and ease of training make diffusion models a robust alternative to GANs, paving the way for text‑to‑image generation.

## Methodology  
The authors model data as a Markov chain: each forward step adds Gaussian noise (forward process), while the reverse process is learned via a denoising network that predicts the added noise given a noisy image. Training minimizes reconstruction loss; inference consists of repeatedly applying this learned denoiser to progressively clean an image from pure noise.

## Results  
Experiments demonstrate that DDPM produces images with PSNR and SSIM scores comparable to or exceeding GAN baselines, and that the step‑by‑step generation yields diverse outputs without mode collapse. When conditioned on text prompts using transformers (as in Stable Diffusion), the model achieves strong text‑to‑image performance.

## Significance  
By replacing adversarial training with a denoising objective, DDPM eliminates many GAN pitfalls such as mode collapse and training instability, enabling reliable, high‑quality image synthesis at scale. This democratizes generative AI, allowing anyone to generate images from text prompts without requiring extensive expertise.

## Related Concepts  
- diffusion process  
- reverse diffusion  
- latent variable model  
- Gaussian noise  
- Markov chain  
- conditional generation  
- transformers as denoisers  
- mode collapse  
- PSNR / SSIM metrics

[[Denoising Diffusion Probabilistic Models" (DDPM)]]