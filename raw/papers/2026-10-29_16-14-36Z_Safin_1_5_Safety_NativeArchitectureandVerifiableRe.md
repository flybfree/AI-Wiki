---
title: Safin-1.5: Safety-Native Architecture and Verifiable Reasoning for Recursive Safety Improvement
published: 2026-10-29T16:14:36Z
authors: Jingnan Zheng, Cheng Jin, Ming Zhang, Huan Sun, Zhongtian Ma, Kaisen Yang, Ziyuan Zhou, Tong Wu, Dongcheng Zhang, Yi Zhang, Xiao Wang, Han Qi, Shu Yu, Ermo Hua, Zongji Yu, Chaozhuo Li, Xiaoyu Wen, Zhekai Chen, Jiawei Zhou, Sirui Chen, Ning Ding, An Zhang, Tat-Seng Chua, Xiangnan He, Xia Hu, Bowen Zhou, Qiaosheng Zhang, Youbang Sun, Xiang Wang, Zhongyu Huang, Chaochao Lu
url: http://arxiv.org/abs/2610.40751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safin-1.5: Safety-Native Architecture and Verifiable Reasoning for Recursive Safety Improvement

## Abstract
Recursive self-improvement (RSI) enables large language models to advance their capabilities through successive updates, but these updates can also introduce new risks and weaken existing safeguards. In line with the AI-45° Law, we pursue Safety RSI, in which safety develops as an intrinsic capability alongside general model capabilities through continual risk discovery and repair, while preserving utility and limiting over-refusal. We introduce Safin-1.5, a model built on a safety architecture and trained through recursive safety improvement, with an inference-time harness that extends its capabilities to formal reasoning. Our approach comprises three components: i) The safety architecture combines persistent safety states with hazardous-knowledge disentanglement. The former retains and selectively invokes safety knowledge, while the latter relocates targeted hazardous knowledge into removable experts, enabling its removal with minimal impact on general capabilities. ii) Recursive safety improvement establishes a discovery-evaluation-repair loop. The loop identifies new vulnerabilities and uses experimental feedback to develop repair strategies. It accepts updates only when they improve safety while preserving general capabilities and limiting over-refusal. iii) The formal reasoning harness combines the model's language understanding with symbolic inference and verification. Proof-obligation-guided semantic bridging recovers missing relations in formal representations, enabling symbolic solvers to construct checkable proofs under formalized premises and accepted semantic bridges. Experimental results demonstrate that Safin-1.5 achieves safety and reasoning performance, outperforming frontier models.

## Metadata
- **Published**: 2026-10-29T16:14:36Z
- **Authors**: Jingnan Zheng, Cheng Jin, Ming Zhang, Huan Sun, Zhongtian Ma, Kaisen Yang, Ziyuan Zhou, Tong Wu, Dongcheng Zhang, Yi Zhang, Xiao Wang, Han Qi, Shu Yu, Ermo Hua, Zongji Yu, Chaozhuo Li, Xiaoyu Wen, Zhekai Chen, Jiawei Zhou, Sirui Chen, Ning Ding, An Zhang, Tat-Seng Chua, Xiangnan He, Xia Hu, Bowen Zhou, Qiaosheng Zhang, Youbang Sun, Xiang Wang, Zhongyu Huang, Chaochao Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.40751v1)