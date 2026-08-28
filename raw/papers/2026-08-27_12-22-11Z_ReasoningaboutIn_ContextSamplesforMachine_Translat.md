---
title: Reasoning about In-Context Samples for Machine-Translation
published: 2026-08-27T12:22:11Z
authors: Maxime Bouthors, Josep Crego, François Yvon
url: http://arxiv.org/abs/2608.27036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning about In-Context Samples for Machine-Translation

## Abstract
Large Language Models (LLMs) can be trained to perform chain-of-thoughts reasoning in order to improve the reliability of their responses. In this work, we investigate how explicit reasoning can be leveraged for LLM-Based Machine Translation (MT) with in-context samples. We introduce a novel fragment-based reasoning framework in which the model first extracts parallel source-target fragments from retrieved similar exemplars, and uses these fragments as intermediate reasoning traces to produce the final translation. To train our model, we distill silver fragments and drafts from a large teacher model. Our experiments with the Qwen3 model family, over 6 languages, including up to 5 domains per language, demonstrate that fragment-based MT significantly outperforms alternative methods like standard k-shot or basic drafting.

## Metadata
- **Published**: 2026-08-27T12:22:11Z
- **Authors**: Maxime Bouthors, Josep Crego, François Yvon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27036v1)