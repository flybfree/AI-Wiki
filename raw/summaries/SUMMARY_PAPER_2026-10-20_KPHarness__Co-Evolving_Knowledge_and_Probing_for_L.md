---
title: KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses
url: http://arxiv.org/abs/2610.27417v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_00-12-14Z_KPHarness_Co_EvolvingKnowledgeandProbingforLong_Ho.md
generated_at: 2026-10-20 22:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
KPHarness introduces a framework for adapting the external execution harness of a frozen vision-language-action (VLA) model through a co-evolutionary process between recovery knowledge and active probing. Rather than simply proposing new recovery rules when a gaming agent fails, the system gathers diagnostic evidence to determine which interventions apply and how to investigate failures, enabling the harness to improve both its intervention strategies and its failure-investigation methods. Experiments on Minecraft tasks spanning mining, combat, and crafting demonstrate improved task coverage over bare policy execution, manually specified fixed harnesses, and knowledge-only harness evolution with non-adaptive probing, with generalization to previously unseen tasks.

## Key Takeaways
- KPHarness separates fast policy execution from a slow research loop, where accumulated knowledge and probing evidence are translated into bounded harness revisions. Each revision is compared against the incumbent harness under matched sandbox conditions and accepted only when paired evaluation demonstrates improvement, ensuring that changes are empirically validated rather than speculative.
- The knowledge-probing co-evolution mechanism is reciprocal: recovery knowledge supplies context-specific intervention hypotheses that guide active probing, while probe outcomes reveal when those hypotheses apply and provide evidence for refining both the recovery knowledge and future probe selection. This dual improvement means the harness learns not only which interventions to apply but also how to investigate failures more effectively.
- The system retains recoveries supported by further validation for cross-task reuse, while immediate interaction feedback and delayed episode-success credit jointly update action-probing and knowledge-probing policies during adaptation. Evaluation on previously unseen tasks confirms that the evolved harness, knowledge bank, and probing policies transfer effectively when held fixed, demonstrating generalization beyond the training tasks.

## Context
This work sits at the intersection of embodied AI, long-horizon task planning, and self-improving agent systems. As vision-language-action models are increasingly deployed in complex interactive environments like games, robotics, and simulation-based training, a critical bottleneck is that the policy itself is often frozen due to cost or deployment constraints, yet the surrounding execution scaffolding must adapt to novel failure modes. KPHarness addresses this by treating the harness as a learnable research system rather than a static configuration, contributing to the broader effort of making frozen foundation models more robust through external adaptation mechanisms.

## Implications
For practitioners deploying VLA-based agents in production gaming, simulation, or robotics pipelines, KPHarness offers a principled recipe for harness self-improvement without retraining the underlying policy, reducing engineering overhead while maintaining safety through sandboxed evaluation gates. For the research community, the knowledge-probing co-evolution paradigm suggests that diagnostic evidence gathering is as important as intervention design, pointing toward future agent architectures where failure investigation is itself a learned skill. Industry teams building long-horizon autonomous agents could adopt the bounded-revision and paired-evaluation discipline to prevent harness drift and ensure that adaptations generalize across task families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27417v1)
