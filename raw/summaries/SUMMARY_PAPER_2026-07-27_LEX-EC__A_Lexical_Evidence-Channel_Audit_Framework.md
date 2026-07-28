---
title: LEX-EC: A Lexical Evidence-Channel Audit Framework for Zero-Shot LLM Personality Classification in Black-Box Settings
url: http://arxiv.org/abs/2607.24435v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_13-45-12Z_LEX_EC_ALexicalEvidence_ChannelAuditFrameworkforZe.md
generated_at: 2026-07-27 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LEX‑EC, a framework for auditing zero‑shot personality classification in black‑box LLMs by combining prevalence diagnostics, agreement checks, lexical ablation, and prompt sensitivity. It shows that text genre influences trait signals: free‑form essays provide the weakest but broadest signal, graduate introductions show measurable Extraversion after masking, and Facebook statuses yield little stable evidence. LEX‑EC distinguishes marginal effects from true trait associations under restricted lexical evidence.

## Key Takeaways
- Free‑form essay text contains a broad but still weak personality signal that can be recovered only with full lexical input.
- Masking in graduate student introductions reduces the observed Extraversion association, indicating that trait signals depend on available lexical cues.
- Single Facebook statuses exhibit minimal stable evidence even when traits are balanced, suggesting a lower bound of content or length for reliable classification.

## Context
Personality labeling by large language models is widely used but often treated as opaque, limiting trust and interpretability. This work bridges the gap by applying classical linguistic methods to black‑box model behavior, offering a systematic way to evaluate how textual evidence shapes predictions.

## Implications
For practitioners, LEX‑EC provides a reproducible audit tool that can be integrated into model evaluation pipelines. It highlights the importance of lexical richness for reliable personality inference and guides designers toward richer or more balanced data inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24435v1)
