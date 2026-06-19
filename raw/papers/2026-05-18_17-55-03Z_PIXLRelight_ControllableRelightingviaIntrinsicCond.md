---

title: 'PIXLRelight: Controllable Relighting via Intrinsic Conditioning'
published: "2026-05-18T17:55:03Z"
authors: Miguel Farinha, Ronald Clark
url: http://arxiv.org/abs/2605.18735v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# PIXLRelight: Controllable Relighting via Intrinsic Conditioning



**Source**: [Original Paper](http://arxiv.org/abs/2605.18735v1)
## Abstract
We present PIXLRelight, a feed-forward approach for physically controllable single-image relighting. Existing methods either provide limited lighting control (e.g. through text or environment maps), accumulate errors when chaining inverse and forward rendering, or require costly per-image optimization. Our key idea is to bridge physically based rendering (PBR) and learned image synthesis through a shared intrinsic conditioning that can be obtained from either real photographs or PBR renders. At training time, paired multi-illumination photographs are decomposed into albedo, diffuse shading, and non-diffuse residuals, which condition the model. At inference time, the same conditioning is computed from a path-traced render of a coarse 3D reconstruction of the input under user-specified PBR lights. A transformer-based neural renderer then applies the target illumination to the source photograph, preserving fine image detail through a per-pixel affine modulation. PIXLRelight enables arbitrary PBR-style lighting control, achieves state-of-the-art relighting quality, and runs in under a tenth of a second per image. Code and models are available at https://mlfarinha.github.io/pixl-relight/.

## Metadata
- **Published**: 2026-05-18T17:55:03Z
- **Authors**: Miguel Farinha, Ronald Clark
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18735v1)