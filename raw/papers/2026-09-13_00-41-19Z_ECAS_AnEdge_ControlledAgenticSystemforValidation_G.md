---
title: ECAS: An Edge-Controlled Agentic System for Validation-Gated Scientific Application Execution
published: 2026-09-13T00:41:19Z
authors: Baixi Sun, Mingze Xia, Huihuo Zheng
url: http://arxiv.org/abs/2609.14211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ECAS: An Edge-Controlled Agentic System for Validation-Gated Scientific Application Execution

## Abstract
Scientific applications increasingly rely on high-performance computing (HPC), yet translating a scientist's high-level goal into a correct target-scale execution remains brittle and labor-intensive. Large language model (LLM) agents promise to automate this, but two obstacles remain: granting a cloud-hosted model direct HPC access exposes credentials and execution authority, while withholding it demands continuous human supervision; and one-shot generation cannot adapt when generated artifacts fail in a site-specific HPC environment. We present \textsc{ECAS}, an \textbf{E}dge-\textbf{C}ontrolled \textbf{A}gentic \textbf{S}ystem for closed-loop execution of scientific computing campaigns with limited human intervention. \textsc{ECAS} separates \emph{reasoning}, \emph{control}, and \emph{execution}: a cloud-hosted LLM proposes plans, artifacts, and repairs; a user-controlled edge agent retains credentials, workflow state, and execution authority while enforcing policy and resource constraints; and the HPC system computes. Its core mechanism is \emph{validation-gated execution}: generated artifacts pass static checks and small-scale validation, failures trigger repairs from sanitized execution feedback, and target-scale execution is permitted only after validation and policy checks pass. \textsc{ECAS} also draws on an edge-resident library of expert-distilled, site-specific skills that is never disclosed to the cloud. In preliminary experiments with three scientific applications on two production ALCF systems under six injected fault types, closed-loop repair improves application success from 0/6 to 6/6 over one-shot generation, validation gating prevents all three observed target-scale failures, and skill conditioning improves success from 4/6 to 6/6. These results show the feasibility of delegating adaptive reasoning to the cloud while retaining execution control at the edge.

## Metadata
- **Published**: 2026-09-13T00:41:19Z
- **Authors**: Baixi Sun, Mingze Xia, Huihuo Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14211v1)