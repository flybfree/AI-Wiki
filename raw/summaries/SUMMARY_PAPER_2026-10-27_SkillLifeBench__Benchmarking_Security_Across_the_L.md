---
title: SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills
url: http://arxiv.org/abs/2610.35215v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_11-07-04Z_SkillLifeBench_BenchmarkingSecurityAcrosstheLifecy.md
generated_at: 2026-10-27 00:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillLifeBench introduces a benchmark that evaluates the security of web agents across the full lifecycle of reusable agent skills, covering implementation, interface, runtime, composition, and version changes across 388 paired scenarios. The benchmark reveals that models performing similarly on static runtime tasks diverge dramatically when agents are allowed to autonomously inspect, select, and reconfigure skills, and that providing execution provenance significantly improves an agent's ability to recover from adversarial skill manipulations.

## Key Takeaways
- The benchmark exposes a critical gap between runtime evaluation and lifecycle evaluation: GPT-5.6-Sol and Sonnet 4.6 both score 82.0% on 89 runtime tasks, yet their lifecycle task success rates diverge to 96.7% and 56.7% respectively, demonstrating that static benchmarks fail to capture security vulnerabilities that emerge when agents autonomously manage skill selection and reconfiguration across 60 lifecycle tasks spanning 12 adversarial templates.
- Joint success—completing a user task while simultaneously avoiding a registered attack goal—drops to 65.2% across lifecycle evaluations, with 103 runs completing both the task and the attack goal, indicating that adversarial skill manipulation frequently compromises agent security even when the primary task appears to succeed.
- Execution provenance is a powerful mitigation: a matched recovery study shows that adding execution logs and metadata raises utility joint success from 49.35% to 65.58%, while a deterministic execution-consistency rule achieves 64.94% with higher benign utility and full restoration reaches 69.48%, suggesting that transparency in execution history is essential for robust agent security.

## Context
As web agents increasingly rely on modular, reusable skill libraries that are versioned, composed, and updated over time, the security surface expands far beyond what single-task benchmarks capture. SkillLifeBench addresses a growing concern in the AI agent community: the assumption that a skill safe in isolation remains safe when selected, loaded, or reconfigured by an autonomous agent across multiple tasks and updates. By linking stored code states, version selections, and loaded implementations to verifiable task outcomes, the benchmark fills a gap left by existing agent evaluations that test static code execution rather than dynamic lifecycle behavior.

## Implications
For practitioners deploying agent systems in production, these findings argue that runtime-only security testing is insufficient; organizations must evaluate agents under lifecycle conditions where skills are autonomously selected and reconfigured, and must instrument execution provenance to enable recovery from adversarial skill states. For the broader AI safety field, the divergence between runtime and lifecycle scores across 14 evaluated models signals that current benchmarking practices systematically underestimate the attack surface introduced by skill management, and that deterministic consistency rules and provenance-aware recovery mechanisms should be integrated into agent frameworks before deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35215v1)
