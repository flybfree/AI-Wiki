---
title: Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded Text to Image Generation
published: 2026-08-07T03:17:49Z
authors: Kuan Xing, Ye Wang, Changyi Gan, Yuheng Li, Thao Nguyen, Yi Chang, Yilin Wang
url: http://arxiv.org/abs/2608.06751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded Text to Image Generation

## Abstract
Artist-grounded image generation requires more than appending an artist name to a prompt. Image models often respond to artist names through canonical shortcuts, such as recurring motifs, generic palettes, or overrepresented period signatures, rather than preserving the user's intended scene. We introduce Atelier, a shortcut-aware control-state planning framework for artist-grounded image generation. Atelier translates underspecified artistic intent into an explicit control state that separates scene anchors, preserve/transform decisions, style-regime hypotheses, role-bound artist evidence, and shortcut-avoidance constraints. It grounds this state using artist-level knowledge and local patch references, compiles backend-aware generation plans, and iteratively refines candidates through global and local authenticity feedback. We further introduce ArtIntentBench, a benchmark covering Van Gogh and Qi Baishi across artwork re-rendering, period/style-controlled generation, historically unseen subjects, shortcut auditing, and human preference evaluation. Across open-weight and closed-source generators, Atelier improves artist-level style fidelity, preserves source structure more faithfully, and substantially reduces shortcut substitution compared with prompt-engineered, retrieval-augmented, and general-purpose agent baselines. These results suggest that artist-grounded generation is bottlenecked not only by image synthesis, but by the upstream inference of explicit, evidence-grounded artistic controls.

## Metadata
- **Published**: 2026-08-07T03:17:49Z
- **Authors**: Kuan Xing, Ye Wang, Changyi Gan, Yuheng Li, Thao Nguyen, Yi Chang, Yilin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06751v1)