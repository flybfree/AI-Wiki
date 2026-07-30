---
title: Pramana: A Composable, Domain-Specific Backend for Empirical Networking Research
published: 2026-07-28T23:51:57Z
authors: Jaber Daneshamooz, Eugene Vuong, Alagappan Ramanathan, Manni Moghimi, Haarika Manda, Satyam Kumar, Snithik Thode, Satyandra Guthula, Sylee Beltiukov, Dongsu Han, Tarun Mangla, Sangeetha Abdu Jyothi, Walter Willinger, Arpit Gupta
url: http://arxiv.org/abs/2607.26352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pramana: A Composable, Domain-Specific Backend for Empirical Networking Research

## Abstract
Networking research advances by turning hypotheses into empirical evidence, so accelerating it means reducing the lag between ideation (synthesizing a hypothesis) and generating the data that tests it. Consider a concrete case: does a bulk BBR download fairly share its bottleneck with competing real-time Google Meet traffic? Validating this requires configuring a realistic bottleneck link, concurrently generating BBR's bulk transfer and Meet's real-time traffic, and collecting relevant service-quality metrics. Today this overhead is high, often forcing researchers to start from scratch for every new idea. This ideation-to-data-generation gap will only worsen in the agentic AI era, where AI-assisted ideation accelerates exponentially, yet its outputs cannot be validated without a data-generation backend.   This paper explores how to bridge this gap. We envision a composable, domain-specific backend, Pramana, shaped as a thin waist, with diverse research intents at the top and disparate execution substrates at the bottom. Pramana realizes this waist through a single contract, the intent specification, which disaggregates an experiment into three independent axes: the intent (what data to generate), the substrate (where to generate it), and the mechanism (how to produce it), so one specification runs on any substrate. We demonstrate Pramana's utility by building a first-of-its-kind corpus of 255 data-generation intents mined from 66 published papers, and show the intent specification satisfies all of them, where no existing tool satisfies more than 13%. Our current proof-of-concept implementation already satisfies 34% of these intents, more than twice the best existing tool, and we lay out a roadmap for closing this abstraction-implementation gap through a broader community effort to build the envisioned data-generation backend and accelerate empirical networking research.

## Metadata
- **Published**: 2026-07-28T23:51:57Z
- **Authors**: Jaber Daneshamooz, Eugene Vuong, Alagappan Ramanathan, Manni Moghimi, Haarika Manda, Satyam Kumar, Snithik Thode, Satyandra Guthula, Sylee Beltiukov, Dongsu Han, Tarun Mangla, Sangeetha Abdu Jyothi, Walter Willinger, Arpit Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26352v1)