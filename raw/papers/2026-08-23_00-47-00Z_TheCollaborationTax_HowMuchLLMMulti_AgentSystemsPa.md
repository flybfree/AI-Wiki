---
title: The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate
published: 2026-08-23T00:47:00Z
authors: Weixiang Sun, Zehong Wang, Hong Huang, Colby Nelson, Yanfang Ye
url: http://arxiv.org/abs/2608.22152v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate

## Abstract
Multi-agent systems built from large language models are deployed widely, yet how much performance is lost when two LLMs must coordinate rather than act alone remains unclear. We formulate the collaboration tax as the team-decentralisation loss of a two-player cooperative game with private information, with two propositions characterising its sign and its equivalence to a max-superadditivity violation. We operationalise this definition on 32 solo-tractable tasks grouped by source of grounding friction and measure it on 11 models from 7 providers. The tax is structured along two no-exception axes: a category ordering across every model and a monotonic decrease with capability. The proximate mechanism is not a reasoning deficit but a four-stage conversational cascade in which agents make ungrounded claims, fail to query the partner, skip integrating both views, and accept the answer without re-derivation. The tax is mechanically predictable from conversation features and partly tractable: a prompt intervention targeting all four stages closes a substantial fraction of the gap, with the dominant bottleneck differing across categories. In heterogeneous pairs the tax is pulled toward the stronger partner rather than the additive midpoint, empirically realising the max-superadditivity violation predicted by our framework. Together these results recast collaboration in LLM systems as a measurable, predictable, and partly tractable cost.

## Metadata
- **Published**: 2026-08-23T00:47:00Z
- **Authors**: Weixiang Sun, Zehong Wang, Hong Huang, Colby Nelson, Yanfang Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22152v1)