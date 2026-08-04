---
title: Auditable Release Control for Pedagogical Leakage in LLM Tutors
published: 2026-08-01T08:24:30Z
authors: Nizam Kadir
url: http://arxiv.org/abs/2608.00515v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditable Release Control for Pedagogical Leakage in LLM Tutors

## Abstract
Large language model tutors can be correct and helpful yet disclose an answer or decisive reasoning before that disclosure is authorized. We formalize this state- and action-dependent failure as pedagogical leakage and introduce an authorization-aware complete-mediation boundary. A selector emits one of five disclosure contracts, trusted policy gates privileged modes, and a renderer proposes language. A single release function applies inspectable checks, optional cumulative verification, and action-specific fallback; replayable traces separate selection, generation, verification, and enforcement failures.   Matched component attribution exposes a safety-utility frontier. On 599 fixed Gemini 3.5 proposals, strict mediation reduces blinded three-model panel-majority leakage flags from 181 to 0 (paired problem-cluster difference -30.22 points, 95% CI [-35.00,-25.72]), while replacing 581 responses and lowering helpfulness. Checker-triggered fallback alone yields 11 majority flags; adding the semantic verifier yields 14 and no reliable marginal gain. A global A1 scaffold yields 0 majority and 54 any-judge flags, outperforming fitted Q on automatic safety and utility. In an externally timestamped replication over 40 unseen problem clusters and 480 attack sequences, high-assurance release reduces majority flags from 42 to 8 (-7.08 points, 95% CI [-13.13,-2.29]); seven failures persist, one is introduced, and mean helpfulness falls by .192. These results establish an auditable release boundary and failure attribution under declared contracts, not universal semantic safety or learning gains.

## Metadata
- **Published**: 2026-08-01T08:24:30Z
- **Authors**: Nizam Kadir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00515v1)