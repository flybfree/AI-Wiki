---
title: SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation
published: 2026-08-11T10:28:59Z
authors: Zhou Liu, Ligang Huang, Zeli Su, Zewei Pan, Zhaoyang Han, Xing Chen, Yuanfeng Song, Wentao Zhang
url: http://arxiv.org/abs/2608.10775v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation

## Abstract
Computer-using agents can perceive rich software interfaces, yet their decisions often lack visual procedural memory: they may recognize individual controls without identifying which familiar workflow is active, which control matters next, or what evidence would confirm progress. Raw interaction traces preserve such information but are long and noisy to condition on, whereas text-only skills often omit the visual state that makes a procedure applicable. We introduce Visual Skill Cards (VSCs), a state-conditioned memory representation that binds reusable procedures with applicability cues, visual evidence, and verification signals. SkillLens constructs VSCs from heterogeneous interaction experience through Trace-to-Visual-Skill-Card and, at inference time, retrieves relevant cards and selectively expands only the evidence needed by a fixed visual-language model executor for grounded GUI action prediction. The same representation also supports CardDistill, which uses VSC evidence as privileged teacher context to train a student that acts without runtime card retrieval. Across Multimodal-Mind2Web and WebLINX-BrowserGym, SkillLens improves the frozen GPT-5.4-mini executor by +11.6 points in Step SR and +2.9 points in Overall, respectively; CardDistill further improves the corresponding student-only Qwen3-VL-2B metrics by +12.0 and +3.2 points.

## Metadata
- **Published**: 2026-08-11T10:28:59Z
- **Authors**: Zhou Liu, Ligang Huang, Zeli Su, Zewei Pan, Zhaoyang Han, Xing Chen, Yuanfeng Song, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10775v1)