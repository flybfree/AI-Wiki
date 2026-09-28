---
title: Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis
published: 2026-09-25T15:44:18Z
authors: Jakub Masłowski, Jarosław A. Chudziak
url: http://arxiv.org/abs/2609.31422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis

## Abstract
Large language model-based multi-agent debate (MAD) systems are being increasingly used as complex decision pipelines in distributed processes. However, their final synthesis phase still remains inadequately controlled. Even with detailed debate logs, summarizing models are prone to fabricating smoothly written debate consensus that is not grounded in the debate's history. To address this safety gap, this paper presents empirical research and studies if the introduction of active post-debate verification can mitigate the production of such factually unsupported summaries, while still providing valuable information. Furthermore, it is examined whether explicitly signalling divergence is preferable in the absence of a reliable compromise. The Active Provenance Gate (APG) is introduced as a post-debate verification layer that treats the source as a hard constraint, analysing the debate logs, auditing each claim, and applying self-correction. In crisis simulations, the self-healing mechanism more than doubles the average data Provenance Fidelity in difficult condition scenarios, before the strict gate blocks unsupported claims and generates divergence reports. In the human study, a vast majority of the users (over 75%) preferred a report explicitly stating failure in critical scenarios, despite most of them perceiving fabricated consensus from the baseline system as more fluent. Our main contribution is the transition of data origin tracing from passive logging to active conditional blocking before publication.

## Metadata
- **Published**: 2026-09-25T15:44:18Z
- **Authors**: Jakub Masłowski, Jarosław A. Chudziak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31422v1)