---
title: CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents
published: 2026-07-31T09:11:56Z
authors: Blaise Delattre, Cong Wang, Yang Cao
url: http://arxiv.org/abs/2607.29190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

## Abstract
Tool-using LLM agents act on typed tool returns, records pairing provenance and categorical fields with numerical values. Runtime permission gates generally authorize the observed return and action, leaving the decision unprotected against small errors in how the return was bound to its source. We ask whether a candidate action stays authorized over a declared neighborhood of plausible correctly bound returns: one admissible binding fault plus bounded numerical drift. We prove that certifying the categorical and numerical channels separately does not compose: perturbations that are safe on each channel alone can jointly turn the same action unsafe. CAGE certifies this joint neighborhood directly, enumerating the discrete branches exactly and certifying the continuous perturbation within each branch. Across synthetic, policy-as-code, regulatory, and real-transaction settings, CAGE removes the in-budget false allows that accurate pointwise gates admit, while keeping a useful fraction of decisions autonomous. When the policy is executable, CAGE-Exact certifies the policy itself; otherwise CAGE-Lip and CAGE-RS certify a learned gate under an explicit, measured fidelity assumption.

## Metadata
- **Published**: 2026-07-31T09:11:56Z
- **Authors**: Blaise Delattre, Cong Wang, Yang Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29190v1)