---
title: RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair
published: 2026-10-20T07:49:56Z
authors: Olivier Nourry, Yoshiki Higo
url: http://arxiv.org/abs/2610.27784v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair

## Abstract
Vulnerability benchmarks and software engineering research depend on rebuilding historical software. Yet builds rely on external resources, such as base images and packages, that change independently of the source code. In this study, we examine this environment decay on 14,159 OSS-Fuzz cases. We find that 69.7% no longer complete reconstruction and verification, and that most failures share a small number of recurring failure symptoms. A recurring failure can therefore be diagnosed once and its repair reused. We present Relay, a hybrid framework that uses an LLM to derive and validate deterministic repair rules from representative failures, reuses them without model calls, and escalates cases unresolved by rules to a per-case agent. We evaluate Relay in human-guided and fully automated rule-derivation campaigns and compare it with a per-case agent approach. We find that rule derivation can be fully automated, and that reusable rules restore as many builds as per-case agents with fewer build executions. However, agents restore cases that the rules cannot. Our results show that a hybrid approach that applies rules first and escalates the remaining cases to an agent restores more builds than either approach alone and at a lower cost than using agents alone.

## Metadata
- **Published**: 2026-10-20T07:49:56Z
- **Authors**: Olivier Nourry, Yoshiki Higo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27784v1)