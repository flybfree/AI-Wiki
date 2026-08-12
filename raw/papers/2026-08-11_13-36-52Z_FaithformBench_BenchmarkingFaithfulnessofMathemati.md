---
title: FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation
published: 2026-08-11T13:36:52Z
authors: Rob Cornish, Iacopo Ghinassi, Po-Hung Yeh, Shuqi Liu, Qiyuan Xu, Haoxuan Yin, Dominik Wagner, Wenda Li, Yee Whye Teh, Luke Ong
url: http://arxiv.org/abs/2608.10916v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation

## Abstract
Autoformalisation (AF) systems map natural language reasoning steps into formal statements in a proof assistant such as Lean. We consider how to assess the faithfulness of these systems. Existing approaches require expensive human-annotated ground truth, or rely on LLM judges or embedding models, which come with limited guarantees of accuracy. In addition, these methods typically only consider inputs that are known to be correct, and therefore do not assess whether the AF translates incorrect inputs faithfully. To address these limitations, we propose a new benchmark for AF faithfulness that is cheap to apply, sound under weak assumptions, and assesses both positive and negative examples. Our method is based on automatically generating perturbed reasoning steps that are designed to be invalid, and then measuring validity preservation on unperturbed steps and invalidity preservation on perturbed steps. We apply our method to eight AF systems across four mathematical datasets, and observe pervasive sycophancy: many AFs "silently correct" invalid inputs into provable statements. The most validity-preserving fine-tuned AFs are also the most sycophantic, suggesting a tension between validity and invalidity preservation in current AF systems.

## Metadata
- **Published**: 2026-08-11T13:36:52Z
- **Authors**: Rob Cornish, Iacopo Ghinassi, Po-Hung Yeh, Shuqi Liu, Qiyuan Xu, Haoxuan Yin, Dominik Wagner, Wenda Li, Yee Whye Teh, Luke Ong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10916v1)