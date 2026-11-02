---
title: How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0
url: http://arxiv.org/abs/2610.38617v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_10-38-43Z_HowDeterministicSASTandAISecurityAgentsDividetheWo.md
generated_at: 2026-11-01 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

This paper introduces VulnBench 2.0, a benchmark of 108 hand-curated, attacker-reachable vulnerabilities across 20 open-source web applications in Go, JavaScript/TypeScript, Python, and Java, and uses it to evaluate nine productized security configurations spanning deterministic SAST (Snyk Code) and AI coding agents (Claude Code, Codex Security, DeepSec). The central finding is that neither deterministic SAST nor AI agents are sufficient alone: Snyk Code achieved 82.4% macro recall while Claude Code with Opus 5 at xhigh effort reached 79.3%, and only their combined coverage reached 101 of 108 vulnerabilities, which also represents the ceiling across all seven comparable configurations.

## Key Takeaways

- The benchmark enforces a strict two-line precision requirement for both the attacker-controlled source and the dangerous sink of each vulnerability, and 62 of the 108 findings span more than one file, making cross-file data-flow reasoning a core challenge. Snyk Code found 89 of 108 vulnerabilities while Claude Code with Opus 5 found 85; the 28-vulnerability disagreement (16 unique to Snyk, 12 unique to Claude) is too small to statistically distinguish the two engines, yet their union reaches 101 of 108, demonstrating that complementary detection is necessary rather than optional.

- The AI harness and its built-in review policy materially shape what a model can find. Without Claude Code's built-in review policy, the same underlying model matched only 16 instead of 9 of the 20 vulnerabilities in policy-excluded or policy-restricted classes, showing that harness configuration can suppress or amplify detection independent of model capability. Similarly, Codex Security with GPT-5.6 Sol located 80 vulnerabilities at file level but only 34 at line level, and DeepSec's model-free file selection strategy restricted its reach to only 56 of the 108 cross-file flows, underscoring that architectural choices in the harness constrain coverage as much as model quality.

- AI configurations reported at least seven real vulnerabilities absent from the curated reference set and not detected by Snyk Code, indicating that the benchmark itself has blind spots and that AI agents can surface findings beyond a fixed ground-truth set. Coverage and cost were only loosely correlated, and all harnesses, fixtures, reference sets, and run data are publicly released to enable reproducible comparison.

## Context

This work sits at the intersection of static analysis research and the rapidly growing deployment of AI coding agents in software security workflows. As organizations increasingly adopt tools like Claude Code, Codex, and DeepSec alongside traditional SAST platforms, practitioners lack rigorous, apples-to-apples benchmarks that account for cross-file data-flow reasoning, multi-language coverage, and the influence of agent harness policies on detection. VulnBench 2.0 fills this gap by providing a blind, reproducible evaluation protocol with strict source-and-sink localization criteria, moving the field beyond single-tool accuracy claims toward understanding complementary strengths and systematic failure modes.

## Implications

For security engineering teams, the findings argue against a single-tool strategy: deterministic SAST and AI agents detect meaningfully different vulnerability subsets, and a combined pipeline is required to approach the practical detection ceiling. For AI agent developers and security product vendors, the results highlight that harness design—review policies, file-selection heuristics, and effort settings—can constrain or expand detection far more than incremental model upgrades, making harness transparency and configurability critical design concerns. For the benchmarking community, the discovery that AI agents surfaced real vulnerabilities missing from a hand-curated reference set calls for iterative, adversarial benchmark maintenance rather than static ground-truth sets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.38617v1)
