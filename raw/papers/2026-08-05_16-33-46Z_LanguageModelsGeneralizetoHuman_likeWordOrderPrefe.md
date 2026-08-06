---
title: Language Models Generalize to Human-like Word Order Preferences
published: 2026-08-05T16:33:46Z
authors: Amanda Popadich, Shane Steinert-Threlkeld
url: http://arxiv.org/abs/2608.05028v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Generalize to Human-like Word Order Preferences

## Abstract
A central question in language acquisition is whether linguistic biases can emerge from general learning mechanisms operating over underdetermined input. Artificial Language Learning (ALL) studies have shown that human learners reliably generalize beyond the evidence provided, including by preferring scope-homomorphic noun phrase modifier orders. In this work, we investigate whether language models exhibit the same bias under similar conditions. We create a controlled learning environment in which models are trained on a corpus where all noun phrases containing multiple modifiers have been removed, eliminating direct evidence about modifier ordering, and are then evaluated on multiple modifier sentences. Across three model sizes, we find that they consistently prefer scope-homomorphic orders despite never observing them during training. These preferences vary in strength by modifier type. To investigate the source of these preferences, we examine noun-modifier association strength using pointwise mutual information (PMI). While PMI reflects known modifier-ordering patterns, it does not explain the models' ordering preferences. These findings demonstrate that LMs can recover human-like linguistic generalizations from impoverished input and provide a controlled framework for investigating the mechanisms underlying such biases.

## Metadata
- **Published**: 2026-08-05T16:33:46Z
- **Authors**: Amanda Popadich, Shane Steinert-Threlkeld
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05028v1)