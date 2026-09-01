---
title: $\mathcal{N}_0$-Foundation: Towards the Age of Tactile Intelligence
published: 2026-08-30T06:46:18Z
authors:  NeoteAI Team,  Fudan TEAI Team
url: http://arxiv.org/abs/2608.29601v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# $\mathcal{N}_0$-Foundation: Towards the Age of Tactile Intelligence

## Abstract
We present $\mathcal{N}_0$-Foundation, a paradigm for tactile-enabled embodied manipulation, which integrates tactile sensing hardware, large-scale multimodal data, tactile representation learning, and standardized evaluation. First, we engineer the infrastructure for scalable data collection, including a vision-based tactile sensor, a tactile Universal Manipulation Interface (UMI), and a synchronized visuo-tactile data collection system supporting both robot embodiments and UMI-based demonstrations. Leveraging this infrastructure, we construct NeoData, which contains more than 30000 hours of synchronized visual and tactile demonstrations, spanning six embodiments, 450 tasks, and billions of paired RGB and tactile frames collected through a mixture of real-robot teleoperation and UMI-based demonstrations. To facilitate open research, we further release OpenNeoData, a 5000-hour open-source subset of NeoData. The dataset addresses a central limitation of existing manipulation corpora, critical for deformable-object manipulation, precise assembly, delicate force control, and sustained surface interaction. Capitalizing on the large-scale, heterogeneous tactile measurements, we propose NeoForce, a visuo-tactile representation model that learn transferable tactile representations across different sensor designs. To enable systematic evaluation of tactile embodied models built upon our infrastructure, datasets and tactile representations, we further propose a comprehensive benchmark, which combines the real-world NeoReal suite and the simulated NeoSim suite for standardized evaluation. Experiments across both suites show that policies benefit from the physical contact state rather than from the device-specific appearance of the tactile signal. We release the dataset, the representation, and the benchmark, aiming at supporting future work on tactile-enabled embodied manipulation.

## Metadata
- **Published**: 2026-08-30T06:46:18Z
- **Authors**:  NeoteAI Team,  Fudan TEAI Team
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29601v1)