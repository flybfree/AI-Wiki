---
title: FLINT: Efficiently Leveraging High Bandwidth Flash for Capacity-Scalable LLM Inference Acceleration
published: 2026-08-25T18:58:14Z
authors: Geraldo F. Oliveira, Arash Tavakkol, Xiangyu Zhu, Ahmet Caner Yüzügüler, Vamanan Arulchelvan, Lukas Cavigelli, Renzo Andri, Mohammad Sadrosadati, Jia Xinglei, Onur Mutlu, Zhou Ke, Shai Bergman, Ji Zhang
url: http://arxiv.org/abs/2608.25062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FLINT: Efficiently Leveraging High Bandwidth Flash for Capacity-Scalable LLM Inference Acceleration

## Abstract
LLM inference is increasingly constrained by accelerator memory capacity rather than compute throughput. This constraint is especially acute in single-accelerator and small-node inference systems, where limited on-package memory capacity restricts the size of deployable models. HBF is an emerging 3D-stacked NAND flash technology that provides multi-terabyte near-accelerator capacity, making it a promising capacity tier for storing LLM weights. However, existing HBF-based proposals face three adoption challenges: they (1) rely on coarse-grained static prefetching for LLM weights aiming to hide the microsecond-level read latency of the NAND flash device while maximizing HBF's read throughput, (2) expose NAND flash management tasks (e.g., refresh operations) to the accelerator-visible critical inference path, and (3) miss optimization opportunities to specialize and optimize the flash-management mechanisms to the workload behavior.   Our goal is to design an efficient HBF substrate that integrates HBF as a memory-capacity tier alongside HBM while addressing these three challenges. To this end, we propose FLINT, a workload-driven HBF substrate for capacity-scalable LLM inference. FLINT introduces three mechanisms: (1) a hardware burst-buffer controller that dynamically coalesces and pipelines HBF reads aiming to utilize existing NAND flash buffers while sustaining high HBF bandwidth, (2) a phantom-plane refresh mechanism, which removes refresh from the critical inference path by moving refresh-related NAND flash operations outside the read foreground back via low-cost resource duplication, and (3) a read-only FTL, which replaces SSD-class support for arbitrary writes with a compact table that translates logical weight bursts to physical HBF locations.

## Metadata
- **Published**: 2026-08-25T18:58:14Z
- **Authors**: Geraldo F. Oliveira, Arash Tavakkol, Xiangyu Zhu, Ahmet Caner Yüzügüler, Vamanan Arulchelvan, Lukas Cavigelli, Renzo Andri, Mohammad Sadrosadati, Jia Xinglei, Onur Mutlu, Zhou Ke, Shai Bergman, Ji Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25062v1)