---

title: Toward Better Geometric Representations for Molecule Generative Models
published: "2026-05-08T13:02:58Z"
authors: Shaoheng Yan, Zian Li, Cai Zhou, Qiaojing Huang, Kai Liu, Muhan Zhang
url: http://arxiv.org/abs/2605.07693v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Toward Better Geometric Representations for Molecule Generative Models



**Source**: [Original Paper](http://arxiv.org/abs/2605.07693v1)
## Abstract
Geometric representation-conditioned molecule generation provides an effective paradigm that decouples molecule representation modeling from structure generation. By decoupling molecule generation into two stages-first generating a meaningful molecule representation, and then generating a 3D molecule conditioned on this representation-the efficiency and quality of the generation process can be significantly enhanced. However, its effectiveness is fundamentally limited by the quality of the representation space: pretrained molecular encoders, such as UniMol, produce representations that are non-smooth and not fully exploited during the generative training process. In this work, we propose LENSEs, a framework that better exploits the potential of molecule representations in representation-conditioned generation methods. In particular, LENSEs introduces three complementary mechanisms: (1) a representation head, simultaneously trained during generative tasks, that extracts multi-level representations from the pretrained encoder; (2) a molecule perceptual loss that optimizes the generator in a semantic-informative representation space; and (3) a node-level representation alignment (REPA) loss that explicitly aligns the generator's hidden states with encoder representations, reducing the semantic gap between pretraining and generation. We demonstrate the effectiveness of these improvements through extensive molecule generation tasks. Specifically, on the challenging molecule generation dataset GEOM-DRUG, LENSEs achieves 97.28% validity and 98.51% molecule stability, surpassing existing advanced methods. Further analyses through Lipschitz constant reduction (4.6x) and QM9 probing tasks also demonstrate the smoother, more informative refined representations, establishing generative training with alignment objectives as a potential pretraining paradigm for molecular encoders.

## Metadata
- **Published**: 2026-05-08T13:02:58Z
- **Authors**: Shaoheng Yan, Zian Li, Cai Zhou, Qiaojing Huang, Kai Liu, Muhan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.07693v1)