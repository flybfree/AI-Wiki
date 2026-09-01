---
title: Benevolent Bias in Multi-Turn Human-Agent Dialogue
published: 2026-08-29T11:42:45Z
authors: Qianqi Liu, Jin Huang, Fethiye Irmak Dogan, Hatice Gunes
url: http://arxiv.org/abs/2608.29206v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benevolent Bias in Multi-Turn Human-Agent Dialogue

## Abstract
Bias in human-agent interaction can manifest not only through hostile language but also as benevolent bias, whereby unequal treatment hides behind a warm, positive tone. To make it detectable, we operationalise benevolent bias along two dimensions, tone and treatment, yielding three classes: neutral support, overt bias, and benevolent bias. Building on these definitions, we construct BENEVDIAL, a class-balanced corpus of 362,880 multi-turn support dialogues spanning user and agent demographics, roles, and generators, to support controlled evaluation. We then test two detector families on it: off-the-shelf safety detectors and prompted large language model (LLM) judges. Our results reveal a detection gap: off-the-shelf detectors reliably flag overt bias yet largely miss benevolent bias, while LLM judges catch more under more explicit detection criteria but increasingly misclassify neutral support as benevolent bias, and demographic context amplifies the false alarms. These findings suggest that fair monitoring of human-agent dialogue must look beyond surface cues to whether the agent's treatment is disparate.

## Metadata
- **Published**: 2026-08-29T11:42:45Z
- **Authors**: Qianqi Liu, Jin Huang, Fethiye Irmak Dogan, Hatice Gunes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29206v1)