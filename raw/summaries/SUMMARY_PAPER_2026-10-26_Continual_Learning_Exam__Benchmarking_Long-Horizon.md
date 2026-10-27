---
title: Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents
url: http://arxiv.org/abs/2610.33956v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_00-00-25Z_ContinualLearningExam_BenchmarkingLong_HorizonRSIa.md
generated_at: 2026-10-26 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces the Continual Learning Exam (CLE), a large-scale benchmark designed to evaluate whether LLM agents can improve over time by accumulating and applying knowledge from experience across realistic professional workflows. Rather than testing isolated task performance, CLE structures 600 levels across 89 professional roles in 12 occupational domains as five-level ladders where later levels depend on knowledge gained from earlier ones. The evaluation reveals that even frontier LLMs struggle with sustained learning from experience, with the best system completing all five levels in only 23.3% of tasks, underscoring a fundamental gap in current agent capabilities.

## Key Takeaways
- CLE is constructed by 50+ domain experts and contains 120 human-authored tasks organized as five-level ladders (600 levels total), spanning 89 professional roles across 12 occupational domains. Each level must be passed to unlock the next, and later levels explicitly build on experience accumulated during earlier assignments, making it a genuine test of knowledge retention and progressive skill acquisition rather than one-shot task solving.
- The benchmark compares two evaluation settings: a single-submission setting and a feedback-revision setting where agents receive diagnostic feedback after failure and are allowed one revision. Across 17 harness-model configurations using frontier LLMs, feedback and revision yield only a median completion gain of 5.3 percentage points, indicating that current LLMs cannot effectively leverage diagnostic feedback to meaningfully improve their performance across a learning sequence.
- Even the best-performing system clears only 47.7% of levels and completes all five levels in just 23.3% of tasks, demonstrating that sustained, experience-driven learning remains a severe unsolved challenge for frontier LLMs. The authors also note that CLE can serve as a post-training dataset to strengthen continual learning capabilities in future models.

## Context
Current LLM evaluation benchmarks overwhelmingly measure single-task performance, treating each query as an isolated problem without any mechanism for an agent to accumulate, refine, or transfer knowledge across a sequence of related tasks. This gap is critical because real-world deployment of LLM agents in professional settings demands exactly the kind of progressive, experience-driven improvement that CLE targets. By grounding evaluation in realistic professional workflows authored by domain experts, CLE shifts the research conversation from static capability assessment to dynamic learning trajectories, aligning benchmarking with the actual operational requirements of autonomous agents.

## Implications
For the AI research community, CLE provides a concrete, reproducible testbed that exposes the limitations of current frontier models in long-horizon experiential learning, setting a clear target for future model development and post-training strategies. For industry practitioners deploying LLM agents in professional domains such as law, engineering, healthcare, and finance, the findings signal that current systems cannot yet be trusted to reliably improve through accumulated workplace experience, necessitating careful human oversight and structured feedback loops. The availability of CLE as a post-training dataset also opens a practical pathway for fine-tuning models specifically to strengthen their capacity for knowledge retention and progressive skill building across extended task sequences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33956v1)
