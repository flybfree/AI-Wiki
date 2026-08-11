---
title: "Summary: Sharp Capacity Thresholds in Linear Associative Memory: From Winner-Take-All to Listwise Retrieval"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Summary: Sharp Capacity Thresholds in Linear Associative Memory: From Winner-Take-All to Listwise Retrieval


**Source**: [Original Paper](http://arxiv.org/abs/2605.05189v1)
Saved: 2026-05-07 22:08
Source: 2026-05-06_17-53-20Z_SharpCapacityThresholdsinLinearAssociativeMemory_F.md

---

## Summary
This paper analyzes the storage capacity of linear associative memory under different retrieval criteria. For top-1 winner-take-all retrieval, the authors show that capacity depends on an extreme-value logarithmic factor and follows the scale d^2 ≍ n log n, with the correlation-matrix memory construction achieving this threshold. For listwise retrieval, they introduce the Tail-Average Margin (TAM) criterion and show that capacity improves to the quadratic scale d^2 ≍ n.

## Semantic links
- [[concepts/papers/2026-06-11_15-36-14Z_CRAFTIIF_Cross_ResolutionAnalyticFour_TypeI_summary.md|Summary: 2026-06-11_15-36-14Z_CRAFTIIF_Cross_ResolutionAnalyticFour_TypeInterpre.md]] — 1 title term overlap; shared tags: ai, paper, research; 10 summary/topic terms overlap
- [[concepts/papers/2026-06-12_17-54-26Z_AComplexityMeasureforActiveLearninginMulti__summary.md|Summary: 2026-06-12_17-54-26Z_AComplexityMeasureforActiveLearninginMulti_groupMe.md]] — 1 title term overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap

## Key Takeaways
- Retrieval criteria materially change the effective memory capacity.
- Winner-take-all decoding pays an unavoidable logarithmic extreme-value cost.
- Listwise retrieval admits a much better d^2 ≍ n scaling.

## Context
The analysis assumes an isotropic Gaussian model for stored key-value pairs. The paper develops asymptotic theory for the TAM empirical-risk minimizer and studies score and margin distributions.

## Implications
The results clarify when linear memory can scale efficiently and when exact top-1 decoding is intrinsically expensive. They also suggest that relaxing retrieval requirements can substantially improve usable capacity.

## Original Reference
- Title: Sharp Capacity Thresholds in Linear Associative Memory: From Winner-Take-All to Listwise Retrieval
- Authors: Nicholas Barnfield, Juno Kim, Eshaan Nichani, Jason D. Lee, Yue M. Lu
- Published: 2026-05-06T17:53:20Z
- URL: http://arxiv.org/abs/2605.05189v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_17-53-20Z_SharpCapacityThresholdsinLinearAssociativeMemory_F.md

## Related Concepts

- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/ai-infrastructure/ai-infrastructure-hub.md|AI Infrastructure Hub]]
- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
