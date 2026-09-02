---
title: EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities
published: 2026-08-31T23:33:33Z
authors: Feitong Qiao, Liren Peng, Shiming Ren, Aishwarya Jadhav, Arghavan Bahadorinejad, Marinette Chen, Muhan Zhang, Abdulaziz Suria, Gennevi Lu, Anish Das Sarma
url: http://arxiv.org/abs/2609.00487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoFlint: An Evolutionary Atlas of Multi-Turn LLM Vulnerabilities

## Abstract
Frontier language models that refuse harmful single-turn prompts often comply when the same intent is reached gradually over many turns, making multi-turn attacks one of the least understood failure modes of large language models. Most automated red-teaming methods treat this as a generation problem: produce attacks that break the model. We argue it is better framed as a search problem: discover, organize, and iteratively refine a diverse archive of attack strategies, producing a structured map of how a target model fails rather than a list of one-off successes. We introduce EvoFlint, which applies evolutionary quality-diversity search to multi-turn red-teaming. Attack strategies are phased conversation plans, not raw prompts, and are evolved through LLM-driven mutation and crossover. A Pareto fitness over attack success rate and peak severity preserves selection signal from near-miss attacks. A risk-indexed archive runs novelty search with local competition over strategy description embeddings inside each cell, maintaining diversity without committing to a predefined style taxonomy. A generation-level memory accumulates target-model insights across the population and feeds them back into strategy generation. On the HarmBench-test split, EvoFlint reaches attack success rates of 35.8% on Claude Sonnet 4.6, 59.7% on GPT-5.4, and 94.3% on Qwen3-32B, alongside 98.7% on the older GPT-4o included as a baseline reference. The resulting archive, organized by risk category, exposes for each target which categories of harm its safety training has and has not covered.

## Metadata
- **Published**: 2026-08-31T23:33:33Z
- **Authors**: Feitong Qiao, Liren Peng, Shiming Ren, Aishwarya Jadhav, Arghavan Bahadorinejad, Marinette Chen, Muhan Zhang, Abdulaziz Suria, Gennevi Lu, Anish Das Sarma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00487v1)