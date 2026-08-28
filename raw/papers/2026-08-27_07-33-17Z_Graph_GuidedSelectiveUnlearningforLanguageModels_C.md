---
title: Graph-Guided Selective Unlearning for Language Models: Controlling Support Routes Beyond Forget Seeds
published: 2026-08-27T07:33:17Z
authors: Waqas Khan, Tabinda Sarwar, Jingyue Cong, Xun Yi, Estrid He
url: http://arxiv.org/abs/2608.26743v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph-Guided Selective Unlearning for Language Models: Controlling Support Routes Beyond Forget Seeds

## Abstract
Enterprises fine-tune language models on proprietary data that may later require removal due to privacy, contractual, or compliance obligations. Selective unlearning removes requested knowledge while preserving model utility, offering a practical alternative to full retraining, but existing methods treat the explicitly identified forget examples as the complete deletion scope. This is insufficient when target knowledge remains recoverable through paraphrases, aliases, or neighboring training examples. We propose GRAPHSU, a graph-guided controller that expands the deletion scope beyond forget seeds by constructing a weighted support-route graph, propagating deletion pressure through it, and applying graded forgetting strengths to high-risk neighbors. On the Task of Fictitious Unlearning (TOFU), a synthetic author-profile question-answering benchmark, and PISTOL, a structural-unlearning benchmark built around interconnected factual samples, with GPT-2 Medium and Llama-3.2-3B-Instruct, GRAPHSU achieves the lowest utility-feasible soft leakage across all deletion settings, reducing leakage by up to 49.5 percentage points over a matched seed-only baseline, demonstrating that effective enterprise unlearning requires controlling support routes, not just forget seeds.

## Metadata
- **Published**: 2026-08-27T07:33:17Z
- **Authors**: Waqas Khan, Tabinda Sarwar, Jingyue Cong, Xun Yi, Estrid He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26743v1)