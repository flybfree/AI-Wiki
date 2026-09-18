---
title: Continual Enterprise World Model Discovery in Dynamic Systems
published: 2026-09-17T01:23:43Z
authors: Shambhavi Mishra, David Vazquez, Perouz Taslakian, Marco Pedersoli, Jose Dolz, Issam H. Laradji
url: http://arxiv.org/abs/2609.19551v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continual Enterprise World Model Discovery in Dynamic Systems

## Abstract
In an enterprise system, updating one field can set another, create a record, or start an approval. These effects are produced by business rules that are not built into the platform but written by each organization and revised over time. An agent working in such a system cannot predict the result of its own actions without knowing these rules. We study continual enterprise world model discovery, where an agent starts without knowledge of these business rules and discovers them by interacting with records and observing the outcomes. From those observations it builds a world model, which it revises as the rules change. To evaluate this, we introduce EnterpriseWorldShift, built on a live ServiceNow environment with nine tables, 25 hidden rules and 600 evaluation actions. It presents four versions of the same enterprise world, with the tables and records held fixed while a rule is modified, then added, then removed, so that discovery, revision, extension and retirement are each tested in turn. Our Continual Discovery Agent (CDA) builds such a model and carries it from one world to the next. It predicts the effects of the hidden rules more accurately than looking them up for each question, the approach taken by prior work, by up to 8.98 IoU points, and it answers from its own model without querying the running system.

## Metadata
- **Published**: 2026-09-17T01:23:43Z
- **Authors**: Shambhavi Mishra, David Vazquez, Perouz Taslakian, Marco Pedersoli, Jose Dolz, Issam H. Laradji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19551v1)