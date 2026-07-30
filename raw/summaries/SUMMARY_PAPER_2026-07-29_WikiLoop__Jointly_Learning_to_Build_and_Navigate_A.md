---
title: WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback
url: http://arxiv.org/abs/2607.26604v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_08-28-30Z_WikiLoop_JointlyLearningtoBuildandNavigateAgent_Na.md
generated_at: 2026-07-29 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WikiLoop, a feedback‑coupled framework that jointly learns to construct and navigate an agent‑native wiki knowledge base. The system uses a shared policy with role‑conditioned components: a Navigator retrieves evidence for queries while a Builder proposes edits evaluated by downstream navigation performance. Training alternates between role‑specific optimization and a final joint stage, achieving 62.6 aggregate answer correctness on AuthTrace—6.3 points higher than prior baselines.

## Key Takeaways
- WikiLoop integrates construction and querying into a single persistent wiki, enabling the Builder to propose edits that are judged by how they improve downstream navigation.
- The Navigator’s objective penalizes retrieval cost only after full evidence is gathered, ensuring sufficiency before efficiency.
- Learned edits remain useful on a held‑out Navigator, demonstrating that the joint training does not degrade specialization.

## Context
The work addresses a longstanding divide in AI knowledge systems where retrieval and generation are trained separately. By coupling these tasks with real downstream feedback, WikiLoop aligns model behavior with actual user needs, moving beyond static index updates to dynamic, usable knowledge bases.

## Implications
For practitioners, WikiLoop offers a template for building self‑improving AI assistants that continuously refine their internal data without external retraining. In industry, this could reduce the cost of maintaining large factual resources and improve answer quality across diverse query types.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26604v1)
