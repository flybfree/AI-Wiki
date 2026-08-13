---
title: Hardware-Aware Deployment of Joint SAR Compression and Despeckling on FPGA
published: 2026-08-11T07:29:13Z
authors: Cédric Léonard, Francescopaolo Sica, Martin Schulz
url: http://arxiv.org/abs/2608.11271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hardware-Aware Deployment of Joint SAR Compression and Despeckling on FPGA

## Abstract
Next-generation Synthetic Aperture Radar (SAR) missions will generate data far faster than they can downlink, making onboard data reduction essential for near-real-time Earth observation. Learned Image Compression (LIC) offers better rate-distortion performance than handcrafted codecs used operationally today, and recent work shows that simultaneously despeckling and compressing SAR imagery enables better representation capacity while unlocking higher compression rates. These methods, however, have yet to be confronted with the strict power, compute, and operational constraints of spaceborne systems. In this work, we bridge this gap by deploying a joint SAR Despeckling and Data Compression (DDC) framework on an embedded ZCU102 FPGA-based platform, introducing model adaptations that respect the accelerator's fixed-point arithmetic and limited set of supported operations. We evaluate four model topologies across precision levels and across CPU, GPU, and FPGA platforms, revealing several findings with direct design implications. We find that replacing conventional GDN activation functions with plain ReLU improves quality on SAR, suggesting that design principles established for compression of natural images do not necessarily transfer to SAR imagery. In addition, we demonstrate that residual blocks offer little representational benefit for ten times the compute, and show that the FPGA is the most energy-efficient of the platforms tested. Together, these results set a functioning edge deployment workflow and an evidence-based starting point for onboard SAR compression. The code is available at https://github.com/CedricLeon/SAR_DDC_FPGA.

## Metadata
- **Published**: 2026-08-11T07:29:13Z
- **Authors**: Cédric Léonard, Francescopaolo Sica, Martin Schulz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11271v1)