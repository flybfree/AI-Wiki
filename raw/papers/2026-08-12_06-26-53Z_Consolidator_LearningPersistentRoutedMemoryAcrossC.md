---
title: Consolidator: Learning Persistent Routed Memory Across Context Boundaries
published: 2026-08-12T06:26:53Z
authors: Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
url: http://arxiv.org/abs/2608.11701v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Consolidator: Learning Persistent Routed Memory Across Context Boundaries

## Abstract
Copying short-term memory (STM) into a slower store can preserve state across a context boundary, but persistence alone does not ensure that the retained state influences subsequent memory access. We test this distinction in a Phasor Memory Network (PMNet) using Consolidator, a shared slot-local operator that transforms routed STM before accumulating it into long-term memory (LTM), without replaying the source tokens. After each consolidation, the KV cache and STM are cleared. The retained LTM can still be read and is also fed into the hierarchical router, thereby conditioning which explicit-memory slots subsequent inputs access. We evaluate this mechanism on a two-segment modulo-10 mapping task in which the second segment updates the mapping at the same memory address. Following a second consolidation and reset, a held-out query must recover the updated mapping from LTM. The backbone and memory interface are frozen, leaving only 12.35K Consolidator parameters trainable (0.041\% of a 29.95M model). Across five paired runs from the same STM-pretraining checkpoint, direct LTM routing raises updated-mapping recall from $44.38\pm1.94\%$ to $87.02\pm1.76\%$ ($+42.64\pm1.10$ percentage points), while immediate STM recall remains 89.90\% in both conditions; both train separate Consolidators and retain the same LTM read paths. Learned consolidation outperforms forced identity accumulation by $21.40\pm1.91$ percentage points without routing and $68.70\pm1.76$ with routing. Thus, on this task, consolidated LTM serves as both retrievable content and an access state that shapes subsequent slot selection.

## Metadata
- **Published**: 2026-08-12T06:26:53Z
- **Authors**: Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11701v1)