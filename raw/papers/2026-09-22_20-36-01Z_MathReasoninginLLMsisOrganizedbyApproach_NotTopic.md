---
title: Math Reasoning in LLMs is Organized by Approach, Not Topic
published: 2026-09-22T20:36:01Z
authors: Sajad Goudarzi, Samaneh Zamanifard, Moloud Nasiri, Hamed Rahimian
url: http://arxiv.org/abs/2609.27041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Math Reasoning in LLMs is Organized by Approach, Not Topic

## Abstract
Mathematical reasoning benchmarks are typically organized by topic, but language models may organize their internal computation by reusable reasoning approach instead. In this paper, we investigate whether open math-capable LLMs organize internally by topical sub-skill or by reasoning approach, and we present evidence that the approach is the key. We introduce a generation-replay protocol: a model first generates a solution, after which we replay the exact prompt-plus-generation trajectory and extract activation-importance signatures over the reasoning tokens. We cluster these signatures without supervision across eight models and five mathematical reasoning sources, then evaluate the recovered structure with structural, semantic, and intervention tests. Across all 40 model-source cells, the recovered clusters outperform matched-size random baselines. Two independent frontier-LLM judges find approach-level coherence in 77-82% of real clusters versus 6-11% in within-source controls, and topic-pure clusters usually receive labels finer than the topic itself. In approach-controlled prompting, changing the requested reasoning approach shifts cluster assignment in seven of eight model conditions, whereas paraphrases largely preserve it. These results indicate that math-capable LLMs organize internal mathematical computation by reasoning approach rather than benchmark topic. The implication is that topic-stratified benchmarks and topic-balanced training corpora can still miss the axis that matters: even deliberately topic-balanced corpora may remain imbalanced over reasoning approaches.

## Metadata
- **Published**: 2026-09-22T20:36:01Z
- **Authors**: Sajad Goudarzi, Samaneh Zamanifard, Moloud Nasiri, Hamed Rahimian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27041v1)