---
title: COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models
url: http://arxiv.org/abs/2608.17234v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_00-45-29Z_COMIC_Reference_AwareSafetyGatingforMultimodalLarg.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces COMIC, a reference‑aware safety gating mechanism for multimodal large language models that addresses a specific failure mode where unsafe behavior only appears when an operation is bound to a visual target. The authors demonstrate that existing defenses degrade because they treat the prompt and image as a single unit rather than focusing on the grounded operation‑target pair. COMIC improves robustness while keeping benign functionality intact.

## Key Takeaways
- COMIC isolates safety evaluation to explicit operation‑target pairs, preventing unsafe actions from emerging when only the prompt or image is benign in isolation.  
- The system infers the requested operation and reference type, generates candidate targets using OCR and open‑vocabulary proposals, then grounds plausible referents before assessing risk.  
- By aggregating max‑risk scores with quality‑aware routing, COMIC makes conservative decisions that block only genuinely hazardous requests.

## Context
Multimodal large language models now routinely process images alongside text, enabling richer interactions but also expanding the attack surface for jailbreaks. Traditional safety modules lack awareness of how visual references are resolved during inference, leading to inconsistent protection. This research highlights a gap in current defenses and proposes a targeted solution that aligns with the operational flow of MLLMs.

## Implications
For developers deploying MLLMs, COMIC offers a practical way to harden systems against reference‑dependent attacks without sacrificing performance on legitimate tasks. The approach could become a standard component in safety pipelines, encouraging research into operation‑specific risk modeling across multimodal AI products.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17234v1)
