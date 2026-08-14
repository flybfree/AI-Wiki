---
title: TopoIntent: Compiling Security Intent into Executable, Compliance-Checked Network Topologies
url: http://arxiv.org/abs/2608.13389v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_15-49-37Z_TopoIntent_CompilingSecurityIntentintoExecutable_C.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
TopoIntent is a system that translates natural‑language security requirements into executable network topologies while checking compliance with CIS Controls v8.1.2. The approach uses a schema contract, retrieves reference architectures via dense‑vector search, and applies staged fusion to align intent with templates. After generation, additive repair fixes structural gaps, and the final topology is exported to Mininet scripts with iptables ACLs.

## Key Takeaways
- TopoIntent automatically generates network topologies that satisfy CIS Controls v8.1.2, improving satisfaction from 0.78 to 1.00 in fewer than 1.5 rounds on average.
- The system uses additive schema‑preserving edits to repair structural gaps without violating the original design constraints.
- A single feedback round raises the post‑ACL policy pass rate from 0.78 to 0.88, demonstrating rapid iteration capability.

## Context
The paper addresses a gap in AI research where natural‑language security intent is not yet reliably converted into structured, compliant network designs. This work exemplifies how generative AI can automate compliance‑driven infrastructure planning, moving beyond post‑design monitoring tools to proactive generation.

## Implications
For practitioners, TopoIntent reduces manual effort and risk of non‑compliant deployments by producing ready‑to‑run topologies that meet regulatory standards. In industry, it enables faster rollout of secure network designs while maintaining auditability through automated CIS checks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13389v1)
