---
title: PCAP-LM: An LLM-Native Text Representation for TLS Bulk Traffic Analysis
url: http://arxiv.org/abs/2607.28100v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-10-12Z_PCAP_LM_AnLLM_NativeTextRepresentationforTLSBulkTr.md
generated_at: 2026-07-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary  
PCAP-LM introduces a flow-centric, LLM-native text representation that converts raw TLS bulk captures into concise semantic summaries using an ASCII alphabet called PacketGlyphs. The method reduces the capture size by 812× compared to standard tshark output and fits entire files within a single LLM context window, while also improving forensic question‑answering accuracy from 51% to 99.3%.

## Key Takeaways  
- BPE vocabulary saturates at 159 tokens, achieving an 812× size reduction over tshark -V and fitting entire captures within a single LLM context window.  
- The lossy design introduces a 24% false‑negative rate for TCP retransmissions, meaning some events may be omitted from the representation.  
- Extending PCAP-LM to heterogeneous mixed‑protocol environments will require retraining the vocabulary to accommodate new packet types.

## Context  
Network traffic analysis traditionally relies on verbose capture formats that exceed LLM context limits, hindering real‑time processing. This paper demonstrates how a lossy summarization step can preserve analytical utility while fitting within model constraints, highlighting a practical bridge between raw data and large language models.

## Implications  
The approach reduces storage and computational overhead for security investigations, enabling full‑capture analysis without exceeding LLM token budgets. Practitioners can leverage PCAP-LM to integrate TLS traffic insights directly into AI‑driven threat detection pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28100v1)
