---
title: Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation
published: 2026-08-13T06:44:40Z
authors: Rana Muhammad Ahmed, Sabahat Abbas
url: http://arxiv.org/abs/2608.12880v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation

## Abstract
Security evaluations of tool-using agents often equate stored labels with behavioral facts. We audit a preserved campaign by tracing 10,200 execution rows to 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. Two schema treatments were delivered, but the planned external payload-family corpus was not. The historical grader exhibited direct treatment leakage: treatment metadata gated the ATTACK_SUCCESS class, so fixed behavior could change class under treatment relabeling. A treatment-blind reconstruction corrects 58 historical ATTACK_SUCCESS or HIJACK_ATTEMPT labels to authorized benign completions while preserving three verified protected-data transfers and one separate unauthorized-forwarding case. The locked v2 census contains exactly zero ATTACK_SUCCESS records, while the forwarding case remains a HIJACK_ATTEMPT at a semantic boundary concerning objective completion. A dual-reviewer blinded concordance review of all 96 requests deemed structurally interpretable by locked v2 produced identical reviewer-consensus classes but differed from the locked codebook on four construct-boundary cases. We contribute a seven-link Integrity Chain and an executable, scope-bounded endpoint-integrity linter. The result is a campaign-bounded measurement audit, not a population attack-rate, model-ranking, defense-efficacy, or causal estimate.

## Metadata
- **Published**: 2026-08-13T06:44:40Z
- **Authors**: Rana Muhammad Ahmed, Sabahat Abbas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12880v1)