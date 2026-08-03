---
title: Mirror Learning
published: 2026-07-30T18:00:31Z
authors: Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood
url: http://arxiv.org/abs/2607.28737v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mirror Learning

## Abstract
We investigate imitation learning through the lens of third-person observation and propose a framework for mirror learning: acquiring actionable policies from passive observation. While behavior cloning (BC) excels under dense, well-aligned first-person data, it fundamentally fails to leverage the rich observational signals arising from third-person demonstrations that humans and animals routinely exploit. We introduce a method that composes (i) a learned perspective transformation that places learners in demonstrators' shoes using a fine-tuned video diffusion model and (ii) an inverse dynamics model that infers action trajectories in the learners' control space. This enables the synthesis of mirror data, pseudo first-person expert data generated from third-person observations of demonstrator behavior. Empirically, we show that mirror data alone can train effective policies, and that augmenting first-person BC training with mirror data further improves downstream policy performance. Our results suggest that modern generative world models implicitly encode sufficient structure to enable a scalable and safe alternative to teleoperation-heavy data collection.

## Metadata
- **Published**: 2026-07-30T18:00:31Z
- **Authors**: Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28737v1)