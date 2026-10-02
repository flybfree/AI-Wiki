---
title: Emergent Unfaithfulness: How Alignment Training Causes Language Models to Silently Override Task Faithfulness
published: 2026-09-30T18:41:05Z
authors: Pardis Sadat Zahraei, Janvijay Singh, Gokhan Tur, Dilek Hakkani-Tur
url: http://arxiv.org/abs/2610.00568v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Emergent Unfaithfulness: How Alignment Training Causes Language Models to Silently Override Task Faithfulness

## Abstract
Large language models are characterized by three key properties: capability, alignment, and faithfulness. Prior work studies the tradeoffs between capability and alignment, and between capability and faithfulness, but a third tension remains underexplored: the alignment-faithfulness conflict. We show that aligned models systematically deviate from their inputs on unsafe or sensitive content without disclosing the modification, a failure mode we call alignment-induced unfaithfulness (AIU). Unlike capability-driven unfaithfulness, which comes from errors in knowledge or reasoning, this is induced by post-training mechanisms that override adherence to the input. We introduce FaithConflict, a controlled dataset isolating both conflicts, and two complementary taxonomies: behavioral (B1-B8) and chain-of-thought reasoning (C0-C6). Across models, AIU increases with scale and more sharply than capability-driven unfaithfulness, a reverse scaling law; intermediate checkpoints show it is amplified during post-training, with DPO the stage at which the gap both grows most and becomes least visible. Prompting-based mitigation does not resolve it, revealing a capability-alignment-faithfulness trilemma in the design and evaluation of LLMs.

## Metadata
- **Published**: 2026-09-30T18:41:05Z
- **Authors**: Pardis Sadat Zahraei, Janvijay Singh, Gokhan Tur, Dilek Hakkani-Tur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00568v1)