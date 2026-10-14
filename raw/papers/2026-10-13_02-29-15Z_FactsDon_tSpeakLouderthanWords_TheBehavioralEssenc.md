---
title: Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation
published: 2026-10-13T02:29:15Z
authors: Yongcan Yu, Jian Liang, Lingxiao He, Kuangpu Guo, Yanbo Wang, Shuo Lu, Meng Wang, Ran He
url: http://arxiv.org/abs/2610.17607v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation

## Abstract
While long chain-of-thought (CoT) distillation significantly improves the reasoning abilities of language models, its underlying mechanism remains poorly understood. Current pipelines generally rely on rejection sampling to gather reasoning traces across diverse prompts, assuming that factual correctness and broad problem coverage are indispensable. Surprisingly, we find that training exclusively on flawed reasoning trajectories or a restricted prompt set yields nearly comparable performance. Driven by this counterintuitive finding, we propose the Behavioral Hypothesis: the essence of Long-CoT distillation is behavioral alignment with structured reasoning patterns, rather than factual knowledge memorization. We then validate this by demonstrating substantial reasoning gains even when models are fine-tuned exclusively on previously mastered problems-effectively isolating behavioral alignment from novel knowledge injection. Having established that reasoning patterns are the true bottleneck, we investigate how to learn them across varying levels of complexity optimally. We reveal a critical interplay: while the recent probability-based loss excels at learning simple patterns, the standard cross-entropy loss is essential for scaling to complex CoTs. We believe these insights demystify CoT distillation and provide a principled foundation for the future development of reasoning models. Code is available on https://github.com/yuyongcan/Long-CoT-Distillation.

## Metadata
- **Published**: 2026-10-13T02:29:15Z
- **Authors**: Yongcan Yu, Jian Liang, Lingxiao He, Kuangpu Guo, Yanbo Wang, Shuo Lu, Meng Wang, Ran He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17607v1)