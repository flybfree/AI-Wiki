---
title: When Protection Overrides Consequences: Understanding Protection Mode in Large Language Model Decision-Making
published: 2026-10-14T10:30:33Z
authors: Yuanfan Li, Junyi Chen, Qi Zhou, Rui Yang,  ZhangLiujie, Weihang Chen
url: http://arxiv.org/abs/2610.19948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Protection Overrides Consequences: Understanding Protection Mode in Large Language Model Decision-Making

## Abstract
Frontier language models excel at complex tasks yet may prioritize protection over larger physical consequences in simple, urgent decisions. GPT-5.6 Sol, for example, moves a girl playing in shallow water before retrieving a submerged camera. We call this Protection Mode and study it with ProtectionBench: 285 prompts, 34 physical families, and nine models. At lowest effort, at least one of four responses prioritizes the subject on 34.74% of Sol prompts and over 83% of MiniMax M3 and Qwen3.5-27B prompts; none of four independent human raters does so. Controls show that choices usually track physical risk. We elicit both risks before requesting an action. Some models assess risk incorrectly; others state the correct ordering but still choose the subject. Qwen3.5-27B with thinking shows 100% correct risk ordering but 57.81% subject choice among eligible conversations on eight selected scenes. Attention audits find no stable reduction in attention to relevant facts; removing the stated risk direction reduces object-first choice in dots3-note-prev but not detectably in Qwen3.5-27B. Adding a general "people or animals before property" rule increases subject choice by 19-38 percentage points, whereas factual reminders favor the object by 0.7-5.2 points. Removing naturally generated versions of that rule lowers subject choice by 10-15 points. We also examine whether post-training introduces this pattern. Base models already show Protection Mode; post-training changes justifications more than choices.

## Metadata
- **Published**: 2026-10-14T10:30:33Z
- **Authors**: Yuanfan Li, Junyi Chen, Qi Zhou, Rui Yang,  ZhangLiujie, Weihang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19948v1)