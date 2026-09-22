---
title: RPMem: Learning Long-Term Recurrent Parametric Memory Across Sessions for LLM Agents
published: 2026-09-20T08:51:10Z
authors: Fanyu Zhao, Ruike Cao, Liang Dong, Fugen Yao, Jian Xu, Guanjun Jiang, Han Zhang, Yifei Zhao, Yinsheng Li
url: http://arxiv.org/abs/2609.23466v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RPMem: Learning Long-Term Recurrent Parametric Memory Across Sessions for LLM Agents

## Abstract
Long-running LLM agents require memory that persists and evolves across sessions. Text-based memory retrieves and reconstructs past interactions at every query, making long-horizon performance increasingly dependent on retrieval quality and contextual reasoning as histories grow. Parametric memory encodes experience directly into model computation, but existing approaches provide limited support for cross-session memory evolution. Their coupling to a specific backbone further restricts memory reuse after model replacement. We introduce RPMem, a two-stage architecture that compiles each session into a model-independent latent memory through forward computation and selectively integrates it with retained memory via a task-trained recurrent gate. The consolidated memory is then mapped to backbone-specific low-rank adaptation (LoRA) parameters, allowing the encoding capability to transfer when the backbone is replaced. Evaluation across three long-term memory benchmarks and five diverse backbones demonstrates broad generalization with near-constant update cost and memory footprint. With Qwen3-8B on PERMA, RPMem reaches 85.52%, outperforming the strongest parametric and text-based baselines by 5.32 and 12.98 percentage points, respectively. Ablations validate the complementary roles of session compilation and cross-session consolidation, while dynamics analyses reveal that the gate acquires task-specific memory integration strategies. These results establish RPMem as a lifecycle-independent parametric memory framework that maintains evolving cross-session memory that remains reusable across backbone replacements. Our implementation is available at https://github.com/Quark-Medical/rpmem/tree/main.

## Metadata
- **Published**: 2026-09-20T08:51:10Z
- **Authors**: Fanyu Zhao, Ruike Cao, Liang Dong, Fugen Yao, Jian Xu, Guanjun Jiang, Han Zhang, Yifei Zhao, Yinsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23466v1)