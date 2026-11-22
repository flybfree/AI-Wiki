---
title: Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic Authorship Attribution
url: http://arxiv.org/abs/2611.23530v1
type: paper-summary
date: 2026-11-21
source_paper: 2026-11-17_21-37-02Z_DreamingUpAuthors_FactualPrevalenceandLLMHallucina.md
generated_at: 2026-11-21 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the relationship between factual prevalence in training data and hallucination rates in Large Language Models, using academic authorship attribution as a controlled test case. The authors curate a dataset of 1.92 million papers across eight scientific disciplines, stratified by citation count as a proxy for factual prevalence, and demonstrate a robust inverse relationship between citation frequency and hallucination rates across three state-of-the-art LLMs. Their mechanistic analysis reveals that hallucinations primarily stem from retrieval limitations rather than knowledge absence, with factual prevalence encoded in pre-generation hidden-state representations.

## Key Takeaways
- The study establishes a clear inverse correlation between citation count (as a proxy for factual prevalence) and hallucination rates in LLMs. For rarely cited papers, hallucination rates exceed 98%, while for highly cited papers, rates fall below 37%. This pattern holds consistently across all three tested models and all eight scientific disciplines, suggesting a universal mechanism rather than a model-specific artifact.
- In-depth analysis demonstrates that these hallucination failures primarily reflect retrieval limitations rather than a fundamental absence of knowledge in the model's parameters. This distinction is critical because it implies that the information may exist within the model but cannot be reliably accessed or generated, pointing toward architectural and attention-mechanism constraints rather than training data gaps.
- Hidden-state probing of open-source models reveals that factual prevalence is encoded in pre-generation representations, providing convergent mechanistic evidence for the prevalence-hallucination relationship. This finding suggests that models internally "know" which facts are well-supported versus poorly supported, yet this internal signal does not reliably prevent hallucinated outputs during generation.

## Context
This work addresses a fundamental and underexplored question in LLM research: why models hallucinate specific facts more than others, and what role training data distribution plays in generating unreliable outputs. While hallucination has been widely documented, the mechanistic link between factual prevalence in training corpora and generation failures has remained poorly understood. By using academic authorship attribution—a task with ground-truth verifiable answers and a natural prevalence proxy through citation counts—the authors create a rigorous experimental framework that isolates the prevalence variable from other confounders, advancing the scientific understanding of LLM failure modes beyond anecdotal observations.

## Implications
For practitioners deploying LLMs in knowledge-intensive applications such as academic search, legal research, or medical literature review, these findings suggest that model reliability is systematically lower for obscure or under-cited information, and that confidence should be calibrated accordingly. For the AI research community, the mechanistic evidence that prevalence is encoded in hidden states but fails to prevent hallucination points toward targeted interventions in retrieval-augmented generation pipelines and attention mechanisms, potentially guiding the development of models that better leverage their internal prevalence signals during generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23530v1)
