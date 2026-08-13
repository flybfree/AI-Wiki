---
title: Disentangling the Expressivity of RoPE
published: 2026-08-12T10:37:21Z
authors: Selim Jerad, Anej Svete, Jiaoda Li, Ryan Cotterell
url: http://arxiv.org/abs/2608.11909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling the Expressivity of RoPE

## Abstract
Two accounts recur in explanations of the success of rotary position embeddings (RoPE). Expressivity studies associate periodic position information with modular predicates, whereas mechanistic and long-context studies emphasize positional anchors and local offsets. We formalize both accounts for fully uniform, finite-precision soft-attention transformers. We find that, if every rotary component is periodic, RoPE transformers recognize exactly the languages definable in past temporal logic with modular predicates. Conventional RoPE is different: The rotations it computes never repeat. This yields a precision-dependent bounded simulation of fixed-offset look-back operators, rather than an all-length modular characterization. Controlled experiments match this separation: Constructed periodic schedules length-generalize on modular languages, while conventional RoPE behaves more like a bounded locality bias and can impair tasks requiring position-invariant access to distant context. Altogether, our findings shed light on RoPE transformers, bringing theoretical expressivity characterizations closer to models used in practice.

## Metadata
- **Published**: 2026-08-12T10:37:21Z
- **Authors**: Selim Jerad, Anej Svete, Jiaoda Li, Ryan Cotterell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11909v1)