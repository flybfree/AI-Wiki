---
title: Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning
published: 2026-07-31T09:30:33Z
authors: Xinyan Guan, Jiali Zeng, Chunlei Xin, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Fandong Meng
url: http://arxiv.org/abs/2607.29211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

## Abstract
Large language models generate computationally expensive yet semantically void reasoning on beyond-capability tasks, creating risks where plausible-sounding but incorrect derivations mislead users. We characterize this \textit{futile reasoning} phenomenon through systematic analysis, revealing universal capability overreach and systematic miscalibration between capability and behavior. The dominant failure mode is specious reasoning, which outputs look superficially valid but contain subtle errors, escalating with task difficulty. To address this, we introduce \textbf{CaRL} (\textbf{Ca}pability-\textbf{a}ligned \textbf{R}einforcement \textbf{L}earning), which aligns model behavior with capability boundaries through reward shaping that incentivizes refusal over futile reasoning and hindsight refusal augmentation that converts failures into refusal supervision. Experiments demonstrate a substantial reduction in futile reasoning while preserving performance across task difficulties, effectively achieving capability-aligned behavior without sacrificing utility. \footnote{https://github.com/icip-cas/Knowing-When-to-Quit}

## Metadata
- **Published**: 2026-07-31T09:30:33Z
- **Authors**: Xinyan Guan, Jiali Zeng, Chunlei Xin, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Fandong Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29211v1)