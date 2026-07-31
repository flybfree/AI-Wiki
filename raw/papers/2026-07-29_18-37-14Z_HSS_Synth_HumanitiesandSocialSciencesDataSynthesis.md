---
title: HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs
published: 2026-07-29T18:37:14Z
authors: Ru Peng, Tianyu Zhao, Xijun Gu, Zhiting Fan, Haokai Xu, Jinyang Zhang, Yawen Zeng, Yihong Zhuang, Kexin Yang, Junyang Lin, Dayiheng Liu, Junbo Zhao
url: http://arxiv.org/abs/2607.27379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs

## Abstract
High-quality, diverse data are vital for large language models (LLMs) but remain scarce and costly. Data synthesis is a viable alternative and succeeds on closed tasks, yet the humanities and social sciences (HSS) are overlooked, and their open-ended nature makes synthesis challenging. Moving beyond prior capability-centric, fragmented attempts, we adopt a subject-centric paradigm, define the first HSS domain system covering 14 mainstream fields, and introduce HSS-Synth, the first data synthesis pipeline for HSS. HSS-Synth comprises: (1) constructing seed documents from web corpora via multi-step filtering and text refinement evaluated by a judge; (2) specifying "requirements + persona" to backtranslate seed documents into diverse yet faithful instructions with a strict Q&A alignment check; and (3) breaking LLM response limits via teacher-forced Answering that feeds seed documents during response generation to anchor semantics, reduce hallucinations, and preserve tone and integrity. HSS-Synth yields 237k high-quality, diverse instruction-tuning samples that outperform 14 leading baselines on 16 benchmarks. The fine-tuned Qwen3-8B-Base sets a new SOTA and approaches the official Qwen3-8B, improving both human preference and knowledge capabilities without performance seesaws. Extensive experiments demonstrate HSS-Synth's robustness and transferability. Our code is publicly available at https://github.com/pengr/HSS-Synth.

## Metadata
- **Published**: 2026-07-29T18:37:14Z
- **Authors**: Ru Peng, Tianyu Zhao, Xijun Gu, Zhiting Fan, Haokai Xu, Jinyang Zhang, Yawen Zeng, Yihong Zhuang, Kexin Yang, Junyang Lin, Dayiheng Liu, Junbo Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27379v1)