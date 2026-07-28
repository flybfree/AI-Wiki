---
title: From Cognitive Architectures to Language Agents: A Mechanism-Level Review of Lineage, Convergence, and Migration Gaps
url: http://arxiv.org/abs/2607.23942v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_02-38-59Z_FromCognitiveArchitecturestoLanguageAgents_AMechan.md
generated_at: 2026-07-27 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper reviews ten historical cognitive architectures and eight language-agent runtime families alongside forty-two mechanism-focused modern systems. It reconstructs mechanisms using state, control, transition, persistence, failure, learning, and resource governance to map convergence gaps between legacy models and contemporary agents. The analysis shows that many adaptive features have been reimplemented independently rather than inherited from earlier designs.

## Key Takeaways
- Modern language agents have operationalized adaptive memory, dynamic team selection, workflow search, skill induction, resource scheduling, and uncertainty-conditioned action but often through independent convergence rather than documented inheritance.
- The strongest remaining opportunities are in couplings among mechanisms such as calibrated multi-skill selection with verification and bounded repair within GraSP.
- Five residual bundles remain: activation latency and action utility; typed impasse resolution; bounded content competition; persistent intention reconsideration; and uncertainty with resource allocation.

## Context
This work situates the evolution of cognitive architectures within the broader AI landscape where modularity, composability, and runtime safety are critical concerns. By focusing on mechanism-level evidence rather than high‑level feature labels, it offers a systematic lens for understanding how complex agents emerge from simpler building blocks.

## Implications
For researchers, the catalog provides an auditable framework to test composable runtime invariants that could guide more reliable agent design. For industry practitioners, recognizing these gaps can inform integration strategies and reduce costly reimplementation efforts across legacy systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23942v1)
