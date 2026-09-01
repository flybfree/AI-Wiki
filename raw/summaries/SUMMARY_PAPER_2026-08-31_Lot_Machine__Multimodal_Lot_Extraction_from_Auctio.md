---
title: Lot Machine: Multimodal Lot Extraction from Auction Catalogs
url: http://arxiv.org/abs/2608.30510v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_09-44-15Z_LotMachine_MultimodalLotExtractionfromAuctionCatal.md
generated_at: 2026-08-31 21:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a pipeline that automatically extracts structured lot-level metadata from German historical auction catalogs. Using Vision‑Language Models with various prompt strategies and constrained decoding, the authors evaluate performance across commercial endpoints, institutional gateways, and locally hosted quantized models.

## Key Takeaways
- Commercial endpoints achieve the highest extraction accuracy, demonstrating that state‑of‑the‑art VLM outputs can reliably produce valid JSON for lot records.
- Institutional gateways provide a privacy‑preserving alternative by hosting quantized models locally, reducing data exposure while maintaining acceptable performance.
- Local deployments are feasible only when strict output formatting is enforced during generation to guarantee correct JSON structure.

## Context
The work addresses the need for machine‑readable representations of archival auction catalogs that are currently inaccessible due to inconsistent formatting. It also highlights trade‑offs between computational resources, budget constraints, and data privacy in deploying AI models for cultural heritage research.

## Implications
By unlocking structured lot data, researchers can conduct large‑scale provenance analyses that were previously impossible. Cultural institutions gain a cost‑effective way to integrate historical catalogs into modern AI pipelines without sacrificing privacy or requiring massive compute budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30510v1)
