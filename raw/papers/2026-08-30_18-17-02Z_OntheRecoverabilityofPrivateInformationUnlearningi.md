---
title: On the Recoverability of Private Information Unlearning in Large Language Models
published: 2026-08-30T18:17:02Z
authors: Shicheng Hu, Runzhi Tian, Ziqiao Wang, Yongyi Mao
url: http://arxiv.org/abs/2608.29943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Recoverability of Private Information Unlearning in Large Language Models

## Abstract
Large language models (LLMs) can memorize sensitive information, raising serious privacy concerns. Machine unlearning offers a potential solution to remove such information, but it remains unclear whether existing methods truly erase it or merely hide it within the model. A key challenge is quantifying the persistence of sensitive data under a unified evaluation framework. To address this, we construct a synthetic dataset containing fake private information and propose a white-box auditing framework to systematically assess whether claimed-forgotten information is genuinely removed. Using this framework, we evaluate five existing unlearning methods and find that a simple "inverse greedy" decoding -- selecting the least likely token at each step -- can recover supposedly forgotten private information. Our results reveal that current unlearning approaches often fail to fully eliminate sensitive information, highlighting the need for more reliable methods to ensure privacy in deployed LLMs.

## Metadata
- **Published**: 2026-08-30T18:17:02Z
- **Authors**: Shicheng Hu, Runzhi Tian, Ziqiao Wang, Yongyi Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29943v1)