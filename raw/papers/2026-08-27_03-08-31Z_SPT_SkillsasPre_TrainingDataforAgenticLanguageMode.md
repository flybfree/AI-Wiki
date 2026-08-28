---
title: SPT: Skills as Pre-Training Data for Agentic Language Models
published: 2026-08-27T03:08:31Z
authors: Yufei Sun, Yudong Li, Yiming Cheng
url: http://arxiv.org/abs/2608.26563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPT: Skills as Pre-Training Data for Agentic Language Models

## Abstract
Agentic (tool-using) language models are mainly trained on tool-call traces and agent trajectories during post-training. These data provide direct behavioral supervision, but producing them requires task environments, execution, and verification, making broad tool and task coverage expensive. Publicly available skills offer another source of training data: they encode reusable tool semantics and workflows but are typically used only as inference-time context. We introduce Skill Pre-Training (SPT), a mid-training method that applies causal language modeling to SkillCorpus, a collection of public multi-file skill packages, optionally mixed with general data. To preserve relations among files within each package, we also introduce Reference Insert, a reference-aware assembly strategy that places supporting files near their mentions in the primary instruction. Experiments across multiple model scales and post-training recipes show that SPT consistently improves agentic performance over mid-training on general or trajectory data, while largely preserving general performance. Data mixture experiments show additional benefits from combining skill data with general annealing corpora. These results indicate that skill packages are a valuable data source for pre-training agentic language models.

## Metadata
- **Published**: 2026-08-27T03:08:31Z
- **Authors**: Yufei Sun, Yudong Li, Yiming Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26563v1)