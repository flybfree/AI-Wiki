---
title: P-ContextBench: From Personal Fact Recall to Personalized Agent Behavior
published: 2026-10-29T20:38:32Z
authors: Grant Nasir Brown, Abdul Basir Bari, Anmol Tadikonda, Isabel Song
url: http://arxiv.org/abs/2610.40959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# P-ContextBench: From Personal Fact Recall to Personalized Agent Behavior

## Abstract
Large language models (LLMs) are increasingly used for personal tasks, yet evaluating their safe use of personal context remains difficult because such contexts are private, fragmented, dynamic, and socially situated. We introduce P-ContextBench, a realistic, verifiable, and scalable benchmark for evaluating personal-context understanding. P-ContextBench constructs population-structured, life-story-grounded digital humans from demographic seeds reflecting the U.S. population. Rather than using explicit, static profiles, P-ContextBench embeds traits, routines, goals, and constraints as implicit evidence across fragmented, evolving synthetic mobile-app records. It evaluates five capabilities: single-source fact recovery, multi-source fact recovery, temporal state tracking, inference of higher-level personal patterns from routine behavior, and safe handling of requests conflicting with persona-specific constraints through compliance, warning, clarification, or refusal. A multi-stage validation pipeline checks persona plausibility, context recoverability, information leakage, evidence preservation, test-case grounding, and human-judge agreement. We instantiate P-ContextBench with 100 personas, 10,088 hidden facts, 18,261 app-trace fragments, and 4,810 verified test cases. The pipeline supports configurable generation across scales and demographic groups. Cost-effective state-of-the-art (SOTA) LLMs relevant to personal agents achieve below 60% accuracy on temporal tracking, higher-level pattern inference, and constraint-aware action-boundary decisions, with fewer than 10% of test cases answered correctly across all three repeated runs. Even a high-performing SOTA model remains inconsistent on these capabilities. P-ContextBench provides measurable targets for improving the accuracy, reliability, and safety of LLM-based personal agents.

## Metadata
- **Published**: 2026-10-29T20:38:32Z
- **Authors**: Grant Nasir Brown, Abdul Basir Bari, Anmol Tadikonda, Isabel Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.40959v1)