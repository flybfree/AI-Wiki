---
title: The Marathon of Scientific Reasoning: Robustness of Scientific Agents to Perturbations in Multi-Turn Interactions
published: 2026-09-28T08:04:00Z
authors: Xiaoting Lyu, Xinbo Ma, Yufei Han, Hangwei Qian, Ziyang Lin, Bin Wang, Bin Wang, Wei Wang
url: http://arxiv.org/abs/2609.34537v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Marathon of Scientific Reasoning: Robustness of Scientific Agents to Perturbations in Multi-Turn Interactions

## Abstract
Large language model (LLM)-based scientific agents are increasingly used for scientific problem solving, yet their robustness to imperfections arising during multi-turn interactions remains poorly understood. We introduce \textsc{SciARP} (\textbf{Sci}entific \textbf{A}gent \textbf{R}obustness to \textbf{P}erturbations), a benchmark for evaluating scientific agents under scientifically plausible perturbations throughout multi-turn problem solving. \textsc{SciARP} transforms 620 scientific problems into interdependent tasks of 3--13 turns and defines 13 perturbation types spanning problem understanding, evidence processing, reasoning, and conclusion formation. Clean and perturbed versions of each task are independently executed under matched settings, producing paired live trajectories for evaluating both task success and process reliability. Experiments across eight LLMs from four model families reveal three key robustness characteristics. First, different classes of scientific perturbations exhibit distinct robustness profiles and can decouple task progression from scientific reliability: agents may continue advancing through the task even after their information or reasoning has become unreliable. Second, stronger clean-task performance does not necessarily translate into stronger robustness, as models with higher clean-task accuracy can exhibit larger degradation under perturbation. Third, perturbation effects exhibit strong temporal dynamics: they may remain latent for multiple turns before emerging and subsequently propagate through downstream dependencies. Together, these findings show that current scientific agents remain insufficiently robust to scientifically plausible perturbations, with failures often remaining undetected, propagating, and resisting recovery.

## Metadata
- **Published**: 2026-09-28T08:04:00Z
- **Authors**: Xiaoting Lyu, Xinbo Ma, Yufei Han, Hangwei Qian, Ziyang Lin, Bin Wang, Bin Wang, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34537v1)