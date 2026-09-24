---
title: Not What You Meant: Can LLMs Follow a Specified Negation Semantics?
published: 2026-09-23T08:14:47Z
authors: Qiming Bao, Agnieszka Mensfelt, Michael J. Witbrock, Kostas Stathis
url: http://arxiv.org/abs/2609.27517v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not What You Meant: Can LLMs Follow a Specified Negation Semantics?

## Abstract
Negation does not carry a uniform interpretation across domains. In legal, regulatory, and medical reasoning, the intended interpretation depends on the reading in force -- open- versus closed-world, two- versus three-valued, and credulous versus skeptical. We study which reading of negation large language models adopt by default and whether they can override that preference when a different reading is explicitly specified. To this end, we introduce NAFBench, a procedural generator of solver-certified instances spanning four semantic viewpoints: SLDNF, well-founded semantics (WFS), and credulous and skeptical reasoning under stable-model semantics. The generator emits ground normal logic programs with controlled depth, width, and cycle structure. Each program is solved under all four viewpoints using SWI-Prolog, a well-founded semantics solver, and clingo, yielding up to four divergent labels. The programs are then verbalized into natural language under multiple framings and rule orderings that leave the answer invariant. The results expose a consistent gap. Across open-source models, following a specified negation semantics remains unsolved: the strongest models score 59--74% across the four semantic viewpoints, while the weakest score 31--67%. All models are order-sensitive on more than half of logically identical rule shufflings, while the two weaker models frequently overcommit on well-founded "undefined." Two frontier models reach 100% on the main fixed-complexity evaluation set, and a third, o4-mini, is near-perfect, falling only to 81% on well-founded "undefined." Delegating reasoning to a solver, fine-tuning on certified traces, or forcing an explicit three-valued verdict each partly closes the gap.

## Metadata
- **Published**: 2026-09-23T08:14:47Z
- **Authors**: Qiming Bao, Agnieszka Mensfelt, Michael J. Witbrock, Kostas Stathis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27517v1)