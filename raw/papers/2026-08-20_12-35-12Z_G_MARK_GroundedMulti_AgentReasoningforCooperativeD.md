---
title: G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs
published: 2026-08-20T12:35:12Z
authors: Bhavya Gupta, Onat Gungor, Tajana Rosing
url: http://arxiv.org/abs/2608.19964v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs

## Abstract
Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects downstream decisions. We propose G-MARK, a grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs (KGs). The resulting KGs preserve object hypotheses together with their source attribution, ego-versus-partner visibility, uncertainty, conflicts, spatial relations, and planning-relevant context. G-MARK then derives a shared feature representation from these KGs, enabling lightweight task heads to support object reasoning, motion prediction, control selection, and trajectory forecasting. Compared with the state-of-the-art baseline, GMARK improves occlusion reasoning accuracy by 42.2%, reduces control-selection error by 13.1%, and achieves comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload. Our code is available at https://github.com/bhavyagupta98/g-mark.

## Metadata
- **Published**: 2026-08-20T12:35:12Z
- **Authors**: Bhavya Gupta, Onat Gungor, Tajana Rosing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19964v1)