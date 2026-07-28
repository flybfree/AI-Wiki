---
title: The Cross-Domain Generalization Cost of Offensive Language Detection
published: 2026-07-26T07:27:54Z
authors: Ruixing Ren, Junhui Zhao, Xiaoke Sun, Qiuping Li
url: http://arxiv.org/abs/2607.23512v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Cross-Domain Generalization Cost of Offensive Language Detection

## Abstract
Offensive language detection models generally suffer performance degradation when deployed across datasets and across languages, yet most existing studies stop at reporting this phenomenon and lack a systematic methodology for decomposing the causes of degradation into attributable components and quantifying the cost of remediation. This paper proposes a diagnosis and optimization framework composed of three coordinated technical components. First, a zero-shot transfer loss decomposition that separates the performance degradation from OLID to MLMA into two independently measurable components, namely dataset effect and language effect. Second, a controlled fine-tuning protocol that quantifies both adaptation efficiency and the hidden damage inflicted on the source task by comparing few shot learning curves under continued fine-tuning and cold-start starting points. Third, three joint training strategies incorpo rating temperature sampling and experience replay, which offer a controllable Pareto trade-off between improving multilingual capability and preserving source-task performance. Experiments built on this framework show that the dataset effect dominates the zero-shot transfer loss and substantially outweighs the language effect. Few-shot adaptation without a replay mechanism, though data-efficient, inflicts source task damage 4 to 9 times greater than that of the joint training strategies, and its damage magnitude is highly unstable. The three joint training strategies trade 3.2 to 4.1 percentage points of source-task performance for 8.1 to 42.6 percentage points of multilingual capability gain, forming a clear and controllable Pareto trade-off.

## Metadata
- **Published**: 2026-07-26T07:27:54Z
- **Authors**: Ruixing Ren, Junhui Zhao, Xiaoke Sun, Qiuping Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23512v1)