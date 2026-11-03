---
title: Simple Features Beat Most AI Control Monitors
published: 2026-10-30T13:21:03Z
authors: Shubhrangshu Debsarkar, Valmik Nahata
url: http://arxiv.org/abs/2610.41713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simple Features Beat Most AI Control Monitors

## Abstract
AI control relies on monitors to catch a capable model that sabotages its work. These monitors are evaluated on their ability to differentiate honest from backdoored code. We show that on a standard evaluation dataset, simple features beat most monitors without ever running the code, outranking 20 of 24 open-weight models prompted as monitors. The dataset gives its labels away in two ways. People wrote the honest solutions and older language models the backdoors, so the style of the code reveals the class. Additionally, problems that LLMs can backdoor have different characteristics, so basic facts about the problem reveal it too. Swapping one class at a time for code by Claude Sonnet 5 shows that these features reward a contrast between authors, since human code against Sonnet 5's backdoors is easier to separate than the original pairs, 0.95 against 0.79. One in seven backdoors in the standard test set fails our validity checks, which distorts comparisons between attackers. A Sonnet 5 monitor appears to catch 77% of the older models' backdoors but 37% of Sonnet 5's, and 78% against 61% once both are verified. We do not show that published monitors rely on these shortcuts, but our findings suggest that a high score on such a dataset is not by itself evidence of sabotage detection. We release the rebuilt dataset and checks.

## Metadata
- **Published**: 2026-10-30T13:21:03Z
- **Authors**: Shubhrangshu Debsarkar, Valmik Nahata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.41713v1)