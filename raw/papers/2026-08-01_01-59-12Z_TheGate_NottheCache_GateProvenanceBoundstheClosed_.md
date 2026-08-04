---
title: The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping
published: 2026-08-01T01:59:12Z
authors: Qi Luo, Shuaijun Liu, Hao Zhao, Kunlin Li, Xiaobo Wang, Ningxing Su, Dongsheng Wang, Yun Chen
url: http://arxiv.org/abs/2608.00391v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Gate, Not the Cache: Gate Provenance Bounds the Closed-Loop Reliability of Training-Free VLA Token Skipping

## Abstract
Token skipping is a widely used training-free way to accelerate vision--language--action (VLA) models by bypassing computation for most visual tokens at each control step according to a gate. When the next gate is harvested from the previous accelerated forward, however, the tokens skipped at one step are also the ones least visible to the next gate, and the damage can compound across control steps until the task fails. We study the two mechanisms this class is built on, reuse and deletion, crossing each against where its gate signal comes from on identical episodes. At a skip ratio of 0.9 on LIBERO-Object, both collapse when the gate comes from the model's own accelerated forwards, to 0.68 under reuse and to 0.31 under deletion against a dense 1.00, and the collapse is invisible to the action-level detectors we evaluate. What separates collapse from dense-level operation is not the mechanism but whether the gate is clean, computed by a forward that skipped nothing. We therefore propose actuation-slack refresh, one dense pass run while the robot executes its current action chunk, off the critical path, that hands the next step a clean gate and a fresh KV base. Since the measured detectors do not reliably reveal the failure, the refresh is unconditional rather than triggered. Both mechanisms then recover to 0.98, keeping the speed of skipping and the information of a dense pass. We then integrate the refresh into state-of-the-art caching and pruning methods across two VLA policies, 4 LIBERO suites, and 4 SIMPLER tasks, where it repairs every collapse caused by using a self-harvested gate. Serve latency drops 18--22\% below dense, measured both in simulation and on a physical robot. Where the gate signal comes from, not how tokens are skipped, decides closed-loop reliability for accelerated VLAs.

## Metadata
- **Published**: 2026-08-01T01:59:12Z
- **Authors**: Qi Luo, Shuaijun Liu, Hao Zhao, Kunlin Li, Xiaobo Wang, Ningxing Su, Dongsheng Wang, Yun Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00391v1)