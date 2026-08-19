---
title: Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents
url: http://arxiv.org/abs/2608.17153v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_21-37-20Z_TowardsSaferRAG_OnlyAgentsCapableofSystem2Thinking.md
generated_at: 2026-08-18 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a refined security principle for Retrieval-Augmented Generation that allows only agents with System 2 reasoning capabilities to access untrusted documents, thereby mitigating knowledge‑poisoning attacks without imposing the strict isolation of the Cordon Principle. Empirical evaluation demonstrates that such reasoning‑capable models are markedly more robust to corrupted evidence than standard language models.

## Key Takeaways
- The refined principle restricts document access to agents capable of deliberative System 2 reasoning, enabling them to detect and resist misinformation while still using the information.  
- Empirical results show a substantial reduction in downstream influence from false documents compared with baseline models that lack such reasoning abilities.  
- This approach achieves comparable performance to strict Cordon‑style isolation but without the associated computational overhead.

## Context
Retrieval-Augmented Generation (RAG) systems rely on external knowledge sources, making them attractive targets for adversarial attacks that inject misinformation into retrieved documents. Current defenses often separate evidence handling from answer synthesis, which can degrade efficiency and scalability in large‑scale applications.

## Implications
The findings suggest a practical path toward secure RAG deployment where reasoning agents act as gatekeepers, balancing safety with performance. Practitioners may implement this principle to reduce false information propagation while maintaining the benefits of knowledge augmentation without sacrificing system efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17153v1)
