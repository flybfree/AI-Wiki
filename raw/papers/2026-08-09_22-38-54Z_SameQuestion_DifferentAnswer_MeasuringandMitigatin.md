---
title: Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access
published: 2026-08-09T22:38:54Z
authors: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, Yuting Xin
url: http://arxiv.org/abs/2608.08942v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access

## Abstract
Large language models (LLMs) are increasingly integrated into healthcare, education, public services, and everyday decision making. They should provide comparable assistance regardless of a user's literacy, communication style, or prompt-engineering expertise. However, existing research on prompt robustness primarily focuses on adversarial attacks, prompt injection, and prompt optimization, while overlooking whether semantically equivalent requests receive different responses simply because they are phrased differently. We refer to this accessibility challenge as "Prompt Privilege": users with greater prompting expertise systematically obtain better model performance despite expressing the same underlying intent.   To address this problem, we present a unified framework for measuring and mitigating accessibility disparities in LLM interactions. We introduce Prompt Equity Score (PES), a quantitative metric for evaluating performance consistency across user populations, and Prompt Equity Transformer (PET), an LLM-based agent that automatically transforms user requests into semantically equivalent, accessibility-oriented prompts while preserving their intent. PET shifts prompt optimization from the user to the AI system, functioning as an intelligent accessibility layer between users and foundation models. Experiments on the MedQA benchmark demonstrate measurable prompt privilege, with statistically significant performance disparities between low-literacy and expert-prompting cohorts. Applying PET eliminates these disparities while preserving semantic fidelity, demonstrating that accessibility-oriented prompt normalization can improve equitable AI access. By introducing prompt privilege as a new dimension of AI accessibility and PET as a practical solution, this work advances system-centered accessibility and provides a foundation for more fair, trustworthy, and inclusive AI systems.

## Metadata
- **Published**: 2026-08-09T22:38:54Z
- **Authors**: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, Yuting Xin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08942v1)