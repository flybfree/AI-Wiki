---
title: Route-and-Generate: KL-Regularized Router Improvement for Reasoning Routing in LLMs
published: 2026-10-21T19:09:04Z
authors: Tien-Phat Nguyen, Truong Nguyen, Thanh-Thien Le, Hoang Phan, Thien Huu Nguyen, Linh Ngo Van, Trung Le
url: http://arxiv.org/abs/2610.30351v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Route-and-Generate: KL-Regularized Router Improvement for Reasoning Routing in LLMs

## Abstract
Large language models often apply complex reasoning indiscriminately, leading to overthinking on simple tasks and underthinking on harder ones. We present Route-and-Generate (Rouge), a hierarchical training framework that enables LLMs to adaptively decide when and how much reasoning is required for each input. Our approach decouples reasoning effort allocation from answer generation by introducing a routing policy that allocates a fixed sampling budget across multiple reasoning formats, while the base model is optimized with GRPO using per-sample rewards. To promote efficient reasoning, we employ a rank-based reward that favors shorter correct solutions, and update the routing policy via a closed-form KL-regularized policy improvement step distilled into a neural router. This design encourages concise answers on easy problems while reserving longer reasoning for harder ones, achieving improved accuracy-efficiency trade-offs across multiple reasoning benchmarks.

## Metadata
- **Published**: 2026-10-21T19:09:04Z
- **Authors**: Tien-Phat Nguyen, Truong Nguyen, Thanh-Thien Le, Hoang Phan, Thien Huu Nguyen, Linh Ngo Van, Trung Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30351v1)