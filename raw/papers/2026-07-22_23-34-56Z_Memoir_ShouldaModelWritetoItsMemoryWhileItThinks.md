---
title: Memoir: Should a Model Write to Its Memory While It Thinks?
published: 2026-07-22T23:34:56Z
authors: Jaber Jaber, Osama Jaber
url: http://arxiv.org/abs/2607.20792v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memoir: Should a Model Write to Its Memory While It Thinks?

## Abstract
Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective. We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. On procedural associative recall with key interference, we compare a coupled arm against an otherwise identical read-only pondering arm. Both arms contain 81,738 parameters, including 76,362 trainable parameters, and use matched declared forward multiply-accumulate counts, data, optimizer, schedule, and seeds. After 240 training steps across 12 seeds, coupled recall is 0.5203 with a 95 percent interval of [0.4522, 0.5883], while read-only recall is 0.6557 with [0.5953, 0.7160]. The arms are paired per seed, and the read-only lead of 0.1354 gives a paired t of 3.23 on 11 degrees of freedom with a 95 percent interval of [0.0431, 0.2277] on the difference, winning on 10 of 12 seeds. After 960 steps across 8 seeds, both arms reach 1.0000, so the measured effect is a learning-speed penalty at a fixed budget, not a demonstrated capability penalty. That longer control is ceiling limited, leaving convergence on a non-saturating task unmeasured. A predicted failure in which memory rewriting corrupts the energy signal did not occur: the energy margin grew and held. Kernel restructuring also reduced delta-rule forward time from 0.907 ms to 0.351 ms on the stated device. Code and evidence are available at https://github.com/RightNow-AI/Memoir

## Metadata
- **Published**: 2026-07-22T23:34:56Z
- **Authors**: Jaber Jaber, Osama Jaber
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20792v1)