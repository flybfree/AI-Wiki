---
title: Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation
published: 2026-10-08T11:50:32Z
authors: Haitong Jiang, Chunlin Liu, Sihan Tang, Chan Wu, Xiaoqing Su, Yuhong Feng
url: http://arxiv.org/abs/2610.11766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation

## Abstract
Safety evaluations of large language models commonly summarize harmful-output behavior with attack success rate (ASR). Yet the same non-harmful outcome can arise for very different reasons. A model may recover a harmful task and refuse it, fail to recover the task, or respond to something else entirely. Distinguishing these cases becomes especially important under intent-obscuring prompts, where a low ASR does not reveal whether the evaluated task was actually engaged. To make this distinction explicit, we pair ASR with operative understanding rate (UR), which measures whether a response both identifies the evaluated task and treats it as the task to be answered. Across interfaces, this paired view reveals substantial variation hidden by ASR: similar ASR values can correspond to sharply different recovery rates. Controlled English reconstructions show that recovery consistently improves as compressed prompts become more explicit, whereas ASR does not follow the same pattern. A complementary contrast comes from FormalLogic, where high recovery can still coincide with frequent harmful assistance. Together, these results show that non-harmful outcomes are not equally informative about model safety, motivating the joint reporting of intent recovery and ASR in LLM safety evaluation. Code and experiment inputs are available at https://github.com/kevinjiang0121-cyber/IRIS.

## Metadata
- **Published**: 2026-10-08T11:50:32Z
- **Authors**: Haitong Jiang, Chunlin Liu, Sihan Tang, Chan Wu, Xiaoqing Su, Yuhong Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11766v1)