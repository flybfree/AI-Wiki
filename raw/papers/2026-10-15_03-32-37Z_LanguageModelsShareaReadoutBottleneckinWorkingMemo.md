---
title: Language Models Share a Readout Bottleneck in Working Memory
published: 2026-10-15T03:32:37Z
authors: Dongyu Gong
url: http://arxiv.org/abs/2610.21176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Share a Readout Bottleneck in Working Memory

## Abstract
Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent items are retrieved instead. On an interference account, attention selects the correct item, but the content of competing items corrupts the decision. We dissociate these accounts in 15 pretrained LLMs from three families (70 million to 14 billion parameters) and in minimal transformers trained from scratch. In all three families, the attention heads that carry the task attend to the target on most missed matches. Linear probes decode near-perfectly whether a matching letter occurred at the target or at a lure position, even on trials where the model false-alarms to the lure, although its own decisions barely distinguish the two. Sharpening attention yields negligible gains, whereas suppressing the letter identity of non-target items improves sensitivity (d') in nearly all model-by-load conditions. In larger models the task is spread over more heads, and removing interference helps more. In minimal transformers, precision limits a single attention layer, but a second layer removes this constraint. The working-memory limit of LLMs therefore lies in reading items out under interference rather than in locating them, consistent with interference accounts of human working memory.

## Metadata
- **Published**: 2026-10-15T03:32:37Z
- **Authors**: Dongyu Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21176v1)