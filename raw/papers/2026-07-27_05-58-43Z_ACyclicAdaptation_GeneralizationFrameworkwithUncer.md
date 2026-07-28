---
title: A Cyclic Adaptation-Generalization Framework with Uncertainty-Guided Self-Paced Learning for Long-Term Brain-Machine Interfaces
published: 2026-07-27T05:58:43Z
authors: Jiyu Wei, Di Hong, Zhanjie Zhang, Dazhong Rong, Qinming He, Yueming Wang
url: http://arxiv.org/abs/2607.24031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Cyclic Adaptation-Generalization Framework with Uncertainty-Guided Self-Paced Learning for Long-Term Brain-Machine Interfaces

## Abstract
Brain-Machine Interfaces (BMIs), which link the brain to external devices, hold great potential in rehabilitation, human performance augmentation, and human-centered robotics. However, invasive BMIs face a critical challenge for long-term deployment due to neural drift, which degrades decoding performance over time and necessitates frequent recalibration. Existing methods designed to mitigate neural drift typically rely on either domain adaptation (DA) or domain generalization (DG) alone and often fail to capture fine-grained distribution shifts across neural subdomains, resulting in limited performance. To overcome these limitations, we propose Uncertainty-guided Self-paced Cycling (UnSPC), a robust framework that synergizes DA and DG for target domain refining under an Uncertainty-guided Self-paced Pseudo-labeling (UnSPL) mechanism. To handle subdomain neural drift across domains, UNSPL is proposed to iteratively mine reliable pseudo-labeled samples with a noise-robust ranking strategy for further fine-tuning. Leveraging these high-quality samples, we introduce a novel Cycling Adaptation and Generalization (CycAG) strategy, which integrates DA and DG within an iterative cycle to progressively mitigate both global and subdomain drift. This cyclic process enables effective alignment to evolving target distributions while preserving robust and transferable representations, thereby mitigating performance degradation under long-term neural drifts. Extensive experiments on multiple neural decoding datasets demonstrate the effectiveness and robustness of UnSPC. To our knowledge, our proposed UnSPC is the first to cyclically integrate DA and DG with pseudo-labeling, paving the way toward stable long-term BMI controls.

## Metadata
- **Published**: 2026-07-27T05:58:43Z
- **Authors**: Jiyu Wei, Di Hong, Zhanjie Zhang, Dazhong Rong, Qinming He, Yueming Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24031v1)