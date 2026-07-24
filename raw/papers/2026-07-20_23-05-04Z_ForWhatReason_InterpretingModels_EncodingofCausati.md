---
title: For What Reason? Interpreting Models' Encoding of Causation and Antithesis
published: 2026-07-20T23:05:04Z
authors: Abhidip Bhattacharyya, Shira Wein
url: http://arxiv.org/abs/2607.18570v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# For What Reason? Interpreting Models' Encoding of Causation and Antithesis

## Abstract
Discourse relations provide document structure, critical to language understanding and enabling language model performance and ethicality. In this work, we investigate how instruction-tuned Transformer models (LLaMA and Mistral) encode discourse relations in English, with a particular focus on the contrasting relations of causation and antithesis. Framing the task as a next-token prediction task and applying a suite of interpretability techniques to test model internals, our findings show that certain early layers make predictive decisions at mid-sequence tokens, while some mid-level layers finalize their decisions closer to the last token. Most of the remaining layers primarily propagate earlier decisions rather than actively influencing them. Additionally, we observe that some layers exhibit a preference for one answer over alternatives, suggesting asymmetric representation of discourse-based reasoning.\footnote{Our code is available at https://github.com/abhidipbhattacharyya/causation_vs_antithesis}

## Metadata
- **Published**: 2026-07-20T23:05:04Z
- **Authors**: Abhidip Bhattacharyya, Shira Wein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18570v1)