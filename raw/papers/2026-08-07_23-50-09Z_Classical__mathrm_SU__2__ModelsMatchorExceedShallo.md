---
title: Classical $\mathrm{SU}(2)$ Models Match or Exceed Shallow Variational Quantum Circuits on Vision Benchmarks
published: 2026-08-07T23:50:09Z
authors: Christopher Fulton, Irene Tsapara, Lawrence Fulton
url: http://arxiv.org/abs/2608.07822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Classical $\mathrm{SU}(2)$ Models Match or Exceed Shallow Variational Quantum Circuits on Vision Benchmarks

## Abstract
Quaternion-valued neural networks and variational quantum circuits (VQCs) both derive local transformations from $\mathrm{SU}(2)$ geometry, yet their performance on classical supervised learning remains poorly understood. We compare real-valued, quaternion-valued, and quantum classification heads on identical frozen features across MNIST, FashionMNIST, and CIFAR-10. CIFAR-10 uses a learned 16-dimensional bottleneck and frozen ImageNet-pretrained ResNet18 features to separate architecture from representation quality. Quaternion classifiers match or approach real-valued baselines while outperforming shallow VQCs. On MNIST and FashionMNIST, quaternion networks nearly equal real-valued MLPs, whereas product-state VQCs show lower accuracy and higher cost. On CIFAR-10, quaternion networks retain 94--97% of real-valued performance and remain stable under a 32-fold increase in dimensionality. Product-state circuits underperform quaternion classifiers, while entanglement gives modest grayscale gains but reverses under pretrained CNN features (9.25 pp degradation vs.\ product-state). Fubini--Study/QFI natural gradients improve geometric alignment but not short-horizon loss reduction vs.\ Adam. A Friedman test on five-seed MNIST detects model differences ($χ^2=12.796$, $p=0.0051$, $n=5$), with Wilcoxon tests yielding large effect sizes ($d>5$) for QuatNet vs.\ quantum comparisons. For FashionMNIST and CIFAR-10, large effects ($d>2.0$) are the primary statistic given $n=3$. These results indicate that quaternion networks provide efficient, stable $\mathrm{SU}(2)$ alternatives to shallow VQCs on tasks lacking intrinsic quantum structure. Shared local $\mathrm{SU}(2)$ geometry and shallow entanglement are insufficient, within the regime studied, to confer practical quantum advantage. Conclusions are limited to shallow, measurement-limited circuits on such tasks.

## Metadata
- **Published**: 2026-08-07T23:50:09Z
- **Authors**: Christopher Fulton, Irene Tsapara, Lawrence Fulton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07822v1)