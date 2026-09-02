---
title: Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO
published: 2026-09-01T08:49:01Z
authors: Prakhar Gupta, Vaibhav Gupta
url: http://arxiv.org/abs/2609.00925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO

## Abstract
Language models can ignore prompt evidence when it conflicts with memorized knowledge. Post-training can make models follow such evidence more reliably, but it is unclear whether these gains require new machinery or strengthen machinery already present. We compare nine post-training arms spanning GRPO, SFT, and DPO from one starting checkpoint, with key comparisons extended across scales and families. We estimate a grounding direction from that checkpoint before training. Across five tested GRPO variants, grounding gains are small. For the two variants replicated across seeds, equivalence tests bound their effects below the conflict-SFT gain even as the rewarded metric improves. Conflict-SFT improves grounding moderately, while DPO drives grounding near ceiling on its matched distribution. Conflict-SFT and DPO largely use the same causal attention-head set as the starting model. Subtracting the starting-model direction suppresses both gains, while adding it to the starting model recovers 35% of DPO's gain at a dose passing all stated side-effect checks. After a supervised warm start makes the context answer appear in more rollouts, the same GRPO recipe adds essentially no further grounding gain. In our setting, grounding gains largely depend on machinery already present in the starting model.

## Metadata
- **Published**: 2026-09-01T08:49:01Z
- **Authors**: Prakhar Gupta, Vaibhav Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00925v1)