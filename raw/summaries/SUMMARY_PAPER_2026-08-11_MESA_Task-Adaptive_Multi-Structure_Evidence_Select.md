---
title: MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory
url: http://arxiv.org/abs/2608.10108v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_18-23-04Z_MESA_Task_AdaptiveMulti_StructureEvidenceSelection.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MESA, a framework that selects and fuses evidence from multiple specialized memory structures to improve long‑horizon agent reasoning. By learning a query‑adaptive composition of views, MESA reduces context size while boosting performance on AMA‑Bench by 8.5% compared with using all structures.

## Key Takeaways
- The optimal memory configuration is not the full union nor a single view but a tailored subset that varies per query and task demand.  
- MESA builds five complementary structure views of each trajectory and selects a query‑specific subset through harness optimization guided by prior knowledge and UCB scheduling.  
- Using only 41% fewer evidence tokens than the all‑structure approach, MESA achieves higher accuracy on AMA‑Bench.

## Context
Long‑horizon agents must retrieve distant evidence from interleaved reasoning steps, a challenge for memory systems that either overload context or ignore complementary information. This paper addresses the need for dynamic, structured evidence selection to balance efficiency and effectiveness in large language models.

## Implications
MESA offers a practical method for reducing token consumption while maintaining high reasoning quality, which can lower computational costs for deploying agents. Practitioners can adopt this adaptive memory strategy to improve performance without sacrificing speed or resource usage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10108v1)
