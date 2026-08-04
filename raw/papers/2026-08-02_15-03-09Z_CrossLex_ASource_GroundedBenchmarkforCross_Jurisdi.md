---
title: CrossLex: A Source-Grounded Benchmark for Cross-Jurisdictional Legal Reasoning in Large Language Models
published: 2026-08-02T15:03:09Z
authors: Xiaocui Yang, Xican Tan, Shoujie Chen, Shihan Xiao, Keke Tong, Xinyu Zhou
url: http://arxiv.org/abs/2608.01292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CrossLex: A Source-Grounded Benchmark for Cross-Jurisdictional Legal Reasoning in Large Language Models

## Abstract
Legal reasoning is inherently jurisdiction-dependent: the same facts can call for different legal rules and yield different conclusions across legal systems. Yet existing benchmarks rarely evaluate whether large language models (LLMs) can recognize such jurisdiction-specific variation, especially when identical fact patterns lead to divergent legal outcomes.We introduce CrossLex, a same-fact, legal-source-grounded benchmark for evaluating cross-jurisdictional legal reasoning in LLMs across three jurisdictions: China, California, and Germany. Built from authoritative legal sources, CrossLex aligns 55 legal issues spanning contract, consumer, criminal, family, and labor law, and constructs jurisdiction-aligned questions paired with answers and supporting citations. In total, CrossLex contains 6,149 instances organized into 385 fact groups, with all legal issues, answers, and cited authorities reviewed by legal professionals.To disentangle basic legal knowledge from cross-jurisdictional reasoning, CrossLex defines three complementary tasks: single-jurisdiction reasoning (T1), joint cross-jurisdictional comparison (T2), and fine-grained cross-jurisdictional evaluation (T3). We further propose Grounded Joint, a metric that jointly assesses answer correctness and legal-source grounding, and provide a unified evaluation for streamlined benchmarking. Extensive experiments on representative LLMs show that, although current models can often answer legal questions correctly, they struggle to provide accurate cross-jurisdictional legal citations.We hope that CrossLex will facilitate future research on source-grounded cross-jurisdictional legal reasoning.

## Metadata
- **Published**: 2026-08-02T15:03:09Z
- **Authors**: Xiaocui Yang, Xican Tan, Shoujie Chen, Shihan Xiao, Keke Tong, Xinyu Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01292v1)