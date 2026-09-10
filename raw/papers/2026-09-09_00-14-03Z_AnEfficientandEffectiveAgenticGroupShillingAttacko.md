---
title: An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems
published: 2026-09-09T00:14:03Z
authors: Quoc Viet Nguyen, Trinh Pham, Viet Huynh, Hongzhi Yin, Quoc Viet Hung Nguyen, Bay Vo, Thanh Tam Nguyen
url: http://arxiv.org/abs/2609.09551v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems

## Abstract
Recommender systems have become core infrastructure for modern online platforms, personalizing content at scale and strongly influencing what users see, click on, and purchase. However, this dependence on user interaction also exposes them to shilling attacks, where malicious actors can inject fake profiles to distort item rankings and control visibility. Existing attacks often rely on target-specific fine-tuning or fixed profile templates, making them either difficult to adapt to different victims or easier to detect. To overcome these limitations, we propose the Agentic Group Attack System (AGAS), a coordinated shilling framework where a central Coordinator directs a group of role-switching worker agents to adaptively promote a target item across different victim families. The Coordinator dynamically adjusts the strategy when progress stalls or suppression signals increase, while workers pursue a shared objective and switch between active and inactive roles to avoid repetitive patterns. Under the same attack budgets and evaluation protocols, AGAS consistently surpasses strong baselines in target promotion while better preserving benign recommendation quality, weakening representative detectors, and achieving higher efficiency than prior attacks. These findings also emphasize that defending recommender systems may require mechanisms that can handle adaptive shilling campaigns, not just isolated fake-profile injections. Our code is available at https://github.com/phkhanhtrinh23/AGAS.

## Metadata
- **Published**: 2026-09-09T00:14:03Z
- **Authors**: Quoc Viet Nguyen, Trinh Pham, Viet Huynh, Hongzhi Yin, Quoc Viet Hung Nguyen, Bay Vo, Thanh Tam Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09551v1)