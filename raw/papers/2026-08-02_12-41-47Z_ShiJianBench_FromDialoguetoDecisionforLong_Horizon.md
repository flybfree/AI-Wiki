---
title: ShiJianBench: From Dialogue to Decision for Long-Horizon Evaluation of Investment Advisors
published: 2026-08-02T12:41:47Z
authors: Jie Gong, Maowei Jiang, Zhiwei Liu, Yang Qiao, Wenxi Wu, Mengxi Xiao, Enze Zhang, Ziyan Kuang, Yankai Chen, Caishuang Huang, Meng Zhou, Xiku Du, Xue Liu, Guojun Xiong, Min Peng, Qianqian Xie, Sophia Ananiadou
url: http://arxiv.org/abs/2608.01204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ShiJianBench: From Dialogue to Decision for Long-Horizon Evaluation of Investment Advisors

## Abstract
Conversational investment advisors influence not only what users know, but also how they make subsequent decisions as market conditions evolve. Existing evaluations primarily assess response quality or observed outcomes, leaving the long-horizon pathway from advisor language to investor behavior difficult to audit. We introduce ShiJianBench, an offline framework for evaluating conversational investment advisors through matched investor trajectories under fixed historical market feedback. At its core is a multi-agent investor simulator with explicit evolving state variables, motive-driven deliberation, long-term memory, and dialogue-grounded updates. The simulator is calibrated against aggregate behavioral patterns from 7,199 real users, and advisor policies are evaluated using separate investor-side, service-side, and content-side metrics under a hard compliance gate. Experiments on Chinese fund-market traces from 2021 to 2026 identify a stable leading group of LLM advisors that combines substantially stronger personalized content with competitive investor-side trajectory outcomes. These results reveal a systematic distinction between producing a high-quality response and delivering an effective long-horizon intervention, motivating trajectory-aware evaluation of conversational advisors.

## Metadata
- **Published**: 2026-08-02T12:41:47Z
- **Authors**: Jie Gong, Maowei Jiang, Zhiwei Liu, Yang Qiao, Wenxi Wu, Mengxi Xiao, Enze Zhang, Ziyan Kuang, Yankai Chen, Caishuang Huang, Meng Zhou, Xiku Du, Xue Liu, Guojun Xiong, Min Peng, Qianqian Xie, Sophia Ananiadou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01204v1)