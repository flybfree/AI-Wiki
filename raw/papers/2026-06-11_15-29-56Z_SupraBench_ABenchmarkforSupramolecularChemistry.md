---
title: SupraBench: A Benchmark for Supramolecular Chemistry
published: 2026-06-11T15:29:56Z
authors: Tianyi Ma, Yijun Ma, Zehong Wang, Weixiang Sun, Ziming Li, Connor R. Schmidt, Chuxu Zhang, Matthew J. Webber, Yanfang Ye
url: http://arxiv.org/abs/2606.13477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SupraBench: A Benchmark for Supramolecular Chemistry

## Abstract
Supramolecular chemistry, which includes the study of non-covalent host-guest assemblies, has advanced various applications. However, designing host-guest systems remains time-consuming, requiring days of dry-lab verification per candidate pair. Although LLMs have emerged as a fast alternative with strong performance on molecular binding tasks, no benchmark currently systematically evaluates LLMs for host-guest reasoning across fundamental supramolecular chemistry tasks, e.g., binding affinity prediction. To this end, we collaborate with domain experts to release the first Supramolecular Benchmark, called SupraBench, to evaluate LLMs in chemistry reasoning. Specifically, we design four fundamental tasks, i.e., binding affinity prediction, top-binder selection, solvent identification, and host-guest description, plus an auxiliary vision-based task for molecular identification. We also release SupraPMC, a curated 16M-token corpus of Supramolecular chemistry articles distilled from Europe PMC, to support the adaptation to the supramolecular domain. We benchmark a broad range of open and proprietary LLMs and find that LLMs leave substantial headroom across all tasks. Domain adaptation pretraining over SupraPMC transfers cleanly to in-distribution regression but trades off against strict letter-format output. Moreover, the difficulty profile differs sharply across task families, revealing distinct failure modes that indicate specific gaps in current supramolecular chemistry reasoning. Our source codes and benchmark datasets are available at https://github.com/Tianyi-Billy-Ma/SupraBench.

## Metadata
- **Published**: 2026-06-11T15:29:56Z
- **Authors**: Tianyi Ma, Yijun Ma, Zehong Wang, Weixiang Sun, Ziming Li, Connor R. Schmidt, Chuxu Zhang, Matthew J. Webber, Yanfang Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.13477v1)