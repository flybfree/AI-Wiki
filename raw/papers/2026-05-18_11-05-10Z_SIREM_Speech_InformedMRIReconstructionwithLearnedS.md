---

title: 'SIREM: Speech-Informed MRI Reconstruction with Learned Sampling'
published: "2026-05-18T11:05:10Z"
authors: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
url: http://arxiv.org/abs/2605.18221v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# SIREM: Speech-Informed MRI Reconstruction with Learned Sampling



**Source**: [Original Paper](http://arxiv.org/abs/2605.18221v1)
## Abstract
Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM

## Metadata
- **Published**: 2026-05-18T11:05:10Z
- **Authors**: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18221v1)