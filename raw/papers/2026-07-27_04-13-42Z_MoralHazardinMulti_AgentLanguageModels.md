---
title: Moral Hazard in Multi-Agent Language Models
published: 2026-07-27T04:13:42Z
authors: Dane Malenfant
url: http://arxiv.org/abs/2607.23982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Moral Hazard in Multi-Agent Language Models

## Abstract
Cooperation can fail when socially valuable effort is costly, weakly observable, and mainly benefits others. Drawing on Holmström's team moral-hazard model, we introduce the Dialogue Moral Hazard Game, a controlled textual game that operationalizes this hidden-action structure for language agents. In each episode, an agent can preserve an immediate local reward or pay a query cost to reveal a hidden safety fact that primarily helps another agent's downstream decision. We evaluate seven open-weight language models and decompose behavior into query use, realized information transfer, local-reward preservation, unsafe choice, format validity, and team success. Base models commonly preserve local reward without team success or query without communicating information that changes the final decision. We then use supervised fine-tuning, RLOO, sequential SFT+RLOO, and GEPA prompt optimization as diagnostic update mechanisms. Their effects are heterogeneous: OLMo-7B shows the clearest mechanism-consistent weight-level improvement, whereas GEPA sometimes improves team success while reducing or eliminating costly queries. Thus, optimization can shift aggregate reward without recovering the intended cooperative mechanism, motivating evaluations that report mechanism-level behavior rather than team success alone.

## Metadata
- **Published**: 2026-07-27T04:13:42Z
- **Authors**: Dane Malenfant
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23982v1)