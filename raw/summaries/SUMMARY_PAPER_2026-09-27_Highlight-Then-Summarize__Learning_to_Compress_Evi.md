---
title: Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding
url: http://arxiv.org/abs/2609.31382v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_15-16-35Z_Highlight_Then_Summarize_LearningtoCompressEvidenc.md
generated_at: 2026-09-27 22:17
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Highlight-Then-Summarize (H2S), a compress-then-reason paradigm designed to improve long-context understanding in large language models by explicitly separating evidence extraction from answer generation. By first isolating question-relevant, source-grounded information and then synthesizing it into a compact summary before producing a final response, the approach effectively mitigates noise and redundancy in lengthy inputs. Experimental evaluations demonstrate that the proposed H2S-14B model significantly outperforms larger baselines while maintaining high accuracy even under strict output constraints.

## Key Takeaways
- The authors propose a two-stage reasoning pipeline called Highlight-Then-Summarize (H2S) that forces models to first identify task-relevant evidence and then integrate it into a question-conditioned summary, ensuring focused and transparent reasoning over extended documents.
- To enable robust training and evaluation, the research introduces H2S-Dataset containing 6,647 examples across eleven benchmark families with an average context length of 43.9K tokens, alongside H2S-RL which applies process-level rewards for both evidence selection and summary construction rather than relying solely on final-answer correctness.
- Evaluated on the seven-task H2S-Bench under a shared 128K input and 4K output budget, the H2S-14B model achieves an average score of 32.60, surpassing Qwen3.8-27B by 10.17 points and demonstrating remarkable efficiency by retaining 97.1% of its higher-budget performance with minimal generation limits.

## Context
Long-context modeling has emerged as a critical challenge in modern AI systems as applications increasingly demand reasoning over extensive documents, multi-turn conversations, and complex codebases. Standard transformer architectures often suffer from attention dilution, computational bottlenecks, and degraded retrieval accuracy when processing sequences that exceed typical window sizes. This research addresses those limitations by introducing structured compression techniques that align model focus with task objectives rather than relying on unfiltered context retention.

## Implications
Practitioners deploying LLMs for document analysis, legal review, or technical debugging can adopt H2S-style architectures to reduce inference costs and improve answer precision without requiring larger parameter counts or extended hardware budgets. The process-level reinforcement learning methodology provides a scalable training paradigm that could be generalized across domains requiring precise information extraction from noisy, multi-thousand-token inputs. Ultimately, this work encourages a shift toward more efficient, interpretable reasoning pipelines where explicit evidence compression becomes a standard architectural component rather than an optional post-processing step.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31382v1)
