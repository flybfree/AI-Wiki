---
title: Architecture as Capability Equalizer for Coding Agents
published: 2026-08-22T03:04:12Z
authors: Arquimedes Canedo
url: http://arxiv.org/abs/2608.21747v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Architecture as Capability Equalizer for Coding Agents

## Abstract
LLM-based coding agents generate complete software systems from high-level descriptions, yet little is known about how the format of architecture specifications affects the quality of generated code or whether this effect depends on model capability. We present a controlled experiment comparing five informationally equivalent specification formats (informal prose, Mermaid diagrams with constraints and ADRs, OpenAPI, C4/Structurizr DSL, and TypeScript interface contracts with ArchUnit-style rules) across six models from three vendor families (Anthropic Claude, OpenAI GPT, Google Gemini). Across 90 multi-turn agent trials, specification format shows a strong format x model interaction. On the strongest models (Sonnet 4.6, GPT-5), format barely matters (quality spread 0.17-0.92). On weaker models, format produces spreads of 0.83-2.42 points, with code-proximate formats (OpenAPI, TypeScript contracts) recovering most of the capability gap. Mid-tier models can consume more tokens than frontier models for worse output when they enter compilation debugging loops that stronger models avoid. Self-validation rates collapse from 100% (Sonnet) to 0% (Gemini Flash) across the capability spectrum. TypeScript contracts triple API route coverage for the weakest model (33% to 100%). Structured architecture specifications serve as a capability equalizer, with value inversely proportional to model strength and the largest returns for cost-optimized deployments.

## Metadata
- **Published**: 2026-08-22T03:04:12Z
- **Authors**: Arquimedes Canedo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21747v1)