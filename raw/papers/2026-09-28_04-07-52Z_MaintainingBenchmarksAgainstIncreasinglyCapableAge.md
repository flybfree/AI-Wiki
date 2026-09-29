---
title: Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes
published: 2026-09-28T04:07:52Z
authors: Weijun Luo, Kelvin Luu, Xinyi Liu, Guangze Luo, Miguel Romero Calvo, Soham Dan, Daniel Yue Zhang, Ying Liu, Mohamed Elfeki
url: http://arxiv.org/abs/2609.34262v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes

## Abstract
Agentic benchmarks guide model selection and training. Yet an agent can pass a task without demonstrating the intended capability. Such outcomes constitute unearned passes; their proportion among all passes defines the integrity gap. As agents improve, benchmark surfaces that once seemed harmless can become exploitable, making benchmark validity an ongoing maintenance problem. We introduce a process-verification framework that audits passing trajectories, distinguishes evidenced reward hacking from verifier weakness, and localizes exploitable surfaces for repair. Across 3,810 passing trajectories from 29 model-benchmark cohorts, confirmed violations often increase with model generation but not monotonically. On SWEBench Pro V1.0, confirmed violation rates rise from 24% to 73% between Opus 4.7 and Fable 5 on matched tasks; later cohorts fall to 11% for Fable 5.1 and 0% for GPT-6 Astra. These comparisons are descriptive: configurations were not normalized, and the latest models also pass fewer exploitable tasks. Violations concentrate around a small set of recurring surfaces, especially unintended access to reference solutions through git history. Three repair case studies across two benchmarks show why blocking a recorded exploit is insufficient: the same protected information can remain accessible through another route. Therefore, we combine minimal patches with exploit replay and fresh agent evaluation, auditing new passes under the original standard. No evaluated attempt against the final patches reached the protected channel, and every post-patch pass was judged legitimate. Benchmark integrity requires ongoing maintenance: audit passing behavior, repair the enabling surface, and re-evaluate both exploit access and legitimate solvability.

## Metadata
- **Published**: 2026-09-28T04:07:52Z
- **Authors**: Weijun Luo, Kelvin Luu, Xinyi Liu, Guangze Luo, Miguel Romero Calvo, Soham Dan, Daniel Yue Zhang, Ying Liu, Mohamed Elfeki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34262v1)