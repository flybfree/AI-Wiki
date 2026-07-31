---
title: FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs
published: 2026-07-29T09:41:07Z
authors: Yifan Zhang, Xinkui Zhao, Sai Liu, Hengxuan Lou, Guanjie Cheng, Chang Liu
url: http://arxiv.org/abs/2607.27267v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs

## Abstract
Large language model (LLM) agents autonomously interleave semantic reasoning with complex system operations. In these dynamic environments, static tool-level permissions are fundamentally insufficient; safe authorization is highly context-dependent and heavily reliant on evolving runtime states and data flows. We present FAVA (Formal Authorization for Verified Agents), a permission-carrying authorization framework for agent execution. FAVA utilizes an LLM-guided Permission Intermediate Representation (IR) to translate ambiguous natural-language tasks into structured constraints. A deterministic lowering pass then converts this IR into an evidence-backed permission graph that explicitly tracks data flows, dependencies, and contextual labels. To provide strict security guarantees, a Satisfiability Modulo Theories (SMT) authorizer mathematically verifies the current graph against security policies before any effectful action executes. A runtime gateway then enforces the solver's result, either authorizing the execution or intercepting it with a precise counterexample. We evaluate FAVA across OpenAgentSafety, OctoBench, and ActPlane scenarios. Our evaluation demonstrates that FAVA achieves a 90.5% Decision Compliance Rate (DCR) over the aggregate dataset, successfully intercepting dynamic violating traces in the evaluated trace-conditioned scenarios.

## Metadata
- **Published**: 2026-07-29T09:41:07Z
- **Authors**: Yifan Zhang, Xinkui Zhao, Sai Liu, Hengxuan Lou, Guanjie Cheng, Chang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27267v1)