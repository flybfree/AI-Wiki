---
title: BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents
published: 2026-09-11T03:36:35Z
authors: Tong Ye, Kunyang Han, Guozhi Wang, Longqiang Luo, Zhifeng Ding, Yongxiang Zhang, Xiaolei Shen, Yuxuan Zhang, Zhuping Zhang, Tao Xu, Yue Pan, Yucheng Zhao, Yupei Hu, Yuanjiang Ouyang, Danfeng Shen, Runqi Lin, Hongda Cai, Zhaoxiong Wang, Mengjia Yan, Yingjie Zhong, Chen Zhou, Zeyu Zhang, Xuwen Zhu, Penggang Shi, Mingcheng Luo, Ziyang Wu, Min Jin, Mingfu Shen, Zairong Xu, Fan Zhang, Hao Wang, Liang Liu, Zhulin Xie, Lijun Yao, Xiao Liang, Liangmin Wen, Liqiang Feng, Feilong Wu, Min Hu, Min Chen, Guanjing Xiong, Xiaohu Ruan, Xiaoxin Chen
url: http://arxiv.org/abs/2609.12394v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents

## Abstract
Mobile GUI agents are shifting from multi-module frameworks to native models trained end-to-end, yet industrial deployment faces three persistent gaps. Sandbox training produces a distribution mismatch with production environments; expensive real-device failures remain underutilized; and fixed benchmarks saturate, losing the power to guide iteration. We present BlueLM-GUI, a 35B-A3B mobile GUI agent built as a real-device-centric flywheel that closes these gaps through three principles. Every Sample Matters: a dual-track pipeline with Heterogeneous Triple-System Consensus evaluation and an Error Correction \& Derivation Module salvages every trajectory into usable supervision. Every Rollout Is Real: a three-stage recipe---continual pre-training, supervised fine-tuning, and agentic reinforcement learning on hundreds of real phones---grounds every rollout in real production environments, so the capability the model learns transfers directly to deployment. Every Query Evolves: a quota-driven benchmark methodology with three orthogonal axes enables precise attribution and allows the benchmark to be systematically upgraded as the model improves. BlueLM-GUI achieves 87.4 on MobileGUI-VBench, surpassing the best closed-source model by 5.1 points, and 84.9 on AndroidWorld, the best result among open-source models and competitive with closed-source models. These results demonstrate that grounding model training and iterative improvement in both real devices and the three Every principles yields strong, robust, and transferable mobile GUI capability.

## Metadata
- **Published**: 2026-09-11T03:36:35Z
- **Authors**: Tong Ye, Kunyang Han, Guozhi Wang, Longqiang Luo, Zhifeng Ding, Yongxiang Zhang, Xiaolei Shen, Yuxuan Zhang, Zhuping Zhang, Tao Xu, Yue Pan, Yucheng Zhao, Yupei Hu, Yuanjiang Ouyang, Danfeng Shen, Runqi Lin, Hongda Cai, Zhaoxiong Wang, Mengjia Yan, Yingjie Zhong, Chen Zhou, Zeyu Zhang, Xuwen Zhu, Penggang Shi, Mingcheng Luo, Ziyang Wu, Min Jin, Mingfu Shen, Zairong Xu, Fan Zhang, Hao Wang, Liang Liu, Zhulin Xie, Lijun Yao, Xiao Liang, Liangmin Wen, Liqiang Feng, Feilong Wu, Min Hu, Min Chen, Guanjing Xiong, Xiaohu Ruan, Xiaoxin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12394v1)