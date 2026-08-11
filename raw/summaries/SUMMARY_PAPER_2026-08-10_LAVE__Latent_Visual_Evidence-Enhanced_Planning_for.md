---
title: LAVE: Latent Visual Evidence-Enhanced Planning for Video Tool-use Agents
url: http://arxiv.org/abs/2608.07585v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-05_10-25-47Z_LAVE_LatentVisualEvidence_EnhancedPlanningforVideo.md
generated_at: 2026-08-10 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LAVE, a training-free framework that reuses latent visual evidence in video tool-use agents. It improves performance on benchmark tasks by integrating stored visual updates with textual observations during planning.

## Key Takeaways
- The visible channel keeps the original text while the latent channel stores pre-verbal visual updates, enabling reuse without retraining.
- Planning retrieves evidence relevant to the current state that is not covered by text, using timestamp-aligned updates and entropy-constrained routing.
- Experiments show a 3.76 point boost on Video-MME over the best baseline within the same frame budget.

## Context
Long video understanding demands efficient reuse of sparse visual evidence across long streams; prior agents rely solely on text, discarding silent computed updates, which limits planning flexibility.

## Implications
This approach reduces the need for retraining or extra data, offering scalable tool-use agents that can operate with existing visual pipelines. Practitioners can integrate LAVE to improve video reasoning without modifying orchestration logic.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07585v1)
