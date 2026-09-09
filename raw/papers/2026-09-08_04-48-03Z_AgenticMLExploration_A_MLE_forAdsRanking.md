---
title: Agentic ML Exploration (A-MLE) for Ads Ranking
published: 2026-09-08T04:48:03Z
authors: Erwin Gao, Vinodh Kumar Sunkara, Jingyi Guan, Qinjin Jia, Hangjun Xu, Xiang Ji, Sherman Wong, Surya Teja Chavali, Pratik Vaishnavi, Aryan Pandhi, Xiaoyu Deng, Zhaodong Wang, Samarth Inani, Fan Yang, Jakob Moberg, Zoe Zu, Nicolas Bievre, Sami Khenissi, Amit Jaspal, Ehsan Fakharizadi, Srinidhi Viswanathan, Dorothy Sun, Abishek Vanam, Sneha Iyer, Sheela Yadawad, Wenjie Chen, Gaby Nahum, Junhua Gu, Peter Chu, Yucheng Liu, Xin Zhao, Vitor Cid, Chaorong Chen, Vijay Pappu, Ashwin Kumar, Wenlin Chen, Ben Schulte, Deepak Chandra, Ritwik Tewari
url: http://arxiv.org/abs/2609.08248v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic ML Exploration (A-MLE) for Ads Ranking

## Abstract
Modern industrial ads ranking stacks are increasingly bottlenecked not by model capacity or training compute, but by the throughput of human ML iteration - the cycles of research, implementation, training, debugging, evaluation, and launch required to surface a single statistically significant improvement. A typical ranking stack contains numerous differentiated models with heterogeneous data, architectures, and infrastructure constraints, and each cycle takes days to weeks of senior engineer attention per model. As a result, techniques that have proven effective on one model diffuse into others slowly and unevenly, leaving substantial recoverable signal unexplored. We present Agentic ML Exploration (A-MLE), an autonomous LLM-agent system that systematically explores ML techniques across a portfolio of ads ranking models. A-MLE decomposes ML iteration into five stages involving hypothesis generation, exploration strategy, experiment execution, result analysis and shared knowledge substrate which are orchestrated by a single agent that invokes domain-specific skills and agentic workflows against a sandboxed execution layer, with human-in-the-loop checkpoints at each stage boundary. We deploy A-MLE across a representative set of large-scale ads ranking models and evaluate it along a tiered capability framework (tool availability, autonomous workflow execution, and open-ended exploration). We further report a controlled cross-LLM study using a fixed agent loop, which surfaces qualitative differences in execution reliability and exploration aggressiveness across the Claude Sonnet, Gemini, and GPT families. We discuss failure modes and the design choices that govern reliability. Our findings suggest that agentic exploration is a practical force multiplier for ML engineers in industrial recommenders, especially for the long tail of models that rarely receive expert attention.

## Metadata
- **Published**: 2026-09-08T04:48:03Z
- **Authors**: Erwin Gao, Vinodh Kumar Sunkara, Jingyi Guan, Qinjin Jia, Hangjun Xu, Xiang Ji, Sherman Wong, Surya Teja Chavali, Pratik Vaishnavi, Aryan Pandhi, Xiaoyu Deng, Zhaodong Wang, Samarth Inani, Fan Yang, Jakob Moberg, Zoe Zu, Nicolas Bievre, Sami Khenissi, Amit Jaspal, Ehsan Fakharizadi, Srinidhi Viswanathan, Dorothy Sun, Abishek Vanam, Sneha Iyer, Sheela Yadawad, Wenjie Chen, Gaby Nahum, Junhua Gu, Peter Chu, Yucheng Liu, Xin Zhao, Vitor Cid, Chaorong Chen, Vijay Pappu, Ashwin Kumar, Wenlin Chen, Ben Schulte, Deepak Chandra, Ritwik Tewari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08248v1)