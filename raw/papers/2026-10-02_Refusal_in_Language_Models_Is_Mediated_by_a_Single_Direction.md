---
title: "Refusal in Language Models Is Mediated by a Single Direction"
arxiv_id: "2406.11717"
version: "v3"
published: "2024-06-17"
updated: "2024-10-30"
authors: "Andy Arditi; Oscar Obeso; Aaquib Syed; Daniel Paleka; Nina Panickssery; Wes Gurnee; Neel Nanda"
primary_category: "cs.LG"
categories: ["cs.LG", "cs.AI", "cs.CL"]
source_url: "https://arxiv.org/abs/2406.11717"
type: "paper"
tags: ["paper", "research", "ai", "alignment", "interpretability", "safety"]
---
# Refusal in Language Models Is Mediated by a Single Direction

**Source**: [Original Paper](https://arxiv.org/abs/2406.11717)

## Abstract

Conversational large language models are fine-tuned for both instruction-following and safety, resulting in models that obey benign requests but refuse harmful ones. While this refusal behavior is widespread across chat models, its underlying mechanisms remain poorly understood. In this work, the authors show that refusal is mediated by a one-dimensional subspace across 13 popular open-source chat models up to 72B parameters in size. For each model, they identify a direction such that erasing it from residual-stream activations prevents refusal of harmful instructions, while adding it elicits refusal on harmless instructions. They use this observation to propose a white-box jailbreak method that disables refusal with minimal effect on other capabilities, and analyze how adversarial suffixes suppress propagation of the refusal-mediating direction.

## Metadata

- **Authors:** Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda
- **Submitted:** 2024-06-17
- **Latest version:** v3, updated 2024-10-30
- **Categories:** cs.LG, cs.AI, cs.CL
- **Canonical source:** https://arxiv.org/abs/2406.11717
