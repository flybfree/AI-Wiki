---
title: How Far Do Persona Effects Generalize in Language Models?
published: 2026-09-26T16:26:03Z
authors: Yufan Zhou, Yuxuan Liu, Enze Ma, Lyumanshan Ye, Zhongqi Yue, Robin De Croon, Yucheng Jin, Katrien Verbert, Zhao Wang
url: http://arxiv.org/abs/2609.32758v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Far Do Persona Effects Generalize in Language Models?

## Abstract
Persona prompts ask language models to answer as particular kinds of people. We test whether relationships learned from these effects predict responses to new questions and remain useful across models and prompts. Across 57 attributes, three behavioral domains, and seven pairs of open 7 to 9B checkpoints, persona effects can be predictable without being portable. Separate attribute and task gains improve prediction beyond shared scaling significantly in OLMo-3 and Qwen2.5, with the most robust evidence in OLMo-3. In that model, target refitting significantly outperforms gains borrowed from each of the other six pairs. Across model transfers, borrowed gains with one amplitude underperform shared scaling in most directions; allowing two target parameters removes the significant losses but yields no significant benefit over target shared scaling. After rewording, refitting significantly outperforms reuse with one amplitude in all six tested pairs, while changes of examples or country context often preserve reuse value. In the tested prompt transfers, regularized updates outperform both reuse strategies in median at 64 target questions per attribute. A separate survey comparison finds that selecting the more responsive checkpoint can worsen human fit; responsiveness is confounded with training status, and temperature calibration largely removes this cost but not errors in group ordering. Within the tested gain representation, apparent transfer can come from target calibration; source relationships must add predictive value beyond calibration and regularization. Code and data are available at https://github.com/thzva/persona-gain

## Metadata
- **Published**: 2026-09-26T16:26:03Z
- **Authors**: Yufan Zhou, Yuxuan Liu, Enze Ma, Lyumanshan Ye, Zhongqi Yue, Robin De Croon, Yucheng Jin, Katrien Verbert, Zhao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32758v1)