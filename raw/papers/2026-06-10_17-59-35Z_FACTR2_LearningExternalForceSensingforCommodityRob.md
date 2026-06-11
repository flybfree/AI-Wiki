---
title: FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning
published: 2026-06-10T17:59:35Z
authors: Steven Oh, Jason Jingzhou Liu, Tony Tao, Philip Han, Kenneth Shaw, Satoshi Funabashi, Ruslan Salakhutdinov, Deepak Pathak
url: http://arxiv.org/abs/2606.12406v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning

## Abstract
Contact-rich manipulation requires force sensitivity, but many robot arms lack dedicated force sensors due to their high cost. We present Neural External Torque Estimation (NEXT), a data-driven method that estimates external joint torques without needing any dedicated force sensors. NEXT trains in 1 minute from only 10 minutes of free-motion data, yet achieves estimates comparable to dedicated joint-torque sensors. NEXT enables force-feedback teleoperation on low-cost arms and improves policy learning through Force-Informed Re-Sampling Training (FIRST), which up-samples pre-contact and contact segments during behavior cloning. Across five long-horizon tasks, FIRST outperforms prior force-aware policies by over 17% in task progress. Together, NEXT and FIRST bring force-aware teleoperation and policy learning to off-the-shelf robots without additional sensing hardware. Video results and code are available at https://jasonjzliu.com/factr2

## Metadata
- **Published**: 2026-06-10T17:59:35Z
- **Authors**: Steven Oh, Jason Jingzhou Liu, Tony Tao, Philip Han, Kenneth Shaw, Satoshi Funabashi, Ruslan Salakhutdinov, Deepak Pathak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12406v1)