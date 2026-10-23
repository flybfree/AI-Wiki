---
title: Invisibilization as a Source of Probability Bias in Language Models
url: http://arxiv.org/abs/2610.30785v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_06-03-35Z_InvisibilizationasaSourceofProbabilityBiasinLangua.md
generated_at: 2026-10-22 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how language models' alignment to avoid using protected attributes like race and gender creates a hidden probability bias, where models disproportionately refuse to assess information from reporters described as Black compared to white-described reporters. Using a controlled two-urn Bayesian game across 6,600 sessions with leading models from OpenAI and Anthropic, the authors demonstrate that models decline to evaluate Black-described reporters 46% of the time versus 9% for white-described reporters, a bias invisible to standard fairness audits. The authors also propose a scoring mechanism that substantially reduces this refusal-rate disparity over repeated interactions.

## Key Takeaways
- Models treat information as worthless at rates determined by the reporter's racial description rather than by the actual evidence presented, declining Black-described reporters 46% of the time versus 9% for white-described reporters, yet paradoxically granting slightly more trust to Black-described reporters when they do engage with the information.
- The bias is invisible to conventional fairness audits that compare average trust levels or examine only assessed cases, meaning standard evaluation frameworks would fail to detect this form of discrimination embedded in refusal behavior.
- The bias follows specific words rather than semantic categories: models invoke race-related reasoning for "Black" but not for its Spanish translation "negro," and never for "Indigenous," suggesting the bias is triggered by token-level associations rather than conceptual understanding. Additionally, the bias worsens under warning instructions that practitioners would typically try first, and grows with increased reasoning effort.

## Context
This work sits at the intersection of AI alignment, fairness auditing, and probabilistic reasoning in large language models. As frontier models from OpenAI and Anthropic are increasingly deployed in decision-support roles where they must weigh testimony and evidence, the alignment practice of suppressing protected attributes introduces a subtle but consequential failure mode. The paper contributes to a growing body of research showing that well-intentioned safety guardrails can produce asymmetric harms that standard evaluation pipelines are structurally blind to, particularly when the harm manifests as non-response or refusal rather than as an incorrect output.

## Implications
For practitioners deploying LLMs in settings involving human testimony, hiring, legal reasoning, or social science research, this finding warns that the most intuitive mitigation—adding explicit warnings about bias—can actually worsen the problem, and that standard fairness audits will not catch refusal-based discrimination. The proposed scoring mechanism offers a practical path forward: by evaluating model trust against revealed truth over repeated rounds, the racial gap in trust can be reduced below 0.02, suggesting that iterative feedback loops rather than static prompt engineering may be more effective for reducing this class of bias in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30785v1)
