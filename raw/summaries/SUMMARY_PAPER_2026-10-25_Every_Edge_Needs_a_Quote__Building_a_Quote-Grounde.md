---
title: Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents
url: http://arxiv.org/abs/2610.32781v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_15-28-39Z_EveryEdgeNeedsaQuote_BuildingaQuote_GroundedKnowle.md
generated_at: 2026-10-25 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a pipeline for constructing a knowledge graph of healthcare software adoption—specifically customer and integration relations—by extracting verbatim quotes from vendor websites, press releases, and third-party pages using language-model agents. The core design principle is that every edge in the graph must be grounded in a directly quotable passage from its source, and a multi-stage verification process involving deterministic checks and a voting panel of five model calls ensures high precision. The pipeline achieves 0.94 precision and 0.71 recall against its own candidate set, and a confidence-scored variant reaches 0.90 precision at 0.90 recall, demonstrating that quote-grounded extraction can produce reliable structured data from the open web.

## Key Takeaways
- The pipeline enforces a strict "every edge needs a quote" rule: a permissive extractor first proposes candidate relations paired with verbatim source quotes, and a layered grounding stage filters them using a referent step (which reads the full page when a quote names only one side of a relation), deterministic string-matching checks, and a panel of five model calls voting on nine criteria. This architecture directly addresses the hallucination and misattribution risks inherent in LLM-based information extraction.
- On 61 healthcare software vendors, the system proposes 6,428 candidate relations and achieves 0.94 precision and 0.71 recall against a page-level key. Against the marketplace's curated golden reference the scores are lower, but 89% of the relations the pipeline retains that the reference lacks are in fact stated on a source page, suggesting the curated reference is incomplete rather than the pipeline being wrong.
- A confidence score derived from the voting panel's agreement levels outperforms a fixed acceptance rule, reaching 0.90 precision at 0.90 recall. The authors also show that using narrow, bounded model calls, string-matched evidence, and multi-model voting mitigates long-context degradation and run-to-run variance that plague single-pass LLM extraction.

## Context
This work sits at the intersection of knowledge-graph construction, agentic web search, and grounded information extraction—three active areas in applied LLM research. Prior work on automated knowledge-graph building often accepts model-generated claims without verifiable provenance, while healthcare procurement decisions carry high stakes for patient safety and institutional reputation. By mandating a verbatim quote for every asserted relation and layering deterministic checks with multi-model voting, the paper offers a concrete, auditable methodology that moves beyond "trust the model" toward "trust the evidence the model points to," a direction increasingly demanded in regulated and high-consequence domains.

## Implications
For healthcare IT buyers, hospital CIOs, and procurement teams, a quote-grounded adoption graph provides a transparent, auditable evidence trail that can inform costly and hard-to-reverse software purchasing decisions without relying on opaque curated lists. For practitioners building agentic extraction pipelines in any domain, the paper demonstrates that combining a permissive extractor with a multi-criteria voting panel and deterministic string checks yields a tunable precision-recall tradeoff via confidence scores, offering a reusable blueprint for reducing hallucination risk. For the broader AI research community, the findings reinforce that bounded, narrow model calls and ensemble voting are practical defenses against long-context degradation and stochastic output variance, informing the design of future grounded-retrieval and fact-verification systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32781v1)
