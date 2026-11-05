---
title: Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale
published: 2026-11-03T08:41:31Z
authors: Brett Daley, Ilya Gorbachev, Anubhav Natani, Nicholas Brown, Athena Dai, Rachel Song, Marcin Pekalski, Josip Domazet, Anchal Choubey, Daniel Ting
url: http://arxiv.org/abs/2611.04515v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale

## Abstract
A/B testing underpins product decisions by providing trustworthy, reproducible quantification of proposed changes' effects. Growing large language model (LLM) capabilities have motivated efforts to automate experimentation workflows. Yet LLMs are nondeterministic and prone to hallucination, properties that conflict with the trust experimentation systems must provide. Experiments are also operationally messy: diagnosing anomalies, debugging configurations, and conducting bespoke follow-up analyses require flexible reasoning and manual effort. These tasks let agents accelerate experimentation without replacing its deterministic statistical foundations.   We report lessons from building and operating such an agent. Our central finding is that this tension is resolved not by making the model deterministic, but by bounding where its nondeterminism can reach; the model selects and sequences procedures, while deterministic code computes every quantity it reports. Three consequences surprised us: withholding information from the model improved its answers, demand concentrated on mundane retrieval rather than the autonomous decisions we anticipated, and the agent's eagerness to help threatened statistical validity.

## Metadata
- **Published**: 2026-11-03T08:41:31Z
- **Authors**: Brett Daley, Ilya Gorbachev, Anubhav Natani, Nicholas Brown, Athena Dai, Rachel Song, Marcin Pekalski, Josip Domazet, Anchal Choubey, Daniel Ting
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.04515v1)