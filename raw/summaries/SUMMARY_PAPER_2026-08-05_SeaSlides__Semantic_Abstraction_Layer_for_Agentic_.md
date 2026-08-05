---
title: SeaSlides: Semantic Abstraction Layer for Agentic Slide Generation
url: http://arxiv.org/abs/2608.03298v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_08-08-28Z_SeaSlides_SemanticAbstractionLayerforAgenticSlideG.md
generated_at: 2026-08-05 01:11
model: nvidia/nemotron-3-nano-4b
---

## Summary  
SeaSlides introduces a semantic abstraction layer that separates slide content from layout and rendering, allowing agents to generate structured decks without embedding raw SVG or HTML details. The framework supports both HTML and Typst backends through reusable components and capability modules, while templates handle styling and layout. Experiments show higher readability and richer content across four generation models on benchmarks that include formulas, code, and charts.

## Key Takeaways  
- The model writes slide content via structured components rather than inline SVG or raw HTML, reducing brittleness for technical slides.  
- Separate capability modules route equations, code, and data graphics to dedicated renderers, improving reliability during generation.  
- Three feedback stages catch errors locally, enabling precise fixes before final export.

## Context  
Current slide‑generation systems either rely on rigid templates that limit adaptation or produce unstructured HTML/SVG that forces low‑level rendering decisions, leading to fragile outputs for technical content. This paper addresses the gap by proposing a unified abstraction layer that balances flexibility with maintainable structure across presentation backends.

## Implications  
Semantic abstraction can make AI‑generated decks more robust and human‑readable, benefiting developers who create data‑heavy presentations. Practitioners may adopt this pattern to streamline authoring pipelines while preserving visual consistency without sacrificing model creativity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03298v1)
