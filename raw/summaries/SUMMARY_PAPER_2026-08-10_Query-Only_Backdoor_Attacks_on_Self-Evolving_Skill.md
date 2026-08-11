---
title: Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning
url: http://arxiv.org/abs/2608.08303v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_19-31-19Z_Query_OnlyBackdoorAttacksonSelf_EvolvingSkillsviaT.md
generated_at: 2026-08-10 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Trajectory Backdoor Attack (TBA), a query‑only method that manipulates self‑evolving skill systems to embed conditional backdoors without altering the underlying model weights. By crafting attacker‑submitted queries that repeatedly trigger a specific action under a defined condition, the system’s evolution pipeline learns and consolidates this pattern as a reusable rule. Experiments across multiple benchmarks and models show that TBA implants backdoors reliably while preserving clean‑task performance, matching or even surpassing direct skill injection attacks.

## Key Takeaways
- TBA demonstrates that an attacker can steer the trusted skill‑evolution process to create conditional backdoors solely through query manipulation.
- The attack exploits the system’s reliance on execution trajectories, turning benign interactions into a conduit for hidden triggers.
- Results indicate that trajectory‑driven evolution is vulnerable to indirect attacks, offering a new threat model beyond direct skill injection.

## Context
Self‑evolving skill systems aim to replace manual skill curation with automated pipeline construction, reducing reliance on external marketplaces. However, they inherit the same trust assumptions as their source models, making them susceptible to subtle manipulation that preserves system integrity while introducing hidden behavior.

## Implications
The findings warn developers and researchers of a critical blind spot in trusted evolution pipelines, urging rigorous testing for query‑driven influence. For industry practitioners, this paper calls for safeguards against indirect backdoors that could compromise autonomous agents without obvious model tampering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08303v1)
