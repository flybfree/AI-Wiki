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
- [Lesson 6 — Evaluation & Verification: The Judge Node](https://github.com/flybfree/AI-Wiki/blob/master/concepts/self-improving-ai-loops/2026-06-10_Lesson6_Evaluation.md) — shared tags: evaluation, 5 topic terms overlap, same area: home
- [Evaluation and Benchmarks Hub](https://github.com/flybfree/AI-Wiki/blob/master/concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md) — 1 title term overlap, shared tags: evaluation, 1 topic term overlap
- [AI/ML Foundations Lesson 15 - Evaluation, Overfitting, and Limits](https://github.com/flybfree/AI-Wiki/blob/master/concepts/ai-foundations/ai-ml-foundations-lesson-15-evaluation-overfitting-and-limits.md) — shared tags: evaluation, 5 topic terms overlap, same area: home

## Core LLM benchmark families

These are the main benchmark families commonly used to describe general-purpose large language model (LLM) capability. They measure different constructs; no single score is a complete measure of model quality.

### Knowledge and broad academic reasoning

- **MMLU (Massive Multitask Language Understanding)** — multiple-choice questions across 57 subjects, including science, humanities, law, medicine, and professional knowledge. It is useful as a broad knowledge-and-reasoning signal, but many questions are static and increasingly exposed to memorization and contamination concerns.
- **MMLU-Pro** — a harder, more reasoning-focused successor to MMLU with more difficult questions and stricter answer choices. It is generally more discriminating among strong models, but it remains a benchmark of selected multiple-choice knowledge rather than open-ended competence.
- **AGIEval** — exam-style tasks drawn from sources such as law, mathematics, and standardized tests. It tests academic and professional question answering, but performance can depend on language, cultural context, and familiarity with exam conventions.
- **BIG-bench / BIG-bench Hard (BBH)** — a broad collection of tasks designed to probe language understanding, reasoning, symbolic manipulation, and instruction following. BBH selects particularly challenging tasks, but the suite is heterogeneous and should be reported task by task when possible.

### Mathematics and difficult reasoning

- **GSM8K** — grade-school mathematics word problems. The usual metric is exact-match accuracy on the final answer. It is a useful basic multi-step arithmetic test, but it is too narrow to represent advanced mathematical reasoning.
- **MATH / MATH-500** — competition-style mathematics at a substantially higher difficulty level than GSM8K. Results are sensitive to answer normalization, chain-of-thought policy, and whether tools are allowed.
- **AIME-style evaluations** — difficult contest mathematics with short numerical answers. These are useful stress tests for advanced reasoning, but small test sets make variance large and scores should not be overinterpreted.
- **GPQA (Graduate-Level Google-Proof Q&A)** — expert-written questions in areas such as biology, physics, and chemistry that are intended to resist simple web lookup. **GPQA-Diamond** is the hardest subset. It measures difficult domain reasoning, but its expert knowledge requirements make it less representative of everyday use.

### Coding and software engineering

- **HumanEval** — short Python function-generation problems scored primarily with **pass@1**, the probability that the first generated solution passes the tests. It measures isolated code completion and is vulnerable to contamination and test-suite overfitting.
- **MBPP (Mostly Basic Python Problems)** — beginner-to-intermediate Python programming tasks with executable tests. It complements HumanEval with broader basic programming coverage, but still does not measure repository-level engineering.
- **SWE-bench** — real GitHub issues requiring an agent to inspect a repository, modify code, and pass project tests. It is closer to practical software engineering than function-generation tests, but results depend heavily on the agent harness, test availability, time budget, and patch-validation protocol.
- **LiveCodeBench** — continually refreshed coding problems intended to reduce contamination. It is useful for measuring current coding and competitive-programming performance, though its task distribution differs from production software work.

### Commonsense, language understanding, and truthfulness

- **HellaSwag** — choose the most plausible continuation of a scenario. It tests commonsense completion, but high scores can reflect dataset familiarity rather than robust world understanding.
- **ARC (AI2 Reasoning Challenge)** — grade-school science questions, commonly reported as **ARC-Easy** and the harder **ARC-Challenge**. It is a compact reasoning and knowledge test, not a general intelligence measure.
- **PIQA (Physical Interaction: Question Answering)** — commonsense reasoning about everyday physical situations. It helps test practical knowledge that academic multiple-choice suites may miss.
- **TruthfulQA** — questions designed to expose common misconceptions, imitation of falsehoods, and misleading answers. It measures truthfulness under a specific adversarial design, and results depend on the scoring rubric and judge.

### Instruction following and reliability

- **IFEval (Instruction Following Evaluation)** — checks whether a model obeys verifiable constraints such as formatting, word counts, required phrases, or structural rules. It is valuable for instruction adherence, but automatic checks cover only a limited slice of real user instructions.
- **FollowBench and related constraint-following suites** — evaluate multiple simultaneous constraints and more complex instruction combinations. These are useful complements to IFEval when the deployment depends on reliable formatting or policy compliance.
- **LiveBench** — a periodically refreshed collection of challenging tasks spanning reasoning, coding, mathematics, and language. Its freshness helps reduce contamination, but scores are harder to compare across time because the task mix changes.

### Multimodal and specialist capability

- **MMMU / MMMU-Pro** — university-level multimodal questions requiring images, diagrams, charts, or other visual evidence alongside language reasoning. They test visual-language integration rather than text-only reasoning.
- **MathVista** — visual mathematical reasoning over charts, diagrams, and images. It is useful for document and visual analysis, but it does not cover general multimodal interaction.
- **Domain-specific suites** — examples include medical, legal, multilingual, safety, retrieval-augmented generation (RAG), and tool-use benchmarks. These are often more useful than general leaderboards when the intended deployment has a clear domain and failure cost.

### How to read benchmark scores

- **Accuracy or exact match** reports the fraction of answers judged correct.
- **Pass@k** estimates the chance that at least one of *k* generated solutions passes, so it is not directly comparable with pass@1.
- **Human or LLM-judge scores** depend on the rubric, judge model, prompt, and calibration procedure.
- **Agent benchmarks** should report task success together with trajectory quality, tool correctness, cost, latency, retries, and side effects.
- Always record the model version, prompting method, tool access, sampling settings, number of attempts, evaluation split, and contamination controls.

## What the wiki currently covers

### 1. Protocol and leaderboard validity

- [Beyond Memory Leaderboards](https://github.com/flybfree/AI-Wiki/blob/master/entities/paper/2026-07-18_15-09-58Z_BeyondMemoryLeaderboards_EvaluatingScientif_summary.md) introduces PAIM and PTr for scientific-memory retrieval. It evaluates 81 papers/66 questions and 252 papers/98 questions, and shows that rankings change with ingestion granularity, raw-text preservation, retrieval budget, modality, and judge choice.
- The practical implication is to report **score + protocol + budget**, not score alone. A leaderboard without those controls is difficult to interpret or reproduce.

### 2. Psychometric and cost-aware evaluation

- [Item Response Theory for AI Safety](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-05_17-25-27Z_ItemResponseTheoryforAISafety_summary.md) applies IRT to eight safety benchmarks and 192 language models. It identifies latent dimensions such as refusal strictness, truthfulness, and contextual harm.
- The paper reports that adaptive item selection can recover benchmark scores with far fewer items than random sampling, reducing evaluation cost while also supporting audits for sandbagging and model/API changes.

### 3. Agent safety and adversarial robustness

- [OpenSkillRisk](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-22_13-24-09Z_OpenSkillRisk_BenchmarkingAgentSafetyWhenUs_summary.md) evaluates agents against 263 risky third-party skills in sandboxed environments. Its key contribution is measuring context-sensitive execution risk rather than only text refusal.
- [IssueTrojanBench](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-22_22-20-02Z_IssueTrojanBench_BenchmarkingAICodingAgents_summary.md) tests coding agents against malicious issue requests delivered through multiple vectors, exposing the gap between model-level rejection and end-to-end agent protection.
- [AuthMem-Bench](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-03_04-15-40Z_WhenMemoryBecomesAuthority_BenchmarkingAuth_summary.md) evaluates whether memory consolidation preserves source authority. This makes authorization errors a measurable benchmark outcome rather than an anecdotal failure mode.
- [HarnessSafe](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-07_09-03-49Z_HarnessSafe_EvaluatingSafetyAcrossPersisten_summary.md) evaluates attack propagation through persistent carriers such as memory, skills, tools, and shared artifacts.

### 4. Coding-agent and harness evaluation

- [SWE-Touch](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsers_summary.md) adds user edits during coding tasks. It shows that strong isolated SWE-bench performance does not guarantee workspace awareness or successful conflict resolution.
- [HarnessOpt-Bench](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-06_17-21-05Z_HarnessOpt_Bench_EvaluatingLLMsatHarnessOpt_20260806_2225_summary.md) treats harness optimization as a capability in its own right, separating model ability from the prompts, tools, and control code surrounding the model.
- [Scientific Knowledge Discovery in the Age of Large Language Models](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-29_09-25-55Z_ScientificKnowledgeDiscoveryintheAgeofLarge_summary.md) finds that many retrieval and screening studies rely on internal validation, reinforcing the need for public, standardized evaluation protocols.

### 5. User-centered and social evaluation

- [CallScreenBench](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-02_06-31-25Z_CallScreenBench_BenchmarkingOn_DeviceModels_summary.md) evaluates on-device phone-secretary models using message fidelity, tone, brevity, privacy, and user endorsement—not just task completion.
- [Social Gym and SPaRTan](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-08-10_05-12-56Z_SocialGymandSPaRTan_BenchmarkingandImprovin_20260810_2344_summary.md) uses 21 rule-defined social games and Elo tournaments to make multi-agent social reasoning more objective and comparable across roles.
- [APEX-Accounting](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-29_17-56-49Z_APEX_Accounting_summary.md) evaluates frontier models on expert-authored accounting workflows involving spreadsheets, PDFs, and simulated accounting systems. It illustrates the move from short-answer tests to professional, multi-step work.

### 6. Domain and capability-specific benchmarks

- [QuantiBias](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-23_08-56-11Z_QuantiBias_BenchmarkingQuantization_Induced_summary.md) measures bias that can remain hidden when compressed models pass conventional safety tests.
- [APEX-Accounting](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-29_17-56-49Z_APEX_Accounting_summary.md) covers financial operations and rubric-based workflow completion.
- [Relative Value Learning](https://github.com/flybfree/AI-Wiki/blob/master/concepts/papers/2026-07-23_09-55-45Z_RelativeValueLearning_summary.md) uses 49 Atari games as an empirical testbed for a new RL value estimator; this is a reminder that benchmark use should distinguish algorithm validation from general capability claims.

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

## Revision history

- **2026-06-10** — Initial AI Benchmarks concept page created.
- **2026-08-11** — Reworked from a placeholder into a corpus-grounded benchmark map covering protocol validity, safety, coding agents, user-centered evaluation, domain benchmarks, and benchmark design principles.

## Source trail

The entries above are drawn from the existing paper and article summaries in this wiki. The central index page is [Evaluation and Benchmarks Hub](https://github.com/flybfree/AI-Wiki/blob/master/concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md).