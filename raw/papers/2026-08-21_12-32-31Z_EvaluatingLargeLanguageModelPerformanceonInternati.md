---
title: Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance
published: 2026-08-21T12:32:31Z
authors: Alexander Thomas, Hubert P. H. Shum, Darren Nellis, Manli Zhu, Phatpicha Yochum, William Bartle, Daniel Wrightson
url: http://arxiv.org/abs/2608.21036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance

## Abstract
The transport of dangerous goods by sea is a high-consequence activity governed by the International Maritime Dangerous Goods (IMDG) Code, a complex regulatory framework where errors in classification, packaging, stowage, or segregation can result in fire, explosion, toxic release, or loss of life or vessel. Correct compliance requires accurately interpreting hundreds of pages of interacting provisions, updated on a two-year amendment cycle. Practitioners increasingly use Large Language Models (LLMs) as decision-support tools, yet no systematic evaluation exists of whether they can reliably interpret IMDG requirements for safety-critical use.   This paper introduces DGEval, the first benchmark for evaluating LLM knowledge of IMDG Amendment 42-24. Built from expert-written questions on the NCB Hazcheck e-learning platform and structured lookups from the Dangerous Goods List (DGL), it comprises 1,678 questions across multiple-choice, open-ended, DGL lookup, and regulatory identification tasks. We evaluate 13 models from six providers across multiple thinking configurations, including one maritime domain-specific fine-tuned model, and test the effect of web search.   Although the best-performing model exceeds the human practitioner baseline on multiple-choice questions, all models are weakest in the operationally safety-critical areas of stowage, segregation, and regulatory recall. These results indicate that LLMs may support compliance tasks, particularly structured DGL lookups with web search, but unreliability in operational areas and regulatory-text recall means human oversight and authoritative source verification remain necessary before deployment in any safety-critical context. DGEval is designed as a safety assurance instrument to be applied continuously as models evolve, not as a settled characterisation of current capability.

## Metadata
- **Published**: 2026-08-21T12:32:31Z
- **Authors**: Alexander Thomas, Hubert P. H. Shum, Darren Nellis, Manli Zhu, Phatpicha Yochum, William Bartle, Daniel Wrightson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21036v1)