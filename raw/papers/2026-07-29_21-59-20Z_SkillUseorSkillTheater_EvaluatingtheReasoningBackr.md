---
title: Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents
published: 2026-07-29T21:59:20Z
authors: Jinwei Hu, Yi Qi, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang
url: http://arxiv.org/abs/2607.27484v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill Use or Skill Theater? Evaluating the Reasoning Backroom in Skill-Augmented Language Agents

## Abstract
Reusable skills are becoming a standard interface for extending language agents with task procedures. Yet evaluators usually infer skill use from visible reasoning or the agent's own attribution. These signals show what the agent appears to use, not whether the skill changed its decision. We ask whether skill-augmented agents exhibit a \textbf{Reasoning Backroom}, a systematic gap between stated skill use and intervention-measured influence. We introduce BACKTRACE, an evaluation framework that pairs each skill-conditioned answer with a matched no-skill counterfactual, intervenes on skill meaning, wording, identity, content, and assignment, and elicits attribution only after the answer is committed. We instantiate the framework as BACKROOMBench, a verified testbed spanning controlled logic and competition mathematics, multiple skill conditions, single-agent and multi-agent settings, and diverse model families. Our evaluation reveals a pervasive provenance failure. Across models and domains, stated skill use often remains stable while causal reliance and signed utility vary, producing both silent uptake and performative use. Behavioral effects follow procedural content more reliably than displayed skill identity, whereas stated attributions respond strongly to artifact availability. Observational detectors based on direct skill-use claims, text mentions, trace similarity, and an LLM judge do not identify which decisions actually depend on the skill. In multi-agent systems, skill influence can survive communication even after its source is lost, while no-skill teams still name skills and sources that were never supplied. These findings establish the Reasoning Backroom as a general AI provenance problem whose audit requires intervention.

## Metadata
- **Published**: 2026-07-29T21:59:20Z
- **Authors**: Jinwei Hu, Yi Qi, Xinmiao Huang, Youcheng Sun, Yi Dong, Xiaowei Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27484v1)