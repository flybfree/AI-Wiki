---
title: MedAgent-R1: Faithfulness-Aware Reinforcement Learning for Evidence-Grounded Medical Reasoning
published: 2026-08-31T12:19:41Z
authors: Jiangwang Chen, Chenghao Zhang, Hengxing Cai
url: http://arxiv.org/abs/2608.30676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedAgent-R1: Faithfulness-Aware Reinforcement Learning for Evidence-Grounded Medical Reasoning

## Abstract
When medical AI systems hallucinate clinical reasoning, the consequences extend beyond incorrect answers: fabricated justifications that superficially reference retrieved evidence can mislead clinicians into unsafe treatment decisions. Medical reasoning agents must therefore produce not only correct answers but also faithful justifications that clinicians can verify against cited evidence. We identify a systematic failure mode in RL-trained retrieval agents: outcome-only rewards improve accuracy while degrading faithfulness, a phenomenon we term confident hallucination. The agent learns to answer from parametric memory and backfill plausible but unsupported justifications; citation fabrication rates rise from 16.5% to 31.8% even as accuracy improves by 5 points over the supervised baseline. We address this with a faithfulness-gated reward design: accuracy credit is conditioned on evidence grounding via a hard gate, complemented by retrieval validity and conciseness signals that close exploitation paths unique to agentic retrieval. The resulting system, MedAgent-R1, reduces citation fabrication from 31.8% to 4.7% and raises evidence completeness from 58.7 to 82.6 while maintaining 75.1% accuracy, with 13.2-point gains on HealthBench Safety. Under the same agentic retrieval setup, MedAgent-R1 outscores GPT-4o on faithfulness-specific dimensions (Factual Support 4.55 vs. 4.25; Overclaiming 4.40 vs. 4.15) while remaining below GPT-4o in overall accuracy, suggesting that explicit faithfulness training yields evidence-grounding gains not achieved by scaling alone.

## Metadata
- **Published**: 2026-08-31T12:19:41Z
- **Authors**: Jiangwang Chen, Chenghao Zhang, Hengxing Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30676v1)