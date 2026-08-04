---
title: Mind the Gap: Zero-Query Jailbreaks via Filter-Generator Discrepancy in Text-to-Image Systems
url: http://arxiv.org/abs/2608.00973v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_03-53-30Z_MindtheGap_Zero_QueryJailbreaksviaFilter_Generator.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a zero-query jailbreak method for text-to-image systems that exploits the Filter-Generator Discrepancy (FGD). By analyzing tokenization and semantic differences between safety filters and image generators, the authors demonstrate how subtle prompt perturbations can evade detection while preserving harmful visual intent. Experiments on six black‑box pipelines raise average attack success rates to 29.2 % (MHSC) and 33.3 % (Q16), outperforming baselines by up to 8–12 percentage points.

## Key Takeaways
- filter-generator discrepancy allows a prompt’s perceived risk to drop for the safety filter while still satisfying the generator’s visual concept  
- the proposed zero‑query framework screens perturbations using observable rules at tokenization and semantic stages, avoiding reliance on surrogate models  
- evolutionary search over high‑potential candidates yields higher success rates than traditional offline adversarial generation

## Context
Text-to-image models are increasingly deployed in creative and commercial settings where safety filters aim to block harmful outputs. However, existing defenses often rely on static thresholds that ignore the mismatch between filter perception and image generation, leaving a loophole exploitable by attackers who cannot query the model directly.

## Implications
The findings highlight a fundamental vulnerability in layered AI safety architectures, urging developers to treat filter and generator objectives as separate problems rather than assuming alignment. For industry practitioners, this means designing more robust prompt‑level defenses that account for such discrepancies or adopting proactive monitoring of anomalous input patterns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00973v1)
