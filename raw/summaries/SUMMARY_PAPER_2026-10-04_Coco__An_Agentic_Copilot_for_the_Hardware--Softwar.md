---
title: Coco: An Agentic Copilot for the Hardware--Software Co-Design Lifecycle
url: http://arxiv.org/abs/2610.02376v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_18-55-52Z_Coco_AnAgenticCopilotfortheHardware__SoftwareCo_De.md
generated_at: 2026-10-04 21:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Coco (Copilot for Codesign) is an agentic platform developed and deployed with TPU architects to accelerate the hardware-software co-design lifecycle, covering experiment setup, simulator sweeping, and insight derivation. The paper addresses a fundamental challenge in ML accelerator design: the evidence needed for high-stakes architectural decisions is generated fresh each quarter and is absent from any LLM's pretraining corpus, making naive retrieval-augmented approaches prone to hallucination. The authors report early deployment experience showing reductions in time-to-simulation and time-to-insight, arguing that co-design constitutes a distinct agentic domain requiring specialized tooling rather than general-purpose chat interfaces.

## Key Takeaways
- Coco is architected as four interlocking layers: a normalized relational datastore that automatically registers every simulation sweep so agents ground numerical claims in SQL queries rather than scraping heterogeneous files; a library of tools with typed APIs that agents compose autonomously without human orchestration; agents encoding recurring analysis workflows such as iso-execution analysis, which compares systems at matched execution configurations including swept-but-dominated points off the Pareto frontier; and a platform UX whose navigation state doubles as agent context, blending IDE-style control with interactive exploration.
- The core problem Coco solves is that co-design evidence—hundreds of gigabytes of fresh simulation sweeps over novel design points—is by construction absent from any LLM's pretraining corpus and has no external literature to retrieve, meaning naive "chat-with-your-data" approaches hallucinate precisely where correctness matters most. This makes retrieval-grounded agentic workflows essential rather than optional.
- The authors argue that co-design is a distinct agentic domain characterized by three properties: its data must be retrieved rather than memorized, its workflows are recurring but context-dependent, and expert adoption hinges on a UX that balances IDE-style control with interactive exploration—distinguishing it from general-purpose coding or research assistants.

## Context
This paper sits at the intersection of agentic AI systems and computer architecture methodology, addressing a domain where the pace of both model evolution and hardware cadence means the analysis burden grows every quarter. As ML accelerators become increasingly specialized and co-design decisions carry enormous financial and performance stakes, the gap between the volume of simulation data generated and the human capacity to reason over it widens. Coco represents a concrete industrial deployment of agentic tooling in a high-stakes engineering setting, moving beyond academic prototypes toward production workflows used by TPU architects at Google.

## Implications
For hardware and ML systems practitioners, Coco demonstrates that agentic copilots can meaningfully compress time-to-simulation and time-to-insight in co-design workflows, potentially accelerating the cadence at which new accelerator architectures are evaluated and iterated. For the broader agentic AI field, the paper establishes a template for domains where all critical data is freshly generated and must be retrieved through structured tool use rather than recalled from training data, suggesting that future agentic systems for scientific and engineering discovery will require purpose-built datastores, typed tool APIs, and UX designs that respect expert workflows rather than imposing generic chat interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02376v1)
