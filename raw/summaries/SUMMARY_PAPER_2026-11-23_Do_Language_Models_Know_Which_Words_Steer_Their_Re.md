---
title: Do Language Models Know Which Words Steer Their Reasoning?
url: http://arxiv.org/abs/2611.27317v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_08-58-26Z_DoLanguageModelsKnowWhichWordsSteerTheirReasoning.md
generated_at: 2026-11-23 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether language models truly understand which words in their input context drive their chain-of-thought reasoning. The authors identify a phenomenon they call Phantom Context Influence (PCI), where models are disproportionately steered by semantically irrelevant words while simultaneously denying those words' relevance when self-reflecting. They propose Online KV Suppression, a targeted intervention that zeroes out the KV-cache entries of high-influence words the model itself judges inert, yielding up to 8.9 percentage point improvements in CoT accuracy across multiple models and benchmarks.

## Key Takeaways
- The authors introduce Leave-One-Out Word JSD analysis, a method that removes one context word at a time from an otherwise intact prompt to isolate its marginal effect on the next-token distribution. Words whose removal flips the model's prediction are identified as "pivot words," revealing hidden dependencies in the reasoning chain that are invisible to standard attention analysis.
- Across four models and three benchmarks, the study demonstrates a Generation-Judgment Contradiction: language models are measurably steered by specific context words during generation, yet when asked to self-judge whether those same words influenced their reasoning, they largely deny the dependence. This exposes a fundamental gap between a model's internal computational behavior and its introspective self-report.
- Online KV Suppression scores every prompt word's influence over the entire chain of thought in a single forward pass, then selectively zeroes the KV-cache entries of the highest-influence word that the model itself judges to be inert, and redecodes. This single-word surgical intervention improves CoT accuracy across four models and five reasoning benchmarks, with gains up to 8.9 percentage points on math reasoning tasks.

## Context
Chain-of-thought prompting has become a dominant technique for eliciting structured reasoning from large language models, yet the mechanistic question of which specific tokens in a prompt actually steer the generated reasoning steps remains poorly understood. Prior interpretability work has examined attention patterns and neuron activations, but this paper shifts focus to a behavioral and self-reflective angle: can the model itself identify the words that drive its own reasoning? The findings challenge assumptions about model introspection and suggest that CoT reasoning is more fragile and context-sensitive than commonly assumed.

## Implications
For practitioners deploying CoT-based reasoning systems, the Generation-Judgment Contradiction implies that models cannot be trusted to self-diagnose which parts of their input are driving errors, making prompt auditing and reasoning trace inspection essential. The Online KV Suppression technique offers a practical, low-cost intervention that can be integrated into inference pipelines to improve accuracy without retraining, suggesting that targeted KV-cache manipulation may become a viable tool for reasoning reliability in production LLM systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27317v1)
