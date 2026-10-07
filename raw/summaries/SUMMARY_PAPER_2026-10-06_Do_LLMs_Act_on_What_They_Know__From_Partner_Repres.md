---
title: Do LLMs Act on What They Know? From Partner Representations to Cooperative Actions
url: http://arxiv.org/abs/2610.08129v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_10-44-55Z_DoLLMsActonWhatTheyKnow_FromPartnerRepresentations.md
generated_at: 2026-10-06 21:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper examines whether large language models can convert knowledge about an unfamiliar partner’s communication conventions into cooperative actions in a controlled Hanabi-derived setting. It finds that intent conventions can be decoded more reliably than target conventions, but models do not consistently act on decoded conventions, and externally computed action recommendations improve cooperation more than rule statements.

## Key Takeaways
- In eight LLMs, linear probes recover sender intent conventions substantially more accurately than target conventions, showing that partner conventions are often decodable from model states or representations even when cooperation remains imperfect.
- Receiving decisions do not consistently align with the sender’s convention, indicating a gap between convention decodability and behavioral use: knowing or detecting a convention does not guarantee that the model will translate it into the correct cooperative action.
- Presenting convention information as general rules produces modest and model-dependent cooperation changes, while action translation yields larger average gains; in Qwen3-8B, matched-state statement reversals show much stronger sensitivity to action recommendations than to rule statements, and activation transfers from oracle-action donors can improve intent accuracy but are not reliably reproduced by tested alternatives.

## Context
Cooperation among agents is a central challenge in multi-agent AI, especially when partners use unfamiliar or implicit conventions. This work matters because it separates three distinct capabilities: decoding partner conventions, making models sensitive to convention information, and achieving cooperative performance. It clarifies that LLMs may possess latent information about partners without reliably using it in action selection.

## Implications
For practitioners, the results suggest that simply providing rules or natural-language convention descriptions may be insufficient for reliable multi-agent coordination. Instead, systems may need explicit action translation, recommendation interfaces, or representation-level interventions to turn partner knowledge into decisions. The findings also caution against assuming that improved internal decodability automatically leads to better cooperative behavior in deployed LLM agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08129v1)
