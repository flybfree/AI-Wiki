---
title: Constitutional Midtraining: Content Presence Drives Alignment Gains
published: 2026-07-29T09:15:40Z
authors: Desiree Cho, Cameron Tice, Bernie Hogan, Hunar Batra, Puria Radmard, Jun Zhao, Nigel Shadbolt
url: http://arxiv.org/abs/2607.26654v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constitutional Midtraining: Content Presence Drives Alignment Gains

## Abstract
Post-training alignment is often shallow, eroding under fine-tuning. Whether midtraining interventions, cleanly isolated from post-training, can produce durable alignment remains untested. We test this via constitutional midtraining: inserting principled, values-based content into midtraining against a replay-only control at 120B scale. Our 394M-token constitutional corpus, built from Anthropic's Constitution, uses a 2x2 factorial design (curriculum ordering x deliberative reasoning) to produce four constitutionally midtrained conditions plus a control, evaluated on self-generated and established benchmarks including alignment under pressure, value conflict resolution, blackmail, and emergent misalignment across three stages: post-midtraining, post-SFT, and post-benign fine-tuning. Constitutionally midtrained models outperform the control on alignment generalization and durability, notably on blackmail: SFT instills a blackmail propensity in all models, but constitutional midtraining blunts it, with the advantage surviving benign fine-tuning (-17.5pp). This durability does not extend to settings requiring active resistance to in-context pressure or conflict, where the advantage attenuates after SFT. The presence of constitutional content at midtraining also matters more than its structure, and constitutional midtraining incurs no cost, on average, on the capabilities we test (MMLU, ARC-Easy, piqa, GSM8K) at any stage. A modest amount of constitutional content at midtraining could therefore yield broad, persistent alignment gains, offering a cheap, complementary addition to SFT-centered pipelines. Code, data, and models are available.

## Metadata
- **Published**: 2026-07-29T09:15:40Z
- **Authors**: Desiree Cho, Cameron Tice, Bernie Hogan, Hunar Batra, Puria Radmard, Jun Zhao, Nigel Shadbolt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26654v1)