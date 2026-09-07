---
title: CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls
published: 2026-09-04T15:26:35Z
authors: Chris Zheng, Geng Yang
url: http://arxiv.org/abs/2609.05269v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls

## Abstract
LLM agent systems increasingly combine provenance tracking, authorization, policy enforcement, protocol adapters, and execution controls. However, individually correct security mechanisms do not necessarily compose into an end-to-end secure system: security-critical context may be dropped, widened, rebound, or reinterpreted as actions cross component boundaries. We identify this failure mode as security-context discontinuity and introduce CONTINUITY, a framework for verifiable composition of agent security controls.   CONTINUITY models each component with an assume-guarantee contract and carries authenticated security context across transitions using signed root grants, provenance commitments, role-bound transition receipts, bounded typed releases, transformation witnesses, and effect-bound execution permits. We formalize end-to-end consequence integrity, requiring every realized external effect to be backed by a valid and current authorization witness linking the principal, task, provenance, delegation, policy state, canonical action, and finality boundary.   We implement a reference verifier and deterministic cross-layer fault-injection suite covering 32 fault classes across four application domains. In 2,560 parameterized attack instances spanning 128 fault-domain classes, the full CONTINUITY configuration commits no harmful external effect, while completing all 700 benign tasks and escalating all 200 ambiguous cases. These results show that secure agent execution requires not only sound individual controls, but explicit contracts that preserve their guarantees across the complete instruction-to-effect path.

## Metadata
- **Published**: 2026-09-04T15:26:35Z
- **Authors**: Chris Zheng, Geng Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05269v1)