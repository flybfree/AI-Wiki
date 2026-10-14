---
title: Trace Evolution Bench: Measuring Whether Agents Improve from Their Own Environment Traces
published: 2026-10-10T16:45:52Z
authors: Fangfei Li, Chenyang Zhao, Long Wang, Feng Tian, Lv Guo
url: http://arxiv.org/abs/2610.15055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trace Evolution Bench: Measuring Whether Agents Improve from Their Own Environment Traces

## Abstract
Self-evolving agents are usually scored by endpoint Gain: held-out success after an update minus success before. That difference can credit a frozen rescore as evolution. We introduce Trace Evolution Bench (TEB), a protocol that separates that rescore from a context or weight update, together with three frozen 80/20/40 packs. An update is accepted only when validation does not fall, held-out identifiers never enter the update, and a text update is not ranked with a weight update. The primary scoreboard is coding, graded by hidden unit tests in a closed workspace. On that pack (40 held-out tasks, one family), DeepSeek v4 Pro under no_evolve never changes its policy yet moves 7.5, 5.0, and 12.5 percentage points across three seeds. Of nine text-update cells inspired by GEPA, ACE, and ExpeL, seven have positive excess above that seed's own band, and one gepa_llm seed moves down by the width of its band (-12.5, regression 0.48). GLM and MiniMax do not reproduce that seven-of-nine pattern. No method stays above its own band on every seed of all three models: GLM has two paired cells above their own bands, and MiniMax expel_llm seed 44 is a third (regression 0.30). The methods were fixed on a validation screen before held-out was read. Office, graded by rule-bounded delivery, and manufacturing table QA are separate packs: office DeepSeek does not exceed its own bands (widest 17.5 points), and manufacturing has no paired positive excess beyond its seed band.

## Metadata
- **Published**: 2026-10-10T16:45:52Z
- **Authors**: Fangfei Li, Chenyang Zhao, Long Wang, Feng Tian, Lv Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15055v1)