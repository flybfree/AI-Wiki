---
title: Counterfactual Self-Evolving Agents for Evidence-Grounded Reasoning
published: 2026-09-26T18:54:50Z
authors: Xing Han, Yuxin Wang, Chen Chen, Wei Dai, Gautham Krishna Gudur, Shijun Li, Hsing-Huan Chung, Gregory D. Hager, Joydeep Ghosh, Paul Pu Liang, Suchi Saria
url: http://arxiv.org/abs/2609.32870v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counterfactual Self-Evolving Agents for Evidence-Grounded Reasoning

## Abstract
Self-play proposer--solver methods improve reasoning by generating tasks and learning from verified solutions. However, for evidence-identifiable tasks, where case-specific evidence and domain knowledge determine a checkable answer, self-play requires generating plausible cases whose answers can be independently verified. We introduce counterfactual self-evolution, which generates counterfactual context for reconsidering the original case. A trainable Proposer constructs targeted evidence edits and describes potential outcome changes with causal explanations. We handcraft an expert-verified counterfactual instruction-tuning dataset to teach the Proposer to generate high-quality counterfactuals across a broad range of action--outcome scenarios. Each counterfactual instruction-tuning example specifies an edit within a defined category and explains its hypothesized causal effect on the decision, teaching the Proposer to reason systematically about what changes and why. We instruction-tune the Proposer on these examples, then formulate a fine-tuning reward that integrates feedback from the Solver and Verifier. Across diverse counterfactual scenarios, this reward favors high-quality counterfactuals and warranted revisions, while penalizing changes that overturn correct decisions. The counterfactual context aims to correct errors and strengthen confidence in correct decisions. Accepted counterfactuals accumulate in memory that supplies in-context evidence to the frozen Solver; the Solver adapts through evolving context rather than weight updates. We apply the framework to clinical reasoning, fact verification, and business reasoning. Our evaluation tracks performance over successive rounds as counterfactual memory grows, including transfer to harder cases. Our method achieves superior results across diverse frontier models.

## Metadata
- **Published**: 2026-09-26T18:54:50Z
- **Authors**: Xing Han, Yuxin Wang, Chen Chen, Wei Dai, Gautham Krishna Gudur, Shijun Li, Hsing-Huan Chung, Gregory D. Hager, Joydeep Ghosh, Paul Pu Liang, Suchi Saria
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32870v1)