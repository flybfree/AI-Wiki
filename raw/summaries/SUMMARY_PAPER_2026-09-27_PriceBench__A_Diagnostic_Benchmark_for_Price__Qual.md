---
title: PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences in LLM Booking Agents
url: http://arxiv.org/abs/2609.31468v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_16-17-28Z_PriceBench_ADiagnosticBenchmarkforPrice_Quality_an.md
generated_at: 2026-09-27 22:15
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces PriceBench, a diagnostic benchmark designed to quantify the implicit price, quality, and brand preferences of Large Language Models acting as autonomous purchasing agents. By applying a logit choice model to booking decisions across 28 LLMs from eight providers on real-world hotel data, the study reveals that model capability is defined by the consistency of choices rather than specific preference directions. The research demonstrates substantial variability in how different models balance price against quality, with mean booked prices shifting dramatically based solely on the underlying model architecture and provider settings.

## Key Takeaways
- Capability in booking agents is correlated with decision consistency rather than specific preference outcomes; more capable models exhibit stronger, more stable preferences, whereas weaker models either rigidly lock onto a single option or display near-indifference, making them vulnerable to manipulation via listing order.
- LLM preferences exhibit extreme heterogeneity across providers and model families, with price sensitivity spanning over an order of magnitude

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31468v1)
