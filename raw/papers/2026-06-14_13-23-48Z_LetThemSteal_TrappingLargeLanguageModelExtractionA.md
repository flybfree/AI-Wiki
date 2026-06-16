---
title: Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot
published: 2026-06-14T13:23:48Z
authors: Yuyang Dai, Yushun Dong
url: http://arxiv.org/abs/2606.15810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot

## Abstract
Large language models deployed as commercial APIs are vulnerable to model extraction attacks, while existing defenses either act too late or degrade utility for legitimate users. We propose \textbf{Knowledge Trap}, a defense that redirects extraction attacks toward low-transferability knowledge through a \emph{Honeypot Knowledge Graph} (HKG) and breadcrumb-guided exploration. Instead of blocking queries or perturbing outputs, Knowledge Trap consumes the attacker's limited query budget on knowledge with negligible downstream utility while preserving benign-user performance. Experiments in medical and financial domains show that Knowledge Trap reduces surrogate Agreement by 6.2\% on average without degrading legitimate-user accuracy, outperforming existing defenses that impose measurable user impact. These results suggest that defending knowledge-space traversal is a practical direction for mitigating LLM extraction attacks.

## Metadata
- **Published**: 2026-06-14T13:23:48Z
- **Authors**: Yuyang Dai, Yushun Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.15810v1)