---
title: Right Reset: Chunking by Prefix Removal
published: 2026-08-05T01:17:12Z
authors: Mike Vegeto
url: http://arxiv.org/abs/2608.04330v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Right Reset: Chunking by Prefix Removal

## Abstract
Removing the left context from a causal language model reveals a useful kind of boundary: an edge where the model processes the same right-hand tokens with little change. We turn this observation into prefix-removal probing and introduce Right Reset (RR), which measures preservation of the right-hand hidden-state trajectory. A dynamic program converts RR edge scores into variable-length chunks. On flattened text formed by concatenating topically similar records after deleting their separators and layout, RR recovers 47.7% of the original records as clean units, versus 25.9% for a BGE embedding boundary, the strongest tested conventional baseline without task-specific model training. The gain persists after rendering and OCR. Passive scores from the same Qwen3-4B layer and direct prompting of a same-scale instruction model perform substantially worse on flattened records. Across six language models, RR-selected cuts also undergo consistently less local output disruption than unselected candidate edges. An observed-token likelihood-ratio readout is competitive in some architectures, indicating that the central contribution is the intervention: context dependence itself can provide a boundary signal when surface structure is weak.

## Metadata
- **Published**: 2026-08-05T01:17:12Z
- **Authors**: Mike Vegeto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04330v1)