---
title: PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning
url: http://arxiv.org/abs/2607.20064v2
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_12-11-51Z_PRO_LONG_ProgrammaticMemoryEnablesLong_HorizonReas.md
generated_at: 2026-07-23 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
PRO‑LONG introduces a minimal context management framework that leverages programmatic memory to support long‑horizon reasoning in LLM agents. The method retains a full structured interaction log and uses recent coding‑agent search techniques to retrieve relevant information efficiently, achieving an average 18 percentage‑point boost over baseline coding agents on the ARC‑AGI‑3 benchmark while using far fewer tokens.

## Key Takeaways
- PRO‑LONG stores a complete, structured interaction log that can be searched programmatically.  
- The framework reduces token consumption by up to five times compared with standard harnesses.  
- On the full ARC‑AGI‑3 public game set, PRO‑LONG improves frontier models by an average of 18 percentage points and reaches pass@1 rates matching specialized harnesses (up to 76.1%).

## Context
Long‑horizon tasks demand agents that can retain and retrieve information over extended observation sequences, a challenge that current LLM harnesses struggle with due to token limits and retrieval inefficiencies. PRO‑LONG’s approach directly tackles this tradeoff by combining persistent memory with efficient search algorithms.

## Implications
For researchers, PRO‑LONG demonstrates that programmatic memory can be integrated into large language models without sacrificing performance or incurring high compute costs. Practitioners can adopt the framework to build more robust agents for continual learning and exploration tasks while conserving token usage and operational expenses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20064v2)
