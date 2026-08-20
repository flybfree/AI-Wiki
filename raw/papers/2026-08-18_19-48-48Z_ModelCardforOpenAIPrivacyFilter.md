---
title: Model Card for OpenAI Privacy Filter
published: 2026-08-18T19:48:48Z
authors: Charles de Bourcy, Sahra Ghalebikesabi, Avi Schwarzschild, Alex Gorbachev, Mihai Maruseac, Annie Chu, Vol Kyrylov, Tong Mu, Ally Bennett, Andy Nguyen, Casey Meehan, Jessica Gan Lee, Shane Bauer, Harold Nguyen, Rodolpho Eckhardt, Yuqi Liu, Charlie Oxborough, Marco Rougeth, Omar Chedid, Caio Costa, Yash Parikh, Yao Li, Congzheng Song, Om Thakkar, Vinnie Monaco
url: http://arxiv.org/abs/2608.18274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Model Card for OpenAI Privacy Filter

## Abstract
OpenAI Privacy Filter is a compact, bidirectional token-classification model for detecting and redacting personally identifiable information (PII) and secrets in unstructured text. The model is derived from an autoregressively pretrained checkpoint and converted into a bidirectional, banded-attention classifier that labels an input sequence in a single forward pass. A constrained Viterbi decoder produces coherent spans across eight privacy categories and exposes configurable operating points for precision-recall tradeoffs. Privacy Filter has 1.5 billion total parameters, 50 million active parameters per token, and a 128,000-token context window. It is designed for efficient local deployment and domain-specific fine-tuning. Privacy Filter is intended as a configurable data-minimization component within layered privacy workflows, not as an anonymization or compliance guarantee.

## Metadata
- **Published**: 2026-08-18T19:48:48Z
- **Authors**: Charles de Bourcy, Sahra Ghalebikesabi, Avi Schwarzschild, Alex Gorbachev, Mihai Maruseac, Annie Chu, Vol Kyrylov, Tong Mu, Ally Bennett, Andy Nguyen, Casey Meehan, Jessica Gan Lee, Shane Bauer, Harold Nguyen, Rodolpho Eckhardt, Yuqi Liu, Charlie Oxborough, Marco Rougeth, Omar Chedid, Caio Costa, Yash Parikh, Yao Li, Congzheng Song, Om Thakkar, Vinnie Monaco
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18274v1)