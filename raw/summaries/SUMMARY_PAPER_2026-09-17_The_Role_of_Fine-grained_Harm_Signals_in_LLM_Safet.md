---
title: The Role of Fine-grained Harm Signals in LLM Safety
url: http://arxiv.org/abs/2609.19366v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-16_19-40-50Z_TheRoleofFine_grainedHarmSignalsinLLMSafety.md
generated_at: 2026-09-17 21:36
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates whether fine-grained, category-specific harmfulness representations—distinct from a general "harm" signal—play a significant role in Large Language Model (LLM) safety. By isolating these category residuals and applying activation steering across 11 risk categories in three different instruction-tuned models, the researchers discovered that these specific signals influence model behavior in complex ways. Specifically, they found that while the consistency of harm encoding varies by category, it remains relatively stable across different models, whereas the tendency to trigger a refusal is more dependent on the specific model being tested.

## Key Takeaways
- Isolation of Category Residuals: The researchers successfully isolated "category residuals" by removing shared general harmfulness representations from categorical ones, finding that these residuals remain orthogonal to general harm at every layer of the network.
- Consistency in Harm Encoding: The study revealed that whether a category residual encodes harmfulness varies across different categories (such as hate speech versus other risks), but this specific pattern remains consistent across multiple instruction-tuned models.
- Impact on Refusal and Alignment: The research demonstrated that while the tendency of these residuals to induce model refusal is model-dependent, they consistently increase the LLM's downstream internal alignment with general harm representations, proving that fine-grained signals are essential for understanding safety.

## Context
This paper matters because current AI safety research often treats "harm" as a monolithic concept or focuses primarily on identifying a single, global representation of toxicity. By exploring the nuances of category-specific residuals, this work provides a deeper understanding of how models internalize complex human values and risks, which is essential for developing more precise and effective alignment techniques.

## Implications
For AI researchers and safety engineers, these findings imply that "surgical" interventions in LLMs must account for the fact that even directions orthogonal to a concept can contribute to its downstream amplification. This suggests that simply identifying or suppressing a general harm signal may not be enough to ensure safe behavior, as fine-grained category residuals play a critical role in how models process and respond to specific types of harmful content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19366v1)
