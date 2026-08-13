---
title: XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication
url: http://arxiv.org/abs/2608.11676v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_05-32-33Z_XBridge_Entity_GroundedLatentBridgeforHeterogeneou.md
generated_at: 2026-08-12 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces XBridge, a decode‑free communication protocol that enables heterogeneous large language model agents to exchange latent representations without converting them into text. By solving the entity grounding problem in cross‑architecture bridges, XBridge improves performance on seven benchmark tasks across three model families while reducing latency by 11× compared with text‑based methods.

## Key Takeaways
- Lexical Anchor Mapping (LAM) creates discrete token anchors that map sender context tokens to receiver vocabulary, preventing rare‑token compression collapse.
- The Latent Enrichment Bridge (LEB) allows the receiver to query the sender’s hidden states for contextual enrichment, grounding bridge signals onto specific entities via self‑attention.
- XBridge requires only 264M trainable parameters (3.8% of the receiver), adds negligible inference overhead, and outperforms both text communication and a KV‑sharing baseline on six out of seven tasks.

## Context
Heterogeneous multi‑agent LLM systems aim to leverage diverse model families to reduce redundant reasoning while maintaining efficient communication. Existing protocols either rely on textual conversion, which discards internal representations, or assume architectural similarity for latent transfer, limiting scalability and efficiency.

## Implications
XBridge demonstrates that low‑parameter, decode‑free bridges can bridge the gap between different LLM architectures, offering a practical path to more flexible and faster multi‑agent AI systems. Practitioners can adopt this protocol to enhance system performance without major architectural changes or high computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11676v1)
