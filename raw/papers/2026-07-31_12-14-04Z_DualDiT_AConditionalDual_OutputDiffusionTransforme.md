---
title: DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation
published: 2026-07-31T12:14:04Z
authors: Fernando García-Torres, Rocío del Amor, Sandra Morales, Álvaro Barroso, Peter Heiduschka, Björn Kemper, Valery Naranjo
url: http://arxiv.org/abs/2607.29337v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualDiT: A Conditional Dual-Output Diffusion Transformer for Joint OCT Image and Segmentation Mask Generation

## Abstract
Background and Objective: Generating realistic medical images with anatomically accurate segmentation masks helps address the shortage of annotated data in medical imaging, particularly in optical coherence tomography (OCT) of mouse eyes, where manual retinal layer delineation is labour-intensive due to tiny structures and required expertise, resulting in scarce datasets. While diffusion models perform well in medical image synthesis, joint image-mask generation has relied mainly on U-Net-based denoisers, leaving diffusion transformers largely unexplored. Methods: We propose a conditional dual-output Diffusion Transformer (DualDiT) for joint synthesis of OCT B-scans and segmentation masks of the upper retinal cell layers in ex vivo mouse retina. DualDiT encodes both modalities into a shared latent space via a pretrained VAE, concatenates their latent representations, and performs conditional diffusion over the joint tensor. We compared DualDiT against two adapted diffusion baselines: DDPM and LDM. Generative quality was assessed via Fréchet Inception Distance (FID) and spatial FID (sFID); practical utility via synthetic data augmentation for downstream U-Net segmentation; and perceptual realism via evaluation by three domain experts. Results: DualDiT achieved the best generative quality (FID 56.14, sFID 114.35), outperforming DDPM and LDM. Expert panels misclassified 46% of synthetic samples as real and 42% of real samples as synthetic. Adding DualDiT-generated images and masks improved Dice and IoU scores on a held-out segmentation test set. Conclusions: DualDiT shows that transformer-based diffusion models can effectively learn the joint distribution of OCT images and segmentation masks, surpassing DDPM- and LDM-based baselines in generative fidelity, downstream utility, and perceptual realism, highlighting its potential for data augmentation in annotation-scarce medical imaging.

## Metadata
- **Published**: 2026-07-31T12:14:04Z
- **Authors**: Fernando García-Torres, Rocío del Amor, Sandra Morales, Álvaro Barroso, Peter Heiduschka, Björn Kemper, Valery Naranjo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29337v1)