---
title: MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling
published: 2026-10-15T08:29:01Z
authors: Renhao Li, Xinjie Shen, Yang Su, Jianhong Tu, Derek F. Wong, Dayiheng Liu, Min Yang
url: http://arxiv.org/abs/2610.21492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling

## Abstract
Language-model agents can accumulate interaction feedback, but reliably turning that feedback into reusable experience remains challenging. Existing methods either optimize external experience scaffolds or train experience-related behavior on specific task distributions, leaving open whether experience learning itself can become a transferable model capability. Training such a capability calls for supervision beyond isolated tasks, which mainly support in-episode problem solving rather than revealing what knowledge remains useful across episodes. In this work, we introduce MetaExp, a scalable framework that trains this capability through verifiable task families with controlled cross-task structure. Each family preserves a reusable factor while varying task-specific realizations, enabling transfer without direct solution reuse. We propose two complementary designs: Shared-Tool families keep black-box tools fixed across tasks to elicit operational experience, while Shared-Workflow families preserve latent procedures across changing realizations to elicit procedural experience. We scale environments under both designs, collect and filter sequential interaction trajectories, and fine-tune Qwen3.5-122B-A10B on 4,956 trajectories from 1,000 task families. With parameters frozen during downstream evolution, MetaExp improves by +8.5 points on SpreadsheetBench, peaks at +2.3 on APEX-Agents, and improves by +14.8 on AutomationBench. The gains persist under domain-excluded training, supporting experience learning as a transferable capability for continued non-parametric improvement after deployment.

## Metadata
- **Published**: 2026-10-15T08:29:01Z
- **Authors**: Renhao Li, Xinjie Shen, Yang Su, Jianhong Tu, Derek F. Wong, Dayiheng Liu, Min Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21492v1)