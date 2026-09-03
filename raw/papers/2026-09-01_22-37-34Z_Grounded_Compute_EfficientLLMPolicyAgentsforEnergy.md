---
title: Grounded, Compute-Efficient LLM Policy Agents for Energy-Poverty Equity in Physically-Constrained Peer-to-Peer Energy Markets
published: 2026-09-01T22:37:34Z
authors: Kunal Jadhav, Siddhesh More
url: http://arxiv.org/abs/2609.01918v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Grounded, Compute-Efficient LLM Policy Agents for Energy-Poverty Equity in Physically-Constrained Peer-to-Peer Energy Markets

## Abstract
Energy poverty is nearly absent from NLP-for-social-good, and the little existing work is either static retrieval/QA or relies on carbon-intensive cloud LLMs, a self-defeating "computational irony" for a humanitarian setting. We present EqGrid, a closed-loop simulation in which a low-frequency, open-weight LLM policy agent sets price and carbon bounds and targeted subsidies over a community of empirically-grounded household personas, while high-frequency multi-agent RL traders clear a continuous double auction constrained by a physical distribution grid (IEEE-33-bus with Dynamic Operating Envelopes). Our contribution is threefold and directly addresses how to measure the social impact of AI: (i) grounded personas (region-matched socio-demographics) whose load curves are checked for shape and level realism against real smart-meter data; (ii) formal energy-poverty equity metrics (Energy Burden, Gini of EB, LIHC) showing the intervention reduces burden inequality without raising net grid cost; and (iii) a compute-efficiency frontier that measures how much equity performance survives compressing the policy agent from a 235B teacher down to a sub-1B model deployable on a laptop, in estimated energy/carbon per decision. A decoupled-safety design (the LLM sets bounds; a validate-and-project grid gate executes) yields zero grid-constraint violations versus 55 under direct LLM control. On energy-poverty equity, the LLM policy lowers the Gini of energy burden to 0.305 (from 0.351) and mean burden by 28% while cutting cost (outperforming a tuned rule baseline), and a 3B-active model retains 95% of the benefit at roughly 9x lower inference energy than the teacher, with even a 0.8B on-device model retaining 92% at roughly 24x lower energy. We will release code and configs.

## Metadata
- **Published**: 2026-09-01T22:37:34Z
- **Authors**: Kunal Jadhav, Siddhesh More
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01918v1)