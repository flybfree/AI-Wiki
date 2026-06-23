---
title: Semantic Browsing: Controllable Diversity for Image Generation
published: 2026-06-22T17:59:17Z
authors: Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik, Daniel Cohen-Or
url: http://arxiv.org/abs/2606.23679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Semantic Browsing: Controllable Diversity for Image Generation

## Abstract
Modern text-to-image models excel in visual fidelity and prompt adherence. However, this strict adherence comes at the cost of diversity: generated samples tend to collapse into a single visual interpretation. Existing methods to improve diversity produce outputs driven by incidental variations rather than meaningful design choices. This motivates a new variant of the diversity task where structure is enforced on the generated samples. We introduce a method for controlled diversity that enables Semantic Browsing, where users can navigate structured image galleries and experience creative exploration through a systematic traversal of meaningful, interpretable axes of variation. Achieving this level of semantic control requires a deep understanding of the scene. We exploit the fact that recent text-to-image models are trained on elaborated captions, effectively decoupling semantic decision-making from pixel generation. This enables a paradigm shift: instead of relying on stochastic variation within the text-to-image model, we induce diversity directly at the text level. By leveraging rich textual representations, we allow a Vision Language Model (VLM) to operate on the full scene context. To overcome the generic outputs typical of standard VLMs, we employ an agentic workflow that explicitly enforces structured variation attuned to the original prompt. We demonstrate that our method produces diverse and navigable design spaces where every variation corresponds to a specific, user-understandable semantic decision.

## Metadata
- **Published**: 2026-06-22T17:59:17Z
- **Authors**: Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik, Daniel Cohen-Or
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.23679v1)