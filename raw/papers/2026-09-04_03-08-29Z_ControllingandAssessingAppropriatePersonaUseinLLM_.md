---
title: Controlling and Assessing Appropriate Persona Use in LLM-based Dialogue Generation
published: 2026-09-04T03:08:29Z
authors: Jongkyung Shin, Inkyu Lee, Chiehyeon Lim
url: http://arxiv.org/abs/2609.04676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Controlling and Assessing Appropriate Persona Use in LLM-based Dialogue Generation

## Abstract
In persona-based dialogue generation (PDG), LLMs often overuse persona attributes by incorporating them regardless of dialogue context, resulting in unnatural responses. Despite its practical significance, the underlying causes remain unexplored, with no method to mitigate this problem or metric to assess the appropriateness of persona use. To address these issues, we first conduct a comprehensive analysis of LLM-based PDG, revealing that LLMs exhibit a systematic bias to incorporate all given persona attributes, and that existing metrics fail to capture contextual appropriateness. Building on these findings, we propose Self-CONtrastive Persona Overuse Suppression (SCONPOS) to mitigate overuse by directly intervening in LLMs' internal representations at the prompt encoding stage, without requiring any response generation. We further propose the Persona Appropriateness Score (PAS), a novel metric that penalizes both overuse and underuse. Experimental results demonstrate that SCONPOS systematically reduces overuse, and PAS captures the contextual appropriateness of persona use.

## Metadata
- **Published**: 2026-09-04T03:08:29Z
- **Authors**: Jongkyung Shin, Inkyu Lee, Chiehyeon Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04676v1)