---
title: Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models
published: 2026-10-02T07:02:13Z
authors: Taiheng Pan
url: http://arxiv.org/abs/2610.02911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models

## Abstract
Methods for training language models on stale samples are judged by comparisons against importance-corrected baselines. We show that details of the experimental harness can reverse the observed ranking of methods, and we introduce PTH (Probe The Harness), a set of checks that makes the harness visible. Our case is a comparison between SAN, a behaviour-free method, and truncated importance sampling (TIS) on verl and in a single-GPU trainer, in which SAN first finished ahead in both stacks. Four details of the harness changed this comparison: the PPO ratio was taken against the learner's own recomputed probabilities, the data seed did not reach the TIS arm, the replay queue reused its first batch for 33 updates, and two loss normalisers differed from their description. In each case the logged quantity looked consistent with a working setup, while the quantity that defines the comparison went unchecked. With the harness checked, TIS matches SAN on verl, and in the trainer TIS learns steadily while SAN keeps a margin. We contribute the signature of each detail and its effect on the comparison, reference results for TIS and uncorrected GRPO under sampler lag, and the PTH checklist.

## Metadata
- **Published**: 2026-10-02T07:02:13Z
- **Authors**: Taiheng Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02911v1)