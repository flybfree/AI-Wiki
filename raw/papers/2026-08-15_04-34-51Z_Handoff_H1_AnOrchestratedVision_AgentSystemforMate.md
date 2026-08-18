---
title: Handoff-H1: An Orchestrated Vision-Agent System for Material Quantity Takeoff from Construction Blueprints
published: 2026-08-15T04:34:51Z
authors: Bruno Chicelli, Henrique Alves, Rodrigo Anselmo, Joshua Weinberg, Felipe Lemos, Jan Baryla
url: http://arxiv.org/abs/2608.15032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Handoff-H1: An Orchestrated Vision-Agent System for Material Quantity Takeoff from Construction Blueprints

## Abstract
Converting a set of architectural blueprints into a complete material quantity takeoff requires visual perception across drawing sheets, dimensional and multi-hop reasoning, and grounding in construction conventions that the drawings never state. We present Handoff-H1, a takeoff system built from three layers: purpose-built computer-vision models that extract primitives; tool-using agents equipped with image operations and in-house visual-task tools, including CV-model-backed counting, detection and plan decomposition; and a persistent, hierarchically structured project foundation, grounded in a curated construction knowledge base. We evaluate on the Construction Blueprint Takeoff Benchmark: 10 real residential blueprint sets paired with consensus-validated expert takeoffs - 2,009 verified line items, restricted for scoring to the 1,348 primary-tier materials that drive an estimate - scored per trade by an LLM judge on material coverage and quantity Precision@25% (P@.25) and combined into a weighted composite. Under identical scoring from the raw PDF, seven frontier and open-weight models span composites of 35-61, and independent professional estimators - scored against the same reconciled gold standard - post 77.6% (65.5% coverage, 87.9% P@.25). Handoff-H1, working end-to-end from the raw PDF, reaches 81.6% (86.1% coverage, 78.8% P@.25): roughly 20 points above the strongest frontier agent, and above the independent estimators by pairing near-human quantity precision with coverage they do not reach. The evaluation harness is public for the open harbor framework; the blueprint sets and ground truth are available upon request for research use.

## Metadata
- **Published**: 2026-08-15T04:34:51Z
- **Authors**: Bruno Chicelli, Henrique Alves, Rodrigo Anselmo, Joshua Weinberg, Felipe Lemos, Jan Baryla
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15032v1)