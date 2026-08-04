---
title: TreeProbe : A Tibetan Medicine Benchmark for Cultural Bias in LLMs
url: http://arxiv.org/abs/2608.00640v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_12-53-24Z_TreeProbe_ATibetanMedicineBenchmarkforCulturalBias.md
generated_at: 2026-08-03 20:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TreeProbe, a benchmark designed to detect cultural bias in large language models concerning Tibetan medicine. The benchmark uses the native Tree of Medicine framework and demonstrates that current LLMs exhibit systematic external ontology drift, favoring biomedical or TCM reasoning over authentic Tibetan medical knowledge.

## Key Takeaways
- TreeProbe contains 4,719 expert‑adjudicated items covering 467 diseases and ten subtasks within the three roots of Tibetan medicine.  
- Experiments on representative LLMs reveal that models often drift toward biomedical or TCM ontologies rather than preserving Tibetan medical structures.  
- The divergence is linked to differences in pretraining data composition and surface resemblance between Tibetan medicine and other medical traditions.

## Context
The paper situates its work within the growing concern that AI systems may reproduce dominant knowledge systems at the expense of marginalized ones, especially in health‑related applications where equity matters. By providing a concrete benchmark for cultural bias, TreeProbe contributes to broader efforts to make AI more inclusive and ethically responsible.

## Implications
For researchers, TreeProbe offers a diagnostic tool to evaluate whether models respect Tibetan medical epistemology, guiding the design of fairer language systems. For industry practitioners, adopting such benchmarks can prevent harmful misrepresentations that could erode trust in culturally sensitive health technologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00640v1)
