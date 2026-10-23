---
title: Route-and-Generate: KL-Regularized Router Improvement for Reasoning Routing in LLMs
url: http://arxiv.org/abs/2610.30351v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_19-09-04Z_Route_and_Generate_KL_RegularizedRouterImprovement.md
generated_at: 2026-10-22 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Route-and-Generate (Rouge), a hierarchical training framework designed to help large language models adaptively determine when and how much reasoning effort to allocate for each input. The core finding is that by decoupling reasoning budget allocation from answer generation and training a neural router via a KL-regularized policy improvement step, LLMs can produce concise answers on simple problems while reserving extended reasoning for harder tasks, yielding improved accuracy-efficiency trade-offs across multiple reasoning benchmarks.

## Key Takeaways
- Rouge decouples reasoning effort allocation from answer generation by introducing a routing policy that distributes a fixed sampling budget across multiple reasoning formats, while the base model is optimized using Group Relative Policy Optimization (GRPO) with per-sample rewards. This separation allows the system to dynamically decide the depth of reasoning needed per input rather than applying a uniform reasoning strategy.
- The framework employs a rank-based reward mechanism that explicitly favors shorter correct solutions, combined with a closed-form KL-regularized policy improvement step that is distilled into a neural router. This dual mechanism ensures that the routing policy learns to prefer efficient reasoning paths without sacrificing correctness, effectively penalizing unnecessary verbosity in the reasoning chain.
- The hierarchical design addresses the dual failure modes of current LLMs: overthinking on simple tasks (wasting compute on trivial problems) and underthinking on harder ones (failing to engage sufficient reasoning depth). By training the router to match reasoning budget to problem difficulty, Rouge achieves measurable improvements in both accuracy and token efficiency across multiple reasoning benchmarks.

## Context
Current reasoning-augmented LLMs, including those trained with chain-of-thought prompting or reinforcement learning methods like GRPO, typically apply a fixed reasoning depth regardless of input difficulty. This one-size-fits-all approach wastes computational resources on easy queries and underperforms on complex ones. Rouge sits at the intersection of adaptive computation, policy optimization, and model distillation, offering a principled training framework that treats reasoning budget as a learnable routing decision rather than a static hyperparameter.

## Implications
For practitioners deploying LLMs at scale, Rouge offers a path toward significant inference cost reduction without accuracy loss, since the router learns to skip unnecessary reasoning steps on easy inputs. For the broader research community, the KL-regularized router distillation approach provides a reusable template for training adaptive control policies in any multi-stage generation pipeline, potentially extending beyond text reasoning to multimodal or agentic settings where compute allocation must be dynamically optimized.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30351v1)
