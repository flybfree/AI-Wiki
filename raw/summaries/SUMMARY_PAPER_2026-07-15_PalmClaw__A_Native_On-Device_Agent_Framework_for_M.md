---
title: PalmClaw: A Native On-Device Agent Framework for Mobile Phones
url: http://arxiv.org/abs/2607.13027v1
type: paper-summary
date: 2026-07-15
source_paper: 2026-07-14_17-58-57Z_PalmClaw_ANativeOn_DeviceAgentFrameworkforMobilePh.md
generated_at: 2026-07-15 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
PalmClaw is an open-source framework that runs natively on mobile phones, allowing LLM agents to execute tasks by directly invoking device capabilities as tools with explicit arguments and structured results. The system reduces execution boundaries, enabling precise control over each action while keeping the agent loop local to the device. Experiments demonstrate an 11.5% relative improvement in task success and a 94.9% reduction in completion time compared to the strongest baseline.

## Key Takeaways
- PalmClaw runs entirely on mobile devices without needing cloud services, preserving user data privacy while enabling direct access to sensors and applications.
- The framework defines each tool call with explicit arguments and structured results, which creates clear execution boundaries that simplify debugging and integration.
- It achieves a 94.9% reduction in task completion time over the strongest baseline, showing substantial efficiency gains through native device execution.

## Context
Mobile AI agents have traditionally relied on desktop or server environments where tool use is well‑supported but data remains off‑device. This paper addresses the gap by providing a framework that brings LLM agent capabilities to smartphones, aligning with the growing expectation for privacy‑preserving and real‑time assistance.

## Implications
For developers, PalmClaw lowers the barrier to integrate mobile‑specific AI agents into everyday apps without complex infrastructure. For industry stakeholders, it demonstrates a path toward on‑device automation that can enhance user experience while complying with data protection regulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.13027v1)
