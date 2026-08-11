---
title: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use
published: 2026-08-09T04:46:58Z
authors: Juan S. Santillana
url: http://arxiv.org/abs/2608.08477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use

## Abstract
We present VectraYX-Vision-1B, a sub-2B vision-language model (VLM) for Spanish/LATAM cybersecurity imagery, coupling a frozen SigLIP-so400m encoder to a 1.04B Spanish/LATAM security decoder via an MLP. To our knowledge, it is the first sub-2B VLM specialized for cyber UI (IDA, Ghidra, Wireshark, Nmap, Metasploit, Volatility) that answers in Spanish, emits structured reasoning via native <|think|> tokens, invokes tools via Model Context Protocol (<|tool_call|>), and exports to llama.cpp's LLaVA mmproj format for air-gapped deployment. We report a negative preliminary visual-grounding result: despite fully functional pipelines, the current vision SFT (400-1900 steps, ~16M tokens) yields near-zero B6 scores (0.08 tool-identification), ignoring image content. We specify remediation (longer SFT, >=60% replay, lower LR) and expose a checkpoint-loader bug (unstripped llm. prefix) masquerading as training collapse. Crucially, we introduce a 3-variant ablation matrix (V0: NoPE-every-4, V1: all-RoPE, V2: NoPE+learned 2D) to study if periodic no-positional-encoding (NoPE) layers help or hurt attention over the 729-token visual block. Code, configs, and weights are released to establish priority on this architectural question. We provide B1-B5 for the text backbone, text controls, preliminary B6/B7 scores, wall times, GGUF efficiency on CPU, and a corpus of 14,596 QA pairs across 10 domains. We open-source all models and trajectories: jsantillana/vectrayx-1b, jsantillana/vectrayx-vision-1b, and jsantillana/vectrayx-vision-1b-checks.

## Metadata
- **Published**: 2026-08-09T04:46:58Z
- **Authors**: Juan S. Santillana
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08477v1)