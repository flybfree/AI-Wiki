---
title: Domain-Grounded Candidate Selection for Agentic Image Editing: A Shadow Removal Case
url: http://arxiv.org/abs/2608.06075v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_14-19-22Z_Domain_GroundedCandidateSelectionforAgenticImageEd.md
generated_at: 2026-08-06 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether commercial vision‑language models can replace traditional low‑level physics‑based methods for shadow removal, a task that depends on scene geometry and illumination. The authors demonstrate that an agentic candidate‑selection pipeline improves the quality of generated edits by grounding prompts in physical principles, achieving a CDD score of 0.0075—47% lower than prior work.

## Key Takeaways
- The editor can produce clean shadow‑free images but often hallucinates or misinterprets shadows as material or geometry, leading to plausible yet physically incorrect results.  
- An agentic pipeline that generates a probe, evaluates it for major failures, and retries when needed yields higher quality outputs by balancing removal with scene preservation.  
- Prompting the generator and evaluator to treat shadows solely as illumination caused by light occlusion, rather than material or structural features, markedly improves consistency.

## Context
Commercial vision‑language models are increasingly used for image editing tasks, offering strong visual priors but limited physical grounding. This study highlights a gap: while these models can generate visually appealing results, they often violate the underlying physics of scenes like shadows, which are essential for realistic perception and downstream applications.

## Implications
For practitioners, this research suggests that integrating low‑level physics constraints remains valuable when fine‑tuning generative editors to avoid hallucinations. It also underscores a need for hybrid approaches that combine high‑level creativity with physical grounding to meet both quality and reliability standards in AI‑driven image editing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06075v1)
