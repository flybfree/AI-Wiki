---
title: HarnessMM: Recursive Self-Improvement for Harness Token Efficiency
url: http://arxiv.org/abs/2610.32813v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_15-47-47Z_HarnessMM_RecursiveSelf_ImprovementforHarnessToken.md
generated_at: 2026-10-25 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HarnessMM (Harness Minus Minus) is a method designed to reduce redundant reasoning calls in agent harnesses by reusing already-resolved decisions instead of re-invoking the model after tool feedback. Through guarded decision reuse and recursive self-improvement (RSI), the approach iteratively refines harness configurations while keeping actor model weights fixed, yielding substantial token savings—up to 87.93% on DeepSeek Harness—without sacrificing task success rates.

## Key Takeaways
- HarnessMM introduces Executable Decision Graphs that store exact actions, literal arguments, causal dependencies, and public guards, enabling a controller at the model-tool boundary to reuse resolved decisions and replace later reasoning callbacks. This "Certified Callback Substitution" removes registered slow callbacks while new semantic decisions, unsupported evidence, or selector abstention still invoke the original actor, preserving correctness.
- Recursive Self-Improvement iteratively refines companion harness configurations from training feedback, with a validation step selecting the best configuration for deployment. This allows the harness to learn which decisions can safely be reused across tasks without retraining the underlying model, keeping actor weights fixed throughout the process.
- Empirical results demonstrate significant efficiency gains: on HumanEval, Codex success is preserved at 90.82% while tokens per task drop from 66.72k to 47.02k (29.54% saving); for DeepSeek Harness, success improves from 71.43% to 85.71% while tokens per task fall from 96.28k to 11.62k (87.93% saving). An MBPP ablation further confirms 26.91% lower cost than single-use graphs and 19.52% lower cost than retained callbacks.

## Context
Modern LLM-based agent harnesses repeatedly invoke reasoning after every tool interaction, even when a prior call has already determined the next action, inflating token costs and latency. This paper addresses a practical bottleneck in agentic AI systems where the overhead of redundant model calls dominates operational expense. By formalizing decision persistence through guarded graphs and separating harness configuration optimization from model training, HarnessMM contributes to the growing body of work on efficient agent orchestration and inference-time optimization.

## Implications
For practitioners deploying agent systems at scale, guarded decision reuse offers a drop-in strategy to cut inference costs by tens of percentage points without retraining or modifying the underlying model, making agentic workflows more economically viable. The RSI loop for harness configuration suggests that system-level tuning can be automated and validated independently of model weights, opening a path toward self-optimizing agent scaffolds. Industry teams building coding assistants, tool-use agents, or multi-step reasoning pipelines can adopt this pattern to reduce per-task token budgets while maintaining or improving task success.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32813v1)
