---
title: MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling
url: http://arxiv.org/abs/2610.21492v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_08-29-01Z_MetaExp_LearningtoSelf_ImprovethroughExperiencevia.md
generated_at: 2026-10-15 21:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MetaExp introduces a scalable training framework that teaches language-model agents to develop a transferable "experience learning" capability by training on verifiable task families with controlled cross-task structure. Rather than optimizing external experience scaffolds or training on isolated task distributions, MetaExp trains models to extract reusable operational and procedural knowledge that persists across episodes, demonstrating that experience learning can become a genuine model capability. Fine-tuning Qwen3.5-122B-A10B on 4,956 trajectories from 1,000 task families yields significant improvements on downstream benchmarks, with gains persisting even under domain-excluded training, confirming the transferability of the learned capability.

## Key Takeaways
- MetaExp constructs two complementary task-family designs: Shared-Tool families keep black-box tools fixed across tasks to elicit operational experience (learning how to use tools effectively), while Shared-Workflow families preserve latent procedures across changing task realizations to elicit procedural experience (learning reusable workflows). Each family maintains a reusable factor while varying task-specific realizations, enabling knowledge transfer without direct solution reuse.
- The framework scales environments under both designs, collects and filters sequential interaction trajectories, and fine-tunes Qwen3.5-122B-A10B on 4,956 trajectories drawn from 1,000 task families. This approach moves beyond in-episode problem solving by providing supervision that reveals what knowledge remains useful across episodes, addressing a fundamental gap in how agents accumulate and reuse interaction feedback.
- With model parameters frozen during downstream evolution, MetaExp achieves +8.5 points on SpreadsheetBench, peaks at +2.3 on APEX-Agents, and improves by +14.8 on AutomationBench. Critically, these gains persist under domain-excluded training, providing strong evidence that experience learning functions as a transferable capability enabling continued non-parametric improvement after deployment without further parameter updates.

## Context
Current approaches to improving language-model agents either optimize external experience scaffolds (such as memory systems or retrieval pipelines) or train experience-related behavior on specific task distributions, leaving open whether experience learning itself can become a transferable model capability. MetaExp addresses this gap by providing supervision beyond isolated tasks, training models to extract cross-episode knowledge through verifiable task families with controlled structure. This work sits at the intersection of agent learning, meta-learning, and scalable environment design, offering a principled path toward agents that genuinely learn from their interactions rather than merely storing them.

## Implications
For practitioners building autonomous agents, MetaExp demonstrates that experience learning can be trained as a transferable capability rather than being bolted on through external scaffolding, enabling continued non-parametric improvement after deployment without retraining model weights. For the broader AI research community, the verifiable cross-task environment scaling methodology provides a reproducible blueprint for training and evaluating experience-transfer capabilities, potentially accelerating progress toward agents that self-improve through accumulated operational and procedural knowledge across diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21492v1)
