---
title: ProtoAct: Turning Wet-Lab Protocols into Embodied Robotic Actions
published: 2026-08-03T04:39:01Z
authors: Zhe Liu, Jiaming Gu, Zhaohui Du, Zhe Wang, Huanbo Jin, Quan Lu, Qi Wang, Ting Xiao, Minting Pan, Dongzhan Zhou
url: http://arxiv.org/abs/2608.01690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProtoAct: Turning Wet-Lab Protocols into Embodied Robotic Actions

## Abstract
Biological wet-lab protocols are written for trained researchers and often leave routine operations, state-dependent conditions, and contextual parameters implicit, making them difficult to translate into robot-executable actions. We present ProtoAct, a structured protocol-grounding framework that converts free-form biological procedures into state-aware, embodiment-ready action sequences. ProtoAct uses ProtoRAG to retrieve manually annotated examples for context-sensitive parsing, employs RefineChecker to detect and revise missing or inconsistent steps, and applies ActSchema to map the refined procedure into constrained JSON function sequences. We further introduce BioP2E, for which we manually annotate 22 cell-culture protocols into 258 monitoring conditions, 910 executable subtasks, and 962 grounded action calls. Evaluation across seven large language models demonstrates that ProtoAct can be effectively instantiated with different backbones. Ablations confirm that retrieval, posterior checking, and schema constraints make complementary contributions. The parsed subtasks further support demonstration collection and VLA model training, enabling successful execution in both simulation and real-robot settings. ProtoAct thus provides a practical interface between biological protocol understanding and embodied robotic execution.

## Metadata
- **Published**: 2026-08-03T04:39:01Z
- **Authors**: Zhe Liu, Jiaming Gu, Zhaohui Du, Zhe Wang, Huanbo Jin, Quan Lu, Qi Wang, Ting Xiao, Minting Pan, Dongzhan Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01690v1)