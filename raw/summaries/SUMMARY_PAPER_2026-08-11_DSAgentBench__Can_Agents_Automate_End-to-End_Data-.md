---
title: DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?
url: http://arxiv.org/abs/2608.10366v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_01-45-56Z_DSAgentBench_CanAgentsAutomateEnd_to_EndData_Scien.md
generated_at: 2026-08-11 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DSAgentBench, a benchmark for testing whether AI agents can automate full end-to-end data-science workflows in real computer environments. It evaluates 275 tasks across the entire lifecycle using tools like notebooks and databases, showing that even top models succeed only about 56.7% of the time.

## Key Takeaways
- DSAgentBench provides a comprehensive set of 275 diverse data-science tasks evaluated with deterministic correctness checks beyond code execution.
- The strongest model Claude‑4.6‑Sonnet achieves a modest 56.70% success rate, indicating agents still struggle with multi‑tool coordination and real‑world grounding.
- Open‑source agents perform poorly, often below 1%, failing at tool orchestration, OS interaction, and step‑wise reasoning.

## Context
This work addresses the gap between theoretical agent capabilities and practical data-science pipelines that require seamless integration of multiple software tools within an operating system. By focusing on real‑computer execution rather than isolated code runs, DSAgentBench reflects current limitations in autonomous AI agents handling complex workflows.

## Implications
The low success rates highlight a significant capability gap that must be closed for reliable agentic data-science systems. Industry practitioners and researchers should use DSAgentBench as a benchmark to guide development of more robust, tool‑aware, and verifiable agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10366v1)
