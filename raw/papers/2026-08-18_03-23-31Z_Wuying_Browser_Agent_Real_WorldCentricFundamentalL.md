---
title: Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents
published: 2026-08-18T03:23:31Z
authors:  AIMAE Team, Tianxiang Chen, Yan Cheng, Zhangye Han, Xiaowei Li, Chang Liu, Cheng Liu, Zhongqiang Ma, Long Peng, Xiaobing Tu, Yinggui Wang, Hongliang Wei, Chen Wu, Daiping Xin, Kunyu Zhou, Pengyang Zhou, Peiyuan Chen, Ziyuan Chen, Yutao Deng, Chunyu Dong, Xiangyu Fu, Yicheng Feng, Ruian He, Haochen Li, Miancan Liu, Zhengqin Liu, Wei Peng, Jinkui Ren, Haoyu Tan, Dong Xiao, Rongkun Xue, Shujian Yang, Xianhang Ye, Ziqi Yuan, Ziyang Yu, Linghan Zhang, Xiantao Zhang, Xuanpu Zhao, Yinan Zhao, Zhenghui Zhao, Bin Zhu, Likai Zou
url: http://arxiv.org/abs/2608.17319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents

## Abstract
Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. We present Wuying-Browser-Agent, a unified framework that addresses each of these levels. A structured browser harness provides stable execution primitives and decision-oriented context management. Reflection and UI-specialized Curriculum SFT (RUIC-SFT) explicitly trains on recovery trajectories and complex-UI interactions. Divergence-Aware Online GRPO (DAO-GRPO) improves long-horizon credit assignment through potential-based reward shaping and divergence-aware step weighting. Finally, we introduce BrowserBench, a bilingual real-web benchmark of 350 tasks averaging 37.9 steps, because most existing benchmarks are too short to expose long-horizon failure modes. Wuying-Browser-Agent-27B achieves 80.6\% on WebVoyager, 66.7\% on Online-Mind2Web, and 65.1\% on BrowserBench, establishing a new open-source state of the art on browser-use benchmarks. The same pipeline also transfers beyond browser use, demonstrating strong general agentic ability and reaching an average score of 73.8 on Tau2-Bench, Claw-Eval, and BFCL-v4.

## Metadata
- **Published**: 2026-08-18T03:23:31Z
- **Authors**:  AIMAE Team, Tianxiang Chen, Yan Cheng, Zhangye Han, Xiaowei Li, Chang Liu, Cheng Liu, Zhongqiang Ma, Long Peng, Xiaobing Tu, Yinggui Wang, Hongliang Wei, Chen Wu, Daiping Xin, Kunyu Zhou, Pengyang Zhou, Peiyuan Chen, Ziyuan Chen, Yutao Deng, Chunyu Dong, Xiangyu Fu, Yicheng Feng, Ruian He, Haochen Li, Miancan Liu, Zhengqin Liu, Wei Peng, Jinkui Ren, Haoyu Tan, Dong Xiao, Rongkun Xue, Shujian Yang, Xianhang Ye, Ziqi Yuan, Ziyang Yu, Linghan Zhang, Xiantao Zhang, Xuanpu Zhao, Yinan Zhao, Zhenghui Zhao, Bin Zhu, Likai Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17319v1)