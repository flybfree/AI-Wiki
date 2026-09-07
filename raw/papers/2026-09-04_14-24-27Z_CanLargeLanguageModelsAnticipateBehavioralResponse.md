---
title: Can Large Language Models Anticipate Behavioral Responses to Social Policies? A Case of Pension Enrollment Prediction among China's Flexible Workers
published: 2026-09-04T14:24:27Z
authors: Yumiao Li, Peixin Liu, Donglin Di, Chen Li, Runhuan Feng
url: http://arxiv.org/abs/2609.05189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Large Language Models Anticipate Behavioral Responses to Social Policies? A Case of Pension Enrollment Prediction among China's Flexible Workers

## Abstract
Assessing the impacts of social policy changes is a widely acknowledged challenge for policymakers. Econometric methods can be unreliable when extrapolating to hypothetical scenarios, while field pilot programs are highly costly. In this paper, we propose using large language models (LLMs) as policy-assessment tools adapted from general-purpose models. We present FlexPension-LLM, the first domain-specialized large language model for a hierarchical pension-enrollment prediction task among flexible workers in China, and introduce DKI-RDistill, which injects policy-grounded cues into the prompt, including Probit-derived marginal effects and hukou-province pension rules. The method then uses LoRA/SFT to distill rationale-augmented supervision into an open-weight MoE student, with teacher errors corrected by regenerating those cases under ground-truth labels. On a CHFS 2019 blind split, FlexPension-LLM achieves 0.9316 Composite F1, surpassing its Claude Sonnet 4.5 teacher and 15 of 17 baselines, and is statistically indistinguishable from Claude Opus 4.6. Across four external surveys, it averages 0.7549 Composite F1 and shows the narrowest performance range among the strongest systems. Component analysis shows that gains come mainly from policy-grounded cue injection and error-filtered supervision, while rationales provide decision traces that can be checked against policy rules.

## Metadata
- **Published**: 2026-09-04T14:24:27Z
- **Authors**: Yumiao Li, Peixin Liu, Donglin Di, Chen Li, Runhuan Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05189v1)