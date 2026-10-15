---
title: RLPE: Teaching LLMs to Prompt with Reinforcement Learning
published: 2026-10-13T18:59:04Z
authors: Rahul Singhal, Karime Maamari, Pradyumna Tambwekar
url: http://arxiv.org/abs/2610.19062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RLPE: Teaching LLMs to Prompt with Reinforcement Learning

## Abstract
Prompting is a widely used method for adapting general-purpose LLMs to domain-specific tasks. Effective prompts can be tedious to create manually, so prompt writing is increasingly handed to LLMs, with recent work training LLMs to write prompts for other models. These techniques either write prompts without observing how the task model behaves, blind to the failure modes the prompt should address, or must run alongside the task LLM at inference time, adding overhead to every query. Neither reflects how prompt engineering is often practiced. To close this gap, we introduce Reinforcement Learned Prompt Engineering (RLPE), which trains a model to analyze traces of a separate task model and write a prompt targeting the failures it observes. RLPE rewards the trained model strictly on prompt performance, so it learns the prompting strategies that improve the task model. The prompt is generated once and reused across the task, so inference does not require the trained model. Since RLPE needs only query access to the model it prompts, it is also compatible with closed-source models. We apply RLPE to Enigmata, BIG-Bench Extra Hard, and PlanBench. We train a 9B-parameter model that writes better prompts than state-of-the-art frontier models (gpt-5.6-sol and claude-opus-5) and prompt optimizers (GEPA and TextGrad) on 2/3 benchmarks. Although the model is never explicitly trained to iterate on prompts, this capability emerges at a level that matches or beats frontier models. The learned prompting capability also generalizes, with the trained model improving task models 6x larger than the one it trained with, including ones from entirely different model families, and matching claude-opus-5 on a fourth benchmark held out from training.

## Metadata
- **Published**: 2026-10-13T18:59:04Z
- **Authors**: Rahul Singhal, Karime Maamari, Pradyumna Tambwekar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19062v1)