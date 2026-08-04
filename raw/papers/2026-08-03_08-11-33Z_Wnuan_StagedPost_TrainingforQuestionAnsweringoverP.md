---
title: Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise Knowledge
published: 2026-08-03T08:11:33Z
authors: Xiaofeng Shi, Xiaosong Qiu, Wenxin Ma, Qian Kou, Yiming Pan, Longbin Yu, Ying Liu, Haiping Wang, Hua Zhou
url: http://arxiv.org/abs/2608.01862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise Knowledge

## Abstract
Enterprise question answering requires models to acquire proprietary knowledge without discarding general capabilities. We present Wnuan, a three-stage pipeline that constructs task-oriented supervision from documents, performs supervised fine-tuning with general-data replay, and applies reinforcement learning to residual errors. On the 707-question WnuanBench, the primary 32B route raises acceptable-answer rate (AAR) from 52.76% before adaptation to 80.06% after SFT and 91.51% after RL. Under a matched 100-update protocol, residual-error sampling outperforms full-pool and size-matched random sampling by 3.11 and 2.97 points, respectively. Source-cluster bootstrap intervals remain above zero for both contrasts, and a same-domain validation set preserves the ordering. The general-benchmark average decreases by 5.17 points across the route, concentrated in instruction following. The automatic evaluation ensemble agrees with an authoritative domain expert on 90.5% of a stratified Wnuan-Inst response sample. These results characterize both the gains and the general-capability cost of staged enterprise adaptation.

## Metadata
- **Published**: 2026-08-03T08:11:33Z
- **Authors**: Xiaofeng Shi, Xiaosong Qiu, Wenxin Ma, Qian Kou, Yiming Pan, Longbin Yu, Ying Liu, Haiping Wang, Hua Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01862v1)