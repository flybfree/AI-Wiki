---
title: FedPA-LoRA: Product-Aligned Framework for Mitigating Aggregation and Initialization Errors in Heterogeneous Federated LoRA
published: 2026-08-15T19:20:31Z
authors: Juseok Jeon, Ramy E. Ali, Doyun Kwon, Myungbeom Her, Jinhwi Kim, Jinhyun So
url: http://arxiv.org/abs/2608.15381v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedPA-LoRA: Product-Aligned Framework for Mitigating Aggregation and Initialization Errors in Heterogeneous Federated LoRA

## Abstract
Low-Rank Adaptation (LoRA) enables efficient federated fine-tuning of large language models, but its factorized parameterization creates a tension between accurate aggregation of local updates and continuity of locally optimized factors. Factor-wise aggregation incurs aggregation mismatch but better preserves factor continuity, whereas product-space reconstruction reduces this mismatch at the cost of greater factor-level initialization mismatch from newly reconstructed factors. We propose FedPA-LoRA, a product-aligned federated LoRA framework that jointly addresses these limitations and provably converges under both homogeneous and heterogeneous client ranks. Each client preserves its local factors across communication rounds and aligns its product toward a rank-specific global reference, maintaining local optimization continuity while promoting global consistency under data heterogeneity. The server aggregates heterogeneous-rank updates in the common product space and efficiently reconstructs a rank-constrained global adapter without forming the dense aggregate. This design supports client-specific computation and communication budgets. Experiments on natural language understanding and generation tasks show that FedPA-LoRA consistently outperforms representative baselines across varying levels of data heterogeneity and homogeneous- and heterogeneous-rank settings, with up to a $6.82$ percentage-point improvement in average GLUE accuracy under heterogeneous client ranks.

## Metadata
- **Published**: 2026-08-15T19:20:31Z
- **Authors**: Juseok Jeon, Ramy E. Ali, Doyun Kwon, Myungbeom Her, Jinhwi Kim, Jinhyun So
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15381v1)