---
title: Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models
published: 2026-07-21T22:24:18Z
authors: Mahdiyeh Farajidizaji, Vatsal Raina
url: http://arxiv.org/abs/2607.19608v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models

## Abstract
Instruction tuning is meant to make language models follow user requests, yet it is unclear whether small models comply when an instruction conflicts with their usual task behavior. We study this across three tasks - multiple-choice question answering (MCQA), sentiment classification, and mathematical question answering - by pairing a standard instruction with a conflicting non-standard one (select an incorrect option, output the opposite sentiment, or return twice the answer). This cross-task design allows us to test whether resistance to conflicting instructions is tied to specific task characteristics or reflects a broader behavioral tendency. As all predictions are scored against the original ground truth, a model that ignores the non-standard instruction still appears accurate. Using standard accuracy, non-standard accuracy, and an Instruction-Following Failure Rate (IFFR), we evaluate instruction-tuned Qwen models across sizes. Both standard accuracy and instruction following generally improve with scale, although the pattern is not consistent across all tasks and datasets. Small models stay competent yet routinely ignore the non-standard instruction, while larger models show a clear gap between the two settings. These findings suggest that gains in task capability do not automatically provide reliable control over model behavior. Task competence and instruction following are therefore distinct abilities, and reporting only standard accuracy hides instruction-following failures.

## Metadata
- **Published**: 2026-07-21T22:24:18Z
- **Authors**: Mahdiyeh Farajidizaji, Vatsal Raina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19608v1)