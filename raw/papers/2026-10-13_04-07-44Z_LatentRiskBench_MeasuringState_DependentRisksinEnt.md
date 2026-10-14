---
title: LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents
published: 2026-10-13T04:07:44Z
authors: Jingyue Cong, Estrid He, Zhuang Li, Nan Wu, Li Shen, Yameng Peng, Xinshu Li, Andy Song
url: http://arxiv.org/abs/2610.17685v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents

## Abstract
Enterprise agents face safety risks that cannot be determined from individual actions alone. Existing safety benchmarks largely evaluate action-local risks, overlooking failures whose safety depends on workflow state. In such state-dependent risks, the same action may be safe in one context but violate policy in another. Hence, we introduce LatentRiskBench for evaluating such state-dependent risks in enterprise settings. It pairs risky trajectories with benign counterparts that share the same terminal action but differ in latent policy-relevant states, requiring models to reconstruct workflow context rather than rely on action-level cues. We also introduce new metrics for state-dependent risk evaluation, including a suite of residual risk (RR) measures. Experiments on the benchmark show that action-level evaluation detects only 0.09 of state-dependent violations, whereas state-level evaluation reaches 0.96. Existing guardrail methods largely overlook such risks unless they are explicitly applied to workflow states. Case studies on a commercial deployed scenario further show that the safety metrics embedded in the benchmark provide a more realistic measure of safety for enterprise agents. Our dataset and code are available at https://github.com/JingyueCong/LatentRiskBench.

## Metadata
- **Published**: 2026-10-13T04:07:44Z
- **Authors**: Jingyue Cong, Estrid He, Zhuang Li, Nan Wu, Li Shen, Yameng Peng, Xinshu Li, Andy Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17685v1)