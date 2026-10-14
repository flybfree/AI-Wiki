---
title: OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools
published: 2026-10-09T17:26:38Z
authors: Chenyang Yan, Yingying Zhang, Kanzhi Cheng, Qiushi Sun, Zhengyuan Pan, Zheng Ma, Hang Yan, Yian Wang, Nuo Chen, Jialin Cao, Xingdong Gong, Wenpo Song, Han Chen, Zichen Ding, Fangzhi Xu, Shujian Huang, Xinyu Dai, Yichen Liu, Tiankuo Yao, Bo Wang, Ben Kao, Jianbing Zhang, Lewei Lu, Dahua Lin
url: http://arxiv.org/abs/2610.14157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools

## Abstract
We introduce OpenMobile-2, a near-frontier mobile agent with fully open training environments and recipes. We make three key advances: (1) Diverse environments with simulated commercial apps: We build MobileGym++, featuring 35 realistic, functionally rich commercial-style apps with cross-app workflows, while preserving full controllability for reset and verification. Together with newly configured apps in Android emulators, this yields a diverse playground spanning over 110 apps. (2) Open training data at scale: Building on this foundation, we curate nearly 12K mobile interaction trajectories for supervised fine-tuning and the largest open collection of verifiable RL training data for mobile agents, comprising over 2K executable tasks with automatic rewards. (3) Hybrid GUI and app-native tool use: We explore an experimental mobile-use setting where apps expose selected functionalities as app-native tools alongside their GUIs, allowing agents to interleave GUI actions and tool calls within a task. We implement this setting in MobileGym++ with over 300 carefully scoped tools across 50+ apps. Additionally, we introduce MobileGym++ Bench for complex, long-horizon commercial mobile scenarios, supporting both GUI-only and hybrid GUI-tool evaluation on a shared task suite. OpenMobile-2 performs competitively across established benchmarks, including AndroidWorld (79.9) and MobileWorld (50.4), while showing promising transfer to real-device mobile use, nearly doubling SPA-Bench performance from 31.9 to 59.6. All resources are available at https://os-copilot.github.io/OpenMobile2-Home/.

## Metadata
- **Published**: 2026-10-09T17:26:38Z
- **Authors**: Chenyang Yan, Yingying Zhang, Kanzhi Cheng, Qiushi Sun, Zhengyuan Pan, Zheng Ma, Hang Yan, Yian Wang, Nuo Chen, Jialin Cao, Xingdong Gong, Wenpo Song, Han Chen, Zichen Ding, Fangzhi Xu, Shujian Huang, Xinyu Dai, Yichen Liu, Tiankuo Yao, Bo Wang, Ben Kao, Jianbing Zhang, Lewei Lu, Dahua Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14157v1)