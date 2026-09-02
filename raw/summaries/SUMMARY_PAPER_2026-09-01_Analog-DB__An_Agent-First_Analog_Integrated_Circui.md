---
title: Analog-DB: An Agent-First Analog Integrated Circuit Database, From Blocks to Systems
url: http://arxiv.org/abs/2609.01286v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-22-37Z_Analog_DB_AnAgent_FirstAnalogIntegratedCircuitData.md
generated_at: 2026-09-01 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Analog-DB, an open‑source database that stores analog integrated circuit designs as process‑neutral topologies with reusable testbenches and machine‑readable datasheets. It demonstrates that 23 circuit‑kit bindings satisfy their own specification bands and that AI agents can reuse these resources to size op‑amp cores with high accuracy.

## Key Takeaways
- The database holds 68 circuits across sixteen classes, each defined by a shareable topology and testbench, enabling full simulation on any process kit.  
- Twenty‑three circuit‑kit bindings meet their own specification bands, and ten meet a common class band, showing robust reuse potential.  
- Seventeen imported sizings fail initial tests but converge within one to three iterations using the annotated sub‑block roles.

## Context
This work tackles the challenge of sharing analog design details in AI‑driven synthesis pipelines where process‑specific information is hidden behind non‑disclosure agreements. By providing a structured, queryable repository, it aligns with trends toward automated and reusable analog circuit libraries that support machine learning agents.

## Implications
Analog-DB reduces iteration time and improves yield by allowing precise simulation across different kits, supporting industry adoption of open‑source analog libraries and AI co‑design tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01286v1)
