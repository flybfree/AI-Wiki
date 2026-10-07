---
title: Beyond Refusal Patterns: Safe-Role Internalization for Robust and Generalizable LLM Safety Alignment
published: 2026-10-04T15:50:42Z
authors: Jinghao Pang, Jitai Hao, Qiang Huang, Zhaochun Ren, Jun Yu
url: http://arxiv.org/abs/2610.07023v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Refusal Patterns: Safe-Role Internalization for Robust and Generalizable LLM Safety Alignment

## Abstract
Large Language Models (LLMs) have achieved remarkable capabilities but remain vulnerable to jailbreak attacks that elicit harmful or unsafe outputs. Existing safety alignment approaches, including Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), often require substantial attack-specific supervision and computational resources, while remaining susceptible to shallow safety alignment and over-refusal. To address these challenges, we introduce SSRFT(Supervised Safe-Role Fine-Tuning), the first framework that reformulates safety alignment as the internalization of a predefined safe role. SSRFT constructs a Safe-Role Question-Answer (SRQA) dataset from psychometric questions, limited jailbreak prompts, and a safe-role description. Role-consistent responses are synthesized, validated, and expanded into diverse scenarios, enabling models to internalize safety-oriented values and principles rather than explicit refusal patterns. Experiments across multiple Base and Instruct models show that SSRFT achieves more robust and generalizable safety alignment than standard SFT. SSRFT shows substantially greater robustness to prefilling attacks and better generalization to unseen jailbreak domains, while reducing over-refusal on benign queries and preserving the model's general capabilities. These results establish safe-role internalization as an effective alternative to refusal-centric safety alignment. Warning: This paper contains examples of harmful and toxic language.

## Metadata
- **Published**: 2026-10-04T15:50:42Z
- **Authors**: Jinghao Pang, Jitai Hao, Qiang Huang, Zhaochun Ren, Jun Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07023v1)