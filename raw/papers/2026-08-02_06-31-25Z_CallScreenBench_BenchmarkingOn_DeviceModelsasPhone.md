---
title: CallScreenBench: Benchmarking On-Device Models as Phone Secretaries
published: 2026-08-02T06:31:25Z
authors: Simiao Ren
url: http://arxiv.org/abs/2608.01033v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CallScreenBench: Benchmarking On-Device Models as Phone Secretaries

## Abstract
Language models small enough to run on a handset, quantized to a few bits, are increasingly capable of acting for their user, making on-device task automation newly plausible. One such task is answering the phone. A phone secretary takes an unknown inbound call on its owner's behalf. Unlike the agents evaluated by most benchmarks, it has no task to complete and no cooperative user: the caller holds the goal, may be an adversary, and must be judged from the opening turn with no oracle. What matters is not task success, but whether the owner would endorse how their proxy handled the call.   We present CallScreenBench, which scores this setting on five quality dimensions. Each dimension is printed beside the counter-metric that bills it and is never averaged into a single number. We also report a guardedness profile for a toolless proxy that holds no credentials and calls no tools. Across six on-device models (0.6-4B parameters, 4-bit quantization), quality scales with capability, but triage does not. The appearance that it does is an artifact of measurement. Scripted degenerate agents supply the missing floors: after correcting for them, the number of model pairs whose triage performance separates falls from 11 of 15 to zero at the preregistered operating point. An agent that simply hangs up and echoes the caller also scores perfect message fidelity. We report which of our own metrics these floors defeat and declare no pass/fail threshold.

## Metadata
- **Published**: 2026-08-02T06:31:25Z
- **Authors**: Simiao Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01033v1)