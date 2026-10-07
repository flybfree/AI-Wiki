---
title: Illusory Pattern Perception Drives Spurious Inference in Large Language Models
url: http://arxiv.org/abs/2610.07791v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_05-37-12Z_IllusoryPatternPerceptionDrivesSpuriousInferencein.md
generated_at: 2026-10-06 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models exhibit illusory pattern perception, a cognitive tendency to infer meaningful relationships from random or ambiguous data. The authors adapt classic psychological paradigms into three empirical tasks and compare model behavior with human behavior, finding that LLMs often show stronger illusory pattern perception than humans. They further use Sparse Autoencoders to identify internal features associated with holistic frequency perception and analytic cognitive orientation, suggesting mechanisms behind these reasoning errors.

## Key Takeaways
- LLMs frequently over-associate frequent positive attributes with majority groups or large organizations, indicating a bias toward constructing apparent patterns from statistical frequency rather than evidence-based reasoning. This behavior can produce spurious inference in downstream applications such as summarization, evaluation, or decision support.
- Models show an increased tendency to construct causal narratives from ambiguous events, mirroring the human tendency to connect unrelated dots. This suggests that LLMs may not merely reproduce language patterns but can actively generate plausible but unsupported explanations when presented with incomplete or noisy information.
- The paper introduces a Sparse Autoencoder-based interpretability framework to analyze internal representations, revealing that holistic frequency perception and analytic cognitive orientation are linked to illusory pattern perception. This provides a mechanistic view of how model internals may contribute to cognitive-like reasoning errors.

## Context
Illusory pattern perception is a well-known human cognitive bias, but its systematic study in large language models has remained limited. This paper matters because it bridges cognitive psychology and AI interpretability, treating LLM reasoning errors as potentially structured phenomena rather than isolated hallucinations. By adapting established psychological paradigms to model evaluation, it expands the tools available for diagnosing reliability failures in modern language systems.

## Implications
For practitioners, these findings suggest that LLM outputs may contain hidden reasoning biases that are difficult to detect through surface-level evaluation alone. In industry settings, such biases could affect automated decision-making, risk assessment, content moderation, and analysis of social or organizational data. The work also encourages the development of interpretability methods and evaluation benchmarks that explicitly test for spurious pattern perception and causal overinterpretation in model reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07791v1)
