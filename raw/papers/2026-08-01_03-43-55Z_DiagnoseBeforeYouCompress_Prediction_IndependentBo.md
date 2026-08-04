---
title: Diagnose Before You Compress: Prediction-Independent Bottleneck Witness Refinement for LLM Serving Traces
published: 2026-08-01T03:43:55Z
authors: Liming Liu, Chao Hu, Mingfei Lu, Cong Tan, Yiwei Ge, Chijin Zhou, Yongjun Xie, Runzhe Wang, Xiaohai Shi, Heyuan Shi
url: http://arxiv.org/abs/2608.00423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diagnose Before You Compress: Prediction-Independent Bottleneck Witness Refinement for LLM Serving Traces

## Abstract
Production LLM serving generates millions of diverse requests, making full-trace replay across serving configurations increasingly expensive. Existing trace reduction methods mainly preserve workload distributions or representative requests, but bottleneck-revealing workloads may be rare and non-representative. Moreover, evidence for one component cannot compensate for missing evidence in another, while using predicted bottlenecks as target truth creates circular evaluation. These limitations make it necessary to preserve evidence for every bottleneck component rather than rely on workload representativeness alone. We propose Bottleneck-Preserving Witnessing (BPW), a quality-constrained framework for compact and diagnostically reliable LLM serving replay suites. BPW first performs Workload Candidate Nomination using response-blind workload features and closed source-side measurements. This stage identifies workloads that may expose scheduler, prefill, decode, or KV-cache bottlenecks. Coverage-Priority Sequence Construction then organizes multi-component proposals as reusable hyperedges and prioritizes weak and uncovered dimensions. Finally, Bottleneck Truth Verification derives prediction-independent labels solely from direct target-system measurements. The verified results determine the earliest prefix satisfying the direct two-witness requirement for every component. Experiments on BurstGPT, ServeGen, and Mooncake show that BPW reaches the verified gate with a compact workload set and outperforms 16 policies, achieving relative improvements of 2.3% and 16.3% in Mean prefix Macro-F1 and WBRC-AUC, respectively. Stage-resolved and sensitivity analyses confirm the distinct contributions and local stability of its three stages. Our code is publicly available at https://github.com/llmllmllm/BPW

## Metadata
- **Published**: 2026-08-01T03:43:55Z
- **Authors**: Liming Liu, Chao Hu, Mingfei Lu, Cong Tan, Yiwei Ge, Chijin Zhou, Yongjun Xie, Runzhe Wang, Xiaohai Shi, Heyuan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00423v1)