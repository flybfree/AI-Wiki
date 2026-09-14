---
title: ORQA: An Occupation-Realistic Question and Answer Framework for LLM Professional Knowledge
published: 2026-09-11T02:36:21Z
authors: Shreyas Krishnan, Serina Chang, Abhishek Nagaraj
url: http://arxiv.org/abs/2609.12366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ORQA: An Occupation-Realistic Question and Answer Framework for LLM Professional Knowledge

## Abstract
We present ORQA, a method for testing occupation-level knowledge in large language models. Prior methods either map abstract LLM skills to occupations via task definitions or utilize expert knowledge which is difficult to obtain at scale and expensive. ORQA complements both of these methods by connecting O*NET occupations to trusted occupation-specific websites (such as regulatory agencies, licensing bodies, professional organizations, and government publications) and converting these into source-traceable question-answer pairs. A combination of an automated pipeline and human review produces a set of high quality questions about occupations. The question set created via our method covers 116 occupations from all 21 major groups in the SOC, with 480 questions sourced from 187 different websites. Each question is designed to probe a real-world skill question that is relevant to the occupation in question. We test 15 state-of-the-art frontier and open-weight models via this method. Claude Opus 4.6, GPT-5.4 and Claude Sonnet 4.6 all perform the best at approximately 58-62% while smaller open-weight models achieve approximately 33-41% performance. Performance varies significantly across occupations. Healthcare-related occupations achieve the highest performance (78%) while Office and Administrative Support achieve approximately 40%. Performance on individual occupations (e.g. Sheet Metal Workers and Fish and Game Wardens) is essentially zero. We also find that open-ended questions and weighting by wage bill do not significantly affect the ranking of models on this benchmark. We believe that leveraging existing trusted occupation-specific information to test LLM knowledge in professional domains may be a scalable and useful method for evaluating occupation-level AI performance in the future. Results and data are available at orqabench.org.

## Metadata
- **Published**: 2026-09-11T02:36:21Z
- **Authors**: Shreyas Krishnan, Serina Chang, Abhishek Nagaraj
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12366v1)