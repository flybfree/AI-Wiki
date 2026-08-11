---
title: "AI Benchmarks"
date: 2026-06-10
type: concept
tags: [ai-benchmarks, evaluation]
---

## Summary

AI benchmarks are measurement instruments, not universal model scores. A useful benchmark specifies the capability being measured, the task and data boundary, the scoring rubric, the evaluation budget, and the failure modes that count. The papers in this wiki show a shift away from one-number leaderboards toward evaluations that are protocol-controlled, adversarial, user-centered, and closer to real workflows.

The strongest recurring lesson is that benchmark results are conditional. Rankings can change when retrieval budget, ingestion protocol, judge choice, user intervention, threat model, or test-time interaction is changed. Benchmark reports should therefore preserve the complete protocol alongside the headline score.

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson6_Evaluation.md|Lesson 6 — Evaluation & Verification: The Judge Node]] — shared tags: evaluation, 5 topic terms overlap, same area: home
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation and Benchmarks Hub]] — 1 title term overlap, shared tags: evaluation, 1 topic term overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-15-evaluation-overfitting-and-limits.md|AI/ML Foundations Lesson 15 - Evaluation, Overfitting, and Limits]] — shared tags: evaluation, 5 topic terms overlap, same area: home

## What the wiki currently covers

### 1. Protocol and leaderboard validity

- [[entities/paper/2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientif_summary.md|Beyond Memory Leaderboards]] introduces PAIM and PTr for scientific-memory retrieval. It evaluates 81 papers/66 questions and 252 papers/98 questions, and shows that rankings change with ingestion granularity, raw-text preservation, retrieval budget, modality, and judge choice.
- The practical implication is to report **score + protocol + budget**, not score alone. A leaderboard without those controls is difficult to interpret or reproduce.

### 2. Psychometric and cost-aware evaluation

- [[concepts/papers/2026-08-05_17-25-27Z_ItemResponseTheoryforAISafety_summary.md|Item Response Theory for AI Safety]] applies IRT to eight safety benchmarks and 192 language models. It identifies latent dimensions such as refusal strictness, truthfulness, and contextual harm.
- The paper reports that adaptive item selection can recover benchmark scores with far fewer items than random sampling, reducing evaluation cost while also supporting audits for sandbagging and model/API changes.

### 3. Agent safety and adversarial robustness

- [[concepts/papers/2026-07-22_13-24-09Z_OpenSkillRisk_BenchmarkingAgentSafetyWhenUs_summary.md|OpenSkillRisk]] evaluates agents against 263 risky third-party skills in sandboxed environments. Its key contribution is measuring context-sensitive execution risk rather than only text refusal.
- [[concepts/papers/2026-07-22_22-20-02Z_IssueTrojanBench_BenchmarkingAICodingAgents_summary.md|IssueTrojanBench]] tests coding agents against malicious issue requests delivered through multiple vectors, exposing the gap between model-level rejection and end-to-end agent protection.
- [[concepts/papers/2026-08-03_04-15-40Z_WhenMemoryBecomesAuthority_BenchmarkingAuth_summary.md|AuthMem-Bench]] evaluates whether memory consolidation preserves source authority. This makes authorization errors a measurable benchmark outcome rather than an anecdotal failure mode.
- [[concepts/papers/2026-08-07_09-03-49Z_HarnessSafe_EvaluatingSafetyAcrossPersisten_summary.md|HarnessSafe]] evaluates attack propagation through persistent carriers such as memory, skills, tools, and shared artifacts.

### 4. Coding-agent and harness evaluation

- [[concepts/papers/2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsers_summary.md|SWE-Touch]] adds user edits during coding tasks. It shows that strong isolated SWE-bench performance does not guarantee workspace awareness or successful conflict resolution.
- [[concepts/papers/2026-08-06_17-21-05Z_HarnessOpt_Bench_EvaluatingLLMsatHarnessOpt_20260806_2225_summary.md|HarnessOpt-Bench]] treats harness optimization as a capability in its own right, separating model ability from the prompts, tools, and control code surrounding the model.
- [[concepts/papers/2026-07-29_09-25-55Z_ScientificKnowledgeDiscoveryintheAgeofLarge_summary.md|Scientific Knowledge Discovery in the Age of Large Language Models]] finds that many retrieval and screening studies rely on internal validation, reinforcing the need for public, standardized evaluation protocols.

### 5. User-centered and social evaluation

- [[concepts/papers/2026-08-02_06-31-25Z_CallScreenBench_BenchmarkingOn_DeviceModels_summary.md|CallScreenBench]] evaluates on-device phone-secretary models using message fidelity, tone, brevity, privacy, and user endorsement—not just task completion.
- [[concepts/papers/2026-08-10_05-12-56Z_SocialGymandSPaRTan_BenchmarkingandImprovin_20260810_2344_summary.md|Social Gym and SPaRTan]] uses 21 rule-defined social games and Elo tournaments to make multi-agent social reasoning more objective and comparable across roles.
- [[concepts/papers/2026-07-29_17-56-49Z_APEX_Accounting_summary.md|APEX-Accounting]] evaluates frontier models on expert-authored accounting workflows involving spreadsheets, PDFs, and simulated accounting systems. It illustrates the move from short-answer tests to professional, multi-step work.

### 6. Domain and capability-specific benchmarks

- [[concepts/papers/2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_Induced_summary.md|QuantiBias]] measures bias that can remain hidden when compressed models pass conventional safety tests.
- [[concepts/papers/2026-07-29_17-56-49Z_APEX_Accounting_summary.md|APEX-Accounting]] covers financial operations and rubric-based workflow completion.
- [[concepts/papers/2026-07-23_09-55-45Z_RelativeValueLearning_summary.md|Relative Value Learning]] uses 49 Atari games as an empirical testbed for a new RL value estimator; this is a reminder that benchmark use should distinguish algorithm validation from general capability claims.

## Benchmark design principles

1. **Define the construct.** State whether the benchmark measures knowledge, reasoning, safety, retrieval, collaboration, social judgment, or workflow execution.
2. **Specify the protocol.** Record data contamination controls, ingestion granularity, retrieval and token budgets, tool access, model version, temperature, judge, and number of runs.
3. **Test the failure surface.** Add adversarial, long-horizon, user-interruption, authorization, and distribution-shift cases where the deployment risk requires them.
4. **Prefer interpretable metrics.** Report component metrics and failure categories alongside aggregate scores; use calibrated human or multi-judge evaluation when automated scoring is brittle.
5. **Separate capability from scaffolding.** For agents, measure the model, harness, tools, memory, and environment separately enough to identify what caused the result.
6. **Avoid false precision.** A score is conditional evidence, not a universal ranking. Report uncertainty, variance, and sensitivity to the evaluation setup.

## Recurring limitations

- Static benchmarks become vulnerable to memorization and contamination.
- Aggregate scores can hide degenerate strategies, uneven role performance, or catastrophic failures in a small but important subset.
- LLM-as-a-judge can be useful but requires calibration and rubric audits.
- Closed benchmarks improve test integrity but reduce reproducibility; open benchmarks improve reproducibility but can be overfit.
- Agent benchmarks must evaluate trajectories and side effects, not only the final answer.

## Source trail

The entries above are drawn from the existing paper and article summaries in this wiki. The central index page is [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation and Benchmarks Hub]].