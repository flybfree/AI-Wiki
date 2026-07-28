---
title: False Prophets: On the Security of World Models in Agentic Systems
published: 2026-07-25T10:55:14Z
authors: Erik Imgrund, Anna Wimbauer, Klim Kireev, Konrad Rieck
url: http://arxiv.org/abs/2607.23147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# False Prophets: On the Security of World Models in Agentic Systems

## Abstract
Large language models now power autonomous agents capable of complex, multi-step tasks in different environments. Accurate and reliable execution of these tasks requires the agent to predict the results of its actions. Recent research proposes to enhance predictive capabilities via specially trained environment simulators-world models. While world models can improve performance, they can also mislead agents into executing harmful actions, creating significant security and privacy risks. In this paper, we raise security concerns regarding the usage of world models in agentic systems. We discover a range of world model specific vulnerabilities, which can be exploited in terminal-based agents to execute malicious code or extract sensitive data. To facilitate future development, we introduce a security benchmark dataset designed for text-based world models. We argue that some risks are intrinsic to approximate world modeling, and show that attackers can induce mispredictions in agentic pipelines with up to 95% success rate, possibly resulting in unintended command execution, denial of service, drainage of wallet and private information extraction. Finally, we provide practical recommendations for practitioners to mitigate the discovered harms and harden agentic systems.

## Metadata
- **Published**: 2026-07-25T10:55:14Z
- **Authors**: Erik Imgrund, Anna Wimbauer, Klim Kireev, Konrad Rieck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23147v1)