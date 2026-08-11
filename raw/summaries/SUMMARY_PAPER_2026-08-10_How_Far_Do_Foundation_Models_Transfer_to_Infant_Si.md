---
title: How Far Do Foundation Models Transfer to Infant Signals? A Cross-Dataset Transfer Audit with a Unified Need Ontology
url: http://arxiv.org/abs/2608.08989v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_01-22-32Z_HowFarDoFoundationModelsTransfertoInfantSignals_AC.md
generated_at: 2026-08-10 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates how well frozen foundation models can transfer knowledge from one infant cry corpus to another using a unified five‑class need ontology. Across four datasets the authors find that single‑corpus evaluation hides large F1 swings, negative cross‑corpus transfer is common, and many clips have conflicting labels. The study also shows that transferring into the noisiest dataset can be beneficial when training size matches or exceeds the source corpus.

## Key Takeaways
- Within‑domain macro‑F1 varies by 0.57–0.80 for the same encoder across corpora, indicating hidden variability in single‑corpus evaluation.  
- Cross‑corpus transfer is on average negative (negative‑transfer ratio 0.19–0.35) and significant in 18 of 30 directed cells, highlighting data incompatibility issues.  
- Transfer into the noisiest corpus yields positive effect sizes at matched training size after near‑duplicate removal, offering a practical recipe for small noisy corpora.

## Context
The rapid growth of foundation models has led to widespread use of pre‑trained encoders on limited, domain‑specific datasets such as infant cry recordings. However, these models are often evaluated in isolation, ignoring how their knowledge may transfer—or degrade—across different but related data sources. This work bridges that gap by providing a systematic audit and shared task framework.

## Implications
For practitioners, the findings suggest that joint training with an ontology can outperform naive label merging, preserving performance even when labels are sparse or noisy. The methodology also offers a template for auditing model transferability in other small‑scale multimodal tasks, encouraging more robust evaluation practices across the AI community.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08989v1)
