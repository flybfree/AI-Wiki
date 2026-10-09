---
title: Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology
published: 2026-10-08T14:20:06Z
authors: Zhaoxin Yu, Qingchao Kong, Dajun Zeng, Wenji Mao
url: http://arxiv.org/abs/2610.12022v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology

## Abstract
Large language models (LLMs) are increasingly deployed in sociotechnical systems where social attribution, the reasoning process attributing external events to the causes and reasons of agents' social behaviors, plays a critical role. These processes involve judgments of social cause, responsibility, and blame/credit to agents. Although attributional models are well-studied in social psychology and cognition through Attribution Theory, social attribution remains underexplored in AI, particularly LLM social reasoning. This paper provides the first systematic exploration of LLM social attribution. Our work focuses on responsibility and blame attributions, examining current LLMs' judgments and their underlying internal mechanisms. Guided by attribution theory, we construct a social attribution benchmark consisting of a Vignette subset based on classic scenarios from attribution theory research and a Reality subset based on real-world social narratives, yielding 7,639 responsibility/blame judgment questions. On this basis, we evaluate 32 representative LLMs and 5 basic non-LLM baselines. To further explore the internal mechanisms underlying the LLM judgment process, we develop a probing-based methodology to investigate the latent-space representations of 5 key attribution dimensions and the consistency of their influences on LLM judgments compared to those in human social attribution. Our research findings reveal that current LLMs exhibit measurable but incomplete agreement with human responsibility and blame judgments, and meanwhile, this agreement is positively correlated with model size. Some attribution dimensions are systematically decodable from specific positions in LLM hidden states, and their influences on the final judgment are consistent with those indicated by human Attribution Theory. The dataset and associated code are available at https://github.com/Yuzhaoxin946/SAB-Bench.

## Metadata
- **Published**: 2026-10-08T14:20:06Z
- **Authors**: Zhaoxin Yu, Qingchao Kong, Dajun Zeng, Wenji Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12022v1)