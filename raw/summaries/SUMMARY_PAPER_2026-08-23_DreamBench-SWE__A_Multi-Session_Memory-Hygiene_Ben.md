---
title: DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents
url: http://arxiv.org/abs/2608.20664v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_01-48-57Z_DreamBench_SWE_AMulti_SessionMemory_HygieneBenchma.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
DreamBench‑SWE is a multi‑session benchmark designed to evaluate software agents’ memory hygiene by requiring later tasks to rely on non‑inferable evidence from earlier sessions and using executable hidden oracles for scoring. The original v2 fold showed no significant difference between the DF‑hybrid–B5 contrast, while the successor audit revealed that only one hosted memory configuration achieved a high pass rate.

## Key Takeaways
- In the original fold the primary DF‑hybrid–B5 contrast was null (95/180 versus 89/180; clustered p=.518, Holm p=1), indicating no evidence of equivalence between conditions.  
- The successor run showed that deterministic verbatim event memory achieved 82/180 passes (rate 0.4556) and the typed‑plus‑raw reference probe reached 83/180 passes (rate 0.4611), but no external memory configuration passed more than 21/180.  
- The registered six‑slot Family A retained unavailable slots at p=1, and all three available comparisons against no memory were rejected after Holm correction.

## Context
This work contributes to the growing effort of benchmarking AI agents’ long‑term memory retention and its impact on task performance in software engineering contexts. By using executable oracles and multi‑session designs, DreamBench‑SWE provides a rigorous test of whether memory hygiene can be measured objectively across different configurations.

## Implications
For industry practitioners, DreamBench‑SWE suggests that current memory‑bearing conditions may not uniformly improve agent capabilities, highlighting the need for targeted interventions. The benchmark also underscores the importance of preregistration and careful evaluation to avoid false conclusions about external system mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20664v1)
