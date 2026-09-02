---
title: Towards a Belief-Based World Model for LLM Agents
published: 2026-08-31T22:48:38Z
authors: Shubham Kumar, Harshit Kumar, Narendra Ahuja, Saurabh Jha
url: http://arxiv.org/abs/2609.00455v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards a Belief-Based World Model for LLM Agents

## Abstract
Large language models (LLMs) are being used as policies for autonomous decision-making and planning in many domains. Despite their strong reasoning capabilities, LLMs struggle with long-horizon tasks, especially under partial observability. World models are a promising way to enhance policy performance, both during training and inference. During inference, agents currently use world models to simulate the consequences of candidate actions before committing to an action, which can improve decision-making. However, we argue that simulation alone is an incomplete interface for decision-making under partial observability: simulation doesn't adequately capture uncertainty about the current state, which agents may need for accurate decision-making. We address this limitation with Belief-Based World Models (BB-WMs), which model and maintain a belief that LLMs can query to access information on what is known and uncertain about the current state. Before developing methods to learn accurate BB-WMs, we first ask a more fundamental question: does exposing a world model's belief directly to an LLM policy improve decision-making? Our results show that giving LLM agents access to world model beliefs improves task performance under partial observability, while remaining complementary to existing simulation-based world models. Code is released at https://github.com/skumar-ml/belief-world-models.

## Metadata
- **Published**: 2026-08-31T22:48:38Z
- **Authors**: Shubham Kumar, Harshit Kumar, Narendra Ahuja, Saurabh Jha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00455v1)