---
title: Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation
published: 2026-08-21T20:19:22Z
authors: Ayush Gupta, Hima Varshini Surisetty, Sreevidya Bollineni, Varad Ingale, Tuhina Tripathi, Abhishek Lalwani, Somya Chatterjee, Sadid Hasan
url: http://arxiv.org/abs/2608.21606v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation

## Abstract
Machine unlearning aims to remove the influence of targeted training data from a model while preserving its remaining capabilities, but evaluating whether such information has truly become inaccessible remains challenging. Existing benchmarks primarily assess unlearning under clean, non-adversarial queries, leaving open whether information that appears forgotten can still be recovered through strategic prompting. We address this gap through a unified evaluation of prompt-based and fine-tuning-based unlearning methods on TOFU using Llama-3.2-3B-Instruct, followed by an adversarial robustness evaluation of methods that perform strongly under standard metrics. We introduce Attack Success Rate (ASR), an LLM-as-judge metric that measures the fraction of adversarial responses whose leakage score exceeds $0.2$, and evaluate recovery across eight attack suites. Our results reveal a substantial gap between clean-query forgetting and adversarial robustness. Although several fine-tuning-based methods achieve Forget Quality above $0.91$, targeted information remains recoverable with ASRs between $72.8\%$ and $84.3\%$, close to the $87.5\%$ ASR of the unprotected base model. In contrast, clean multilingual reformulations yield only $2.95\%$ measured leakage. A manual audit further finds agreement between binary ASR decisions and human factual assessments in seven of ten cases, indicating that ASR provides a useful, though imperfect, signal of behavioral recoverability. These findings show that strong standard-metric performance alone is insufficient to establish robustness after unlearning and motivate adversarial stress-testing as a complementary component of unlearning evaluation.

## Metadata
- **Published**: 2026-08-21T20:19:22Z
- **Authors**: Ayush Gupta, Hima Varshini Surisetty, Sreevidya Bollineni, Varad Ingale, Tuhina Tripathi, Abhishek Lalwani, Somya Chatterjee, Sadid Hasan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21606v1)