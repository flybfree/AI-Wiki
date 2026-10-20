---
title: CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?
url: http://arxiv.org/abs/2610.25078v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-18_07-38-03Z_CoEvo_RSI_WhenHarnessesEvolve_WhichModelsShouldFol.md
generated_at: 2026-10-19 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoEvo-RSI addresses the persistent "brain–body mismatch" problem in recursive self-improving (RSI) agent systems, where an evolving execution harness demands behaviors its underlying model has not learned or restricts capabilities the model already possesses. The paper introduces a framework built on agent-driven, bidirectional historical inheritance through a shared evolutionary archive, enabling a meta-agent to coordinate harness evolution with model checkpoint selection, merging, and adaptation. Using only supervised fine-tuning on self-generated rejection-sampled trajectories, the approach makes a 9B-parameter model competitive with substantially larger models across diverse vertical applications.

## Key Takeaways
- The brain–body mismatch problem is identified as a critical but overlooked failure mode in model–harness co-evolution paradigms: as the execution scaffold (harness) evolves, it can impose behavioral demands the model (brain) has never been trained to satisfy, or conversely, it can constrain capabilities the model already possesses, creating a persistent misalignment that degrades agent performance over successive improvement cycles.
- CoEvo-RSI introduces a meta-agent that draws on a shared evolutionary archive of historical harness designs and execution feedback to coordinate two directions of inheritance: forward inheritance selects or merges model checkpoints whose capabilities align with the evolving harness, while backward inheritance adapts the model under the selected harness through supervised fine-tuning on rejection-sampled trajectories, ensuring that inherited capabilities match current execution requirements.
- Empirically, CoEvo-RSI applied to Qwen3.5-9B surpasses DeepSeek-V4-Pro by +14.16 agent accuracy on TraceElephant (multi-agent failure attribution) and GLM-5.3 by +4.90 success rate on HomeBench VM (smart-home instruction following), demonstrating that proper brain–body alignment through bidirectional inheritance can close or even reverse the performance gap between small and large models without requiring additional pretraining or reinforcement learning.

## Context
Recursive self-improving agents have become a prominent research direction in AI, with model–harness co-evolution representing one of the most active sub-paradigms where agents iteratively refine both their execution scaffolds and their intrinsic model weights. However, most existing co-evolution pipelines treat the harness and model as loosely coupled components, leading to systematic misalignment as either component evolves independently. This paper fills a critical gap by formalizing the brain–body mismatch as a distinct research problem and proposing a principled coordination mechanism, positioning itself at the intersection of evolutionary computation, meta-learning, and agentic AI systems.

## Implications
For practitioners building agentic systems in production—such as multi-agent orchestration, text-to-SQL pipelines, or smart-home automation—CoEvo-RSI demonstrates that careful alignment between model capabilities and execution harnesses can yield performance gains comparable to scaling model size, offering a cost-effective path for deploying smaller, locally hosted models in specialized verticals. For the broader AI research community, the framework challenges the assumption that model scale is the primary lever for agent capability, suggesting instead that bidirectional historical inheritance and meta-agent coordination represent a complementary and potentially more sustainable route toward recursive self-improvement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25078v1)
