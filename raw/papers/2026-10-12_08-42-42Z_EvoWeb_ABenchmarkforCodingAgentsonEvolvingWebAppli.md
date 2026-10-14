---
title: EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications
published: 2026-10-12T08:42:42Z
authors: David Nukrai, Bar Alon, Nativ Levy, Ido Andrew Atad, Ido Cohen, Itamar Zimerman, Lior Wolf, Eli David, Ilan Naiman
url: http://arxiv.org/abs/2610.16402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications

## Abstract
Web application development often proceeds through successive requests that extend an existing implementation. Yet web-generation benchmarks primarily evaluate development toward fixed specifications. We introduce EvoWeb, a novel benchmark comprising 320 cumulative requests over 32 web applications, grounded in real-world product features and structured by functional dependency graphs. Agents iteratively modify a persistent codebase, while a multimodal web agent tests each intermediate application in a live browser, assessing newly requested functionality, cross-request integration, and previously requested functionality. To characterize reliability throughout development, we integrate trajectory performance across user-tolerance thresholds rather than impose a fixed stopping criterion. Experiments across open- and closed-source frontier models show that EvoWeb reveals clear performance differences between models, with cross-request integration emerging as a key challenge. Further analysis shows that later requests with deeper or more numerous dependencies are solved less accurately, while runtime errors become more frequent over successive requests. EvoWeb provides a testbed for evaluating and improving coding agents in long-horizon, multi-request development.

## Metadata
- **Published**: 2026-10-12T08:42:42Z
- **Authors**: David Nukrai, Bar Alon, Nativ Levy, Ido Andrew Atad, Ido Cohen, Itamar Zimerman, Lior Wolf, Eli David, Ilan Naiman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16402v1)