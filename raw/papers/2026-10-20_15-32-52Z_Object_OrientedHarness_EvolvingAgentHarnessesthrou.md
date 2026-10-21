---
title: Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design
published: 2026-10-20T15:32:52Z
authors: Gaotang Li, Bhavana Dalvi Mishra, Yifei Ming, Yanfei Chen, Zhongying CuiZhu, Lesly Miculicich, Long T. Le, Rui Meng, Chun-Liang Li, Hanghang Tong, Chen-Yu Lee, Tomas Pfister
url: http://arxiv.org/abs/2610.28380v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design

## Abstract
Agent harnesses are executable code that specifies the prompts, tools, and control flow around a language model. A single global harness can struggle with heterogeneous tasks that require different execution strategies. In this work, we introduce Object-Oriented Harness (OO-Harness), a harness optimization framework that evolves a hierarchy of executable harness classes using object-oriented design. During training, an evolution agent uses execution records to create a family of specialized harnesses, each implemented as a subclass of the base or an existing specialized harness via inheritance. At test time, a harness router uses routing lessons accumulated during training to select a specific harness for each task. Across three long-horizon benchmarks spanning business workflows, workspace tasks, and tool use, OO-Harness achieves the best performance among the compared methods, with an absolute improvement of up to 15% over the base. Extensive ablation studies examine the contributions of its core components.

## Metadata
- **Published**: 2026-10-20T15:32:52Z
- **Authors**: Gaotang Li, Bhavana Dalvi Mishra, Yifei Ming, Yanfei Chen, Zhongying CuiZhu, Lesly Miculicich, Long T. Le, Rui Meng, Chun-Liang Li, Hanghang Tong, Chen-Yu Lee, Tomas Pfister
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28380v1)