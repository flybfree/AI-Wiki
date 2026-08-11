---
title: "Summary: 2026-04-22_17-45-27Z_ConvergentEvolution_HowDifferentLanguageModelsLear.md"
date: 2026-04-22
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-04-22_17-45-27Z_ConvergentEvolution_HowDifferentLanguageModelsLear.md


**Source**: [Original Paper](http://arxiv.org/abs/2604.20817v1)
Saved: 2026-05-08 03:23:13Z
Source: 2026-04-22_17-45-27Z_ConvergentEvolution_HowDifferentLanguageModelsLear.md
Model: None
---

## Summary
This paper studies how different model families learn number representations from natural text. It finds that Transformers, Linear RNNs, LSTMs, and classical word embeddings often develop Fourier-domain periodic features with dominant periods at 2, 5, and 10. However, only some of these features are geometrically separable enough to support linear classification by number modulo T. The authors argue that Fourier sparsity alone is not sufficient for such separability and show that training details strongly influence whether it emerges.

## Semantic links
- [[concepts/papers/2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionfo_summary.md|Summary: 2026-06-15_17-52-27Z_DEEPRUBRIC_Evidence_TreeRubricSupervisionforEffici.md]] — 3 title terms overlap; shared tags: ai, paper, research; 6 summary/topic terms overlap
- [[concepts/papers/2026-06-12_17-48-27Z_HumP_KD_AHybridUncertainty_AwareMulti_Stage_summary.md|Summary: 2026-06-12_17-48-27Z_HumP_KD_AHybridUncertainty_AwareMulti_StageProgres.md]] — 3 title terms overlap; shared tags: ai, paper, research; 6 summary/topic terms overlap

## Key Takeaways
- Diverse architectures can learn similar periodic number features.
- Fourier-domain spikes at periods 2, 5, and 10 are common but not enough for mod-T classification.
- Geometric separability depends on data, architecture, optimizer, and tokenizer.
- Two routes to separable features are identified: complementary language co-occurrence signals and multi-token addition tasks.

## Context
The work connects representation learning in language models with number structure in text. It examines both broad natural-language training signals and controlled numeric tasks to explain when periodic features become linearly usable.

## Implications
The results suggest that similar internal features can arise across model types through different training paths. This supports the idea of convergent evolution in representation learning and highlights that feature shape in Fourier space does not fully determine downstream linear separability.

## Original Reference
- Title: Convergent Evolution: How Different Language Models Learn Similar Number Representations
- Authors: Deqing Fu, Tianyi Zhou, Mikhail Belkin, Vatsal Sharan, Robin Jia
- URL: http://arxiv.org/abs/2604.20817v1
- Published: 2026-04-22T17:45:27Z

[[Convergent Evolution: How Different Language Models Learn Similar Number Representations]]

## Related Concepts

- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/ai-infrastructure/ai-infrastructure-hub.md|AI Infrastructure Hub]]
- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
- [[concepts/data-curation/data-curation-hub.md|Data Curation Hub]]
