---
title: GEPA-Curator: Curated Learning for Self Improving Agents
url: http://arxiv.org/abs/2610.37651v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_17-58-11Z_GEPA_Curator_CuratedLearningforSelfImprovingAgents.md
generated_at: 2026-10-27 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
GEPA-Curator addresses a critical flaw in existing reflective prompt optimizers for LLM-based agents: the assumption that all failed agent rollouts provide useful learning signal for prompt improvement. The authors argue that agentic failures often stem from harness limitations, stochastic execution, or noisy judges rather than genuine prompt weaknesses, making indiscriminate learning from failures potentially harmful. GEPA-Curator introduces a two-component framework—task curation and prior success retrieval—that selectively filters which experiences inform prompt optimization, achieving performance gains of up to 20.7% over GEPA and 21.2% over ACE across multiple agentic benchmarks.

## Key Takeaways
- Task curation filters out tasks likely to produce noisy or unreliable learning signals, recognizing that not every failed rollout reflects a prompt deficiency. Agentic failures can arise from environmental stochasticity, harness constraints, or unreliable evaluation judges, and feeding these into a prompt optimizer can degrade rather than improve agent performance. This filtering step ensures the optimizer only learns from experiences that genuinely reflect prompt weaknesses.
- Prior success retrieval selectively retrieves past successful trajectories for a given task and provides them as additional context to the prompt optimizer. Rather than learning only from failures, the system leverages proven successful strategies as exemplars, giving the optimizer concrete, reliable patterns to reinforce in the prompt rather than speculative corrections derived from ambiguous failures.
- The framework was evaluated across four diverse agentic benchmarks (GoBrowse, ALFWorld, AppWorld, and τ-bench) using two frontier optimizer models (Gemini 3.1 Pro and Claude Opus 5), demonstrating consistent improvements over both GEPA and ACE baselines. The gains of up to 20.7% and 21.2% respectively indicate that curation strategy is a broadly applicable improvement rather than a benchmark-specific trick.

## Context
This work sits at the intersection of prompt optimization, agentic AI systems, and data curation for self-improving language models. As LLMs are increasingly deployed in multi-turn agentic workloads requiring sustained interaction with complex environments, the quality of learning signals fed back into prompt optimizers becomes a bottleneck. Prior reflective optimizers like GEPA and ACE treat all rollout outcomes uniformly, an approach that mirrors broader concerns in machine learning about noisy labels and distribution shift. GEPA-Curator reframes prompt optimization as a data curation problem, aligning with growing research on selective training data and curriculum learning in large-scale model training.

## Implications
For practitioners building self-improving agent pipelines, GEPA-Curator suggests that indiscriminate learning from agent failures can actively harm performance, and that investing in curation infrastructure—filtering unreliable signals and retrieving successful exemplars—is more impactful than simply scaling the volume of rollout data. For the broader field, this work highlights that agentic evaluation systems themselves introduce noise that must be accounted for in any self-improvement loop, urging developers to treat the learning signal pipeline as a first-class engineering concern rather than an afterthought. The approach is model-agnostic and benchmark-agnostic, making it a practical addition to any agentic system that iteratively refines prompts through experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37651v1)
