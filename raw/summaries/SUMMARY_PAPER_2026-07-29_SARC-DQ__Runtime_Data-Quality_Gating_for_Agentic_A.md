---
title: SARC-DQ: Runtime Data-Quality Gating for Agentic AI: Silent Evidence Defects, the Incompetence Shield, and Downstream-Only Remediation
url: http://arxiv.org/abs/2607.26313v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_22-22-52Z_SARC_DQ_RuntimeData_QualityGatingforAgenticAI_Sile.md
generated_at: 2026-07-29 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SARC-DQ, a framework that detects silent data-quality defects in agentic AI systems by measuring how often metadata-borne errors cause costly actions without raising flags. Experiments on a priced replenishment benchmark show agents convert injected defects into wrongful actions about 60% of the time with no quality alerts, and this rate is flat across model tiers. A downstream-only remediation gate recovers loss only for covered predicates.

## Key Takeaways
- The most dangerous defects are metadata-borne: a stale price or superseded record that appears well-formed but causes wrong actions without being flagged.
- Across four model tiers with 15x inference price variation, the defect conversion rate stays flat at about 60%, indicating capability does not buy skepticism.
- A downstream-only remediation gate recovers full loss only for predicates it covers; uncovered defects remain unmitigated.

## Context
Agentic AI systems rely on data to guide actions, yet many quality issues are invisible because they reside in metadata rather than payload. This creates a blind spot where agents cannot detect or question such errors, leading to hidden costs. The paper highlights that evidence integrity is a separate system axis from model capability, requiring enforcement at the right layer.

## Implications
Practitioners must implement data-quality gating independent of model performance to prevent silent defects from propagating downstream. This work provides a framework for auditing and remediating metadata issues without relying on model introspection. It underscores that effective AI systems need layered safeguards beyond algorithmic competence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26313v1)
