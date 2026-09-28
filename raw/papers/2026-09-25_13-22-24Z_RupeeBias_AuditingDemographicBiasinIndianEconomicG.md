---
title: RupeeBias: Auditing Demographic Bias in Indian Economic Guidance from Large Language Models
published: 2026-09-25T13:22:24Z
authors: Pavithra P M Nair, Bhavik Talaviya, Shourya Bhushan, Rahul Pankajakshan, Seema Guruvadoo, Avinash Agarwal, Gilad Gressel, Krishnashree Achuthan
url: http://arxiv.org/abs/2609.31245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RupeeBias: Auditing Demographic Bias in Indian Economic Guidance from Large Language Models

## Abstract
Individuals turn to large language models (LLMs) for guidance across a wide range of economic tasks, from comparing loan options and planning savings to deciding what raise to ask for or how much to charge for their services. LLMs are known to reproduce social biases, and biased economic guidance may influence what users believe they are worth, what they ask for, and what they ultimately accept. This risk is especially salient in India, where economic outcomes are shaped by demographic categories such as caste and urban-rural location. Existing LLM bias benchmarks, however, are largely designed around Western demographic categories and therefore miss key axes of economic disparity in the Indian context. We introduce RupeeBias, a benchmark for auditing demographic bias in LLM-generated economic guidance across Indian economic settings. RupeeBias consists of 39,150 prompts spanning four use cases: salary estimation, salary increment estimation, counter-offer recommendation, and service pricing recommendation. The benchmark follows a single-attribute counterfactual design, holding the description of the user's qualifications, experience, or service offering fixed while varying one demographic identifier at a time. RupeeBias covers 87 India-specific demographic identifiers across six axes: caste, religion, regional identity, gender, disability, and urban-rural location, with all prompts constructed in both English and Hinglish. We evaluate nine LLMs on RupeeBias and find systematic demographic disparities across all six axes. For otherwise identical prompts that differ only in demographic identifier, LLM-generated economic outputs differ by 20.2% on average. We publicly release RupeeBias to support future research on demographic bias in LLM-generated economic guidance across India-specific demographic and economic contexts.

## Metadata
- **Published**: 2026-09-25T13:22:24Z
- **Authors**: Pavithra P M Nair, Bhavik Talaviya, Shourya Bhushan, Rahul Pankajakshan, Seema Guruvadoo, Avinash Agarwal, Gilad Gressel, Krishnashree Achuthan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31245v1)