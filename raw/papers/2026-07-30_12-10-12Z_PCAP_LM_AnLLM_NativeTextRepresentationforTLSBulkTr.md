---
title: PCAP-LM: An LLM-Native Text Representation for TLS Bulk Traffic Analysis
published: 2026-07-30T12:10:12Z
authors: Xavier Marjou, Lucas Tamic, Ilan Jaffeux-Cheniout
url: http://arxiv.org/abs/2607.28100v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PCAP-LM: An LLM-Native Text Representation for TLS Bulk Traffic Analysis

## Abstract
Large language models (LLMs) offer powerful reasoning capabilities for network traffic analysis, but standard capture formats and their textual equivalents are prohibitively verbose, overflowing LLM context windows by two orders of magnitude. We present PCAP-LM, a flow-centric, LLM-native text representation that acts as a lossy knowledge extraction step rather than a standard compression tool: raw captures are transcoded into semantic summaries using PacketGlyphs - a novel ASCII alphabet coined in this paper that encodes packet direction, TCP/TLS state, log-scale size, and inter-packet delay. Combined with a constrained PMI-BPE tokenizer and motif run-length encoding, repetitive behavioural patterns are aggressively collapsed. A @REFS side-index preserves lossless drill-down into the original packets. Evaluated on a homogeneous corpus of 5G/4G TLS 1.3 bulk-download traffic, the BPE vocabulary fully saturates at 159 tokens, achieving an 812x size reduction over tshark -V and fitting entire captures within a single LLM context window. In a forensic question-answering evaluation over 30 held-out files, a frontier LLM achieves 99.3% accuracy from PCAP-LM documents versus 51.0% from a token-budget-matched tshark -V prefix. The lossy design introduces known blind spots - most notably a 24% false-negative rate for TCP retransmissions - and extending to heterogeneous mixed-protocol environments will require vocabulary retraining.

## Metadata
- **Published**: 2026-07-30T12:10:12Z
- **Authors**: Xavier Marjou, Lucas Tamic, Ilan Jaffeux-Cheniout
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28100v1)