---
title: EPRA U-Net: An Efficient Pyramid Residual Attention Framework for Accurate Infarct Segmentation in Diffusion-Weighted MRI
published: 2026-07-03T19:17:51Z
authors: Hasan Ulutas, Muhammet Emin Sahin, Mustafa Fatih Erkoc, Esra Yuce, Turker Tuncer, Sengul Dogan, Serkan Kiranyaz
url: http://arxiv.org/abs/2607.03568v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EPRA U-Net: An Efficient Pyramid Residual Attention Framework for Accurate Infarct Segmentation in Diffusion-Weighted MRI

## Abstract
Objective: Accurate identification of acute ischemic infarcts on diffusion-weighted magnetic resonance imaging (DWI) is a critical prerequisite for reliable lesion quantification and effective clinical decision support in the management of cerebrovascular events. Methods: This study presents EPRA U-Net (Efficient Pyramid Residual Attention U-Net), a task-specific integrated architecture for efficient and accurate infarct segmentation of DWI images. In the proposed architecture, an EfficientNet-based encoder was used as a hierarchical feature extractor with a minimized parameterization. In addition, a Residual-Recurrent (R2) block (recurrent unrolling step t = 2, following the original formulation) and Atrous Spatial Pyramid Pooling (ASPP) were integrated to enhance the performance of spatial dependency modeling. Additionally, a dual attention mechanism was incorporated to highlight lesion-related activations while concurrently enabling the suppression of extraneous background responses. To prioritize lesion detection consistent with clinical imperative, a Tversky loss function was adopted, emphasizing the sensitivity of detection over its specificity during the optimization process. Results: Experimental evaluations were conducted utilizing an in-house dataset comprising 167 patients with 4,895 DWI slices; subsequently, the performance of the proposed EPRA U-Net was assessed in comparison with state-of-the-art models, specifically UNet++, DeepLabV3+, and TransUNet. The experimental results suggest that EPRA U-Net attained superior performance, evidenced by a pixel-aggregated Dice of 0.8984, a per-sample Dice of 0.9469, an IoU of 0.8155, a Recall of 0.8887, a Lesion F1 of 0.9378, and an HD95 of 11.62 px. Furthermore, a clear reduction in the rate of missed lesions, specifically by 16%, 25%, and 29%, was observed when compared with UNet++, DeepLabV3+, and TransUNet, respectively.

## Metadata
- **Published**: 2026-07-03T19:17:51Z
- **Authors**: Hasan Ulutas, Muhammet Emin Sahin, Mustafa Fatih Erkoc, Esra Yuce, Turker Tuncer, Sengul Dogan, Serkan Kiranyaz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03568v1)