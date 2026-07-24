---
title: The Story Shapes the Agent: Narrative Priors in LLM Behavior
published: 2026-07-20T23:03:16Z
authors: Yixuan Wang, James Lester, Shashank Srivastava
url: http://arxiv.org/abs/2607.18566v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Story Shapes the Agent: Narrative Priors in LLM Behavior

## Abstract
Persona prompting is widely used to steer LLM agent behavior, yet the narrative framing of a task can matter more than the assigned persona. We isolate this effect through structural isomorphism, constructing three text-based investigation games that share the same action space, stage progression, and resource constraints while varying only task narrative: disease investigation, IT troubleshooting, and murder mystery. Across 1,890 sessions spanning 3 models and 10 personas, we identify narrative priors: systematic action tendencies activated by a task's story framing, independent of its decision structure. Narrative priors explain 5-31x more behavioral variance than persona, are consistent across model architectures, and in two of three domains are negatively associated with task success. Persona effects that do transfer across narratives arise from behavioral anchors, persona descriptions whose language maps directly onto shared actions. Causal interventions confirm this: removing anchor words from a high-transfer persona reduces cross-narrative consistency by 95%. Our framework also generalizes to a held-out fourth narrative and yields a persona-selection method that improves cross-narrative transfer. These results suggest that LLM behavior that survives narrative changes should be grounded in concrete actions rather than abstract descriptions.

## Metadata
- **Published**: 2026-07-20T23:03:16Z
- **Authors**: Yixuan Wang, James Lester, Shashank Srivastava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18566v1)