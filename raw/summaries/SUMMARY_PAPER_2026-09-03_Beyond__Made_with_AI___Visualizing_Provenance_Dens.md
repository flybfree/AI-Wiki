---
title: Beyond "Made with AI": Visualizing Provenance Density to Mitigate the Transparency Penalty
url: http://arxiv.org/abs/2609.03460v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-18-42Z_Beyond_MadewithAI__VisualizingProvenanceDensitytoM.md
generated_at: 2026-09-03 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Provenance Density, an interface that visualizes the density of verified claims within a text to help users distinguish AI‑generated from human content. In a user study with 81 participants, the idealized interface produced a significant discrimination gap between truth and fabrication (+4.15 points, d=1.82), while participants without any signal showed no detectable difference. A technical audit of 200 samples revealed that retrieval density alone is insufficient; instead, the Consistency Veto provides most of the discriminative power on dynamic queries.

## Key Takeaways
- The idealized Provenance Density interface creates a large discernment gap (+4.15 points, d=1.82) between truth and fabricated text.
- Retrieval density alone is insufficient for discrimination; the Consistency Veto contributes most of the signal on dynamic queries.
- Without any provenance signal users cannot reliably differentiate AI‑generated from human content.

## Context
Generative AI has produced fluent text that can be indistinguishable from human writing, eroding trust in fluency as a truth proxy. Traditional transparency measures such as binary 'Made with AI' labels fail to convey supporting evidence. This work addresses the need for evidence‑based transparency by providing an interface that visualizes verified claims.

## Implications
For researchers and industry practitioners, Provenance Density offers a concrete method to embed verifiable claims into AI outputs, reducing the Fluency Trap. By shifting focus from authorship disclosure to evidence visualization, it aligns with user expectations for trustworthy information in an era of synthetic text.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03460v1)
