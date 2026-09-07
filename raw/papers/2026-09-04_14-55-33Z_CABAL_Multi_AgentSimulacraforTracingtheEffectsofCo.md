---
title: CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review
published: 2026-09-04T14:55:33Z
authors: Jicheng Zhou, Kemou Li, Kahim Wong, Zheyuan Li, Zhuan Shi, Fengpeng Li, Haiwei Wu, Jiantao Zhou
url: http://arxiv.org/abs/2609.05227v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review

## Abstract
Recent reports during the AAAI-27 review cycle highlight the risk of reviewers coordinating bids for reciprocal assignment advantage. Prior work treats bidding, reviewer assignment, and review manipulation as separate stages, leaving the lifecycle effects of collusive bidding unclear. Real-world analysis is further constrained by typically unobservable collusive intent and the lack of counterfactuals for the same conference. Motivated by this gap, we introduce \alg, an end-to-end multi-agent simulacra framework for studying reviewer assignment integrity by holding the conference environment fixed and configuring LLM-driven reviewer agents with honest or collusive policies. We further develop an affinity-guided collusive bidding strategy that uses mutual reviewer-paper affinities to construct collusion rings and select target papers, producing expertise-consistent rather than arbitrarily targeted attacks. Controlled experiments show that collusive bidding more than doubles target-paper capture and that assigned colluders score target papers about two points higher than honest co-reviewers, while conference-wide effects remain comparatively modest. Evaluated bid-phase detectors provide only limited evidence of collusion: in a fixed-triplet detector stress test, native positive-bid graphs are confounded by benign affinity, while a Very-High-only diagnostic view enables precise but low-coverage local recovery.

## Metadata
- **Published**: 2026-09-04T14:55:33Z
- **Authors**: Jicheng Zhou, Kemou Li, Kahim Wong, Zheyuan Li, Zhuan Shi, Fengpeng Li, Haiwei Wu, Jiantao Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05227v1)