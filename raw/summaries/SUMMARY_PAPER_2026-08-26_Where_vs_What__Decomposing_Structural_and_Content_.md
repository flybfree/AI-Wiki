---
title: Where vs What: Decomposing Structural and Content Failures in LLM-Generated Structured Outputs
url: http://arxiv.org/abs/2608.25358v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_04-32-06Z_WherevsWhat_DecomposingStructuralandContentFailure.md
generated_at: 2026-08-26 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Structure-Content Decomposition (SCD) to separate placement errors from value errors in LLM structured outputs, shows structural fidelity degrades earlier than content accuracy with complexity, and demonstrates SA-RLVR improves VPA. The framework also reveals that this degradation pattern is consistent across models, highlighting a fundamental limitation in current evaluation practices.

## Key Takeaways
- structural fidelity degrades earlier and more sharply than content accuracy as task complexity increases, with DeepSeek-V4-Flash misplacing 35% of values at highest complexity.
- Qwen2.5-7B shows even higher placement errors, misplacing 74%, indicating a pattern linked to semantic shortcuts rather than topological understanding.
- SA-RLVR converts SCD metrics into verifiable rewards via GRPO and lifts JSON Value Placement Accuracy from 26% to 63%, generalizing across schemas.

## Context
Structured output generation is essential for AI systems that rely on precise data representation, yet current evaluation treats placement and value errors as a single metric. This separation helps researchers understand failure modes and design better reinforcement learning objectives. Understanding these failures guides the development of more robust prompting and training strategies.

## Implications
Practitioners can use SA-RLVR to improve model reliability in JSON and table generation tasks. By rewarding correct structural addressing, models become less prone to misplaced data, which is critical for downstream applications requiring accurate structured information. This approach can be extended to other structured formats, fostering a culture of error decomposition in AI research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25358v1)
