---
title: RepoClean: Evaluating Coding Agents on Repository-Level Obsolete Code Cleanup
url: http://arxiv.org/abs/2611.30350v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_09-22-53Z_RepoClean_EvaluatingCodingAgentsonRepository_Level.md
generated_at: 2026-11-24 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces RepoClean, a benchmark of 200 cleanup tasks from 34 popular open-source Python repositories, designed to evaluate whether LLM coding agents can safely identify and remove obsolete or redundant code at the repository level. Tasks are constructed by automatically reintroducing code deleted in real repository histories into newer versions, while preserving current implementations and retaining cases where previously passing tests fail. Evaluating seven models, even the best-performing model, GPT-6 Astra, resolves only 23% of tasks, and agents remove substantially less obsolete code when cleanup is not explicitly requested.

## Key Takeaways
- RepoClean isolates repository-level obsolete code cleanup, a capability that remains insufficiently evaluated in isolation, using 200 tasks drawn from 34 popular open-source Python repositories.
- The benchmark is built by reintroducing deleted historical code into newer versions while preserving current implementations and keeping instances where previously passing tests consequently fail, so agents must use repository interfaces and cross-file dependencies to decide which historical code to remove and which implementations to preserve.
- Performance is low: even GPT-6 Astra, the best-performing model, resolves only 23% of tasks, and agents remove substantially less obsolete code when cleanup is not explicitly requested.

## Context
Large language model agents have demonstrated strong repository-level programming capabilities, but as software evolves, code can become redundant or obsolete, increasing maintenance costs and potentially introducing functional issues. Autonomous repository-level cleanup is therefore a distinct and under-studied capability that differs from ordinary feature development, which is why RepoClean is designed to measure it in isolation rather than as a side effect of broader coding benchmarks.

## Implications
The results indicate that current coding agents are far from reliable autonomous software maintenance, suggesting that explicit cleanup requests and stronger cross-file dependency reasoning are needed before agents can safely remove code. For the field and practitioners, RepoClean provides a foundation for systematically studying cleanup challenges and advancing coding agents toward autonomous software maintenance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.30350v1)
