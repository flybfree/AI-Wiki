---
title: Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization
published: 2026-10-12T14:17:21Z
authors: Huihao Jing, Shaojin Chen, Wenbin Hu, Yuxuan Liu, Haochen Shi, Zhongwei Xie, Haoran Li, Yangqiu Song
url: http://arxiv.org/abs/2610.16838v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization

## Abstract
As language-model agents write code, move money and change records on behalf of users, deciding whether an action is authorized has become a central safety problem. Guardrails are often placed in front of these actions, yet few evaluations ask whether their decisions follow authorization: blocking unauthorized actions while still allowing the same actions under valid permission. We introduce \bench{}, a benchmark that contrasts authorization evidence for the same operation in its language track. It combines expert-annotated natural-language scenarios with executed and verified operations, plus externally sourced native-policy requests. \bench{} checks each decision for correctness, usability and resulting effect, and tracks each request across guardrail changes. Our experiments show that many blocked operations stem from failed reviews, not correct denials. Repairing the output format restores usable decisions but changes which authorized requests are honored, and adding a second reviewer removes some errors while rejecting valid authorization. Guardrails should therefore be evaluated on both the unauthorized actions they stop and the authorized actions they let through.

## Metadata
- **Published**: 2026-10-12T14:17:21Z
- **Authors**: Huihao Jing, Shaojin Chen, Wenbin Hu, Yuxuan Liu, Haochen Shi, Zhongwei Xie, Haoran Li, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16838v1)