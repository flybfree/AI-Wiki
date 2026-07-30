---
title: DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues
published: 2026-07-28T18:36:46Z
authors: Takyoung Kim, Kang-wook Kim, Sang Hoon Woo, Julia Hirschberg, Gunhee Kim, Dilek Hakkani-Tür
url: http://arxiv.org/abs/2607.26178v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues

## Abstract
Turn-taking is a central component of full-duplex interaction. Which turn-taking behaviors are appropriate varies with the scenario, yet current models apply a single norm regardless of context. This limitation originates in their training data: human-human speech corpora capture natural timing phenomena but provide little role grounding or scenario-specific norms, while heuristic or prompted synthesis methods inject turn-taking behaviors without basing them on human preferences. We introduce DuplexGen, a framework for generating dialogues with scenario-adaptive turn-taking by calibrating LLM predictions against a small set of slot-level human preference annotations. In six cooperative and competitive tasks, human turn-taking preferences differ systematically, and DuplexGen aligns substantially more closely with those preferences than uncalibrated prompting or training solely on generic human-human data; a full-duplex model trained on DuplexGen-generated data exhibits distinctive, human-preferred turn-taking behaviors. These results show that human calibration, not corpus scale or prompt design alone, is what allows turn-taking synthesis to be scenario-specific.

## Metadata
- **Published**: 2026-07-28T18:36:46Z
- **Authors**: Takyoung Kim, Kang-wook Kim, Sang Hoon Woo, Julia Hirschberg, Gunhee Kim, Dilek Hakkani-Tür
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26178v1)