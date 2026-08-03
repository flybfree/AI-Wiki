---
title: Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory
published: 2026-07-31T08:46:27Z
authors: Jinghan Xu, Yiyong Xiao, Wanru Shao, Hankai Liu, Xinjin Li
url: http://arxiv.org/abs/2607.29167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory

## Abstract
Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authority. Existing prompt filters, content sanitizers, and tool guards do not enforce source-authority non-amplification after lossy memory consolidation. We formalize this boundary and instantiate it as Provenance-Preserving Memory Fire wall (PPMF), a lightweight memory middleware that preserves platform-maintained provenance and authorizes tool calls by matching action risk to the authority of action-relevant memories. In our schema-grounded evaluation with fixed risk policies, vulnerable consolidated memories reach up to 1.000 attack success rate(ASR); with intact platform-maintained provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the PPMF gate while confirmed benign actions and targeted low-risk memory use remain executable.

## Metadata
- **Published**: 2026-07-31T08:46:27Z
- **Authors**: Jinghan Xu, Yiyong Xiao, Wanru Shao, Hankai Liu, Xinjin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29167v1)