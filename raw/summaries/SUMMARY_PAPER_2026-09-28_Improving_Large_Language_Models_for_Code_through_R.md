---
title: Improving Large Language Models for Code through Runtime Program-State Reasoning
url: http://arxiv.org/abs/2609.34359v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_05-37-40Z_ImprovingLargeLanguageModelsforCodethroughRuntimeP.md
generated_at: 2026-09-28 22:56
model: qwen3.6-35b-a3b
---

## Summary
Large language models receive limited explicit training in reasoning about runtime program states, which hinders their effectiveness in complex software engineering tasks such as debugging and patch generation. This paper introduces Comet-9B, a 9B parameter model based on Qwen3.5-9B Base, developed through a staged post-training pipeline that incorporates two novel program-state reasoning tasks: buggy input-output reasoning and precondition-postcondition reasoning. The authors demonstrate that training models to predict execution behavior and characterize bug-triggering conditions yields substantial gains in patch generation, regression testing, and security proof-of-concept creation, allowing Comet-9B to match the performance of significantly larger or more advanced proprietary models on key benchmarks like SWE-bench Pro and SWT-Bench Verified.

## Key Takeaways
- The study proposes two complementary reasoning tasks: buggy input-output reasoning, where models generate inputs exposing behavioral differences between buggy and hidden correct implementations while predicting execution outcomes, and precondition-postcondition reasoning, which requires symbolically characterizing bug triggers, predicting postconditions, explaining causal links, and generating executable regression tests.
- Incorporating these tasks into supervised fine-tuning improves success rates by 7.25 percentage points on SWE-bench Pro and 9.70 points on SWT-Bench Verified compared to baseline issue resolution training, while sequential reinforcement learning on these tasks provides additional gains of up to 26.79 percentage points on SWT-Bench Verified.
- Despite having only 9B parameters, Comet-9B achieves a score comparable to reported GPT-5.2 results on SWE-bench Pro and matches the success rate of a GPT-4o-based agent on SWT-Bench Verified, demonstrating that targeted runtime state reasoning can bridge performance gaps with much larger models.

## Context
Most large language models rely heavily on syntactic patterns and pre-training data for code generation but lack explicit mechanisms to simulate or reason about dynamic program execution states. This research addresses a critical limitation by focusing on post-training strategies that instill runtime awareness, enabling models to understand the causal relationships between code changes and their effects on system behavior. By emphasizing reasoning over scale, the work aligns with broader efforts to make AI-driven software engineering tools more reliable and interpretable through structured cognitive capabilities rather than brute-force parameter increases.

## Implications
The findings suggest that developers can achieve state-of-the-art results in

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34359v1)
