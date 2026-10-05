---
title: Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild
published: 2026-10-01T19:36:57Z
authors: Elad David, Max Fomin
url: http://arxiv.org/abs/2610.02413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild

## Abstract
LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it. A cheap, increasingly common move, borrowed from LLM-as-judge prompting, is to append a short classification instruction after the user's turn and read the probe at that point, to sharpen it: the instruction asks the model to represent the incoming request as a class, concentrating the signal the probe must separate, at negligible serving cost. But does the wording of that suffix matter, and does its benefit hold in the wild, on attack types the probe never saw in training, the regime a deployed monitor faces? We test this with a controlled ladder of post-user suffixes under strict leave-one-dataset-out (LODO) evaluation across 13 safety benchmarks (jailbreak, injection, and benign chat) and three open-weight model families (Llama-3.1-8B, Qwen3.5-9B, Gemma-4-12B). On a single-position probe, a classification suffix consistently improves out-of-distribution detection over no suffix (up to ~4 AUC points); yet which suffix matters: prompting the model to classify the input, even into content-free labels, reliably wins; an off-topic or merely-attentive suffix helps little. The gain comes from the classification format, not the named criterion: a content-free suffix matches the real malicious/benign one, with the criterion adding precision only at strict thresholds. This is not an artifact of the single-position read: the benefit carries to the multi-position pooling probes used in production (attention, multi-max, MLP), though the best-performing suffix there is readout-dependent. Served through a KV-cache fork, it is a cheap drop-in for any activation-probe monitor, though not an automatic win: which suffix helps, and by how much, depends on the model and the readout.

## Metadata
- **Published**: 2026-10-01T19:36:57Z
- **Authors**: Elad David, Max Fomin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02413v1)