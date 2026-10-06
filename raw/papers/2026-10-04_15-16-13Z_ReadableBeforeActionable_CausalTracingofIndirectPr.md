---
title: Readable Before Actionable: Causal Tracing of Indirect Prompt Injection
published: 2026-10-04T15:16:13Z
authors: Zhe Yu, Wenpeng Xing, Xingxing Yang, Meng Han
url: http://arxiv.org/abs/2610.05295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Readable Before Actionable: Causal Tracing of Indirect Prompt Injection

## Abstract
Indirect prompt injection causes LLM agents to follow commands embedded in external data. A probe may distinguish instructions from data without identifying a state edit that changes the next action. We study this gap through counterfactual role probes, component-wise activation patching, and separate interventions on AgentDojo trajectories. Role decoding survives changes in content and format. In controlled Qwen tests, it precedes strong tool-choice effects from patches along an independently estimated role direction. On AgentDojo, directions estimated from hijacked and resisted training trajectories reduce attack success at pre-action and injected-span positions, but have little effect at random positions. In longer Qwen trajectories, single-position edits become less effective at later layers; span-wide and repeated edits reduce attack success on the same evaluation set. Removing the learned channel subspace preserves role decoding, yet effective intervention directions transfer poorly across the tested channels. These findings distinguish a readable role signal from an effective behavioral intervention: depth matters in controlled tool choice, while position and context also matter in attack trajectories.

## Metadata
- **Published**: 2026-10-04T15:16:13Z
- **Authors**: Zhe Yu, Wenpeng Xing, Xingxing Yang, Meng Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05295v1)