---
title: AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories
published: 2026-09-06T18:58:56Z
authors: Ruoxi Shang, Christina-Maria Androna, Orfeas Menis Mastromichalakis, Yu Feng, Aniruddhan Ramesh, Rico Angell, Shang Hong Sim, Chrysoula Zerva, Emmanouil Koukoumidis
url: http://arxiv.org/abs/2609.06783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories

## Abstract
LLM agents operate in workflows where unsafe actions can have real consequences. Existing safety evaluations often reduce behavior to a single score, obscuring risk recognition, pre-action detection, and safe task completion when a safe solution exists. We introduce AURA-Eval, a framework combining controlled augmentation with granular diagnosis of behavior in tool-use trajectories. Its pipeline identifies safety-critical decision points, generates controlled variations, and constructs counterparts differing in whether a request has a safe fulfillment path. Using 157 sourced trajectories, we generate 1,249 evaluation items and evaluate 20 frontier and open-weight models. We developed rubrics to classify risk detection, action strategy, and scenario-specific action safety. Our results show that LLM agents engage in unsafe behavior more often when no safe fulfillment path exists. In these cases, frontier proprietary models more often recognize risk and exhibit safer behavior by proposing alternatives, while evaluated open-weight models more often directly execute unsafe requests. Increasing impact or reducing opportunities for oversight before execution also exposes greater vulnerability across models.

## Metadata
- **Published**: 2026-09-06T18:58:56Z
- **Authors**: Ruoxi Shang, Christina-Maria Androna, Orfeas Menis Mastromichalakis, Yu Feng, Aniruddhan Ramesh, Rico Angell, Shang Hong Sim, Chrysoula Zerva, Emmanouil Koukoumidis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06783v1)