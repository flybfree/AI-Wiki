---
title: Are Large Reasoning Models Good Everyday Reasoners? A Comparison with Non-Reasoning Models on Logical Reasoning Tasks
url: http://arxiv.org/abs/2610.22538v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-15_18-37-22Z_AreLargeReasoningModelsGoodEverydayReasoners_AComp.md
generated_at: 2026-10-20 16:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper systematically evaluates whether Large Reasoning Models (LRMs), which use test-time computation to excel on mathematical and scientific benchmarks, can reliably handle everyday logical reasoning that deviates from formal textbook logic. The authors introduce a new benchmark grounded in linguistic and pragmatic reasoning phenomena and compare LRMs against non-reasoning models under controlled prompting conditions, finding that reasoning models often underperform on everyday reasoning tasks and that some non-reasoning models with chain-of-thought prompting can surpass them.

## Key Takeaways
- Reasoning models exhibit degraded performance on everyday reasoning tasks when those tasks depart from formal logical rules, suggesting that the test-time computation strategies optimized for structured mathematical or scientific problems do not transfer well to the ambiguous, context-dependent reasoning humans perform in daily life.
- Certain non-reasoning models equipped with chain-of-thought prompting outperform comparable reasoning models on everyday reasoning benchmarks, indicating that the architectural and training choices specific to LRMs may introduce biases toward formal logic rather than pragmatic inference, and that prompting strategies alone can sometimes compensate for the absence of dedicated reasoning training.
- Adding supplementary instructions to prompts provides only limited control over the reasoning behavior of these models, implying that post-training objectives and internalized reasoning patterns are difficult to steer through external guidance, and that more fundamental changes to training objectives and evaluation frameworks are needed to capture diverse forms of human reasoning.

## Context
Large Reasoning Models have rapidly advanced performance on structured benchmarks such as mathematics competitions, code generation, and scientific problem-solving, leading to their widespread deployment in commercial AI products. However, the field has largely evaluated these models on tasks that closely mirror formal logic or well-defined problem structures, leaving a significant gap in understanding how these systems handle the informal, pragmatic, and linguistically nuanced reasoning that characterizes everyday human cognition. This paper addresses that gap by constructing a benchmark rooted in linguistic and pragmatic reasoning phenomena, providing a more ecologically valid test of reasoning capabilities.

## Implications
For AI practitioners and product developers deploying reasoning models in real-world applications such as customer support, legal analysis, or conversational assistants, these findings caution that strong benchmark scores do not guarantee reliable everyday reasoning, and that non-reasoning models with careful prompting may sometimes be preferable for pragmatic tasks. For the research community, the results motivate a rethinking of post-training objectives and evaluation suites to include diverse, context-sensitive reasoning tasks, ensuring that future models generalize beyond formal logic to the full spectrum of human inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22538v1)
