---
title: JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols
published: 2026-08-27T11:28:32Z
authors: Chen Chen, Yaolin Chen, Xuehan Sun, Juan Lin, Xueluan Gong, Yuhang Zheng, Qian Wang, Kwok-Yan Lam
url: http://arxiv.org/abs/2608.26982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols

## Abstract
Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing extraction methods do not specifically target LLM judges and provide limited support for multiple evaluation protocols under restricted query budgets. In this study, we propose JUDGESTEALER, the first query-efficient model extraction framework for replicating judging capabilities across pointwise scoring, pairwise comparison, and listwise ranking protocols. JUDGESTEALER exploits the strong cross-protocol agreement to acquire pointwise scores and transform them into pairwise and listwise supervisions without additional victim queries. To capture informative judge patterns and improve query efficiency, JUDGESTEALER dynamically selects pointwise inputs based on semantic diversity, predictive uncertainty, and potential judge biases. It further applies score smoothing and multi-protocol review to preserve the ordinal structure of scores and mitigate catastrophic forgetting during surrogate adaptation. Extensive experiments on state-of-the-art LLM-as-a-judge and reward models show that JUDGESTEALER consistently outperforms existing extraction baselines, achieving up to 73.3%, 87.0%, and 71.6% accuracy for pointwise, pairwise, and listwise evaluation, respectively. JUDGESTEALER also remains effective across different sur- rogate model scales, adaptation strategies, and reasoning settings. Moreover, JUDGESTEALER demonstrates robustness against representative extraction defenses.

## Metadata
- **Published**: 2026-08-27T11:28:32Z
- **Authors**: Chen Chen, Yaolin Chen, Xuehan Sun, Juan Lin, Xueluan Gong, Yuhang Zheng, Qian Wang, Kwok-Yan Lam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26982v1)