---
title: Inspect India Evals: An Open Benchmarking Framework for Evaluating Large Language Models in the Indian Linguistic and Cultural Context
published: 2026-07-28T07:30:12Z
authors: Abhishek Kumar Singh, Shrey Nag,  Sachita, Lipi Goel, Rajeshwar Singh Janwar
url: http://arxiv.org/abs/2607.25375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inspect India Evals: An Open Benchmarking Framework for Evaluating Large Language Models in the Indian Linguistic and Cultural Context

## Abstract
India is a vast nation of over 1.4 billion people, varied by hundreds of diverse and locally specific traditions and cultures and 22 officially recognized languages. Large language models (LLMs) are now being deployed on a massive scale throughout the mainland as well as in remote villages. However, the common benchmarks - MMLU, BIG-Bench, and TruthfulQA are almost exclusively English- and Western-centric. They do not identify those safety, fairness, and accuracy failures unique to the Indian context. That is the gap Inspect India Evals seeks to fill. It is an open-source framework built on top of UK AISI's Inspect AI platform. It has six benchmarks: Multilingual MMLU across sixteen Indian languages, BharatBBQ (our adaptation of BBQ for Indian social bias), a safety evaluation for Digital Public Infrastructure, a multilingual safety test using harmful prompts in Indian languages, a multi-turn jailbreak resistance test, and an Indian cultural knowledge benchmark scored using LLM-as-judge rubrics. In this study, we tested five open-weight models ranging from 8B to 32B parameters. Sarvam-M 24B and Gemma 2 27B came out on top, both scoring 80% on the composite India Fairness Index, with Sarvam-M even beating larger 32B models on Indian cultural knowledge and DPI safety compliance. All models scored 100% refusal on Multilingual Safety, whereas DPI safety varied from 20% to 100%. The framework is public. It's built to work with the UK AISI registry. Anyone can reproduce or extend this work.

## Metadata
- **Published**: 2026-07-28T07:30:12Z
- **Authors**: Abhishek Kumar Singh, Shrey Nag,  Sachita, Lipi Goel, Rajeshwar Singh Janwar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25375v1)