---
title: Evaluating the Hidden Costs of Personalization in Large Language Models
published: 2026-08-28T20:05:12Z
authors: Yumeng Wang, Yuchen Wu, Cheng Qian, Zhiyuan Fan, Hyeonjeong Ha, Shujin Wu, Jiayu Liu, Heng Ji, Ge Wang
url: http://arxiv.org/abs/2608.28833v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating the Hidden Costs of Personalization in Large Language Models

## Abstract
While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user satisfaction when conditioned on personal context such as conversation history, inferred preferences, and user profiles. Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo chambers; and (3) sycophantic bias, where models agree excessively with user opinions. As a result, models may reference personal information in contexts where it is unnecessary, inadvertently collapse response diversity, or agree excessively with user opinions. Despite the growing use of personalization in AI assistants, there has been limited systematic evaluation of its potential side effects. To bridge this gap, we propose PRISK, a dynamic evaluation framework with automated data generation and tailored metrics that uncovers systematic limitations in current LLM personalization and how personalized information shapes its responses. Our empirical analysis across 13 LLMs demonstrates the presence of user profiles and retrieved memories consistently exacerbates biases, resulting in an average drop of 45.9% in irrelevant personalization, 41.7% in preference narrowing and 61.7% in sycophantic bias.

## Metadata
- **Published**: 2026-08-28T20:05:12Z
- **Authors**: Yumeng Wang, Yuchen Wu, Cheng Qian, Zhiyuan Fan, Hyeonjeong Ha, Shujin Wu, Jiayu Liu, Heng Ji, Ge Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28833v1)