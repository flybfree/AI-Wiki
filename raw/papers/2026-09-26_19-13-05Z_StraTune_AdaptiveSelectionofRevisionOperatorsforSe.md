---
title: StraTune: Adaptive Selection of Revision Operators for Self-Evolving LLM Skills
published: 2026-09-26T19:13:05Z
authors: Zeping Liu, Yan Li, Ni Lao, Gil Wolff, Gengchen Mai
url: http://arxiv.org/abs/2609.32886v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StraTune: Adaptive Selection of Revision Operators for Self-Evolving LLM Skills

## Abstract
Large language models (LLMs) can learn reusable textual skills from execution feedback without updating their parameters, but effectively deciding how to revise these skills remains a key challenge. Existing methods typically rely on a fixed revision operator, a search strategy and the revision forms applied under it. However, we observe that no single revision operator consistently performs best across tasks, and repeatedly applying an unsuitable operator can limit further improvement. We propose StraTune (strategy-guided skill tuning), which lets a frozen optimizer LLM choose the revision operator at every round from the optimization state, which is defined as the current execution feedback together with the recorded outcomes of earlier strategies and forms. Candidate skills from every revision operator pass one candidate evaluation, which screens for gains and regressions on a small sample set and validates them on a larger one, and every outcome is written back to the optimization state for later choices. Across four benchmarks and two LLM settings, StraTune outperforms all five baselines in most settings. Ablations attribute the gains to the adaptive choice of the revision operator, since fixed, random, scheduled, and bandit strategy choices all score lower, and skills learned with a small target LLM also improve a stronger one. Code and learned skills are available at https://github.com/seai-lab/StraTune.

## Metadata
- **Published**: 2026-09-26T19:13:05Z
- **Authors**: Zeping Liu, Yan Li, Ni Lao, Gil Wolff, Gengchen Mai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32886v1)