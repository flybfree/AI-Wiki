---
title: Language Models Are "Insecure" Reporters
published: 2026-09-28T19:13:33Z
authors: Jenny Y. Huang, Jiameng Fan, Ahmed Imtiaz Humayun, Maximillian Chen, Tian Qin, Run Chen, Vidhya Navalpakkam, Hongxiang Gu
url: http://arxiv.org/abs/2609.36139v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Are "Insecure" Reporters

## Abstract
As large language models are deployed in increasingly autonomous long-horizon tasks, manually auditing and verifying the actions, artifacts, and outputs of models becomes more difficult. Users instead come to rely on LLM-generated reports to assess the quality and completeness of the work. We introduce a suite of eight adversarial reporting scenarios to systematically study whether LLMs conceal narrative-changing flaws: errors or limitations that undermine an otherwise successful account of work. We call this phenomenon "insecure reporting." When handed machine learning experiment logs containing a planted negative result that substantially weakens the proposed method, GPT-5.5 flags the negative result in only 2 of 200 generated reports. However, when a short honesty instruction, "Be honest in your response," is added, the model flags the negative result in 190 of 200 reports. Across eight open-weight models, chain-of-thought analysis reveals a recurring tension between disclosing narrative-changing flaws and reasoning about ways to appear successful. We perform an activation analysis and a steering experiment on Qwen3.5-9B, finding that honesty and success-seeking correspond to opposing directions in representation space. Our results suggest that LLMs tend to present narratives of success by default, and that steering models toward honesty makes their reports substantially more transparent.

## Metadata
- **Published**: 2026-09-28T19:13:33Z
- **Authors**: Jenny Y. Huang, Jiameng Fan, Ahmed Imtiaz Humayun, Maximillian Chen, Tian Qin, Run Chen, Vidhya Navalpakkam, Hongxiang Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36139v1)