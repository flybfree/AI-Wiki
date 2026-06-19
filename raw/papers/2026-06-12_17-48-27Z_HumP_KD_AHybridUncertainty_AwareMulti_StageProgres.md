---

title: "HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification"
published: "2026-06-12T17:48:27Z"
authors: Mohammed Arif Mainuddin, Najifa Tabassum, Omar Ibne Shahid, Riasat Khan
url: http://arxiv.org/abs/2606.14684v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification



**Source**: [Original Paper](http://arxiv.org/abs/2606.14684v1)
## Abstract
Real-time fire classification systems require models that are simultaneously accurate, computationally efficient, and deployable on resource-constrained hardware. This work proposes \textbf{HumP-KD}, a Hybrid Uncertainty-aware Multi-stage Progressive Knowledge Distillation framework for efficient fire classification. Two datasets, FlameVision and Dataset-II, containing 8,600 and 31,309 images, are used. Various CNN and transformer baselines are applied under standard preprocessing, online augmentation, Gaussian noise and motion blur robustness conditions. The proposed HumP-KD model distills knowledge from two frozen heterogeneous transformer teachers, Swin-Tiny and ViT-Base, along with their Meta-MLP ensemble, into a lightweight MobileViT-S student via three tightly integrated components. Hierarchical Progressive Knowledge Distillation employs a Hierarchical Feature Builder. It generates a fused spatial attention mask to guide distillation toward discriminative regions selectively. Multi-Stage Knowledge Distillation progressively activates three distillation stages across training. On Dataset-II, HumP-KD achieves a mean F1 score of $0.9876 \pm 0.0063$ across 10 independent trials, significantly outperforming the MobileViT-S baseline trained without distillation ($0.9537 \pm 0.0351$), with statistical significance confirmed by both independent t-test ($p = 0.0195$) and Wilcoxon signed-rank test ($W = 1$, $p = 0.0039$). The proposed method also demonstrates strong generalization across datasets and robustness under degraded visual conditions. The student model retains only 4.94M parameters and 19.01Mb model size, representing a $5.7\times$ parameter reduction over Swin-Tiny and a $17.5\times$ reduction over ViT-Base, while achieving 37.72 CPU FPS, making it suitable for real-time deployment.

## Metadata
- **Published**: 2026-06-12T17:48:27Z
- **Authors**: Mohammed Arif Mainuddin, Najifa Tabassum, Omar Ibne Shahid, Riasat Khan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.14684v1)