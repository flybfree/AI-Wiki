---
title: RAISE: Reinforcing Access Control Policy Synthesis in LLMs via Symbolic Evaluation
url: http://arxiv.org/abs/2609.33796v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_17-53-13Z_RAISE_ReinforcingAccessControlPolicySynthesisinLLM.md
generated_at: 2026-09-28 21:44
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces RAISE, a method to reinforce access control policy synthesis in Large Language Models using symbolic evaluation and formal verification. It presents CedarInstruct, the first dataset for training and evaluating formally verifiable Cedar policies, containing 5,800 scenarios with verified targets and executable verification plans. RAISE employs a two-stage approach of verified supervised fine-tuning followed by reinforcement learning, achieving significant semantic success improvements over frontier models like GPT-6 Astra and Claude Opus 5.

## Key Takeaways
- The authors construct CedarInstruct, a novel dataset comprising 5,800 scenarios across 44 domains and 1,408 single-organization instances, each equipped with verified target policies and executable verification plans to support both training and semantic evaluation of formally verifiable Cedar policy synthesis.
- RAISE utilizes a two-stage training pipeline starting with verified supervised fine-tuning, which leverages the model's latent authorization logic, followed by reinforcement learning where the verifier signal is crucial; specifically, only the RAISE-OC variant using off-context GRPO effectively improves upon SFT by turning failed checks and symbolic counterexamples into guided exploration.
- Using approximately 5.4K verified scenarios with LoRA fine-tuning on Qwen3.5-9B, RAISE-OC surpasses zero-shot GPT-6 Astra and Claude Opus 5 by 13.33 and 16.26 percentage points respectively in semantic success on held-out scenarios, demonstrating effective transfer to the independent CedarBench dataset.

## Context
As LLMs are increasingly deployed for automated policy generation and security-critical decision-making, ensuring that generated access control policies adhere to strict formal semantics remains a significant challenge due to hallucinations and reasoning errors. This work addresses the gap in verifiable policy synthesis by bridging natural language requirements with executable Cedar policies through rigorous symbolic evaluation, moving beyond simple text generation toward formally correct authorization logic.

## Implications
The introduction of CedarInstruct and the RAISE framework provides practitioners with a scalable pathway to train domain-specific policy synthesizers that can be formally verified, reducing the risk of security vulnerabilities caused by

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33796v1)
