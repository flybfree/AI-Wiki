---
title: Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs
url: http://arxiv.org/abs/2609.28150v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_14-06-52Z_ExactFeedbackIsNotControl_EvaluatingText_basedClos.md
generated_at: 2026-09-23 22:11
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper investigates the reliability of closed-loop revision in Large Language Models (LLMs), specifically examining whether providing "exact" feedback is sufficient to ensure a model can successfully correct its own errors. By utilizing a fixed-budget revision protocol with deterministic verifiers, the researchers isolated model behavior from feedback quality and discovered that even with perfect instructions, models exhibit significant and inconsistent success rates in correcting specific constraints.

## Key Takeaways
- The researchers introduced a novel evaluation framework using deterministic verifiers to measure success across exact-length, lexical, and compositional constraints. This method allows for the isolation of model-side revision behavior by ensuring that the feedback provided is always perfectly accurate and complete.
- Evaluation across 19 different models revealed massive performance disparities, with final joint success rates ranging from 17.4% to 99.8%. These gaps persisted even when all models started with identical initial drafts, suggesting that some models are fundamentally less capable of iterative correction than others.
- The study identified a significant issue with "recurrence," where failed revision attempts often result in the model repeating previous outputs. Furthermore, the research found that removing earlier dialogue history did not consistently improve success rates or help models escape these repetitive failure loops, indicating that some models struggle to break out of incorrect patterns even when the context is cleared.

## Context
As LLMs are increasingly used for complex tasks like software engineering and content creation, "closed-loop" systems—where a model receives feedback and tries again—are becoming standard. This paper matters because it identifies a fundamental limitation in current AI: providing better instructions does not automatically result in more reliable autonomous correction or higher reliability in multi-turn interactions.

## Implications
For developers and researchers, these findings suggest that simply improving the clarity of human-provided feedback may not be enough to guarantee success if the underlying model lacks robust revision capabilities. Practitioners should prioritize selecting models based on their demonstrated "recoverability" and recognize that scaling and post-training do not consistently bridge the gap in reliable closed-loop performance across all constraint types.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.28150v1)
