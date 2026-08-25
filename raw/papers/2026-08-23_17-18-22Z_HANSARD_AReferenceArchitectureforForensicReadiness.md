---
title: HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems
published: 2026-08-23T17:18:22Z
authors: Christos Sardianos, Iliana Pla, Vasilis Efthymiou, Iraklis Varlamis, Thomas Lagkas, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos
url: http://arxiv.org/abs/2608.22512v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

## Abstract
Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, attribution laundering, i.e., spreading an act across redundant agents until none is a but-for cause. Worse, the record is produced by the suspects, which comprises the assumption adopted throughout this work. Agents may therefore anticipate the investigation and the part of logging infrastructure may itself collude. In this paper, HANSARD is proposed, a reference architecture treating accountability as a life-cycle property. First, a readiness profile sealed before operation bounds what later findings may claim. Second, capturing at five choke points beyond the agents' reach makes omissions detectable, not only tampering. Third, a typed PROV-DM-aligned causal graph accrues as the system runs, and three indicators read it live to gate oversight without adjudicating. Fourth, post-incident replay yields contingent effects under the modified Halpern-Pearl definition, together with a compensation-set size. Finally, a synergy residual measures harm due to the combination rather than to individuals, making laundering visible. Cause, responsibility and accountability are then reported separately, each capped by an evidentiary tier, while a future research agenda is also provided.

## Metadata
- **Published**: 2026-08-23T17:18:22Z
- **Authors**: Christos Sardianos, Iliana Pla, Vasilis Efthymiou, Iraklis Varlamis, Thomas Lagkas, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22512v1)