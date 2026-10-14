---
title: What Survives When Activation Steering Is Used as Memory
published: 2026-10-10T14:31:47Z
authors: Vedant Jumle
url: http://arxiv.org/abs/2610.14958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Survives When Activation Steering Is Used as Memory

## Abstract
Activation steering has recently been used as a memory for skills: past experiences of an agent are stored as steering vectors and retrieved later. Facts and preferences about the user are assumed to need text instead. We test that assumption with a training-free activation memory beside a frozen LLM. The change an experience causes in late-layer states is stored as a shift, filed under a whitened key for the conversation's gist, and added back in a later session only when the gist matches. We argue that such a shift is a fixed average of an effect that attention, in context, recomputes for every question, so only question-independent content can survive. In a pre-registered study on Qwen3.5-2B and 9B, with judges from four model families, the memory is selective (about 98% of unrelated replies are unchanged), but facts are stored as the word to say, in the last layers only, and are almost never used (at most 15% clean use, against 96-98% in context). Leanings transfer only in a narrow strength window. Most strikingly, the reference subtracted when writing a preference decides whether its concept or its direction survives: unless the opposite is subtracted, a stored dislike is recalled as a like.

## Metadata
- **Published**: 2026-10-10T14:31:47Z
- **Authors**: Vedant Jumle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14958v1)