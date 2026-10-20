---
title: CoMem: Learning to Anticipate Failures from Retrieved Experience
url: http://arxiv.org/abs/2610.25790v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_04-54-46Z_CoMem_LearningtoAnticipateFailuresfromRetrievedExp.md
generated_at: 2026-10-19 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoMem (Compounding Memory) is a framework for LLM agents that integrates retrieved cross-task experience directly into the learned parametric memory, rather than feeding both sources side-by-side to a solver as prior methods do. By making retrieved reflections an input to the memory module at both training and inference time, CoMem produces grounded failure hypotheses and reflective diversity, achieving strong results across two model backbones and five benchmarks spanning math, code generation, and multi-hop question answering, while also generalizing to out-of-distribution tasks and enabling smaller models to guide stronger solvers.

## Key Takeaways
- CoMem addresses a fundamental limitation in reflective LLM agents: when an agent reflects only on its own single-task attempts, it tends to regenerate the same failure explanation repeatedly. Cross-task reflective memory in existing systems comes in two disconnected forms—retrieved memory (explicit but bounded by a fixed bank) and parametric memory (generalizing but ungrounded beyond the task description)—and current agents merely concatenate their outputs additively, meaning retrieved experience never actually reshapes what the learned memory produces. CoMem breaks this additive barrier by making retrieved experience a direct input to the learned memory itself.
- The mechanism involves building a bank of the agent's own successful and failed reflections, training the memory module to write failure hypotheses (candidate explanations of how an attempt is likely to go wrong) conditioned on retrieved cases, and at test time reasoning from newly retrieved cases to guide each attempt. Varying the retrieved cases yields reflective diversity that is not merely stochastic sampling but is grounded in concrete prior experience, producing genuinely different diagnostic perspectives on the same task.
- Empirically, CoMem demonstrates strong overall performance across two backbone architectures and five benchmarks in mathematics, code, and multi-hop QA. Additional evaluations confirm that the approach generalizes to out-of-distribution tasks and, notably, enables smaller language models to provide effective guidance to stronger solvers, suggesting a practical path toward efficient multi-model agent pipelines.

## Context
This work sits at the intersection of LLM agent self-improvement, retrieval-augmented generation, and meta-learning. As autonomous agents increasingly tackle complex multi-step tasks, the ability to learn from past failures without retraining is critical. Prior reflection pipelines treat memory as a static lookup or a fine-tuned parameter update, but neither mechanism truly compounds experience across tasks. CoMem represents a shift toward compounding memory architectures where retrieval and parametric learning are co-trained and co-inferred, aligning with broader trends in the field toward lifelong learning agents and compositional memory systems that go beyond simple RAG or fine-tuning.

## Implications
For practitioners building agentic systems in software engineering, scientific reasoning, or multi-hop information retrieval, CoMem offers a blueprint for agents that genuinely learn from accumulated cross-task experience rather than repeating the same mistakes. The finding that smaller models can effectively guide stronger solvers through grounded failure hypotheses suggests cost-efficient multi-model architectures where a lightweight reflective module steers a large solver, reducing compute overhead while improving reliability. For the research community, the compounding-memory paradigm challenges the prevailing additive fusion of retrieval and parametric memory and opens new directions for training agents that treat retrieved experience as a first-class signal in their internal reasoning pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25790v1)
