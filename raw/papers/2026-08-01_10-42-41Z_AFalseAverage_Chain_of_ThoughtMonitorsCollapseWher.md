---
title: A False Average: Chain-of-Thought Monitors Collapse Where They Are the Only Defense
published: 2026-08-01T10:42:41Z
authors: Shikhar Shiromani, Leo Richter
url: http://arxiv.org/abs/2608.00583v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A False Average: Chain-of-Thought Monitors Collapse Where They Are the Only Defense

## Abstract
Chain-of-thought (CoT) monitoring is meant to catch the reward hacks that look clean in the actions and betray themselves only in the reasoning. We show that this is exactly where an adversary who controls the reasoning can defeat it. Rewriting only an agent's reasoning to read as good-faith engineering, while copying every command and output verbatim so the exploit is unchanged, drops a held-out monitor's catch rate on that subset from about 95% to under 11% in one gradient-free shot. A monitor's aggregate accuracy is a false average: dominated by hacks the actions give away, it hides the near-total collapse this rewrite produces on the subset where CoT monitoring is the only signal. The attack transfers across monitor families and agent models, reproduces with live agents, though against a calibrated monitor evasion concentrates in the strongest agent. Trace-only defenses recover it only partially, even one primed on the attack, because the rewrite stays truthful about what happened and lies only about intent; only information from outside the trace helps substantially. A probe on an open-weight surrogate monitor's activations separates the hacks its verdict misses, but a causal control shows this is a detector, not evidence the monitor secretly knows.

## Metadata
- **Published**: 2026-08-01T10:42:41Z
- **Authors**: Shikhar Shiromani, Leo Richter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00583v1)