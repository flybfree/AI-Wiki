---
title: Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation
published: 2026-10-26T13:33:07Z
authors: Atri Vivek Sharma, Brian Formento, Alessio Lomuscio
url: http://arxiv.org/abs/2610.35426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation

## Abstract
Multi-turn agents are commonly evaluated with LLM-based simulated users, which can be overly cooperative and can therefore overestimate an agent's performance. We here introduce StressSim, an intent-preserving adversarial user simulator framework for stress-testing agents with challenging yet valid user interactions. StressSim optimises the simulator's high-level adversarial plan for each task instance. Candidate planner prompts are evolved with a genetic prompt-optimisation loop that uses rollout traces, granular task-completion signals, and validity feedback to favour conversations that reduce task success without changing the user's underlying goal. We evaluate the approach on the MultiWOZ dataset and the retail and airline domains from tau-bench with three target LLM agents, comparing against standard simulators and hand-designed non-collaborative user behaviours. We demonstrate the effectiveness of StressSim in exposing robustness gaps across frontier LLMs, with tau-bench pass^4 scores decreasing by up to 69% on gemini-3.8-flash and 62% on gpt-5.6-sol. StressSim maintains goal preservation performance (which decreases by at most 10%), using an optimisation budget of 20 rollouts per task. Sensitivity analysis suggests that increasing the budget further decreases task success. Overall our results demonstrate that StressSim exposes robustness gaps missed by standard and hand-designed user simulators while maintaining conversation realism. This is achieved through lightweight prompt optimisation alone, without model fine-tuning.

## Metadata
- **Published**: 2026-10-26T13:33:07Z
- **Authors**: Atri Vivek Sharma, Brian Formento, Alessio Lomuscio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35426v1)