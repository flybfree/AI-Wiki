---
title: Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought
url: http://arxiv.org/abs/2608.24790v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_16-37-39Z_RightDiagnoses_DecorativeReasoning_APerturbationAu.md
generated_at: 2026-08-25 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a perturbation audit to test whether medical chain-of-thought rationales truly influence model outputs. It applies clinically motivated edits to both chains and questions across 14 LLMs on medical QA benchmarks and finds that in many cases the chain is decoupled from answer changes, indicating it may be decorative rather than functional.

## Key Takeaways
- The Chain-Decoupling Rate (CDR) measures how often a model’s edited chain does not affect its answer, reaching 72.9% on clinically meaningful destructive edits, showing that the chain is often ignored by the system.
- Accuracy remains unchanged when only the chain is altered, suggesting the chain does not impact correctness and can be removed without loss of performance.
- When CoT prompting is omitted, accuracy stays the same, indicating the chain is not essential for correct reasoning.

## Context
Medical chain-of-thought prompts are widely used to simulate human-like reasoning in large language models but their reliability has never been empirically verified. This study fills that gap by providing a systematic method to detect when these prompts serve as mere documentation rather than genuine reasoning aids, which is crucial given the growing reliance on AI for clinical decision support.

## Implications
For developers and clinicians, this work warns against assuming that visible rationales translate into reliable outputs, urging rigorous testing of model behavior under perturbations. The CDR metric can be adopted as a standard yardstick to evaluate faithfulness in medical AI systems, guiding both research and deployment decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24790v1)
