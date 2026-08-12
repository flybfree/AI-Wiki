---
title: UserToolBench: A User-Profile-Hidden Benchmark for Personalized Decision Making in Tool-Use LLMs
published: 2026-08-10T09:32:38Z
authors: Xuexiong Yin, Zechuan Chen, Yongsen Zheng, Yuxiang Zhang, Jingyuan Yang, Bin Wang, Yubin Wang, Keze Wang
url: http://arxiv.org/abs/2608.10042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UserToolBench: A User-Profile-Hidden Benchmark for Personalized Decision Making in Tool-Use LLMs

## Abstract
Tool-use LLMs are increasingly asked to act on users' behalf, but existing benchmarks usually focus on profile recall, style imitation, generic tool use, or response-level personalization. We introduce UserToolBench , a benchmark for personalized decision making in tool-use LLMs. UserToolBench tests whether a model can infer latent user preferences from interaction history, recognize when clarification is needed, and produce user-aligned tool-call trajectories under incomplete information. The benchmark is built from privacy-sanitized real interaction traces and combines structured persona profiles, public API-style tool ecosystems, and long-horizon multi-turn trajectories. It includes 10 user profiles, 36 tool sets, 1,065 turns, 170 unique tools, and evaluation-focused task types covering lack-of-information, single-tool, and multi-tool settings. Experiments with strong tool-use LLMs show that current models still have difficulty with personalized delegation. Multi-tool coordination, missing-constraint inference, and long-horizon behavioral consistency remain major bottlenecks. These results suggest that personalization evaluation should move beyond asking whether outputs sound user-specific and instead ask whether LLMs make correct decisions for the users they represent.

## Metadata
- **Published**: 2026-08-10T09:32:38Z
- **Authors**: Xuexiong Yin, Zechuan Chen, Yongsen Zheng, Yuxiang Zhang, Jingyuan Yang, Bin Wang, Yubin Wang, Keze Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10042v1)