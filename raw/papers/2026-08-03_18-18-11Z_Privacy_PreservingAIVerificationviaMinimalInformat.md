---
title: Privacy-Preserving AI Verification via Minimal Information Disclosure
published: 2026-08-03T18:18:11Z
authors: Sleem Abdelghafar, Gabriel Kulp
url: http://arxiv.org/abs/2608.02774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Privacy-Preserving AI Verification via Minimal Information Disclosure

## Abstract
AI verification crosses a trust boundary: a verifier must learn enough to establish an authorized claim, yet the same evidence can reveal sensitive details about the model, workload, or hardware. We introduce minimal information disclosure (MID), which designs and quantifies the information content of verifier-facing evidence itself. MID measures collateral leakage with conditional mutual information: what the release reveals about the protected property after the authorized result is known. MID is general by design: it can accommodate different verification goals, protected properties, evidence sources, and deployment constraints. To demonstrate MID's practicality, we evaluate it on four physical measurements and six verification tasks spanning execution type, hardware identity, compute scale, and model identity. These experiments use three mechanism-design variables--the evidence channel, collection policy, and release transformation--but MID is not limited to these choices and can accommodate other deployable mechanisms. Across these tasks, MID produces three releases with perfect held-out verification and zero measured collateral leakage, while the remaining tasks yield explicit privacy--utility frontiers. MID also supports ZKP-certified releases: we demonstrate our proposed linear-projection mechanism using a Groth16 zk-SNARK.

## Metadata
- **Published**: 2026-08-03T18:18:11Z
- **Authors**: Sleem Abdelghafar, Gabriel Kulp
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02774v1)