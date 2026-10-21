---
title: KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses
published: 2026-10-20T00:12:14Z
authors: Zhikang Chen, Yueqing Sun, Sen Cui, Ziang Ye, Yu Wang, Yan Feng2, Xierui Song, Yu Zhang, Tingting Zhu
url: http://arxiv.org/abs/2610.27417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses

## Abstract
A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPHarness, a framework that adapts the external execution harness of a frozen vision-language-action model through knowledge-probing co-evolution. Recovery knowledge supplies context-specific intervention hypotheses that guide active probing; probe outcomes reveal when these hypotheses apply and provide evidence for refining both recovery knowledge and later probe selection. This reciprocal process allows the harness to improve not only which interventions it applies, but also how it investigates failures. KPHarness separates fast policy execution from a slow research loop that translates accumulated knowledge and probing evidence into bounded harness revisions. Each revision is compared with the incumbent under matched sandbox conditions and accepted only when the paired evaluation shows improvement. Recoveries supported by further validation are retained for cross-task reuse, while immediate interaction feedback and delayed episode-success credit update action- and knowledge-probing policies during adaptation. Experiments on Minecraft tasks spanning mining, combat, and crafting show improved task coverage over bare policy execution, a manually specified fixed harness, and knowledge-only harness evolution with non-adaptive probing. Evaluation on previously unseen tasks further shows improved task completion with the evolved harness, knowledge bank, and probing policies held fixed,

## Metadata
- **Published**: 2026-10-20T00:12:14Z
- **Authors**: Zhikang Chen, Yueqing Sun, Sen Cui, Ziang Ye, Yu Wang, Yan Feng2, Xierui Song, Yu Zhang, Tingting Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27417v1)