---
title: AutoRedClaw: Automated Red-Teaming for Claw-Style Agents
url: http://arxiv.org/abs/2610.27244v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_20-15-39Z_AutoRedClaw_AutomatedRed_TeamingforClaw_StyleAgent.md
generated_at: 2026-10-20 21:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AutoRedClaw is an automated red-teaming framework designed to evaluate the security of persistent, personalized "claw-style" agent systems (such as OpenClaw) that maintain long-term memory, configuration files, and reusable skills across sessions. The paper introduces a pipeline that automatically generates both adversarial attacks and the execution environments needed to run them, achieving an effective attack rate above 30% at under $0.10 per successful sample, and produces RedClaw-Bench, a 330-case benchmark that yields substantially higher attack success rates than prior benchmarks like AgentDojo, AgentDyn, and DTap.

## Key Takeaways
- Claw-style agents introduce a fundamentally new security threat model: because persistent state (AGENTS.md configs, long-term memory, reusable skills) is repeatedly reloaded into context, a single poisoned artifact can propagate across tasks and sessions, making traditional per-task security evaluations inadequate. AutoRedClaw addresses this by generating end-to-end attacks that operate across the full lifecycle of these persistent systems.
- The framework combines a strict quality-checking protocol with execution-based validation to guarantee correctness, realism, and effectiveness of generated attack samples, while using task-driven environment construction to keep generation costs low. Generation is organized along risk categories, attack strategies, attack stages, and attack surfaces, with experience-guided exploration steering the pipeline toward under-explored regions to maximize coverage.
- RedClaw-Bench, constructed from AutoRedClaw outputs, demonstrates that most agent systems across seven harnesses and four frontier models exceed 50% attack success rates, confirming that the red-teaming pipeline provides a strong evaluation signal even for the most advanced agent systems and substantially outperforms existing benchmarks in ASR.

## Context
As AI agent architectures evolve from narrow, task-scoped tool-use systems toward persistent personal assistants with long-term memory and configurable skill libraries, the attack surface expands dramatically. Existing red-teaming and safety evaluation frameworks were designed for single-turn or single-task interactions and rely on manually curated test cases that quickly become outdated as agent capabilities advance. AutoRedClaw fills a critical gap by providing a scalable, automated evaluation methodology tailored to the persistent-state threat model that defines next-generation agent deployments.

## Implications
For practitioners deploying claw-style agents in production, AutoRedClaw offers a practical, low-cost pathway to continuously stress-test agent security as systems evolve, reducing reliance on brittle manual test suites. For the broader AI safety community, the demonstration that frontier models exceed 50% ASR on RedClaw-Bench signals that current agent safety mitigations remain insufficient for persistent-state architectures, underscoring the urgency of automated, environment-aware red-teaming as a standard component of agent deployment pipelines. The open-source release of code and benchmark at the SaFo-Lab GitHub repository enables reproducible evaluation and community-driven extension of the threat taxonomy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27244v1)
