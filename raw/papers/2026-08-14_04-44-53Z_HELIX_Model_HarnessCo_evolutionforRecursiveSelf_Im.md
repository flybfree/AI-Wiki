---
title: HELIX: Model-Harness Co-evolution for Recursive Self-Improvement
published: 2026-08-14T04:44:53Z
authors: Tianyu Fan, Chao Huang
url: http://arxiv.org/abs/2608.13951v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HELIX: Model-Harness Co-evolution for Recursive Self-Improvement

## Abstract
Scaling agent capability has largely focused on improving the model, yet an interactive agent acts through a runtime harness that mediates context, tools, control flow, and stopping. The harness shapes both what a model can accomplish and the trajectories from which it learns. This coupling motivates model-harness co-evolution for recursive self-improvement: build harnesses for a fixed model, update the model from verified sibling trajectories, and rebuild the harnesses as model capabilities change. Realizing this loop requires a controlled way to evolve harnesses while preserving intervention identity and effect. We present HELIX, a source-traceable substrate for harness evolution. HELIX decomposes agent systems into typed ports, reusable atoms, recipes, product shells, and runtime policies. It makes interventions explicit and auditable while retaining trajectories, test outcomes, and provenance. Harness evolution thus serves two linked roles: improving fixed-model execution and producing matched successes, regressions, near misses, and alternative solutions as data for subsequent model improvement. We evaluate HELIX in one evolution round on code repair. A 65-candidate portfolio discovers a fixed harness that improves task coverage by 4.0% over Pi, while the full portfolio exposes up to 58.0% more verified coverage through complementary sibling behavior. Selected candidates are assessed with repeated runs and the SWE-bench evaluator. A 200-slot sibling slice yields 438 verified SFT, critic, filter, and preference records. These results show how harness, model, and data form a feedback system: harness evolution expands current capability and creates learning signal for the next model; model updates motivate the next round of harness evolution. HELIX provides an auditable interface for studying this recursive process. Code is available at https://github.com/HKUDS/HELIX.

## Metadata
- **Published**: 2026-08-14T04:44:53Z
- **Authors**: Tianyu Fan, Chao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13951v1)