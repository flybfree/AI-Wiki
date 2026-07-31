---
title: A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models
published: 2026-07-30T09:24:27Z
authors: Xiangyu Yin, Tora Bodin, Rohan Menon, Chih-Hong Cheng
url: http://arxiv.org/abs/2607.27910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models

## Abstract
Inference time defences against vision language model jailbreaks often subtract a calibrated direction from the residual stream at a chosen decoder layer. We compare five defence candidates across 15 model and layer cells from four architectural families under a magnitude controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control of the same norm. The candidates are the mean image conditioning shift, a CMRM style refusal direction, a ShiftDC style attack specific residual, a prompt instruction to ignore the image, and a random control. No single candidate dominates on both refusal recovery and utility preservation. The image conditioning shift leads on LLaVA 1.5 and Pixtral 12B and is the only candidate whose utility loss remains at the measurement noise floor in every family. The prompt instruction leads on Qwen2.5 VL, while the attack specific residual leads on Qwen2 VL 2B. The image conditioning direction is direction specific in 13 of 15 cells, but strongly architecture specific and nontransferable across the only dimension compatible pair, LLaVA 1.5 13B and Pixtral 12B. We also connect text only and multimodal refusal geometry. The CMRM direction has positive cosine alignment with the image conditioning shift in all 15 cells, with mean 0.35, range 0.17 to 0.65, 15 to 25 times the random vector null, and a sign test p value of about 3e-5. These results show that the two recipes recover partially overlapping geometry and that direction based defences should be calibrated separately for each language decoder family.

## Metadata
- **Published**: 2026-07-30T09:24:27Z
- **Authors**: Xiangyu Yin, Tora Bodin, Rohan Menon, Chih-Hong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27910v1)