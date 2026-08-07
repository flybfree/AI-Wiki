---
title: HyTBE: Hyperbolic Target-Background Expert Model for Cross-Domain Infrared Small Target Detection
published: 2026-08-06T09:02:09Z
authors: Aohua Li, Jin Kuang, Yubing Lu, Pingping Liu
url: http://arxiv.org/abs/2608.05771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyTBE: Hyperbolic Target-Background Expert Model for Cross-Domain Infrared Small Target Detection

## Abstract
Infrared small target detection (IRSTD) has achieved substantial progress under domain-consistent evaluation, yet detector performance often degrades markedly when generalizing to unseen infrared domains. Existing methods primarily improve detection by enhancing target responses and suppressing background interference. However, when trained on only a limited set of source domains, their learned decision rules are inevitably established from a restricted range of source-domain target-background relation patterns. We formulate this cross-domain failure as target-background relation shift: unseen domains may exhibit relation patterns that are not observed during training, thereby weakening the discriminative capability learned from the source domains. To address this problem, we propose HyTBE, a Hyperbolic Target-Background Expert model that expands source-domain relation patterns and adaptively adjusts visual representations using explicit relation cues. The Target-Background Relation Intervention selectively perturbs either targets or backgrounds, broadening the observable relation patterns during training while maintaining valid supervision. Subsequently, the Hyperbolic Relation Modeling maps multi-scale visual cues into a Poincaré ball and characterizes the target-background relation of each feature token according to its relative distances to the target and background anchors. The Hyperbolic-guided MoE Adapter further uses these hyperbolic relation representations to calibrate multi-scale visual features and aggregate expert-specific feature corrections for different relation patterns. Leave-one-domain-out experiments on NUAA-SIRST, NUDT-SIRST, and IRSTD-1K demonstrate that HyTBE achieves stronger cross-domain generalization than competitive baselines.

## Metadata
- **Published**: 2026-08-06T09:02:09Z
- **Authors**: Aohua Li, Jin Kuang, Yubing Lu, Pingping Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05771v1)