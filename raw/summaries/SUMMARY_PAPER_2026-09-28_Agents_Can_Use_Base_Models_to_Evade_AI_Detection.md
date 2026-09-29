---
title: Agents Can Use Base Models to Evade AI Detection
url: http://arxiv.org/abs/2609.31876v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_18-13-40Z_AgentsCanUseBaseModelstoEvadeAIDetection.md
generated_at: 2026-09-28 22:12
model: qwen3.6-35b-a3b
---

## Summary
This study demonstrates that coding agents equipped with base language models can effectively evade AI detection by orchestrating the assembly of responses directly from model samples, avoiding the semantic drift associated with iterative paraphrasing techniques. The research shows that a Claude Opus 5 agent harnessing a local OLMo-2 base model maintains high task accuracy while generating outputs composed largely of base LM tokens, significantly reducing detection rates for both post-hoc detectors and soft watermarking schemes.

## Key Takeaways
- Direct orchestration of base model samples allows coding agents to produce coherent, task-specific text without the semantic degradation inherent in iterative humanization techniques that rely on paraphrasing AI outputs over multiple steps.
- A Claude Opus 5 agent operating in a Claude Code harness can effectively manage a local 32B parameter OLMo-2 base model to generate responses that achieve comparable task accuracy across diverse benchmarks while utilizing up to 90% tokens from the base LM, thereby reducing detection rates for Pangram v4 from 77% to 24%.
- While this evasion strategy successfully undermines both post-hoc detectors and a priori soft watermarking (dropping detection to approximately 10% at low false positive rates), it necessitates a substantially higher consumption of input and output tokens, which can increase the monetary cost per query by up to 30 times at standard API pricing.

## Context
As AI-generated content becomes ubiquitous, the development of robust detection mechanisms is critical for maintaining integrity in educational, professional, and security domains; however, this work highlights a fundamental

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31876v1)
