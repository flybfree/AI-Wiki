---
title: When Agents Fail: Model or Harness--Who's to Blame?
url: http://arxiv.org/abs/2610.32483v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_10-57-54Z_WhenAgentsFail_ModelorHarness__Who_stoBlame.md
generated_at: 2026-10-26 11:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a systematic framework for disentangling the contributions of underlying LLM models from the execution harnesses (agent scaffolds) that wrap them, arguing that agentic benchmark scores reflect the joint behavior of both components. By proposing five complementary evaluation measures—Valid Completion Rate, Model-Harness Fit, Cross-Model Fit, Interaction Residuals, and Token Load—the authors evaluate four general-purpose harnesses against four core models across six benchmarks, producing 52,168 trajectories across 111 settings. The central finding is that harness rankings are not universal: they shift depending on the model and benchmark, and task performance scores can mask fundamentally different execution profiles, meaning that a single leaderboard cannot fairly attribute success or failure to either the model or the harness alone.

## Key Takeaways
- The paper defines Valid Completion Rate (VCR) as a measure of how reliably an agent finishes normally and produces evaluable output, independent of whether the task answer is correct. This separates infrastructure reliability from task accuracy, revealing that some model-harness pairings fail to even produce a scorable result, which traditional benchmarks silently ignore.
- Model-Harness Fit and Cross-Model Fit together show that a harness optimized for one model can perform poorly with another, and that no single harness dominates across all models. OpenCode achieved the top cross-model ranking, yet DeepSeek V4 Flash Preview maintained consistently high Mean VCR regardless of which harness was used, suggesting that some models are inherently more robust to scaffold variation.
- Interaction Residuals expose pairing-specific strengths and weaknesses that component-level summaries (model-only or harness-only leaderboards) completely hide. Two pairings can produce nearly identical task scores while having very different token consumption profiles and failure modes, meaning that aggregate benchmark numbers can be misleading for practitioners selecting a deployment stack.

## Context
As agentic systems proliferate in software engineering, research automation, and multimodal workflows, the industry increasingly benchmarks agents as monolithic units, conflating model capability with scaffold engineering. This paper addresses a critical gap in the evaluation literature: without decomposing performance into model and harness contributions, practitioners cannot make informed decisions about which component to improve, and model developers cannot isolate genuine reasoning gains from scaffold-induced artifacts. The work sits within a growing movement toward more transparent, component-aware evaluation methodologies in the LLM agent community.

## Implications
For practitioners and platform teams, the findings argue against treating any single harness as universally optimal and instead advocate for model-aware harness selection and task-specific scaffold tuning. For model developers, the results motivate training models to be transferable across harnesses rather than overfitting to a particular scaffold, potentially reducing vendor lock-in. For the broader AI evaluation community, the framework provides a reproducible methodology for auditing agent systems, which could inform procurement decisions, safety assessments, and the design of future agentic benchmarks that report model and harness contributions separately.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32483v1)
