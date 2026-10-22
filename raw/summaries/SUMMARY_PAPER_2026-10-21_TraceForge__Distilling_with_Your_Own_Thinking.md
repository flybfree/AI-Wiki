---
title: TraceForge: Distilling with Your Own Thinking
url: http://arxiv.org/abs/2610.29680v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_12-57-29Z_TraceForge_DistillingwithYourOwnThinking.md
generated_at: 2026-10-21 23:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TraceForge proposes a method for generating synthetic reasoning traces in the style of a student model family, using only a teacher model's context and final answer as input, to enable distillation training when frontier providers withhold their chain-of-thought outputs. The two-stage training pipeline (supervised generation followed by adversarial critic refinement) produces reasoning traces that are judged as authentic as real traces, and the approach yields measurable improvements on coding benchmarks such as HumanEval+ and MBPP+ compared to training on the teacher's own reasoning content.

## Key Takeaways
- Frontier LLM providers increasingly return only final answers or short summaries rather than detailed reasoning traces, creating a bottleneck for distillation-based training of smaller models. The existing workaround of replaying encrypted reasoning blocks across models violates providers' terms of service, making it unsuitable for long-term product development. TraceForge sidesteps this restriction entirely by generating reasoning traces from scratch using the student model's own family style.
- The training pipeline is two-stage: a generator is trained supervised to reconstruct reasoning traces from context and answer pairs, then an adversarial critic is trained to discriminate real from generated traces. An independent judge scores authenticity on a 0-to-1 scale, where TraceForge-generated traces average 0.68, real traces score 0.66, and critic-selected candidates reach 0.82, demonstrating that the generated traces are indistinguishable from genuine reasoning in style.
- On controlled experiments across five benchmarks with all other variables held fixed, TraceForge-generated reasoning outperforms the teacher model's own thinking content on coding tasks. With identical 5,000 questions and the same teacher answers, HumanEval+ improves by 3.7 points and MBPP+ by 7.1 points at the final checkpoint, with the MBPP+ advantage sustained at every checkpoint, supporting the hypothesis that reasoning written in the student's family style is easier for that model to internalize.

## Context
This paper addresses a growing tension in the LLM training ecosystem: distillation from frontier models is standard practice for open-source development, yet proprietary providers increasingly restrict access to their reasoning traces, limiting the training signal available to downstream models. TraceForge represents a principled alternative that respects provider terms while restoring the reasoning supervision signal, positioning itself as a practical bridge between closed-model ecosystems and open-source training pipelines.

## Implications
For practitioners building smaller models through distillation, TraceForge offers a ToS-compliant path to recover reasoning supervision without relying on provider cooperation or fragile workarounds like encrypted-block replay. The finding that family-style reasoning improves learning over the teacher's own reasoning suggests that future distillation pipelines should prioritize stylistic alignment with the target model, potentially reshaping how synthetic training data is generated across the open-source ecosystem.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29680v1)
